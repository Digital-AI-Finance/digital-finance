"""
Fix overflow warnings in lesson files.
Main strategies:
1. Reduce chart widths (0.72 -> 0.65, 0.65 -> 0.55)
2. Add [t] option to frames if missing
3. Reduce vspace values
"""

from pathlib import Path
import re
import subprocess

PROJECT_DIR = Path(__file__).parent.parent
MODULE_DIRS = [
    PROJECT_DIR / 'module_01_fintech',
    PROJECT_DIR / 'module_02_blockchain',
    PROJECT_DIR / 'module_03_ai_ml',
    PROJECT_DIR / 'module_04_traditional',
]

def check_overflows(tex_path):
    """Compile and count overflow warnings."""
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=tex_path.parent
        )
        output = result.stdout + result.stderr
        overflows = len(re.findall(r'Overfull', output))
        return overflows
    except Exception as e:
        return -1

def fix_file(filepath):
    """Apply overflow fixes to a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    fixes_applied = []

    # Fix 1: Reduce large chart widths
    # 0.75 -> 0.65
    if '0.75\\textwidth' in content:
        content = content.replace('0.75\\textwidth', '0.65\\textwidth')
        fixes_applied.append('reduced 0.75 to 0.65')

    # 0.72 -> 0.65
    if '0.72\\textwidth' in content:
        content = content.replace('0.72\\textwidth', '0.65\\textwidth')
        fixes_applied.append('reduced 0.72 to 0.65')

    # 0.70 -> 0.65
    if '0.70\\textwidth' in content:
        content = content.replace('0.70\\textwidth', '0.65\\textwidth')
        fixes_applied.append('reduced 0.70 to 0.65')

    # Fix 2: Reduce vspace values that are too large
    # \vspace{8mm} -> \vspace{5mm}
    content = re.sub(r'\\vspace\{8mm\}', r'\\vspace{5mm}', content)
    # \vspace{10mm} -> \vspace{5mm}
    content = re.sub(r'\\vspace\{10mm\}', r'\\vspace{5mm}', content)

    # Fix 3: Add [t] to frames without positioning
    # \begin{frame}{Title} -> \begin{frame}[t]{Title}
    content = re.sub(
        r'\\begin\{frame\}\{([^}]+)\}',
        r'\\begin{frame}[t]{\1}',
        content
    )
    # But don't duplicate [t] if already there
    content = content.replace('[t][t]', '[t]')
    content = content.replace('[T][t]', '[T]')

    # Fix 4: Reduce footnotesize blocks that might overflow
    # Already using footnotesize in bottomnote, that's fine

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, fixes_applied

    return False, []

def main():
    print("Fixing overflow warnings...")
    print("=" * 70)

    lessons_with_overflows = []

    # First pass: identify lessons with overflows
    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue

        tex_files = sorted(module_dir.glob('lesson_*.tex'))
        for tex_file in tex_files:
            overflows = check_overflows(tex_file)
            if overflows > 0:
                lessons_with_overflows.append((tex_file, overflows))

    print(f"Found {len(lessons_with_overflows)} lessons with overflows")
    print("-" * 70)

    # Second pass: apply fixes
    fixed = 0
    for tex_file, initial_overflows in lessons_with_overflows:
        print(f"\n{tex_file.name} ({initial_overflows} overflows):")

        modified, fixes = fix_file(tex_file)
        if modified:
            print(f"  Applied fixes: {', '.join(fixes) if fixes else 'spacing adjustments'}")

            # Recompile to check
            new_overflows = check_overflows(tex_file)
            if new_overflows < initial_overflows:
                print(f"  Reduced: {initial_overflows} -> {new_overflows}")
                fixed += 1
            elif new_overflows == 0:
                print(f"  FIXED: 0 overflows")
                fixed += 1
            else:
                print(f"  Still has {new_overflows} overflows")
        else:
            print(f"  No automatic fixes available")

    print("\n" + "=" * 70)
    print(f"Fixed/improved: {fixed} lessons")

    # Final check
    print("\nFinal status:")
    remaining = 0
    for module_dir in MODULE_DIRS:
        if not module_dir.exists():
            continue
        tex_files = sorted(module_dir.glob('lesson_*.tex'))
        for tex_file in tex_files:
            overflows = check_overflows(tex_file)
            if overflows > 0:
                print(f"  {tex_file.name}: {overflows} overflows")
                remaining += overflows

    print(f"\nTotal remaining overflows: {remaining}")

if __name__ == '__main__':
    main()
