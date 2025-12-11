"""
Fix overflow warnings across all 4 modules.
Applies chart width reductions and path fixes.
"""
import subprocess
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3')

MODULES = {
    'module_01_fintech': list(range(1, 13)),
    'module_02_blockchain': list(range(13, 25)),
    'module_03_ai_ml': list(range(25, 37)),
    'module_04_traditional': list(range(37, 49)),
}

# Width reductions to apply
WIDTH_FIXES = [
    (r'width=0\.95\\textwidth', r'width=0.82\\textwidth'),
    (r'width=0\.90\\textwidth', r'width=0.78\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.75\\textwidth'),
    (r'width=0\.85\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.82\\textwidth', r'width=0.70\\textwidth'),
    (r'width=0\.80\\textwidth', r'width=0.68\\textwidth'),
]


def get_lesson_files(module_dir):
    """Get all .tex lesson files in a module."""
    return sorted(module_dir.glob('lesson_*.tex'))


def fix_figure_paths(tex_path, figures_dir):
    """Fix figure path references from figures/X.pdf to figures/X/X.pdf."""
    content = tex_path.read_text(encoding='utf-8')
    original = content

    pattern = r'(\\includegraphics\[[^\]]*\]\{figures/)([^/}]+)(\.pdf\})'

    def replace_path(match):
        prefix = match.group(1)
        name = match.group(2)
        suffix = match.group(3)

        direct_path = figures_dir / f'{name}.pdf'
        folder_path = figures_dir / name / f'{name}.pdf'

        if direct_path.exists():
            return match.group(0)
        elif folder_path.exists():
            return f'{prefix}{name}/{name}{suffix}'
        else:
            return match.group(0)

    content = re.sub(pattern, replace_path, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True
    return False


def fix_chart_widths(tex_path):
    """Reduce chart widths to prevent overflow."""
    content = tex_path.read_text(encoding='utf-8')
    original = content

    for pattern, replacement in WIDTH_FIXES:
        content = re.sub(pattern, replacement, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True
    return False


def check_overflows(tex_path):
    """Compile and count overflow warnings."""
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
            timeout=90
        )
        overflow_pattern = r'Overfull \\vbox \((\d+\.?\d*)pt too high\)'
        overflows = re.findall(overflow_pattern, result.stdout)
        critical = sum(1 for o in overflows if float(o) > 50)
        return len(overflows), critical
    except subprocess.TimeoutExpired:
        return -1, -1


def process_module(module_name, module_dir):
    """Process all lessons in a module."""
    print(f"\n{'='*70}")
    print(f"PROCESSING: {module_name}")
    print(f"{'='*70}")

    figures_dir = module_dir / 'figures'
    lessons = get_lesson_files(module_dir)

    results = []

    for tex_path in lessons:
        print(f"\n  {tex_path.name}:")

        # Fix paths
        path_fixed = fix_figure_paths(tex_path, figures_dir)
        if path_fixed:
            print(f"    - Fixed figure paths")

        # Fix widths
        width_fixed = fix_chart_widths(tex_path)
        if width_fixed:
            print(f"    - Reduced chart widths")

        # Check overflows
        overflows, critical = check_overflows(tex_path)
        if overflows == 0:
            print(f"    - Status: OK (0 overflows)")
        elif overflows > 0:
            print(f"    - Status: {overflows} overflows ({critical} critical)")
        else:
            print(f"    - Status: TIMEOUT")

        results.append({
            'lesson': tex_path.name,
            'overflows': overflows,
            'critical': critical
        })

    return results


def main():
    print("=" * 70)
    print("FIXING OVERFLOW WARNINGS - ALL MODULES")
    print("=" * 70)

    all_results = {}

    for module_name in MODULES:
        module_dir = BASE / module_name
        if module_dir.exists():
            all_results[module_name] = process_module(module_name, module_dir)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    total_overflows = 0
    total_critical = 0
    total_ok = 0

    for module_name, results in all_results.items():
        module_overflows = sum(r['overflows'] for r in results if r['overflows'] >= 0)
        module_critical = sum(r['critical'] for r in results if r['critical'] >= 0)
        module_ok = sum(1 for r in results if r['overflows'] == 0)

        print(f"\n  {module_name}:")
        print(f"    Lessons OK: {module_ok}/{len(results)}")
        print(f"    Total overflows: {module_overflows} ({module_critical} critical)")

        total_overflows += module_overflows
        total_critical += module_critical
        total_ok += module_ok

    print(f"\n  TOTAL: {total_ok} lessons OK, {total_overflows} overflows ({total_critical} critical)")
    print("=" * 70)

    return all_results


if __name__ == '__main__':
    main()
