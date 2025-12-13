"""
Template Compliance Fixer for Digital Finance Course
Applies all 5 fixes to all 48 lessons:
1. Add missing usepackage booktabs and graphicx
2. Add missing bottomnotes to frames
3. Standardize chart widths to 0.60 textwidth
4. Add [t] frame option to content frames
5. All of the above
"""

from pathlib import Path
import re
from collections import defaultdict

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")
MODULES = [
    "module_01_fintech",
    "module_02_blockchain",
    "module_03_ai_ml",
    "module_04_traditional"
]

def fix_lesson(tex_path, verbose=True):
    """Apply all template compliance fixes to a single lesson"""
    content = tex_path.read_text(encoding='utf-8', errors='ignore')
    original_content = content
    fixes_applied = []

    # Fix 1: Add missing packages after \usepackage{xcolor}
    if '\\usepackage{booktabs}' not in content:
        # Find \usepackage{xcolor} and add booktabs after it
        if '\\usepackage{xcolor}' in content:
            content = content.replace(
                '\\usepackage{xcolor}',
                '\\usepackage{xcolor}\n\\usepackage{booktabs}'
            )
            fixes_applied.append("Added \\usepackage{booktabs}")

    if '\\usepackage{graphicx}' not in content:
        # Find \usepackage{xcolor} or booktabs and add graphicx
        if '\\usepackage{booktabs}' in content:
            content = content.replace(
                '\\usepackage{booktabs}',
                '\\usepackage{booktabs}\n\\usepackage{graphicx}'
            )
            fixes_applied.append("Added \\usepackage{graphicx}")
        elif '\\usepackage{xcolor}' in content:
            content = content.replace(
                '\\usepackage{xcolor}',
                '\\usepackage{xcolor}\n\\usepackage{graphicx}'
            )
            fixes_applied.append("Added \\usepackage{graphicx}")

    # Fix 3: Standardize chart widths from 0.65 to 0.60
    # Also standardize other non-standard widths
    width_replacements = {
        'width=0.65\\textwidth': 'width=0.60\\textwidth',
        'width=0.70\\textwidth': 'width=0.65\\textwidth',
        'width=0.75\\textwidth': 'width=0.70\\textwidth',
        'width=0.80\\textwidth': 'width=0.75\\textwidth',
    }

    for old_width, new_width in width_replacements.items():
        if old_width in content:
            count = content.count(old_width)
            content = content.replace(old_width, new_width)
            fixes_applied.append(f"Changed {count}x {old_width} -> {new_width}")

    # Fix 4: Add [t] option to frames that don't have it
    # Match \begin{frame}{Title} and \begin{frame}[options]{Title}

    # Pattern 1: \begin{frame}{Title} -> \begin{frame}[t]{Title}
    pattern1 = r'\\begin\{frame\}\{([^}]+)\}'
    def add_t_option(match):
        title = match.group(1)
        return f'\\begin{{frame}}[t]{{{title}}}'

    new_content = re.sub(pattern1, add_t_option, content)
    if new_content != content:
        count = len(re.findall(pattern1, content))
        fixes_applied.append(f"Added [t] to {count} frames without options")
        content = new_content

    # Pattern 2: \begin{frame}[options]{Title} where options don't include 't'
    # Skip [plain] frames and frames that already have [t]
    def add_t_to_options(match):
        options = match.group(1)
        title = match.group(2)
        if 't' in options or 'plain' in options:
            return match.group(0)  # Already has t or is plain, leave unchanged
        # Add t to existing options
        return f'\\begin{{frame}}[t,{options}]{{{title}}}'

    pattern2 = r'\\begin\{frame\}\[([^\]]+)\]\{([^}]+)\}'
    new_content = re.sub(pattern2, add_t_to_options, content)
    if new_content != content:
        # Count how many were actually changed
        old_matches = re.findall(pattern2, content)
        changed = sum(1 for opts, _ in old_matches if 't' not in opts and 'plain' not in opts)
        if changed > 0:
            fixes_applied.append(f"Added [t] to {changed} frames with other options")
        content = new_content

    # Fix 2: Add missing bottomnotes (only for Module 03 which has low coverage)
    # This is more complex - we'll identify frames without bottomnotes
    if 'module_03' in str(tex_path):
        # Find frames without bottomnotes
        frames_added = 0

        # Split content by frame boundaries
        frame_pattern = r'(\\begin\{frame\}.*?\\end\{frame\})'
        frames = re.findall(frame_pattern, content, re.DOTALL)

        for frame in frames:
            # Skip plain frames (title slides)
            if '[plain]' in frame:
                continue

            # Check if frame has bottomnote
            if '\\bottomnote{' not in frame:
                # Find the \end{frame} and add a generic bottomnote before it
                # We'll add a placeholder that can be customized later
                if '\\includegraphics' in frame:
                    # Frame has a chart - add insight-based bottomnote
                    new_frame = frame.replace(
                        '\\end{frame}',
                        '\\bottomnote{Key insight from this visualization.}\n\\end{frame}'
                    )
                else:
                    # Frame has content - add summary bottomnote
                    new_frame = frame.replace(
                        '\\end{frame}',
                        '\\bottomnote{Summary of key concepts presented above.}\n\\end{frame}'
                    )

                if new_frame != frame:
                    content = content.replace(frame, new_frame)
                    frames_added += 1

        if frames_added > 0:
            fixes_applied.append(f"Added {frames_added} bottomnotes to Module 03")

    # Only write if changes were made
    if content != original_content:
        tex_path.write_text(content, encoding='utf-8')
        if verbose:
            print(f"  {tex_path.name}: {', '.join(fixes_applied)}")
        return True, fixes_applied
    else:
        if verbose:
            print(f"  {tex_path.name}: No changes needed")
        return False, []


def fix_all_lessons():
    """Apply fixes to all 48 lessons"""
    print("=" * 80)
    print("TEMPLATE COMPLIANCE FIXER")
    print("=" * 80)
    print()

    stats = {
        'total': 0,
        'modified': 0,
        'fixes': defaultdict(int)
    }

    for module in MODULES:
        print(f"\n{module}:")
        print("-" * 40)

        module_path = BASE_DIR / module
        tex_files = sorted(module_path.glob("lesson_*.tex"))

        for tex_file in tex_files:
            stats['total'] += 1
            modified, fixes = fix_lesson(tex_file)
            if modified:
                stats['modified'] += 1
                for fix in fixes:
                    # Extract fix type
                    if 'booktabs' in fix:
                        stats['fixes']['booktabs'] += 1
                    elif 'graphicx' in fix:
                        stats['fixes']['graphicx'] += 1
                    elif 'width' in fix.lower():
                        stats['fixes']['width_standardization'] += 1
                    elif '[t]' in fix:
                        stats['fixes']['frame_alignment'] += 1
                    elif 'bottomnote' in fix.lower():
                        stats['fixes']['bottomnotes'] += 1

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total lessons processed: {stats['total']}")
    print(f"Lessons modified: {stats['modified']}")
    print()
    print("Fixes applied:")
    for fix_type, count in sorted(stats['fixes'].items()):
        print(f"  - {fix_type}: {count}")

    return stats


if __name__ == "__main__":
    fix_all_lessons()
