"""
P2P Model Evolution
Shows how P2P business models have evolved

Output: p2p_model_evolution.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P Model Evolution',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_model_evolution'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P model evolution diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Lending Business Model Evolution', fontsize=17, fontweight='bold', ha='center')

    # Timeline arrow
    ax.annotate('', xy=(12, 5), xytext=(1, 5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=3))
    ax.text(6.5, 4.4, 'TIME / MATURITY', ha='center', fontsize=10, fontweight='bold')

    # Model stages
    models = [
        {
            'name': 'Pure P2P',
            'period': '2007-2014',
            'x': 2.5, 'y': 7,
            'color': '#4A90E2',
            'features': ['Individual investors', 'Retail focus', 'True marketplace',
                        'Manual selection'],
        },
        {
            'name': 'Hybrid Model',
            'period': '2014-2018',
            'x': 6.5, 'y': 7,
            'color': '#FF7F0E',
            'features': ['Institutional + retail', 'Auto-invest', 'Whole loan sales',
                        'Securitization'],
        },
        {
            'name': 'Bank/Balance Sheet',
            'period': '2018+',
            'x': 10.5, 'y': 7,
            'color': '#44A044',
            'features': ['Bank charter', 'Deposit funding', 'Hold loans on B/S',
                        'Full banking services'],
        },
    ]

    for model in models:
        # Box
        box = mpatches.FancyBboxPatch((model['x']-1.5, model['y']-1), 3, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=model['color'], alpha=0.2,
                                       edgecolor=model['color'], lw=2)
        ax.add_patch(box)
        ax.text(model['x'], model['y']+1.4, model['name'], ha='center',
               fontsize=12, fontweight='bold', color=model['color'])
        ax.text(model['x'], model['y']+0.9, model['period'], ha='center',
               fontsize=10, color='#666666')

        for i, feature in enumerate(model['features']):
            ax.text(model['x'], model['y']+0.2-i*0.4, f'* {feature}', ha='center', fontsize=9)

    # Drivers of change
    drivers_box = mpatches.FancyBboxPatch((1, 1), 11, 2.3, boxstyle='round,pad=0.1',
                                           facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(drivers_box)
    ax.text(6.5, 3, 'Drivers of Evolution', ha='center', fontsize=12, fontweight='bold')

    drivers = [
        'Regulatory pressure for capital/licensing',
        'Need for stable funding sources',
        'Lower cost of capital (deposits vs marketplace)',
        'Unit economics favor scale and bank model',
    ]
    for i, driver in enumerate(drivers):
        ax.text(1.3 + (i % 2) * 5.5, 2.4 - (i // 2) * 0.5, f'* {driver}', fontsize=10)

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL EVOLUTION MODEL]',
            fontsize=9, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_model_evolution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
