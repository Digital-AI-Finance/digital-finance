"""
Add template-style bottomnote command to all lesson files in Modules 02, 03, 04.
This adds the bottomnote definition but does NOT add bottomnote calls to frames
(that would require content-aware analysis).

Output: Updates lesson files with bottomnote command definition
"""

from pathlib import Path
import re

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Template bottomnote command (from template_beamer_final.tex)
BOTTOMNOTE_COMMAND = r'''% Bottom note command for key takeaways
\newcommand{\bottomnote}[1]{%
\vfill
\vspace{-2mm}
\textcolor{mllavender2}{\rule{\textwidth}{0.4pt}}
\vspace{1mm}
\footnotesize
\textbf{#1}
}
'''

def has_bottomnote_command(content):
    """Check if file already has bottomnote command defined."""
    return r'\newcommand{\bottomnote}' in content or r'ewcommand{ottomnote}' in content

def add_bottomnote_command(filepath):
    """Add bottomnote command definition to a lesson file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has bottomnote
    if has_bottomnote_command(content):
        return False, "already has bottomnote"

    # Find insertion point: after \setbeamersize or before \title
    # Look for the pattern: \setbeamersize{...}\n\n\title
    insertion_patterns = [
        # After setbeamersize
        (r'(\\setbeamersize\{[^}]+\})\s*\n', r'\1\n\n' + BOTTOMNOTE_COMMAND + '\n'),
        # After setbeamertemplate{itemize items}
        (r'(\\setbeamertemplate\{itemize items\}\[[^\]]+\])\s*\n', r'\1\n\n' + BOTTOMNOTE_COMMAND + '\n'),
        # Before \title
        (r'\n(\\title\{)', '\n' + BOTTOMNOTE_COMMAND + '\n\\1'),
    ]

    new_content = content
    for pattern, replacement in insertion_patterns:
        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content, count=1)
            break

    if new_content == content:
        return False, "could not find insertion point"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "added bottomnote command"

def main():
    print("Adding template-style bottomnote command to Modules 02, 03, 04...")
    print("=" * 70)

    added = 0
    skipped = 0
    errors = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            print(f"Module directory not found: {module_dir}")
            continue

        print(f"\n{module_dir.name}:")
        print("-" * 50)

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            success, message = add_bottomnote_command(tex_file)
            if success:
                print(f"  [ADDED] {tex_file.name}")
                added += 1
            elif "already has" in message:
                print(f"  [SKIP]  {tex_file.name} - {message}")
                skipped += 1
            else:
                print(f"  [ERROR] {tex_file.name} - {message}")
                errors += 1

    print("\n" + "=" * 70)
    print(f"Added:   {added} files")
    print(f"Skipped: {skipped} files (already have bottomnote)")
    print(f"Errors:  {errors} files")
    print("\nNote: This only adds the command definition.")
    print("Bottomnote calls must be added manually to each frame.")

if __name__ == '__main__':
    main()
