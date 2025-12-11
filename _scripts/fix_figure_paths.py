"""
Fix figure path references in Module 01 .tex files.

Problem: .tex files reference figures/name.pdf
Actual:  Files are at figures/name/name.pdf

Solution: Update paths from figures/X.pdf to figures/X/X.pdf
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_01_fintech')
FIGURES_DIR = BASE / 'figures'

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


def fix_figure_paths(tex_path):
    """Fix figure path references in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    original = content
    fixes = []

    # Find all includegraphics references
    pattern = r'(\\includegraphics\[[^\]]*\]\{figures/)([^/}]+)(\.pdf\})'

    def replace_path(match):
        prefix = match.group(1)  # \includegraphics[...]{figures/
        name = match.group(2)    # name (without .pdf)
        suffix = match.group(3)  # .pdf}

        # Check if the direct path exists (figures/name.pdf)
        direct_path = BASE / 'figures' / f'{name}.pdf'
        # Check if the folder path exists (figures/name/name.pdf)
        folder_path = BASE / 'figures' / name / f'{name}.pdf'

        if direct_path.exists():
            # Already correct, no change needed
            return match.group(0)
        elif folder_path.exists():
            # Fix: change to figures/name/name.pdf
            new_path = f'{prefix}{name}/{name}{suffix}'
            fixes.append(f'  {name}.pdf -> {name}/{name}.pdf')
            return new_path
        else:
            # File doesn't exist in either location
            fixes.append(f'  WARNING: {name}.pdf not found anywhere')
            return match.group(0)

    content = re.sub(pattern, replace_path, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True, fixes
    return False, fixes


def main():
    print("=" * 70)
    print("FIXING FIGURE PATH REFERENCES")
    print("=" * 70)

    total_fixed = 0

    for lesson in LESSONS:
        tex_path = BASE / lesson
        if not tex_path.exists():
            print(f"\nSKIP: {lesson} not found")
            continue

        print(f"\n{lesson}:")
        changed, fixes = fix_figure_paths(tex_path)

        if changed:
            total_fixed += 1
            print(f"  FIXED - {len(fixes)} paths updated")
            for fix in fixes[:5]:
                print(fix)
            if len(fixes) > 5:
                print(f"  ... and {len(fixes) - 5} more")
        else:
            if fixes:
                print("  No changes (warnings below):")
                for fix in fixes:
                    print(fix)
            else:
                print("  No changes needed")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {total_fixed} files modified")
    print("=" * 70)


if __name__ == '__main__':
    main()
