"""
Detailed Overflow Analysis Script for Module 01
Analyzes each lesson to identify exact overflow locations and causes.
"""
import subprocess
import re
from pathlib import Path
from dataclasses import dataclass


BASE = Path(r'D:\Joerg\Research\slides\DigitalFinance_3')

LESSONS = [
    'lesson_03_mobile_wallets.tex',
    'lesson_04_neobanks.tex',
    'lesson_05_open_banking.tex',
    'lesson_06_digital_identity.tex',
    'lesson_07_p2p_lending.tex',
    'lesson_08_robo_advisors.tex',
    'lesson_09_insurtech.tex',
    'lesson_10_regtech.tex',
    'lesson_11_regulatory_frameworks.tex',
    'lesson_12_business_models.tex',
]


@dataclass
class Overflow:
    line: int
    amount_pt: float
    frame_title: str
    frame_start: int
    frame_end: int
    content_snippet: str
    figures: list
    recommendation: str


def parse_tex_frames(tex_path):
    """Parse .tex file to extract frame information."""
    content = tex_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    frames = []
    current_frame = None
    frame_start = 0

    for i, line in enumerate(lines, 1):
        # Detect frame start
        if r'\begin{frame}' in line:
            frame_start = i
            # Extract title if present
            title_match = re.search(r'\{([^}]+)\}', line)
            if title_match:
                title = title_match.group(1)
            else:
                title = "(no title)"
            current_frame = {'title': title, 'start': i, 'lines': [], 'figures': []}

        # Detect frame title on next line
        elif current_frame and r'\frametitle{' in line:
            title_match = re.search(r'\\frametitle\{([^}]+)\}', line)
            if title_match:
                current_frame['title'] = title_match.group(1)

        # Collect frame content
        if current_frame:
            current_frame['lines'].append((i, line))

            # Track figures
            fig_match = re.search(r'\\includegraphics.*\{([^}]+)\}', line)
            if fig_match:
                current_frame['figures'].append(fig_match.group(1))

        # Detect frame end
        if r'\end{frame}' in line and current_frame:
            current_frame['end'] = i
            frames.append(current_frame)
            current_frame = None

    return frames, lines


def find_frame_at_line(frames, line_num):
    """Find which frame contains a given line number."""
    for frame in frames:
        if frame['start'] <= line_num <= frame['end']:
            return frame
    return None


def check_figure_exists(tex_path, fig_path):
    """Check if a referenced figure file exists."""
    # Handle relative paths
    if not fig_path.startswith('/') and not fig_path[1:3] == ':\\':
        full_path = tex_path.parent / fig_path
    else:
        full_path = Path(fig_path)

    # Add .pdf extension if missing
    if not full_path.suffix:
        full_path = full_path.with_suffix('.pdf')

    return full_path.exists()


def get_recommendation(overflow_pt, frame, tex_path):
    """Generate fix recommendation based on overflow amount."""
    if overflow_pt > 100:
        return "CRITICAL: Split frame into 2 slides or remove 50%+ content"
    elif overflow_pt > 50:
        return "Reduce chart width to 0.65\\textwidth OR remove 2-3 bullet points"
    elif overflow_pt > 20:
        return "Reduce chart width to 0.75\\textwidth OR remove 1-2 bullet points"
    else:
        return "Minor: Use \\vspace{-2mm} or reduce chart width slightly"


def analyze_lesson(tex_path):
    """Analyze a single lesson for overflow warnings."""
    print(f"\n{'='*70}")
    print(f"ANALYZING: {tex_path.name}")
    print(f"{'='*70}")

    # Run pdflatex
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', str(tex_path)],
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
            timeout=90
        )
    except subprocess.TimeoutExpired:
        print("  TIMEOUT during compilation")
        return []

    # Parse frames
    frames, lines = parse_tex_frames(tex_path)

    # Find overflow warnings
    overflow_pattern = r'Overfull \\vbox \((\d+\.?\d*)pt too high\) detected at line (\d+)'
    overflows = []

    for match in re.finditer(overflow_pattern, result.stdout):
        amount_pt = float(match.group(1))
        line_num = int(match.group(2))

        # Find the frame
        frame = find_frame_at_line(frames, line_num)

        if frame:
            # Get content snippet around the overflow line
            snippet_lines = [l for ln, l in frame['lines'] if abs(ln - line_num) <= 3]
            snippet = '\n'.join(snippet_lines[:5])

            # Check figures
            fig_status = []
            for fig in frame['figures']:
                exists = check_figure_exists(tex_path, fig)
                fig_status.append(f"{fig} ({'EXISTS' if exists else 'MISSING'})")

            overflow = Overflow(
                line=line_num,
                amount_pt=amount_pt,
                frame_title=frame['title'],
                frame_start=frame['start'],
                frame_end=frame['end'],
                content_snippet=snippet,
                figures=fig_status,
                recommendation=get_recommendation(amount_pt, frame, tex_path)
            )
            overflows.append(overflow)
        else:
            overflows.append(Overflow(
                line=line_num,
                amount_pt=amount_pt,
                frame_title="(unknown frame)",
                frame_start=0,
                frame_end=0,
                content_snippet="",
                figures=[],
                recommendation=""
            ))

    return overflows


def print_report(lesson_name, overflows):
    """Print detailed report for a lesson."""
    if not overflows:
        print(f"\n  No overflows detected!")
        return

    print(f"\n  Found {len(overflows)} overflow(s):\n")

    for i, ov in enumerate(overflows, 1):
        print(f"  Overflow {i}: Line {ov.line} ({ov.amount_pt:.1f}pt too high)")
        print(f"    Frame: \"{ov.frame_title}\" (lines {ov.frame_start}-{ov.frame_end})")

        if ov.figures:
            print(f"    Figures:")
            for fig in ov.figures:
                print(f"      - {fig}")

        print(f"    Recommendation: {ov.recommendation}")
        print()


def main():
    print("="*70)
    print("MODULE 01 OVERFLOW DETAILED ANALYSIS")
    print("="*70)

    all_results = {}

    for lesson in LESSONS:
        tex_path = BASE / 'module_01_fintech' / lesson
        if not tex_path.exists():
            print(f"\n  SKIP: {lesson} not found")
            continue

        overflows = analyze_lesson(tex_path)
        all_results[lesson] = overflows
        print_report(lesson, overflows)

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    total_overflows = 0
    critical_count = 0

    for lesson, overflows in all_results.items():
        count = len(overflows)
        total_overflows += count
        critical = sum(1 for ov in overflows if ov.amount_pt > 50)
        critical_count += critical

        status = "OK" if count == 0 else f"{count} overflows ({critical} critical)"
        print(f"  {lesson}: {status}")

    print(f"\n  Total: {total_overflows} overflows ({critical_count} critical)")
    print("="*70)

    return all_results


if __name__ == '__main__':
    main()
