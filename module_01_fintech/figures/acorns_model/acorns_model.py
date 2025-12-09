"""
Acorns Business Model
Shows Acorns micro-investing platform model

Output: acorns_model.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Acorns Business Model',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/acorns_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Acorns business model diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Acorns: Micro-Investing Pioneer', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Founded 2012 | 10M+ subscribers', fontsize=13, ha='center', color='#666666')

    # Product tiers
    tiers = [
        {
            'name': 'Acorns Personal',
            'price': 'USD 3/mo',
            'x': 2.5, 'y': 6,
            'color': '#44A044',
            'features': ['Round-ups investing', 'Diversified ETF portfolios', 'Retirement account (IRA)']
        },
        {
            'name': 'Acorns Family',
            'price': 'USD 5/mo',
            'x': 7, 'y': 6,
            'color': '#4A90E2',
            'features': ['Everything in Personal', 'Kids investing accounts', 'Family unlimited']
        },
        {
            'name': 'Acorns Premium',
            'price': 'USD 12/mo',
            'x': 11.5, 'y': 6,
            'color': '#6B5B95',
            'features': ['All Family features', 'Bonus investing rewards', 'Expert guidance']
        },
    ]

    for tier in tiers:
        box = mpatches.FancyBboxPatch((tier['x']-1.8, tier['y']-2), 3.6, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=tier['color'], alpha=0.2,
                                       edgecolor=tier['color'], lw=2)
        ax.add_patch(box)
        ax.text(tier['x'], tier['y']+1.5, tier['name'], ha='center',
               fontsize=13, fontweight='bold', color=tier['color'])
        ax.text(tier['x'], tier['y']+0.9, tier['price'], ha='center',
               fontsize=14, fontweight='bold')

        for i, feat in enumerate(tier['features']):
            ax.text(tier['x'], tier['y']+0.1-i*0.5, f'* {feat}', ha='center', fontsize=10)

    # Key metrics
    metrics = """Key Metrics (2024):
    - USD 18B+ AUM
    - USD 3,500 avg account
    - 90%+ subscribers
    - Break-even focused"""

    ax.text(4, 2, metrics, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Innovation
    innovation = """Innovations:
    - Found Money (cashback investing)
    - Acorns Early (kids accounts)
    - Acorns Banking (checking)
    - ESG portfolios
    - Bitcoin exposure"""

    ax.text(10, 2, innovation, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Acorns company filings, SEC registration (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'acorns_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
