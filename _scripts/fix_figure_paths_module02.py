"""
Fix figure path references in Module 02 .tex files.

Problem: .tex files reference figures/name.pdf
Actual:  Files are at figures/name/name.pdf
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')
FIGURES_DIR = BASE / 'figures'


def fix_figure_paths(tex_path):
    """Fix figure path references in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    original = content
    fixes = []

    pattern = r'(\\includegraphics\[[^\]]*\]\{figures/)([^/}]+)(\.pdf\})'

    def replace_path(match):
        prefix = match.group(1)
        name = match.group(2)
        suffix = match.group(3)

        direct_path = FIGURES_DIR / f'{name}.pdf'
        folder_path = FIGURES_DIR / name / f'{name}.pdf'

        if direct_path.exists():
            return match.group(0)
        elif folder_path.exists():
            new_path = f'{prefix}{name}/{name}{suffix}'
            fixes.append(f'  {name}.pdf -> {name}/{name}.pdf')
            return new_path
        else:
            fixes.append(f'  WARNING: {name}.pdf not found anywhere')
            return match.group(0)

    content = re.sub(pattern, replace_path, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True, fixes
    return False, fixes


def main():
    print("=" * 70)
    print("FIXING FIGURE PATH REFERENCES - MODULE 02")
    print("=" * 70)

    total_fixed = 0
    lessons = sorted(BASE.glob('lesson_*.tex'))

    for tex_path in lessons:
        print(f"\n{tex_path.name}:")
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
