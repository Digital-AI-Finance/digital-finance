"""
Template Compliance Analysis for Digital Finance Course
Checks all 48 lessons against template_beamer_final.tex standards

Requirements from template:
- Document: 8pt, aspectratio=169, beamer, Madrid theme
- Colors: mlblue, mlpurple, mllavender, mlorange, mlgreen, mlred
- Commands: \bottomnote{} on content slides
- Frame alignment: [t] option for top alignment
- Two-column: [T] with 0.48\textwidth
- Charts: Various widths (0.60-0.95\textwidth)
- Tables: booktabs (\toprule, \midrule, \bottomrule)
- Margins: 5mm left/right
"""

from pathlib import Path
import re
from collections import defaultdict
import json

BASE_DIR = Path(r"D:\Joerg\Research\slides\DigitalFinance_3")
MODULES = [
    "module_01_fintech",
    "module_02_blockchain",
    "module_03_ai_ml",
    "module_04_traditional"
]

# Template requirements
REQUIRED_SETTINGS = {
    'document_class': r'\\documentclass\[8pt,aspectratio=169\]\{beamer\}',
    'theme': r'\\usetheme\{Madrid\}',
    # Match both \usepackage{booktabs} and \usepackage{...,booktabs,...}
    'booktabs': r'\\usepackage\{[^}]*booktabs[^}]*\}',
    'graphicx': r'\\usepackage\{[^}]*graphicx[^}]*\}',
}

REQUIRED_COLORS = ['mlblue', 'mlpurple', 'mllavender', 'mlorange', 'mlgreen', 'mlred']

REQUIRED_COMMANDS = {
    'bottomnote': r'\\newcommand\{\\bottomnote\}',
}

def analyze_lesson(tex_path):
    """Analyze a single lesson for template compliance"""
    content = tex_path.read_text(encoding='utf-8', errors='ignore')

    results = {
        'file': tex_path.name,
        'module': tex_path.parent.name,
        'settings': {},
        'colors': {},
        'commands': {},
        'frames': {
            'total': 0,
            'with_t_option': 0,
            'with_bottomnote': 0,
            'plain_frames': 0,
        },
        'charts': {
            'total': 0,
            'widths': defaultdict(int),
            'in_figures_folder': 0,
            'other_location': 0,
        },
        'columns': {
            'total': 0,
            'with_T_option': 0,
            'widths': defaultdict(int),
        },
        'tables': {
            'total': 0,
            'with_booktabs': 0,
            'with_hline': 0,
        },
        'issues': [],
    }

    # Check document settings
    for name, pattern in REQUIRED_SETTINGS.items():
        results['settings'][name] = bool(re.search(pattern, content))
        if not results['settings'][name]:
            results['issues'].append(f"Missing/incorrect: {name}")

    # Check colors defined
    for color in REQUIRED_COLORS:
        results['colors'][color] = f'\\definecolor{{{color}}}' in content

    # Check commands defined
    for name, pattern in REQUIRED_COMMANDS.items():
        results['commands'][name] = bool(re.search(pattern, content))

    # Analyze frames
    frames = re.findall(r'\\begin\{frame\}(\[[^\]]*\])?\{([^}]*)\}', content)
    plain_frames = len(re.findall(r'\\begin\{frame\}\[plain\]', content))
    results['frames']['total'] = len(frames) + plain_frames
    results['frames']['plain_frames'] = plain_frames

    # Count frames with [t] option
    t_frames = len(re.findall(r'\\begin\{frame\}\[t[,\]]', content))
    t_frames += len(re.findall(r'\\begin\{frame\}\[[^\]]*t[^\]]*\]', content))
    results['frames']['with_t_option'] = t_frames

    # Count bottomnotes
    bottomnotes = len(re.findall(r'\\bottomnote\{', content))
    results['frames']['with_bottomnote'] = bottomnotes

    # Analyze charts (includegraphics)
    chart_matches = re.findall(r'\\includegraphics\[([^\]]*)\]\{([^}]*)\}', content)
    results['charts']['total'] = len(chart_matches)

    for options, path in chart_matches:
        # Extract width
        width_match = re.search(r'width=([0-9.]+)\\textwidth', options)
        if width_match:
            width = width_match.group(1)
            results['charts']['widths'][width] += 1

        # Check if in figures folder
        if 'figures/' in path:
            results['charts']['in_figures_folder'] += 1
        else:
            results['charts']['other_location'] += 1

    # Analyze columns
    columns_env = re.findall(r'\\begin\{columns\}(\[[^\]]*\])?', content)
    results['columns']['total'] = len(columns_env)

    for opts in columns_env:
        if opts and 'T' in opts:
            results['columns']['with_T_option'] += 1

    # Column widths
    col_widths = re.findall(r'\\column\{([0-9.]+)\\textwidth\}', content)
    for w in col_widths:
        results['columns']['widths'][w] += 1

    # Analyze tables
    tables = len(re.findall(r'\\begin\{tabular\}', content))
    results['tables']['total'] = tables
    results['tables']['with_booktabs'] = len(re.findall(r'\\toprule|\\midrule|\\bottomrule', content)) > 0
    results['tables']['with_hline'] = len(re.findall(r'\\hline', content)) > 0

    if results['tables']['with_hline'] and tables > 0:
        results['issues'].append("Uses \\hline instead of booktabs")

    # Check for common issues
    content_frames = results['frames']['total'] - results['frames']['plain_frames']
    if content_frames > 0:
        bottomnote_ratio = bottomnotes / content_frames
        if bottomnote_ratio < 0.5:
            results['issues'].append(f"Low bottomnote usage: {bottomnotes}/{content_frames} frames ({bottomnote_ratio:.0%})")

    if results['frames']['with_t_option'] < results['frames']['total'] * 0.3:
        results['issues'].append("Few frames use [t] alignment option")

    return results


def analyze_all_lessons():
    """Analyze all 48 lessons"""
    all_results = []

    for module in MODULES:
        module_path = BASE_DIR / module
        tex_files = sorted(module_path.glob("lesson_*.tex"))

        for tex_file in tex_files:
            results = analyze_lesson(tex_file)
            all_results.append(results)

    return all_results


def generate_report(all_results):
    """Generate comprehensive compliance report"""
    print("=" * 80)
    print("TEMPLATE COMPLIANCE ANALYSIS REPORT")
    print("=" * 80)
    print()

    # Summary statistics
    total_lessons = len(all_results)
    total_frames = sum(r['frames']['total'] for r in all_results)
    total_charts = sum(r['charts']['total'] for r in all_results)
    total_bottomnotes = sum(r['frames']['with_bottomnote'] for r in all_results)

    print(f"Total Lessons: {total_lessons}")
    print(f"Total Frames: {total_frames}")
    print(f"Total Charts: {total_charts}")
    print(f"Total Bottomnotes: {total_bottomnotes}")
    print()

    # Settings compliance
    print("-" * 80)
    print("DOCUMENT SETTINGS COMPLIANCE")
    print("-" * 80)

    for setting in REQUIRED_SETTINGS.keys():
        compliant = sum(1 for r in all_results if r['settings'].get(setting, False))
        print(f"  {setting}: {compliant}/{total_lessons} ({compliant/total_lessons*100:.0f}%)")
    print()

    # Color definitions
    print("-" * 80)
    print("COLOR DEFINITIONS")
    print("-" * 80)

    for color in REQUIRED_COLORS:
        defined = sum(1 for r in all_results if r['colors'].get(color, False))
        print(f"  {color}: {defined}/{total_lessons}")
    print()

    # Bottomnote usage
    print("-" * 80)
    print("BOTTOMNOTE USAGE BY MODULE")
    print("-" * 80)

    for module in MODULES:
        module_results = [r for r in all_results if r['module'] == module]
        frames = sum(r['frames']['total'] - r['frames']['plain_frames'] for r in module_results)
        notes = sum(r['frames']['with_bottomnote'] for r in module_results)
        ratio = notes / frames * 100 if frames > 0 else 0
        print(f"  {module}: {notes}/{frames} frames ({ratio:.0f}%)")
    print()

    # Chart width distribution
    print("-" * 80)
    print("CHART WIDTH DISTRIBUTION")
    print("-" * 80)

    width_totals = defaultdict(int)
    for r in all_results:
        for w, count in r['charts']['widths'].items():
            width_totals[w] += count

    for width in sorted(width_totals.keys(), key=lambda x: float(x), reverse=True):
        count = width_totals[width]
        bar = "#" * (count // 5)
        print(f"  {width}\\textwidth: {count:3d} {bar}")
    print()

    # Column alignment
    print("-" * 80)
    print("COLUMN ALIGNMENT ([T] OPTION)")
    print("-" * 80)

    total_columns = sum(r['columns']['total'] for r in all_results)
    with_T = sum(r['columns']['with_T_option'] for r in all_results)
    print(f"  Columns with [T]: {with_T}/{total_columns} ({with_T/total_columns*100:.0f}%)" if total_columns > 0 else "  No columns found")
    print()

    # Column widths
    print("-" * 80)
    print("COLUMN WIDTH DISTRIBUTION")
    print("-" * 80)

    col_width_totals = defaultdict(int)
    for r in all_results:
        for w, count in r['columns']['widths'].items():
            col_width_totals[w] += count

    for width in sorted(col_width_totals.keys(), key=lambda x: float(x), reverse=True):
        count = col_width_totals[width]
        print(f"  {width}\\textwidth: {count}")
    print()

    # Table analysis
    print("-" * 80)
    print("TABLE FORMATTING")
    print("-" * 80)

    total_tables = sum(r['tables']['total'] for r in all_results)
    with_booktabs = sum(1 for r in all_results if r['tables']['with_booktabs'])
    with_hline = sum(1 for r in all_results if r['tables']['with_hline'])
    print(f"  Total lessons with tables: {sum(1 for r in all_results if r['tables']['total'] > 0)}")
    print(f"  Using booktabs: {with_booktabs}")
    print(f"  Using \\hline (not recommended): {with_hline}")
    print()

    # Issues summary
    print("-" * 80)
    print("ISSUES BY MODULE")
    print("-" * 80)

    for module in MODULES:
        module_results = [r for r in all_results if r['module'] == module]
        issues = []
        for r in module_results:
            for issue in r['issues']:
                issues.append(f"  {r['file']}: {issue}")

        print(f"\n{module} ({len(issues)} issues):")
        if issues:
            for issue in issues[:5]:  # Show first 5
                print(issue)
            if len(issues) > 5:
                print(f"  ... and {len(issues)-5} more")
        else:
            print("  No issues found")

    print()
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)

    # Generate recommendations
    recommendations = []

    bottomnote_ratio = total_bottomnotes / (total_frames - sum(r['frames']['plain_frames'] for r in all_results))
    if bottomnote_ratio < 0.8:
        recommendations.append(f"- Add \\bottomnote{{}} to more frames (current: {bottomnote_ratio:.0%})")

    if width_totals.get('0.65', 0) > width_totals.get('0.60', 0):
        recommendations.append("- Consider using 0.60\\textwidth as standard chart width (prevents overflow)")

    if with_T / total_columns < 0.9 if total_columns > 0 else False:
        recommendations.append("- Use [T] option on all \\begin{columns} for top alignment")

    if with_hline > 0:
        recommendations.append("- Replace \\hline with booktabs (\\toprule, \\midrule, \\bottomrule)")

    for rec in recommendations:
        print(rec)

    if not recommendations:
        print("No major issues found - templates are well-followed!")

    print()
    return all_results


def save_detailed_report(all_results, output_path):
    """Save detailed JSON report"""
    # Convert defaultdicts to regular dicts for JSON
    for r in all_results:
        r['charts']['widths'] = dict(r['charts']['widths'])
        r['columns']['widths'] = dict(r['columns']['widths'])

    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"Detailed report saved to: {output_path}")


if __name__ == "__main__":
    print("Analyzing 48 lessons for template compliance...\n")
    results = analyze_all_lessons()
    generate_report(results)

    # Save detailed JSON
    output_path = BASE_DIR / "_scripts" / "template_compliance_report.json"
    save_detailed_report(results, output_path)
