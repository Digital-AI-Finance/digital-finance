"""
Fix corrupted bottomnote commands in lesson files.
The previous script corrupted backslashes - this fixes them.
"""

from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Correct bottomnote command (template style)
CORRECT_BOTTOMNOTE = r'''% Bottom note command for key takeaways
\newcommand{\bottomnote}[1]{%
\vfill
\vspace{-2mm}
\textcolor{mllavender2}{\rule{\textwidth}{0.4pt}}
\vspace{1mm}
\footnotesize
\textbf{#1}
}'''

def fix_file(filepath):
    """Fix corrupted bottomnote in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has corrupted bottomnote (missing backslashes)
    if 'ewcommand{ottomnote}' in content or 'ewcommand{\x08ottomnote}' in content:
        # Find the corrupted section and replace it
        lines = content.split('\n')
        new_lines = []
        skip_until_closing_brace = False
        found_corrupted = False

        i = 0
        while i < len(lines):
            line = lines[i]

            # Detect start of corrupted bottomnote
            if '% Bottom note command for key takeaways' in line:
                # Skip all lines until we find the closing brace of the command
                found_corrupted = True
                # Add the correct bottomnote
                new_lines.append(CORRECT_BOTTOMNOTE)
                # Skip until we find '}' on its own line or similar pattern
                i += 1
                while i < len(lines):
                    if lines[i].strip() == '}':
                        i += 1
                        break
                    # Also check for line starting with \title which means we went too far
                    if lines[i].strip().startswith('\\title'):
                        break
                    i += 1
                continue

            new_lines.append(line)
            i += 1

        if found_corrupted:
            new_content = '\n'.join(new_lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

    return False

def main():
    print("Fixing corrupted bottomnote commands...")
    print("=" * 60)

    fixed = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            if fix_file(tex_file):
                print(f"Fixed: {tex_file.name}")
                fixed += 1

    print("=" * 60)
    print(f"Fixed: {fixed} files")

if __name__ == '__main__':
    main()
