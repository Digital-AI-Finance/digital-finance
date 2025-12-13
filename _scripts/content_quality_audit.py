"""
Content Quality Audit for Digital Finance Course
Checks pedagogical structure and content quality across all 48 lessons
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


def analyze_lesson_quality(tex_path):
    """Analyze a single lesson for content quality"""
    content = tex_path.read_text(encoding='utf-8', errors='ignore')

    results = {
        'file': tex_path.name,
        'module': tex_path.parent.name,
        'metrics': {},
        'issues': [],
        'warnings': [],
    }

    # 1. Check for title slide
    has_titlepage = r'\titlepage' in content
    results['metrics']['has_titlepage'] = has_titlepage
    if not has_titlepage:
        results['issues'].append("Missing title slide")

    # 2. Check for learning objectives
    has_objectives = 'Learning Objectives' in content or 'learning objectives' in content.lower()
    results['metrics']['has_objectives'] = has_objectives
    if not has_objectives:
        results['issues'].append("Missing learning objectives slide")

    # 3. Count sections
    sections = re.findall(r'\\section\{([^}]+)\}', content)
    results['metrics']['sections'] = len(sections)
    if len(sections) < 2:
        results['warnings'].append(f"Only {len(sections)} sections (recommend 3-5)")

    # 4. Count frames
    frames = len(re.findall(r'\\begin\{frame\}', content))
    results['metrics']['frames'] = frames
    if frames < 10:
        results['warnings'].append(f"Only {frames} frames (minimum 10 recommended)")
    elif frames > 30:
        results['warnings'].append(f"{frames} frames (may be too long)")

    # 5. Check bullet point density
    # Count itemize environments and items within them
    itemize_blocks = re.findall(r'\\begin\{itemize\}(.*?)\\end\{itemize\}', content, re.DOTALL)
    total_items = 0
    max_items_in_block = 0
    for block in itemize_blocks:
        items = block.count(r'\item')
        total_items += items
        max_items_in_block = max(max_items_in_block, items)

    results['metrics']['bullet_points'] = total_items
    results['metrics']['max_bullets_per_list'] = max_items_in_block
    if max_items_in_block > 6:
        results['warnings'].append(f"Dense bullet list ({max_items_in_block} items) - consider splitting")

    # 6. Count charts
    charts = len(re.findall(r'\\includegraphics', content))
    results['metrics']['charts'] = charts

    # 7. Calculate chart ratio
    content_frames = frames - 1  # Exclude title slide
    if content_frames > 0:
        chart_ratio = charts / content_frames
        results['metrics']['chart_ratio'] = round(chart_ratio, 2)
        if chart_ratio < 0.3:
            results['warnings'].append(f"Low chart density ({chart_ratio:.0%}) - consider more visuals")

    # 8. Check for summary/takeaway slide
    has_summary = any(x in content.lower() for x in ['key takeaway', 'summary', 'conclusion', 'recap'])
    results['metrics']['has_summary'] = has_summary
    if not has_summary:
        results['warnings'].append("No summary/takeaway slide detected")

    # 9. Check bottomnote coverage
    bottomnotes = len(re.findall(r'\\bottomnote\{', content))
    results['metrics']['bottomnotes'] = bottomnotes
    if content_frames > 0:
        bn_ratio = bottomnotes / content_frames
        results['metrics']['bottomnote_ratio'] = round(bn_ratio, 2)
        if bn_ratio < 0.8:
            results['warnings'].append(f"Low bottomnote coverage ({bn_ratio:.0%})")

    # 10. Check for code blocks (should be minimal on slides)
    verbatim = len(re.findall(r'\\begin\{verbatim\}|\\begin\{lstlisting\}|\\begin\{minted\}', content))
    results['metrics']['code_blocks'] = verbatim
    if verbatim > 2:
        results['warnings'].append(f"{verbatim} code blocks - prefer charts over code")

    return results


def generate_quality_report(all_results):
    """Generate comprehensive quality report"""
    print("=" * 80)
    print("CONTENT QUALITY AUDIT REPORT")
    print("=" * 80)
    print()

    # Overall statistics
    total_lessons = len(all_results)
    total_frames = sum(r['metrics']['frames'] for r in all_results)
    total_charts = sum(r['metrics']['charts'] for r in all_results)
    total_issues = sum(len(r['issues']) for r in all_results)
    total_warnings = sum(len(r['warnings']) for r in all_results)

    print(f"Total Lessons: {total_lessons}")
    print(f"Total Frames: {total_frames}")
    print(f"Total Charts: {total_charts}")
    print(f"Average frames/lesson: {total_frames/total_lessons:.1f}")
    print(f"Average charts/lesson: {total_charts/total_lessons:.1f}")
    print(f"Total Issues: {total_issues}")
    print(f"Total Warnings: {total_warnings}")
    print()

    # Quality metrics by module
    print("-" * 80)
    print("QUALITY METRICS BY MODULE")
    print("-" * 80)

    for module in MODULES:
        module_results = [r for r in all_results if r['module'] == module]
        frames = sum(r['metrics']['frames'] for r in module_results)
        charts = sum(r['metrics']['charts'] for r in module_results)
        bn = sum(r['metrics']['bottomnotes'] for r in module_results)
        issues = sum(len(r['issues']) for r in module_results)
        warnings = sum(len(r['warnings']) for r in module_results)

        print(f"\n{module}:")
        print(f"  Frames: {frames}, Charts: {charts}, Bottomnotes: {bn}")
        print(f"  Chart ratio: {charts/frames:.0%}")
        print(f"  Issues: {issues}, Warnings: {warnings}")

    # Lessons with issues
    print()
    print("-" * 80)
    print("LESSONS WITH ISSUES")
    print("-" * 80)

    lessons_with_issues = [r for r in all_results if r['issues']]
    if lessons_with_issues:
        for r in lessons_with_issues:
            print(f"\n{r['file']}:")
            for issue in r['issues']:
                print(f"  [ISSUE] {issue}")
    else:
        print("\nNo critical issues found!")

    # Lessons with warnings
    print()
    print("-" * 80)
    print("LESSONS WITH WARNINGS (top 10)")
    print("-" * 80)

    lessons_with_warnings = sorted(
        [r for r in all_results if r['warnings']],
        key=lambda x: len(x['warnings']),
        reverse=True
    )[:10]

    for r in lessons_with_warnings:
        print(f"\n{r['file']} ({len(r['warnings'])} warnings):")
        for w in r['warnings'][:3]:
            print(f"  [WARN] {w}")
        if len(r['warnings']) > 3:
            print(f"  ... and {len(r['warnings'])-3} more")

    # Quality score
    print()
    print("-" * 80)
    print("QUALITY SCORES BY LESSON")
    print("-" * 80)

    def calculate_score(r):
        score = 100
        score -= len(r['issues']) * 20  # Major deductions for issues
        score -= len(r['warnings']) * 5  # Minor deductions for warnings
        return max(0, score)

    scores = [(r['file'], calculate_score(r)) for r in all_results]
    scores.sort(key=lambda x: x[1])

    # Show lowest scoring lessons
    print("\nLowest scoring lessons:")
    for name, score in scores[:5]:
        print(f"  {name}: {score}/100")

    print("\nHighest scoring lessons:")
    for name, score in scores[-5:]:
        print(f"  {name}: {score}/100")

    avg_score = sum(s for _, s in scores) / len(scores)
    print(f"\nAverage quality score: {avg_score:.1f}/100")

    return all_results


def main():
    all_results = []

    for module in MODULES:
        module_path = BASE_DIR / module
        tex_files = sorted(module_path.glob("lesson_*.tex"))

        for tex_file in tex_files:
            results = analyze_lesson_quality(tex_file)
            all_results.append(results)

    generate_quality_report(all_results)


if __name__ == "__main__":
    main()
