"""
Chart Verification Script for Digital Finance Course
Checks that all chart scripts have corresponding PDFs
"""

from pathlib import Path
from datetime import datetime
import json

BASE_DIR = Path(__file__).parent
CHARTS_DIR = BASE_DIR / "charts"

MODULES = [
    ("module_01_fintech", "figures"),
    ("module_02_blockchain", "charts"),
    ("module_03_ai_ml", "figures"),
    ("module_04_traditional", "figures"),
]


def verify_all_charts():
    """Verify all chart scripts have PDFs"""
    results = {
        'timestamp': datetime.now().isoformat(),
        'modules': {},
        'summary': {
            'total_scripts': 0,
            'total_pdfs': 0,
            'missing_pdfs': [],
        }
    }

    for module_name, charts_folder in MODULES:
        module_results = {
            'scripts': [],
            'pdfs': [],
            'missing': [],
            'complete': []
        }

        # Check module's figures/charts folder
        module_charts = BASE_DIR / module_name / charts_folder
        if module_charts.exists():
            for py_file in module_charts.rglob("*.py"):
                if py_file.name.startswith("__") or py_file.name.startswith("generate_"):
                    continue

                module_results['scripts'].append(str(py_file))
                results['summary']['total_scripts'] += 1

                # Check for PDF
                pdf_same_name = py_file.with_suffix('.pdf')
                pdf_folder_name = py_file.parent / f"{py_file.parent.name}.pdf"

                if pdf_same_name.exists() or pdf_folder_name.exists():
                    module_results['complete'].append(py_file.name)
                    results['summary']['total_pdfs'] += 1
                else:
                    module_results['missing'].append(py_file.name)
                    results['summary']['missing_pdfs'].append(str(py_file))

        # Check standalone charts folder
        standalone = CHARTS_DIR / module_name
        if standalone.exists():
            for py_file in standalone.rglob("*.py"):
                if py_file.name.startswith("__"):
                    continue

                module_results['scripts'].append(str(py_file))
                results['summary']['total_scripts'] += 1

                pdf_same_name = py_file.with_suffix('.pdf')
                pdf_folder_name = py_file.parent / f"{py_file.parent.name}.pdf"

                if pdf_same_name.exists() or pdf_folder_name.exists():
                    module_results['complete'].append(py_file.name)
                    results['summary']['total_pdfs'] += 1
                else:
                    module_results['missing'].append(py_file.name)
                    results['summary']['missing_pdfs'].append(str(py_file))

        results['modules'][module_name] = module_results

    return results


def print_report(results):
    """Print formatted verification report"""
    print("=" * 70)
    print("CHART VERIFICATION REPORT")
    print("=" * 70)
    print(f"Timestamp: {results['timestamp']}")

    print("\nMODULE SUMMARY:")
    for module, data in results['modules'].items():
        scripts = len(data['scripts'])
        complete = len(data['complete'])
        missing = len(data['missing'])

        if scripts == 0:
            continue

        pct = complete / scripts * 100 if scripts > 0 else 0
        status = "OK" if missing == 0 else "INCOMPLETE"
        print(f"  [{status:10s}] {module}: {complete}/{scripts} PDFs ({pct:.0f}%)")

        if missing > 0 and missing <= 5:
            for m in data['missing']:
                print(f"               Missing: {m}")
        elif missing > 5:
            for m in data['missing'][:3]:
                print(f"               Missing: {m}")
            print(f"               ... and {missing - 3} more")

    total = results['summary']['total_scripts']
    pdfs = results['summary']['total_pdfs']
    missing = len(results['summary']['missing_pdfs'])

    print("\nOVERALL:")
    print(f"  Total scripts: {total}")
    print(f"  PDFs created:  {pdfs}")
    print(f"  Missing PDFs:  {missing}")
    print(f"  Completion:    {pdfs/max(1,total)*100:.1f}%")
    print("=" * 70)


if __name__ == "__main__":
    results = verify_all_charts()
    print_report(results)

    # Save report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = BASE_DIR / f"chart_verification_{timestamp}.json"
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nReport saved: {report_path}")
