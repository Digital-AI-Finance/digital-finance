"""
Fix corrupted bottomnote commands across all modules.
The issue is backslashes getting corrupted during regex replacement.

This script uses line-by-line replacement to avoid regex escaping issues.
"""

from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Correct bottomnote command - stored as list of lines to avoid escaping issues
CORRECT_BOTTOMNOTE_LINES = [
    '% Bottom note command for key takeaways',
    '\\newcommand{\\bottomnote}[1]{%',
    '\\vfill',
    '\\vspace{-2mm}',
    '\\textcolor{mllavender2}{\\rule{\\textwidth}{0.4pt}}',
    '\\vspace{1mm}',
    '\\footnotesize',
    '\\textbf{#1}',
    '}',
]

def is_corrupted(line):
    """Check if a line contains corrupted LaTeX commands."""
    corrupted_patterns = [
        'ewcommand{',
        'ottomnote}',
        'fill',
        'space{',
        'extcolor{',
        'ule{',
        'extwidth',
        'ootnotesize',
        'extbf{',
    ]
    # Check for pattern without backslash (corruption)
    for pattern in corrupted_patterns:
        if pattern in line and '\\' + pattern[0] not in line:
            # But make sure it's not a valid word
            if pattern == 'fill' and ('vfill' in line or '\\fill' in line):
                continue
            return True
    return False

def fix_file(filepath):
    """Fix corrupted bottomnote in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    # Check if file has corrupted bottomnote
    has_corruption = False
    for line in lines:
        if 'ewcommand' in line and 'ottomnote' in line:
            has_corruption = True
            break
        if 'ewcommand{ottomnote}' in line:
            has_corruption = True
            break

    if not has_corruption:
        return False, "no corruption found"

    # Find and remove the corrupted bottomnote block
    new_lines = []
    i = 0
    found_corrupted = False

    while i < len(lines):
        line = lines[i]

        # Detect start of bottomnote command (comment line)
        if '% Bottom note command for key takeaways' in line:
            found_corrupted = True
            # Add the correct bottomnote
            new_lines.extend(CORRECT_BOTTOMNOTE_LINES)
            new_lines.append('')  # blank line after

            # Skip the corrupted lines until we find closing brace or \title
            i += 1
            while i < len(lines):
                if lines[i].strip() == '}':
                    i += 1
                    break
                if lines[i].strip().startswith('\\title'):
                    break
                # Skip corrupted lines
                if is_corrupted(lines[i]) or lines[i].strip() in ['', '}']:
                    i += 1
                    continue
                # If we hit a normal line, we've gone too far
                if lines[i].strip() and not is_corrupted(lines[i]):
                    break
                i += 1
            continue

        new_lines.append(line)
        i += 1

    if found_corrupted:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        return True, "fixed"

    return False, "no corruption found"

def main():
    print("Fixing corrupted bottomnote commands across all modules...")
    print("=" * 70)

    fixed = 0
    clean = 0

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        print(f"\n{module_dir.name}:")
        print("-" * 50)

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            success, message = fix_file(tex_file)
            if success:
                print(f"  [FIXED] {tex_file.name}")
                fixed += 1
            else:
                print(f"  [CLEAN] {tex_file.name}")
                clean += 1

    print("\n" + "=" * 70)
    print(f"Fixed: {fixed} files")
    print(f"Clean: {clean} files")

if __name__ == '__main__':
    main()
