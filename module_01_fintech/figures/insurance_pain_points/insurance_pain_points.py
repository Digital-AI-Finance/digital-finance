"""
Insurance Pain Points
Shows traditional insurance industry challenges

Output: insurance_pain_points.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Insurance Pain Points',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/insurance_pain_points'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create insurance pain points diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Traditional Insurance: Key Pain Points', fontsize=20, fontweight='bold', ha='center')

    # Pain points
    pain_points = [
        {
            'name': 'Complex Products',
            'x': 2.2, 'y': 6.5,
            'color': '#D62728',
            'issues': ['Difficult to understand', 'Hidden exclusions', 'Over-insurance common'],
        },
        {
            'name': 'Slow Processes',
            'x': 7, 'y': 6.5,
            'color': '#FF7F0E',
            'issues': ['Lengthy applications', 'Manual underwriting', 'Paper-heavy claims'],
        },
        {
            'name': 'Poor Experience',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'issues': ['Infrequent contact', 'Adversarial claims', 'Limited transparency'],
        },
        {
            'name': 'High Costs',
            'x': 2.2, 'y': 2.5,
            'color': '#4A90E2',
            'issues': ['Agent commissions (15-20%)', 'Legacy IT systems', 'Fraud losses (5-10%)'],
        },
        {
            'name': 'Risk Assessment',
            'x': 7, 'y': 2.5,
            'color': '#44A044',
            'issues': ['Limited data points', 'Static pricing', 'Cross-subsidization'],
        },
        {
            'name': 'Distribution',
            'x': 11.8, 'y': 2.5,
            'color': '#333333',
            'issues': ['Agent dependency', 'Limited digital reach', 'Channel conflicts'],
        },
    ]

    for point in pain_points:
        # Box
        box = mpatches.FancyBboxPatch((point['x']-1.8, point['y']-1.3), 3.6, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=point['color'], alpha=0.15,
                                       edgecolor=point['color'], lw=2)
        ax.add_patch(box)
        ax.text(point['x'], point['y']+1.1, point['name'], ha='center',
               fontsize=14, fontweight='bold', color=point['color'])

        for i, issue in enumerate(point['issues']):
            ax.text(point['x'], point['y']+0.3-i*0.5, f'* {issue}', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, '[INDUSTRY ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'insurance_pain_points.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
