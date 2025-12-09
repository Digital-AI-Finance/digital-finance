"""
Crypto Investing Platforms
Shows crypto wealth platforms landscape

Output: crypto_investing_platforms.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Crypto Investing Platforms',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/crypto_investing_platforms'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create crypto investing platforms diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Crypto Wealth Management Platforms', fontsize=20, fontweight='bold', ha='center')

    # Platform types
    platforms = [
        {
            'name': 'Exchanges',
            'x': 2.5, 'y': 6.5,
            'color': '#FF7F0E',
            'examples': 'Coinbase, Kraken, Gemini',
            'features': 'Trading, custody, staking'
        },
        {
            'name': 'Crypto Robos',
            'x': 7, 'y': 6.5,
            'color': '#4A90E2',
            'examples': 'Makara, Titan',
            'features': 'Automated crypto portfolios'
        },
        {
            'name': 'Hybrid Apps',
            'x': 11.5, 'y': 6.5,
            'color': '#44A044',
            'examples': 'Robinhood, SoFi, Revolut',
            'features': 'Crypto + stocks in one app'
        },
        {
            'name': 'Yield Platforms',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'examples': 'Lido, Rocket Pool',
            'features': 'Staking, DeFi yield'
        },
        {
            'name': 'Institutional',
            'x': 9.25, 'y': 2.5,
            'color': '#333333',
            'examples': 'NYDIG, Galaxy, Anchorage',
            'features': 'Custody, trading for FIs'
        },
    ]

    for plat in platforms:
        box = mpatches.FancyBboxPatch((plat['x']-1.8, plat['y']-1.3), 3.6, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=plat['color'], alpha=0.15,
                                       edgecolor=plat['color'], lw=2)
        ax.add_patch(box)
        ax.text(plat['x'], plat['y']+1, plat['name'], ha='center',
               fontsize=13, fontweight='bold', color=plat['color'])
        ax.text(plat['x'], plat['y']+0.3, plat['examples'], ha='center', fontsize=10, style='italic')
        ax.text(plat['x'], plat['y']-0.4, plat['features'], ha='center', fontsize=10)

    # 2024 developments
    developments = "2024 Milestone: Bitcoin & Ethereum ETFs approved | Institutional adoption accelerating"
    ax.text(7, 0.8, developments, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CryptoCompare, Galaxy Digital research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'crypto_investing_platforms.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
