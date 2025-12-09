"""
Progressive Snapshot
Shows Progressive's telematics program

Output: progressive_snapshot.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Progressive Snapshot',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/progressive_snapshot'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Progressive Snapshot diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Progressive Snapshot: UBI Pioneer', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Launched 2011 - First major US telematics program', fontsize=13, ha='center', color='#666666')

    # How it works
    steps = [
        {'name': 'Enroll', 'x': 2, 'y': 6.5, 'desc': 'Sign up for\nSnapshot\nprogram'},
        {'name': 'Device/App', 'x': 5, 'y': 6.5, 'desc': 'OBD-II dongle\nor mobile\napp tracks'},
        {'name': 'Monitor', 'x': 8, 'y': 6.5, 'desc': '6-month\ndriving\nmonitoring'},
        {'name': 'Discount', 'x': 11, 'y': 6.5, 'desc': 'Up to 30%\nsavings\nbased on score'},
    ]

    for i, step in enumerate(steps):
        # Box
        box = mpatches.FancyBboxPatch((step['x']-1.2, step['y']-1.5), 2.4, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.2,
                                       edgecolor='#4A90E2', lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1, step['name'], ha='center',
               fontsize=13, fontweight='bold', color='#4A90E2')
        ax.text(step['x'], step['y']-0.3, step['desc'], ha='center', va='center', fontsize=11)

        # Arrow
        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-1.4, 6.5), xytext=(step['x']+1.4, 6.5),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Scoring factors
    factors = [
        {'name': 'Hard Braking', 'weight': 'High Impact', 'color': '#D62728'},
        {'name': 'High-Speed Driving', 'weight': 'High Impact', 'color': '#D62728'},
        {'name': 'Night Driving', 'weight': 'Medium Impact', 'color': '#FF7F0E'},
        {'name': 'Miles Driven', 'weight': 'Medium Impact', 'color': '#FF7F0E'},
    ]

    ax.text(4, 3.8, 'Scoring Factors:', fontsize=14, fontweight='bold', ha='center')
    for i, factor in enumerate(factors):
        y_pos = 3.2 - i * 0.6
        ax.text(2.5, y_pos, f'* {factor["name"]}', fontsize=11)
        ax.text(5.5, y_pos, factor['weight'], fontsize=11, color=factor['color'], fontweight='bold')

    # Results
    results = """Program Results (2024):
    - 35M+ drivers enrolled since launch
    - Average discount: 15%
    - Best drivers save: up to 30%
    - 25% fewer accidents among participants
    - $1B+ in customer savings"""

    ax.text(10.5, 2.5, results, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Progressive Insurance annual reports, company website (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'progressive_snapshot.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
