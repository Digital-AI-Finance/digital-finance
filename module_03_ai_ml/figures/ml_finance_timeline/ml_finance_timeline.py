"""
Evolution of ML in Finance
Historical timeline

Output: ml_finance_timeline.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'ML in Finance Timeline',
    'module': 'module_03_ai_ml',
    'lesson': 25,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/ml_finance_timeline'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 5))

    events = [
        (1980, 'Expert Systems\nfor Credit'),
        (1990, 'Neural Networks\nfor Trading'),
        (2000, 'Statistical\nArbitrage'),
        (2008, 'HFT\nAlgorithms'),
        (2012, 'Deep Learning\nBreakthrough'),
        (2016, 'Robo-Advisors\nMainstream'),
        (2020, 'GPT/LLMs\nin Finance'),
        (2024, 'AI Agents\n& Automation')
    ]

    years = [e[0] for e in events]
    labels = [e[1] for e in events]

    # Timeline
    ax.plot([1975, 2028], [0, 0], 'k-', linewidth=2)

    # Events
    for i, (year, label) in enumerate(events):
        y_offset = 0.3 if i % 2 == 0 else -0.3
        ax.scatter(year, 0, s=150, color='#4A90E2', zorder=5)
        ax.plot([year, year], [0, y_offset * 0.8], 'k-', linewidth=1)
        ax.text(year, y_offset, label, ha='center', va='center' if y_offset > 0 else 'top',
                fontsize=9, fontweight='bold')

    ax.set_xlim(1975, 2028)
    ax.set_ylim(-0.6, 0.6)
    ax.axis('off')
    ax.set_title('Evolution of Machine Learning in Finance', fontsize=14, fontweight='bold', pad=20)

    # Year markers
    for year in range(1980, 2025, 10):
        ax.text(year, -0.45, str(year), ha='center', fontsize=9, color='#666666')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_finance_timeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
