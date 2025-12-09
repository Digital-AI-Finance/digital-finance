"""
eToro Business Model
Shows eToro's social trading platform model

Output: etoro_model.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'eToro Business Model',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/etoro_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create eToro business model diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'eToro: Social Trading Pioneer', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Founded 2007 | 30M+ users | 100+ countries', fontsize=13, ha='center', color='#666666')

    # Key features
    features = [
        {
            'name': 'CopyTrader',
            'x': 2.5, 'y': 6,
            'color': '#44A044',
            'desc': 'Auto-copy top traders\nwith one click'
        },
        {
            'name': 'Social Feed',
            'x': 5.5, 'y': 6,
            'color': '#4A90E2',
            'desc': 'Follow traders\nsee their moves'
        },
        {
            'name': 'Multi-Asset',
            'x': 8.5, 'y': 6,
            'color': '#FF7F0E',
            'desc': 'Stocks, crypto, ETFs\nforex, commodities'
        },
        {
            'name': 'Smart Portfolios',
            'x': 11.5, 'y': 6,
            'color': '#6B5B95',
            'desc': 'Themed portfolios\nby strategy/sector'
        },
    ]

    for feat in features:
        box = mpatches.FancyBboxPatch((feat['x']-1.3, feat['y']-1.2), 2.6, 2.4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=feat['color'], alpha=0.2,
                                       edgecolor=feat['color'], lw=2)
        ax.add_patch(box)
        ax.text(feat['x'], feat['y']+0.7, feat['name'], ha='center',
               fontsize=13, fontweight='bold', color=feat['color'])
        ax.text(feat['x'], feat['y']-0.2, feat['desc'], ha='center', fontsize=10)

    # Revenue model
    revenue = """Revenue Model:
    - Spread fees on trades
    - Overnight/weekend fees
    - Withdrawal fees
    - Currency conversion
    - Interest on cash"""

    ax.text(4, 2.5, revenue, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Popular Investor Program
    pip = """Popular Investor Program:
    - Get paid for being copied
    - Up to 1.5% of AUM annually
    - Tiered system (Cadet to Elite)
    - Encourages quality trading"""

    ax.text(10, 2.5, pip, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Metrics
    metrics = "2024 Revenue: USD 1.2B+ | Valuation (2021 SPAC): USD 10B"
    ax.text(7, 0.8, metrics, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: eToro company reports, SEC filings (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'etoro_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
