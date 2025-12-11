"""
Fix chart widths in Module 02 .tex files - Version 2
Handles all remaining width patterns.
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')

# Comprehensive width reductions
WIDTH_FIXES = [
    # Handle column charts (within \column{0.48\textwidth})
    (r'(\\column\{0\.48\\textwidth\}[\s\S]*?)width=\\textwidth\}', r'\1width=0.92\\textwidth}'),
    # Large center charts
    (r'width=0\.9\\textwidth', r'width=0.65\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.62\\textwidth'),
    (r'width=0\.85\\textwidth', r'width=0.60\\textwidth'),
    (r'width=0\.82\\textwidth', r'width=0.58\\textwidth'),
    (r'width=0\.80\\textwidth', r'width=0.56\\textwidth'),
    (r'width=0\.78\\textwidth', r'width=0.55\\textwidth'),
    (r'width=0\.75\\textwidth', r'width=0.52\\textwidth'),
    (r'width=0\.72\\textwidth', r'width=0.50\\textwidth'),
    (r'width=0\.70\\textwidth', r'width=0.48\\textwidth'),
    (r'width=0\.68\\textwidth', r'width=0.48\\textwidth'),
    (r'width=0\.65\\textwidth', r'width=0.48\\textwidth'),
    (r'width=0\.62\\textwidth', r'width=0.48\\textwidth'),
    (r'width=0\.60\\textwidth', r'width=0.48\\textwidth'),
    (r'width=0\.58\\textwidth', r'width=0.48\\textwidth'),
]


def fix_widths(tex_path):
    """Fix chart widths in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    original = content

    for pattern, replacement in WIDTH_FIXES:
        content = re.sub(pattern, replacement, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=" * 70)
    print("FIXING CHART WIDTHS - MODULE 02 (V2)")
    print("=" * 70)

    total_fixed = 0
    lessons = sorted(BASE.glob('lesson_*.tex'))

    for tex_path in lessons:
        changed = fix_widths(tex_path)
        if changed:
            total_fixed += 1
            print(f"  Fixed: {tex_path.name}")
        else:
            print(f"  No changes: {tex_path.name}")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {total_fixed} files modified")
    print("=" * 70)


if __name__ == '__main__':
    main()
