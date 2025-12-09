"""
Risk Scoring Model
Shows customer risk scoring model

Output: risk_scoring_model.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Risk Scoring Model',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/risk_scoring_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create risk scoring model diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Customer Risk Scoring Model', fontsize=20, fontweight='bold', ha='center')

    # Risk factors
    factors = [
        {'name': 'Customer Type', 'weight': '20%', 'items': ['Individual', 'Corporate', 'Non-profit']},
        {'name': 'Geography', 'weight': '25%', 'items': ['Country risk', 'Jurisdiction', 'FATF status']},
        {'name': 'Product/Service', 'weight': '20%', 'items': ['Cash-intensive', 'Cross-border', 'Anonymous']},
        {'name': 'Transaction', 'weight': '20%', 'items': ['Volume', 'Patterns', 'Counterparties']},
        {'name': 'Channel', 'weight': '15%', 'items': ['In-person', 'Online', 'Third-party']},
    ]

    # Input factors on left
    ax.text(3, 8, 'Risk Factors', fontsize=14, fontweight='bold', ha='center', color='#4A90E2')
    for i, factor in enumerate(factors):
        y = 7 - i * 1.2
        box = mpatches.FancyBboxPatch((1, y-0.4), 4, 0.9,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(box)
        ax.text(1.2, y, factor['name'], fontsize=11, fontweight='bold', va='center')
        ax.text(4.8, y, factor['weight'], fontsize=11, ha='right', va='center', color='#4A90E2')

    # Arrow to model
    ax.annotate('', xy=(6.5, 4.5), xytext=(5.2, 4.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Model box
    model_box = mpatches.FancyBboxPatch((6.5, 3), 3, 3,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#FF7F0E', alpha=0.2,
                                         edgecolor='#FF7F0E', lw=3)
    ax.add_patch(model_box)
    ax.text(8, 5.5, 'ML Risk', ha='center', fontsize=14, fontweight='bold', color='#FF7F0E')
    ax.text(8, 5, 'Scoring', ha='center', fontsize=14, fontweight='bold', color='#FF7F0E')
    ax.text(8, 4.3, 'Model', ha='center', fontsize=14, fontweight='bold', color='#FF7F0E')
    ax.text(8, 3.5, 'XGBoost/NN', ha='center', fontsize=10, style='italic')

    # Arrow to output
    ax.annotate('', xy=(10.5, 4.5), xytext=(9.7, 4.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Risk tiers output
    ax.text(12, 8, 'Risk Tiers', fontsize=14, fontweight='bold', ha='center')
    tiers = [
        {'name': 'Low (1-30)', 'color': '#44A044', 'action': 'Standard DD'},
        {'name': 'Medium (31-60)', 'color': '#FF7F0E', 'action': 'Enhanced DD'},
        {'name': 'High (61-80)', 'color': '#D62728', 'action': 'Senior review'},
        {'name': 'Prohibitive (81+)', 'color': '#333333', 'action': 'Decline/Exit'},
    ]

    for i, tier in enumerate(tiers):
        y = 7 - i * 1.3
        box = mpatches.FancyBboxPatch((10.5, y-0.5), 3, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=tier['color'], alpha=0.2,
                                       edgecolor=tier['color'], lw=2)
        ax.add_patch(box)
        ax.text(12, y+0.1, tier['name'], ha='center', fontsize=11, fontweight='bold', color=tier['color'])
        ax.text(12, y-0.3, tier['action'], ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, '[ILLUSTRATIVE MODEL STRUCTURE]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_scoring_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
