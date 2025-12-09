"""
Master Chart Generation Script for Digital Finance Course
Generates ALL charts with progress tracking and error handling

Usage:
    python generate_all_charts.py                    # Generate all charts
    python generate_all_charts.py --module module_01_fintech  # Generate specific module
    python generate_all_charts.py --verify           # Verify only, don't generate
"""

import subprocess
import sys
import time
import json
import argparse
import gc
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).parent
CHARTS_DIR = BASE_DIR / "charts"
MODULES_DIR = BASE_DIR

TIMEOUT_SECONDS = 120  # 2 minutes per chart
MAX_RETRIES = 2

# Module configuration
MODULES = [
    ("module_01_fintech", "figures"),
    ("module_02_blockchain", "charts"),
    ("module_03_ai_ml", "figures"),
    ("module_04_traditional", "figures"),
]


def discover_chart_scripts(module_filter=None):
    """Find all chart Python scripts"""
    scripts = []

    for module_name, charts_folder in MODULES:
        if module_filter and module_name != module_filter:
            continue

        # Check in module's figures/charts folder
        module_charts = MODULES_DIR / module_name / charts_folder
        if module_charts.exists():
            for item in module_charts.rglob("*.py"):
                if item.name.startswith("__") or item.name.startswith("generate_"):
                    continue
                scripts.append({
                    'script': item,
                    'module': module_name,
                    'name': item.stem,
                    'folder': charts_folder,
                })

        # Also check in charts/module_XX folder
        standalone_charts = CHARTS_DIR / module_name
        if standalone_charts.exists():
            for item in standalone_charts.rglob("*.py"):
                if item.name.startswith("__"):
                    continue
                scripts.append({
                    'script': item,
                    'module': module_name,
                    'name': item.stem,
                    'folder': 'charts',
                })

    return scripts


def run_chart_script(script_info, attempt=1):
    """Execute a single chart script"""
    script_path = script_info['script']

    result = {
        'script': str(script_path),
        'module': script_info['module'],
        'name': script_info['name'],
        'success': False,
        'error': None,
        'output': None,
        'duration': 0,
        'pdf_created': False,
        'attempt': attempt
    }

    start_time = time.time()

    try:
        proc = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            cwd=script_path.parent
        )

        result['output'] = proc.stdout
        result['duration'] = time.time() - start_time

        if proc.returncode == 0:
            # Check if PDF was created
            pdf_candidates = list(script_path.parent.glob("*.pdf"))
            if pdf_candidates:
                result['success'] = True
                result['pdf_created'] = True
            else:
                result['success'] = False
                result['error'] = "Script ran but no PDF created"
        else:
            result['error'] = proc.stderr[:500] if proc.stderr else "Unknown error"

    except subprocess.TimeoutExpired:
        result['error'] = f"Timeout after {TIMEOUT_SECONDS}s"
        result['duration'] = TIMEOUT_SECONDS
    except Exception as e:
        result['error'] = str(e)
        result['duration'] = time.time() - start_time

    gc.collect()
    return result


def run_batch_sequential(scripts, progress_callback=None):
    """Run all scripts sequentially"""
    results = []
    total = len(scripts)

    for idx, script_info in enumerate(scripts, 1):
        if progress_callback:
            progress_callback(idx, total, script_info['name'])

        result = run_chart_script(script_info)

        # Retry on failure
        if not result['success'] and result['attempt'] < MAX_RETRIES:
            print(f"    Retrying {script_info['name']}...")
            time.sleep(1)
            result = run_chart_script(script_info, attempt=result['attempt'] + 1)

        results.append(result)

        status = "OK" if result['success'] else "FAIL"
        duration = f"{result['duration']:.1f}s"
        print(f"  [{idx:3d}/{total}] [{status:4s}] {script_info['name'][:40]:<40} ({duration})")

        if not result['success'] and result['error']:
            print(f"           Error: {result['error'][:60]}")

    return results


def verify_outputs(results):
    """Verify all expected PDFs exist"""
    verification = {
        'total': len(results),
        'success': sum(1 for r in results if r['success']),
        'failed': sum(1 for r in results if not r['success']),
        'errors': [{'name': r['name'], 'error': r['error']}
                   for r in results if not r['success']]
    }
    return verification


def generate_report(results, verification, start_time, end_time, module_filter):
    """Generate execution report"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'duration_seconds': (end_time - start_time).total_seconds(),
        'module_filter': module_filter,
        'total_scripts': len(results),
        'successful': verification['success'],
        'failed': verification['failed'],
        'success_rate': f"{verification['success']/max(1,len(results))*100:.1f}%",
        'errors': verification['errors'][:20]  # Limit error list
    }

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = BASE_DIR / f"chart_generation_report_{timestamp}.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    return report, report_path


def main():
    parser = argparse.ArgumentParser(description='Generate Digital Finance charts')
    parser.add_argument('--module', type=str, help='Generate specific module only')
    parser.add_argument('--verify', action='store_true', help='Verify only, no generation')
    args = parser.parse_args()

    print("=" * 70)
    print("DIGITAL FINANCE CHART GENERATION")
    print("=" * 70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if args.module:
        print(f"Module filter: {args.module}")

    start_time = datetime.now()

    # Discover scripts
    print("\n[1/3] Discovering chart scripts...")
    scripts = discover_chart_scripts(args.module)
    print(f"  Found {len(scripts)} chart scripts")

    # Group by module for display
    modules = {}
    for s in scripts:
        modules.setdefault(s['module'], []).append(s)
    for module, module_scripts in modules.items():
        print(f"    {module}: {len(module_scripts)} scripts")

    if args.verify:
        print("\n[VERIFY MODE] Checking existing PDFs only...")
        # Just check which PDFs exist
        for s in scripts:
            pdf_path = s['script'].with_suffix('.pdf')
            alt_pdf = s['script'].parent / f"{s['name']}.pdf"
            exists = pdf_path.exists() or alt_pdf.exists()
            status = "EXISTS" if exists else "MISSING"
            print(f"  [{status}] {s['name']}")
        return 0

    # Execute
    print("\n[2/3] Generating charts (sequential mode)...")
    results = run_batch_sequential(scripts)

    # Verify
    print("\n[3/3] Verification...")
    verification = verify_outputs(results)

    end_time = datetime.now()

    # Report
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total scripts: {verification['total']}")
    print(f"Successful:    {verification['success']}")
    print(f"Failed:        {verification['failed']}")
    print(f"Success rate:  {verification['success']/max(1,verification['total'])*100:.1f}%")
    print(f"Duration:      {(end_time - start_time).total_seconds():.1f} seconds")

    report, report_path = generate_report(results, verification, start_time, end_time, args.module)
    print(f"\nReport saved: {report_path}")

    if verification['failed'] > 0:
        print("\nFailed scripts (first 10):")
        for err in verification['errors'][:10]:
            print(f"  - {err['name']}: {err['error'][:50]}...")

    print("=" * 70)

    return 0 if verification['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
