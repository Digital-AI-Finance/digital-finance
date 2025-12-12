"""
Check status of all lessons: overflows and missing charts.
"""

from pathlib import Path
import subprocess
import re

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

def check_overflows(tex_path):
    """Compile and count overflow warnings."""
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=tex_path.parent
        )
        output = result.stdout + result.stderr
        overflows = len(re.findall(r'Overfull', output))
        return overflows
    except Exception as e:
        return -1  # Error

def count_missing_charts(tex_path):
    """Count charts referenced but potentially missing."""
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all includegraphics references
    charts = re.findall(r'\\includegraphics[^{]*\{([^}]+)\}', content)
    missing = 0
    synthetic = 0

    for chart in charts:
        chart_path = tex_path.parent / chart
        if not chart_path.exists():
            missing += 1
        else:
            # Check if it's a placeholder/synthetic
            py_path = chart_path.parent / (chart_path.stem + '.py')
            if py_path.exists():
                with open(py_path, 'r', encoding='utf-8') as f:
                    py_content = f.read()
                    if 'SYNTHETIC' in py_content or 'placeholder' in py_content.lower():
                        synthetic += 1

    return missing, synthetic, len(charts)

def main():
    print("Checking lesson status...")
    print("=" * 80)

    total_overflows = 0
    total_missing = 0
    total_synthetic = 0
    total_charts = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        print(f"\n{module_dir.name}:")
        print("-" * 60)

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            overflows = check_overflows(tex_file)
            missing, synthetic, charts = count_missing_charts(tex_file)

            status = []
            if overflows > 0:
                status.append(f"{overflows} overflows")
                total_overflows += overflows
            if missing > 0:
                status.append(f"{missing} missing charts")
                total_missing += missing
            if synthetic > 0:
                status.append(f"{synthetic} synthetic")
                total_synthetic += synthetic

            total_charts += charts

            if status:
                print(f"  {tex_file.name}: {', '.join(status)}")
            else:
                print(f"  {tex_file.name}: OK ({charts} charts)")

    print("\n" + "=" * 80)
    print(f"SUMMARY:")
    print(f"  Total overflows: {total_overflows}")
    print(f"  Missing charts: {total_missing}")
    print(f"  Synthetic/placeholder: {total_synthetic}")
    print(f"  Total charts: {total_charts}")

if __name__ == '__main__':
    main()
