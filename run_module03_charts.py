"""
Run all Module 03 chart scripts to generate PDFs
"""

import subprocess
import sys
from pathlib import Path

def run_all_charts():
    module_path = Path(__file__).parent / 'module_03_ai_ml' / 'figures'

    if not module_path.exists():
        print(f"Module path not found: {module_path}")
        return

    chart_folders = sorted([d for d in module_path.iterdir() if d.is_dir()])

    print(f"Found {len(chart_folders)} chart folders in module_03_ai_ml")
    print("=" * 60)

    success = 0
    failed = 0

    for folder in chart_folders:
        script = folder / f"{folder.name}.py"
        if script.exists():
            print(f"Running: {folder.name}...", end=" ")
            try:
                result = subprocess.run(
                    [sys.executable, str(script)],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    cwd=str(folder)
                )
                if result.returncode == 0:
                    print("OK")
                    success += 1
                else:
                    print(f"FAILED: {result.stderr[:100]}")
                    failed += 1
            except subprocess.TimeoutExpired:
                print("TIMEOUT")
                failed += 1
            except Exception as e:
                print(f"ERROR: {e}")
                failed += 1
        else:
            print(f"Script not found: {script}")
            failed += 1

    print("=" * 60)
    print(f"Results: {success} succeeded, {failed} failed out of {len(chart_folders)} total")
    return success, failed

if __name__ == '__main__':
    run_all_charts()
