"""
Trading Venues Landscape
Major global exchanges and venues

Output: trading_venues.pdf
Module: module_04_trad_finance
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Trading Venues',
    'module': 'module_04_trad_finance',
    'lesson': 37,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/trading_venues'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Top Exchanges by Market Cap
    ax1 = axes[0]

    exchanges = ['NYSE', 'NASDAQ', 'Shanghai SE', 'Euronext', 'Tokyo SE',
                 'Shenzhen SE', 'Hong Kong SE', 'LSE', 'TMX', 'BSE India']
    market_cap = [27.5, 22.1, 7.3, 7.0, 6.5, 5.2, 4.8, 3.5, 3.2, 3.0]

    colors = plt.cm.Blues(np.linspace(0.3, 0.9, len(exchanges)))[::-1]

    bars = ax1.barh(exchanges[::-1], market_cap[::-1], color=colors, edgecolor='black', alpha=0.8)

    for bar, cap in zip(bars, market_cap[::-1]):
        ax1.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'${cap}T', va='center', fontsize=9, fontweight='bold')

    ax1.set_xlabel('Market Capitalization (Trillions USD)', fontsize=11)
    ax1.set_title('Top Stock Exchanges by Market Cap', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 32)
    ax1.xaxis.grid(True, alpha=0.3)

    # US Market Share by Venue
    ax2 = axes[1]

    venues = ['NYSE', 'NASDAQ', 'CBOE\nEdge', 'IEX', 'Dark\nPools', 'Other\nATSs']
    share = [22, 18, 15, 4, 32, 9]
    colors2 = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#888888', '#D62728']

    wedges, texts, autotexts = ax2.pie(share, labels=venues, autopct='%1.0f%%',
                                        colors=colors2, startangle=90,
                                        explode=[0.02, 0.02, 0, 0, 0.05, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax2.set_title('US Equity Market Share by Venue', fontsize=12, fontweight='bold')

    fig.suptitle('Global Trading Venues Landscape', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'trading_venues.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
