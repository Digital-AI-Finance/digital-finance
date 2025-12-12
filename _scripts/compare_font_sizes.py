"""
Compare font sizes and formatting between template_beamer_final.tex and lesson files.
Checks for consistency in:
- Document class font size
- Font size commands used
- bottomnote command implementation
- Other formatting differences
"""

import re
from pathlib import Path
from collections import defaultdict

# Paths
PROJECT_DIR = Path(__file__).parent.parent
TEMPLATE_PATH = PROJECT_DIR / 'template_beamer_final.tex'
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

# Font size commands to check
FONT_SIZE_COMMANDS = [
    r'\\tiny',
    r'\\scriptsize',
    r'\\footnotesize',
    r'\\small',
    r'\\normalsize',
    r'\\large',
    r'\\Large',
    r'\\LARGE',
    r'\\huge',
    r'\\Huge',
]

def extract_document_class(content):
    """Extract document class and options."""
    match = re.search(r'\\documentclass\[(.*?)\]\{(.*?)\}', content)
    if match:
        return {'options': match.group(1), 'class': match.group(2)}
    return None

def extract_bottomnote(content):
    """Extract bottomnote command definition."""
    # Look for the full bottomnote definition
    pattern = r'\\newcommand\{\\bottomnote\}\[1\]\{(.*?)\n\}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return None

def count_font_commands(content):
    """Count occurrences of font size commands."""
    counts = {}
    for cmd in FONT_SIZE_COMMANDS:
        count = len(re.findall(cmd, content))
        if count > 0:
            counts[cmd.replace('\\\\', '\\')] = count
    return counts

def analyze_file(filepath):
    """Analyze a single tex file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': str(e)}

    return {
        'doc_class': extract_document_class(content),
        'bottomnote': extract_bottomnote(content),
        'font_counts': count_font_commands(content),
        'has_scriptsize': '\\scriptsize' in content,
        'has_footnotesize': '\\footnotesize' in content,
        'has_small': '\\small' in content,
    }

def main():
    print("=" * 80)
    print("FONT SIZE AND FORMATTING COMPARISON")
    print("=" * 80)

    # Analyze template
    print("\n" + "=" * 40)
    print("TEMPLATE: template_beamer_final.tex")
    print("=" * 40)

    template_info = analyze_file(TEMPLATE_PATH)

    if 'error' in template_info:
        print(f"ERROR: {template_info['error']}")
        return

    print(f"\nDocument Class: {template_info['doc_class']}")
    print(f"\nFont Size Commands Used:")
    for cmd, count in sorted(template_info['font_counts'].items()):
        print(f"  {cmd}: {count}")

    print(f"\nBottomnote Definition:")
    if template_info['bottomnote']:
        print(template_info['bottomnote'])
    else:
        print("  Not found")

    # Analyze lessons
    print("\n" + "=" * 40)
    print("LESSON FILES COMPARISON")
    print("=" * 40)

    differences = []

    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        tex_files = sorted(module_dir.glob('lesson_*.tex'))

        for tex_file in tex_files:
            lesson_info = analyze_file(tex_file)

            if 'error' in lesson_info:
                print(f"\n{tex_file.name}: ERROR - {lesson_info['error']}")
                continue

            # Check for differences
            issues = []

            # Check document class
            if lesson_info['doc_class'] != template_info['doc_class']:
                issues.append(f"Doc class: {lesson_info['doc_class']} (template: {template_info['doc_class']})")

            # Check bottomnote
            if lesson_info['bottomnote'] != template_info['bottomnote']:
                issues.append("Different bottomnote definition")

            # Check for scriptsize usage (template doesn't use it in bottomnote)
            if lesson_info['has_scriptsize']:
                issues.append(f"Uses \\scriptsize ({lesson_info['font_counts'].get('\\scriptsize', 0)} times)")

            if issues:
                differences.append({
                    'file': tex_file.name,
                    'module': module_dir.name,
                    'issues': issues,
                    'bottomnote': lesson_info['bottomnote'],
                })

    # Summary
    print("\n" + "=" * 40)
    print("SUMMARY OF DIFFERENCES")
    print("=" * 40)

    if not differences:
        print("\nAll lessons match the template!")
    else:
        print(f"\nFound {len(differences)} files with differences:\n")

        for diff in differences:
            print(f"\n{diff['module']}/{diff['file']}:")
            for issue in diff['issues']:
                print(f"  - {issue}")

    # Detailed bottomnote comparison
    print("\n" + "=" * 40)
    print("BOTTOMNOTE IMPLEMENTATION COMPARISON")
    print("=" * 40)

    print("\nTEMPLATE bottomnote:")
    print("-" * 40)
    if template_info['bottomnote']:
        print(template_info['bottomnote'])

    # Show first lesson's bottomnote for comparison
    if differences:
        print("\nSAMPLE LESSON bottomnote (first found):")
        print("-" * 40)
        for diff in differences:
            if diff.get('bottomnote'):
                print(diff['bottomnote'])
                break

    # Recommendations
    print("\n" + "=" * 40)
    print("RECOMMENDATIONS")
    print("=" * 40)

    print("""
1. BOTTOMNOTE DIFFERENCE:
   - Template uses: \\footnotesize + \\textbf{#1}
   - Lessons use: \\small + \\textit{#1} in beamercolorbox

   The template style is:
   - Horizontal line separator
   - Bold text
   - Footnotesize font

   The lesson style is:
   - Colored background box
   - Italic text
   - Small font

   DECISION NEEDED: Which style to standardize on?

2. SCRIPTSIZE USAGE:
   - Lessons use \\scriptsize in column layouts
   - This is appropriate for dense two-column content
   - Template doesn't show this pattern but it's acceptable

3. FONT SIZE HIERARCHY:
   - 8pt base (document class)
   - \\scriptsize for dense columns
   - \\footnotesize for bottomnotes (template)
   - \\small for bottomnotes (current lessons)
""")

if __name__ == '__main__':
    main()
