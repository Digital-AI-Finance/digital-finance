"""
Fix minor (non-critical) overflow issues with vspace adjustments.
"""
import re
from pathlib import Path

BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3\module_02_blockchain')

def add_vspace_after_frametitle(tex_path):
    """Add \vspace{-2mm} after frame titles to reduce minor overflows."""
    content = tex_path.read_text(encoding='utf-8')
    original = content

    # Add vspace after \begin{frame}{Title} if not already present
    pattern = r'(\\begin\{frame\}\{[^}]+\})\n(?!\\vspace)'
    replacement = r'\1\n\\vspace{-2mm}\n'
    content = re.sub(pattern, replacement, content)

    # Add vspace after \begin{frame}[options]{Title} if not already present
    pattern2 = r'(\\begin\{frame\}\[[^\]]+\]\{[^}]+\})\n(?!\\vspace)'
    replacement2 = r'\1\n\\vspace{-2mm}\n'
    content = re.sub(pattern2, replacement2, content)

    if content != original:
        tex_path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=" * 70)
    print("FIXING MINOR OVERFLOWS - MODULE 02")
    print("=" * 70)

    total_fixed = 0
    lessons = sorted(BASE.glob('lesson_*.tex'))

    for tex_path in lessons:
        changed = add_vspace_after_frametitle(tex_path)
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
