"""
P2P Lending Future Scenarios
Shows potential future directions for P2P lending

Output: p2p_future_scenarios.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P Future Scenarios',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_future_scenarios'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P future scenarios diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Lending: Future Scenarios', fontsize=17, fontweight='bold', ha='center')

    # Scenarios
    scenarios = [
        {
            'name': 'Bank Convergence',
            'x': 2.2, 'y': 6,
            'color': '#4A90E2',
            'prob': 'High',
            'details': ['P2P platforms become banks', 'Deposit funding model',
                       'Full financial services', 'Example: LendingClub'],
        },
        {
            'name': 'Embedded Lending',
            'x': 6.5, 'y': 6,
            'color': '#44A044',
            'prob': 'High',
            'details': ['BaaS/API infrastructure', 'White-label solutions',
                       'BNPL integration', 'Platform partnerships'],
        },
        {
            'name': 'DeFi Integration',
            'x': 10.8, 'y': 6,
            'color': '#FF7F0E',
            'prob': 'Medium',
            'details': ['Tokenized loan assets', 'Smart contract lending',
                       'Global liquidity pools', 'Regulatory challenges'],
        },
    ]

    for scenario in scenarios:
        # Box
        box = mpatches.FancyBboxPatch((scenario['x']-1.8, scenario['y']-2), 3.6, 4.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=scenario['color'], alpha=0.15,
                                       edgecolor=scenario['color'], lw=2)
        ax.add_patch(box)
        ax.text(scenario['x'], scenario['y']+1.8, scenario['name'], ha='center',
               fontsize=12, fontweight='bold', color=scenario['color'])
        ax.text(scenario['x'], scenario['y']+1.2, f"Probability: {scenario['prob']}", ha='center',
               fontsize=10, color='#666666')

        for i, detail in enumerate(scenario['details']):
            ax.text(scenario['x'], scenario['y']+0.4-i*0.45, f'* {detail}', ha='center', fontsize=10)

    # Key trends
    trends_box = mpatches.FancyBboxPatch((1, 1), 11, 2.2, boxstyle='round,pad=0.1',
                                          facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(trends_box)
    ax.text(6.5, 2.9, 'Key Trends Shaping the Future', ha='center', fontsize=12, fontweight='bold')

    trends = [
        'AI/ML risk assessment becoming standard',
        'Open Banking enabling new data sources',
        'Regulatory frameworks maturing globally',
        'Consolidation of smaller platforms',
    ]
    for i, trend in enumerate(trends):
        ax.text(1.3 + (i % 2) * 5.5, 2.4 - (i // 2) * 0.5, f'* {trend}', fontsize=10)

    # Source
    fig.text(0.5, 0.02, '[SCENARIO ANALYSIS]',
            fontsize=9, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_future_scenarios.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
