"""
Automated Reporting Flow
Shows automated regulatory reporting workflow

Output: automated_reporting_flow.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Automated Reporting Flow',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/automated_reporting_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create automated reporting flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Automated Regulatory Reporting Flow', fontsize=20, fontweight='bold', ha='center')

    # Process flow
    steps = [
        {'name': 'Source\nSystems', 'x': 1.5, 'y': 6, 'color': '#4A90E2',
         'items': ['Core banking', 'Trading', 'Risk']},
        {'name': 'Data\nIngestion', 'x': 4, 'y': 6, 'color': '#44A044',
         'items': ['APIs', 'ETL', 'Validation']},
        {'name': 'Data\nHub', 'x': 6.5, 'y': 6, 'color': '#FF7F0E',
         'items': ['Single source', 'Lineage', 'Quality']},
        {'name': 'Report\nGeneration', 'x': 9, 'y': 6, 'color': '#6B5B95',
         'items': ['Templates', 'Rules engine', 'Formatting']},
        {'name': 'Submission', 'x': 11.5, 'y': 6, 'color': '#D62728',
         'items': ['Regulator APIs', 'Confirmation', 'Archive']},
    ]

    for i, step in enumerate(steps):
        box = mpatches.FancyBboxPatch((step['x']-1.1, step['y']-1.8), 2.2, 3.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1.3, step['name'], ha='center',
               fontsize=12, fontweight='bold', color=step['color'])

        for j, item in enumerate(step['items']):
            ax.text(step['x'], step['y']+0.3-j*0.5, f'* {item}', ha='center', fontsize=10)

        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-1.2, 6), xytext=(step['x']+1.2, 6),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Benefits
    benefits = [
        {'metric': '90%', 'desc': 'Reduction in\nmanual effort'},
        {'metric': '99.9%', 'desc': 'On-time\nsubmission'},
        {'metric': '70%', 'desc': 'Cost\nreduction'},
        {'metric': '<1%', 'desc': 'Error\nrate'},
    ]

    ax.text(7, 3.2, 'Automation Benefits:', fontsize=14, fontweight='bold', ha='center')
    for i, ben in enumerate(benefits):
        x = 2 + i * 3.3
        box = mpatches.FancyBboxPatch((x-1, 1.5), 2, 1.4,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.1,
                                       edgecolor='#44A044', lw=1.5)
        ax.add_patch(box)
        ax.text(x, 2.5, ben['metric'], ha='center', fontsize=14, fontweight='bold', color='#44A044')
        ax.text(x, 1.8, ben['desc'], ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL WORKFLOW]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'automated_reporting_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
