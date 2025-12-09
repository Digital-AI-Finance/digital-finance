"""
Traditional AML Process
Shows traditional AML workflow

Output: traditional_aml_process.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Traditional AML Process',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/traditional_aml_process'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create traditional AML process diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Traditional AML Process Flow', fontsize=20, fontweight='bold', ha='center')

    # Process steps
    steps = [
        {'name': 'Transaction\nData', 'x': 1.5, 'y': 6, 'color': '#4A90E2'},
        {'name': 'Rules-Based\nScreening', 'x': 4, 'y': 6, 'color': '#44A044'},
        {'name': 'Alert\nGeneration', 'x': 6.5, 'y': 6, 'color': '#FF7F0E'},
        {'name': 'Manual\nReview', 'x': 9, 'y': 6, 'color': '#6B5B95'},
        {'name': 'SAR\nFiling', 'x': 11.5, 'y': 6, 'color': '#D62728'},
    ]

    # Draw arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-0.9, 6), xytext=(steps[i]['x']+0.9, 6),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    for step in steps:
        box = mpatches.FancyBboxPatch((step['x']-1, step['y']-1), 2, 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y'], step['name'], ha='center', va='center',
               fontsize=12, fontweight='bold', color=step['color'])

    # Volume funnel
    volumes = [
        {'stage': 'Transactions', 'vol': '1,000,000', 'y': 4},
        {'stage': 'Alerts', 'vol': '10,000', 'y': 3.2},
        {'stage': 'Investigations', 'vol': '1,000', 'y': 2.4},
        {'stage': 'SARs Filed', 'vol': '50-100', 'y': 1.6},
    ]

    ax.text(3.5, 4.6, 'Typical Monthly Volume:', fontsize=13, fontweight='bold', ha='center')
    for vol in volumes:
        ax.text(2, vol['y'], vol['stage'] + ':', fontsize=11, ha='left')
        ax.text(5, vol['y'], vol['vol'], fontsize=12, fontweight='bold', ha='right', color='#4A90E2')

    # Problems with traditional approach
    problems = """Traditional Approach Problems:
    - Static rules miss evolving patterns
    - 95%+ false positive rate
    - Analyst fatigue
    - Slow adaptation to new threats
    - Siloed data"""

    ax.text(10.5, 3, problems, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFEBEB', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, '[ILLUSTRATIVE WORKFLOW]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'traditional_aml_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
