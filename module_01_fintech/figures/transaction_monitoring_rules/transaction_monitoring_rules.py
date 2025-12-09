"""
Transaction Monitoring Rules
Shows typical AML transaction monitoring rules

Output: transaction_monitoring_rules.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Transaction Monitoring Rules',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/transaction_monitoring_rules'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create transaction monitoring rules diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Traditional AML: Rules-Based Detection', fontsize=20, fontweight='bold', ha='center')

    # Rules categories
    rules = [
        {
            'category': 'Threshold Rules',
            'x': 2.5, 'y': 6.5,
            'color': '#4A90E2',
            'examples': ['Cash > $10,000', 'Wire > $50,000', 'Multiple txns summing\nto threshold']
        },
        {
            'category': 'Pattern Rules',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'examples': ['Structuring (9,900 x 3)', 'Round amounts', 'Rapid movement']
        },
        {
            'category': 'Watchlist Rules',
            'x': 11.5, 'y': 6.5,
            'color': '#FF7F0E',
            'examples': ['OFAC sanctions', 'PEP screening', 'High-risk countries']
        },
        {
            'category': 'Behavioral Rules',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'examples': ['Deviation from profile', 'Dormant account activity', 'Unusual geography']
        },
        {
            'category': 'Network Rules',
            'x': 9.25, 'y': 2.5,
            'color': '#D62728',
            'examples': ['Circular transactions', 'Shell company patterns', 'Layering detection']
        },
    ]

    for rule in rules:
        # Box
        box = mpatches.FancyBboxPatch((rule['x']-1.8, rule['y']-1.5), 3.6, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=rule['color'], alpha=0.15,
                                       edgecolor=rule['color'], lw=2)
        ax.add_patch(box)
        ax.text(rule['x'], rule['y']+1.2, rule['category'], ha='center',
               fontsize=13, fontweight='bold', color=rule['color'])

        for i, ex in enumerate(rule['examples']):
            ax.text(rule['x'], rule['y']+0.3-i*0.6, f'* {ex}', ha='center', fontsize=10)

    # Limitation note
    limitation = "Limitation: Criminals adapt faster than rules can be updated (avg. 6-12 months to deploy new rule)"
    ax.text(7, 0.8, limitation, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, '[TYPICAL RULE CATEGORIES]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'transaction_monitoring_rules.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
