"""
Fix chart widths in Module 02 .tex files to eliminate overflow warnings.
More aggressive width reductions specific to Module 02.
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')

# More aggressive width reductions
WIDTH_FIXES = [
    # Full-width charts - reduce significantly
    (r'width=\\textwidth\}', r'width=0.88\\textwidth}'),
    (r'width=0\.95\\textwidth', r'width=0.78\\textwidth'),
    (r'width=0\.90\\textwidth', r'width=0.75\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.85\\textwidth', r'width=0.70\\textwidth'),
    (r'width=0\.82\\textwidth', r'width=0.68\\textwidth'),
    (r'width=0\.80\\textwidth', r'width=0.65\\textwidth'),
    (r'width=0\.78\\textwidth', r'width=0.65\\textwidth'),
    (r'width=0\.75\\textwidth', r'width=0.62\\textwidth'),
    (r'width=0\.72\\textwidth', r'width=0.60\\textwidth'),
    (r'width=0\.70\\textwidth', r'width=0.58\\textwidth'),
    (r'width=0\.7\\textwidth', r'width=0.58\\textwidth'),
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
    print("FIXING CHART WIDTHS - MODULE 02")
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
