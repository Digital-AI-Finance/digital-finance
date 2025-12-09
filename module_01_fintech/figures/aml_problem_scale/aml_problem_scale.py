"""
AML Problem Scale
Shows the scale of money laundering and detection challenges

Output: aml_problem_scale.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'AML Problem Scale',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/aml_problem_scale'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create AML problem scale diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The Scale of Money Laundering', fontsize=20, fontweight='bold', ha='center')

    # Key statistics boxes
    stats = [
        {
            'value': '$2-5 Trillion',
            'desc': 'Laundered annually\n(2-5% of global GDP)',
            'x': 3.5, 'y': 6.5, 'color': '#D62728'
        },
        {
            'value': '<1%',
            'desc': 'Detected by\ncurrent systems',
            'x': 10.5, 'y': 6.5, 'color': '#FF7F0E'
        },
    ]

    for stat in stats:
        box = mpatches.FancyBboxPatch((stat['x']-2.5, stat['y']-1.5), 5, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=stat['color'], alpha=0.15,
                                       edgecolor=stat['color'], lw=3)
        ax.add_patch(box)
        ax.text(stat['x'], stat['y']+0.7, stat['value'], ha='center',
               fontsize=24, fontweight='bold', color=stat['color'])
        ax.text(stat['x'], stat['y']-0.5, stat['desc'], ha='center', fontsize=12)

    # Detection challenges
    challenges = [
        {'issue': 'False Positives', 'rate': '95-99%', 'desc': 'Manual review burden'},
        {'issue': 'Investigation Time', 'rate': '30-60 min', 'desc': 'Per alert average'},
        {'issue': 'Compliance Cost', 'rate': '$30B+', 'desc': 'Annual FI spending'},
        {'issue': 'Fines (2023)', 'rate': '$6B+', 'desc': 'AML violations'},
    ]

    ax.text(7, 4, 'Current System Challenges:', fontsize=14, fontweight='bold', ha='center')

    for i, ch in enumerate(challenges):
        x = 2 + (i % 4) * 3.3
        y = 2.8 if i < 4 else 1.5

        box = mpatches.FancyBboxPatch((x-1.3, y-0.7), 2.6, 1.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.1,
                                       edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(box)
        ax.text(x, y+0.4, ch['issue'], ha='center', fontsize=11, fontweight='bold')
        ax.text(x, y-0.1, ch['rate'], ha='center', fontsize=13, fontweight='bold', color='#D62728')

    # Opportunity
    opportunity = "RegTech Opportunity: AI/ML can reduce false positives by 50-70%, cut investigation time by 80%"
    ax.text(7, 0.8, opportunity, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: UN Office on Drugs and Crime, FATF, McKinsey (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'aml_problem_scale.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
