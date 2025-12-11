"""
Fix chart widths in Module 01 .tex files to eliminate overflow warnings.

Strategy:
- Full-width charts (0.85-0.88): Reduce to 0.75
- Column charts (width=\textwidth): Reduce to 0.95\textwidth
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_01_fintech')

LESSONS = [
    'lesson_03_mobile_wallets.tex',
    'lesson_04_neobanks.tex',
    'lesson_05_open_banking.tex',
    'lesson_06_digital_identity.tex',
    'lesson_07_p2p_lending.tex',
    'lesson_08_robo_advisors.tex',
    'lesson_09_insurtech.tex',
    'lesson_10_regtech.tex',
    'lesson_11_regulatory_frameworks.tex',
    'lesson_12_business_models.tex',
]

# Width reductions
WIDTH_FIXES = [
    # Full-width charts - reduce to prevent overflow
    (r'width=0\.88\\textwidth', r'width=0.75\\textwidth'),
    (r'width=0\.85\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.82\\textwidth', r'width=0.70\\textwidth'),
    (r'width=0\.80\\textwidth', r'width=0.68\\textwidth'),
    # Column charts - reduce slightly
    (r'width=\\textwidth\}', r'width=0.92\\textwidth}'),
]


def fix_widths(tex_path):
    """Fix chart widths in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    original = content
    fixes = []

    for pattern, replacement in WIDTH_FIXES:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            fixes.append(f"  {pattern} -> {replacement} ({len(matches)} times)")

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True, fixes
    return False, fixes


def main():
    print("=" * 70)
    print("FIXING CHART WIDTHS TO ELIMINATE OVERFLOWS")
    print("=" * 70)

    total_fixed = 0

    for lesson in LESSONS:
        tex_path = BASE / lesson
        if not tex_path.exists():
            print(f"\nSKIP: {lesson} not found")
            continue

        print(f"\n{lesson}:")
        changed, fixes = fix_widths(tex_path)

        if changed:
            total_fixed += 1
            print(f"  FIXED")
            for fix in fixes:
                print(fix)
        else:
            print("  No changes needed")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {total_fixed} files modified")
    print("=" * 70)


if __name__ == '__main__':
    main()
