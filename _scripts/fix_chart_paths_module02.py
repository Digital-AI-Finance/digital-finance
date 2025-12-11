"""
Fix chart path references in Module 02 .tex files.

Problem: .tex files reference charts/lesson_XX/name.pdf
Actual:  Files are at figures/name/name.pdf

This script updates the paths.
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')
FIGURES_DIR = BASE / 'figures'


def fix_chart_paths(tex_path):
    """Fix chart path references in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    original = content
    fixes = []
    warnings = []

    # Pattern: charts/lesson_XX/name.pdf
    pattern = r'(\\includegraphics\[[^\]]*\]\{)charts/lesson_\d+/([^}]+)(\.pdf\})'

    def replace_path(match):
        prefix = match.group(1)
        name = match.group(2)
        suffix = match.group(3)

        # Check if figure exists in figures/name/name.pdf
        folder_path = FIGURES_DIR / name / f'{name}.pdf'

        if folder_path.exists():
            new_path = f'{prefix}figures/{name}/{name}{suffix}'
            fixes.append(f'  charts/.../{name}.pdf -> figures/{name}/{name}.pdf')
            return new_path
        else:
            warnings.append(f'  WARNING: {name}.pdf not found in figures/')
            return match.group(0)

    content = re.sub(pattern, replace_path, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True, fixes, warnings
    return False, fixes, warnings


def main():
    print("=" * 70)
    print("FIXING CHART PATH REFERENCES - MODULE 02")
    print("=" * 70)

    total_fixed = 0
    all_warnings = []
    lessons = sorted(BASE.glob('lesson_*.tex'))

    for tex_path in lessons:
        print(f"\n{tex_path.name}:")
        changed, fixes, warnings = fix_chart_paths(tex_path)

        if changed:
            total_fixed += 1
            print(f"  FIXED - {len(fixes)} paths updated")
            for fix in fixes[:5]:
                print(fix)
            if len(fixes) > 5:
                print(f"  ... and {len(fixes) - 5} more")

        if warnings:
            print(f"  WARNINGS: {len(warnings)} missing figures")
            all_warnings.extend(warnings)
            for w in warnings[:3]:
                print(w)
            if len(warnings) > 3:
                print(f"  ... and {len(warnings) - 3} more")

        if not changed and not warnings:
            print("  No changes needed")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {total_fixed} files modified, {len(all_warnings)} missing figures")
    print("=" * 70)

    if all_warnings:
        print("\nMISSING FIGURES (need to generate):")
        unique_missing = sorted(set(w.split()[-1] for w in all_warnings if 'WARNING' in w))
        for fig in unique_missing[:20]:
            print(f"  - {fig}")
        if len(unique_missing) > 20:
            print(f"  ... and {len(unique_missing) - 20} more")


if __name__ == '__main__':
    main()
