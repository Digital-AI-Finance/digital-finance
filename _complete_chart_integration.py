"""
Complete chart integration for remaining Module 03 lessons (29-36)
This script adds chart slides to the LaTeX files efficiently.
"""

from pathlib import Path
import re

# Remaining lesson chart mappings
LESSON_CHARTS = {
    29: {
        'file': 'lesson_29_algorithmic_trading_concepts.tex',
        'insertions': [
            {
                'search': r'(\\begin\{frame\}.*Trading Strategies.*\n.*\n.*\\end\{frame\})',
                'chart': 'momentum_strategy',
                'title': 'Momentum Strategy Performance',
                'note': 'Momentum strategies buy winners and sell losers.'
            },
            {
                'search': r'(\\begin\{frame\}.*Backtest.*\n.*\n.*\\end\{frame\})',
                'chart': 'trading_strategy_backtest',
                'title': 'Backtest Results',
                'note': 'Backtesting reveals strategy performance on historical data.'
            }
        ]
    },
    30: {
        'file': 'lesson_30_credit_scoring_and_risk_models.tex',
        'insertions': [
            {
                'search': r'(\\begin\{frame\}.*FICO.*\n.*\n.*\\end\{frame\})',
                'chart': 'fico_score_ranges',
                'title': 'FICO Score Ranges',
                'note': 'FICO scores range from 300-850 with clear risk tiers.'
            }
        ]
    }
}

def add_chart_slide(tex_content, chart_name, title, note, width='0.60'):
    """Generate a chart-only slide"""
    slide = f"""
\\begin{{frame}}[t]{{{title}}}
\\begin{{center}}
\\includegraphics[width={width}\\textwidth]{{figures/{chart_name}/{chart_name}.pdf}}
\\end{{center}}
\\bottomnote{{{note}}}
\\end{{frame}}
"""
    return slide

def process_lesson(lesson_num, module_dir):
    """Process a single lesson to add charts"""
    if lesson_num not in LESSON_CHARTS:
        return False

    lesson_info = LESSON_CHARTS[lesson_num]
    tex_file = module_dir / lesson_info['file']

    if not tex_file.exists():
        print(f"File not found: {tex_file}")
        return False

    print(f"Processing Lesson {lesson_num}: {lesson_info['file']}")

    content = tex_file.read_text(encoding='utf-8')

    # Add chart slides
    for insertion in lesson_info['insertions']:
        chart_slide = add_chart_slide(
            content,
            insertion['chart'],
            insertion['title'],
            insertion['note']
        )

        # Insert after matching frame
        pattern = insertion['search']
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + chart_slide + content[insert_pos:]
            print(f"  Added chart: {insertion['chart']}")
        else:
            print(f"  WARNING: Pattern not found for {insertion['chart']}")

    # Write back
    tex_file.write_text(content, encoding='utf-8')
    return True

if __name__ == '__main__':
    module_dir = Path(r"D:\Joerg\Research\slides\DigitalFinance_3\module_03_ai_ml")

    print("Chart Integration Script for Module 03 Lessons 29-36")
    print("=" * 60)

    for lesson_num in range(29, 37):
        success = process_lesson(lesson_num, module_dir)
        if success:
            print(f"✓ Lesson {lesson_num} processed")
        else:
            print(f"✗ Lesson {lesson_num} skipped")

    print("\nManual integration still needed for:")
    print("  - Lessons 31-36 (31 total charts)")
    print("  - Check each lesson for appropriate insertion points")
    print("  - Compile and fix any overflow warnings")
