"""
Fix duplicate/orphaned bottomnote code in lesson files.
Some files have duplicate bottomnote definitions or orphaned code fragments.
"""

from pathlib import Path
import re

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Correct bottomnote command block
CORRECT_BOTTOMNOTE = '''% Bottom note command for key takeaways
\\newcommand{\\bottomnote}[1]{%
\\vfill
\\vspace{-2mm}
\\textcolor{mllavender2}{\\rule{\\textwidth}{0.4pt}}
\\vspace{1mm}
\\footnotesize
\\textbf{#1}
}'''

def fix_file(filepath):
    """Fix duplicate bottomnote definitions in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern to find the bottomnote definition and any orphaned code after it
    # Look for the pattern: bottomnote def + orphaned \vfill...\textbf{#1} }
    pattern = r'(% Bottom note command for key takeaways\n\\newcommand\{\\bottomnote\}\[1\]\{%\n\\vfill\n\\vspace\{-2mm\}\n\\textcolor\{mllavender2\}\{\\rule\{\\textwidth\}\{0\.4pt\}\}\n\\vspace\{1mm\}\n\\footnotesize\n\\textbf\{#1\}\n\})\s*\n\s*(\\vfill\n\\vspace\{-2mm\}\n\\textcolor\{mllavender2\}\{\\rule\{\\textwidth\}\{0\.4pt\}\}\n\\vspace\{1mm\}\n\\footnotesize\n\\textbf\{#1\}\n\})'

    # Try to match and remove the duplicate
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1', content)

    # Alternative: just look for orphaned \vfill blocks before \title
    # Pattern: } followed by orphaned bottomnote code before \title
    orphan_pattern = r'\}\s*\n\s*(\\vfill\n\\vspace\{-2mm\}\n\\textcolor\{mllavender2\}\{\\rule\{\\textwidth\}\{0\.4pt\}\}\n\\vspace\{1mm\}\n\\footnotesize\n\\textbf\{#1\}\n\})\s*\n\s*(\\title)'

    if re.search(orphan_pattern, content):
        content = re.sub(orphan_pattern, r'}\n\n\2', content)

    # Simpler approach: find and remove any line-by-line orphaned code
    lines = content.split('\n')
    new_lines = []
    i = 0
    in_orphan = False
    brace_depth = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is the start of the bottomnote command
        if '% Bottom note command for key takeaways' in line:
            # Add the command block
            new_lines.append(line)
            i += 1
            # Continue until we find the closing brace
            while i < len(lines) and lines[i].strip() != '}':
                new_lines.append(lines[i])
                i += 1
            if i < len(lines):
                new_lines.append(lines[i])  # Add closing brace
                i += 1

            # Now skip any orphaned duplicate code
            while i < len(lines):
                next_line = lines[i].strip()
                # Skip empty lines
                if not next_line:
                    i += 1
                    continue
                # If we hit \title, we're done skipping
                if next_line.startswith('\\title'):
                    break
                # If it looks like orphaned bottomnote code, skip it
                if next_line in ['\\vfill', '\\vspace{-2mm}', '\\vspace{1mm}',
                                 '\\footnotesize', '\\textbf{#1}', '}'] or \
                   '\\textcolor{mllavender2}' in next_line or \
                   '\\rule{\\textwidth}' in next_line:
                    i += 1
                    continue
                # Otherwise, we're past the orphan
                break
            continue

        new_lines.append(line)
        i += 1

    new_content = '\n'.join(new_lines)

    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    print("Fixing duplicate bottomnote definitions...")
    print("=" * 70)

    fixed = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        print(f"\n{module_dir.name}:")
        print("-" * 50)

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            if fix_file(tex_file):
                print(f"  [FIXED] {tex_file.name}")
                fixed += 1
            else:
                print(f"  [OK]    {tex_file.name}")

    print("\n" + "=" * 70)
    print(f"Fixed: {fixed} files")

if __name__ == '__main__':
    main()
