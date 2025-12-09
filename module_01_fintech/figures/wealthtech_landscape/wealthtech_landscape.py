"""
WealthTech Landscape
Shows the WealthTech ecosystem overview

Output: wealthtech_landscape.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Landscape',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wealthtech_landscape'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create WealthTech landscape diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'WealthTech Ecosystem', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Technology transforming wealth management and retail investing', fontsize=13,
           ha='center', color='#666666')

    # Segments
    segments = [
        {
            'name': 'Robo-Advisors',
            'x': 2.2, 'y': 6,
            'color': '#4A90E2',
            'players': 'Betterment, Wealthfront',
            'focus': 'Automated portfolio mgmt'
        },
        {
            'name': 'Trading Apps',
            'x': 5.5, 'y': 6,
            'color': '#44A044',
            'players': 'Robinhood, eToro',
            'focus': 'Commission-free trading'
        },
        {
            'name': 'Micro-Investing',
            'x': 8.5, 'y': 6,
            'color': '#FF7F0E',
            'players': 'Acorns, Stash',
            'focus': 'Spare change investing'
        },
        {
            'name': 'Social Trading',
            'x': 11.8, 'y': 6,
            'color': '#6B5B95',
            'players': 'eToro, Public',
            'focus': 'Copy expert traders'
        },
        {
            'name': 'B2B Platforms',
            'x': 3.8, 'y': 2.5,
            'color': '#D62728',
            'players': 'Addepar, Orion',
            'focus': 'Advisor technology'
        },
        {
            'name': 'Alt Investments',
            'x': 7, 'y': 2.5,
            'color': '#333333',
            'players': 'Fundrise, Masterworks',
            'focus': 'Democratized alternatives'
        },
        {
            'name': 'Crypto Wealth',
            'x': 10.2, 'y': 2.5,
            'color': '#17BECF',
            'players': 'BlockFi, Coinbase',
            'focus': 'Digital asset investing'
        },
    ]

    for seg in segments:
        box = mpatches.FancyBboxPatch((seg['x']-1.5, seg['y']-1.3), 3, 2.7,
                                       boxstyle='round,pad=0.1',
                                       facecolor=seg['color'], alpha=0.15,
                                       edgecolor=seg['color'], lw=2)
        ax.add_patch(box)
        ax.text(seg['x'], seg['y']+1, seg['name'], ha='center',
               fontsize=12, fontweight='bold', color=seg['color'])
        ax.text(seg['x'], seg['y']+0.1, seg['players'], ha='center', fontsize=10, style='italic')
        ax.text(seg['x'], seg['y']-0.6, seg['focus'], ha='center', fontsize=10)

    # Market size
    market = "Global WealthTech Market: USD 5T+ retail AUM | 150M+ app users | CAGR: 15%"
    ax.text(7, 0.8, market, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CB Insights, Statista WealthTech reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealthtech_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
