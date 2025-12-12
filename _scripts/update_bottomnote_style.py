"""
Update all lesson files to use the template bottomnote style.

Template style:
\newcommand{\bottomnote}[1]{%
\vfill
\vspace{-2mm}
\textcolor{mllavender2}{\rule{\textwidth}{0.4pt}}
\vspace{1mm}
\footnotesize
\textbf{#1}
}
"""

import re
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Old bottomnote pattern (beamercolorbox style)
OLD_BOTTOMNOTE_PATTERN = r'''% Bottom note command for key takeaways
\\newcommand\{\\bottomnote\}\[1\]\{%
\\vfill
\\begin\{beamercolorbox\}\[wd=\\textwidth,ht=2\.5ex,dp=1ex,leftskip=0\.5em\]\{palette tertiary\}
\\small\\textit\{#1\}
\\end\{beamercolorbox\}
\}'''

# New bottomnote (template style)
NEW_BOTTOMNOTE = '''% Bottom note command for key takeaways
\\newcommand{\\bottomnote}[1]{%
\\vfill
\\vspace{-2mm}
\\textcolor{mllavender2}{\\rule{\\textwidth}{0.4pt}}
\\vspace{1mm}
\\footnotesize
\\textbf{#1}
}'''

def update_file(filepath):
    """Update bottomnote in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has the old bottomnote style
    if 'beamercolorbox' in content and 'bottomnote' in content:
        # Replace the old bottomnote definition
        new_content = re.sub(OLD_BOTTOMNOTE_PATTERN, NEW_BOTTOMNOTE, content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

    return False

def main():
    print("Updating bottomnote style to template format...")
    print("=" * 60)

    updated = 0
    skipped = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            if update_file(tex_file):
                print(f"Updated: {tex_file.name}")
                updated += 1
            else:
                print(f"Skipped: {tex_file.name} (no match or already updated)")
                skipped += 1

    print("=" * 60)
    print(f"Updated: {updated} files")
    print(f"Skipped: {skipped} files")
    print("\nNew bottomnote style:")
    print("-" * 40)
    print(NEW_BOTTOMNOTE)

if __name__ == '__main__':
    main()
