"""
Market Segments by Asset Class
Global market size comparison

Output: market_segments.pdf
Module: module_04_trad_finance
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Market Segments',
    'module': 'module_04_trad_finance',
    'lesson': 37,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/market_segments'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Market Size by Asset Class
    ax1 = axes[0]

    asset_classes = ['Fixed Income', 'Equities', 'Forex', 'Derivatives\n(Notional)',
                    'Commodities', 'Real Estate']
    sizes = [130, 110, 7.5, 600, 5, 330]  # In trillions USD

    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#888888']

    bars = ax1.barh(asset_classes, sizes, color=colors, alpha=0.8, edgecolor='black')

    for bar, size in zip(bars, sizes):
        label = f'${size:.0f}T' if size >= 10 else f'${size:.1f}T'
        ax1.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Market Size (Trillions USD)', fontsize=11)
    ax1.set_title('Global Market Size by Asset Class', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 700)
    ax1.xaxis.grid(True, alpha=0.3)

    # Daily Trading Volume
    ax2 = axes[1]

    markets = ['Forex', 'US\nEquities', 'US\nTreasuries', 'Crypto', 'Commodities']
    daily_volume = [6600, 500, 600, 100, 150]  # Billions USD

    colors2 = ['#FF7F0E', '#44A044', '#4A90E2', '#D62728', '#9B59B6']

    bars2 = ax2.bar(markets, daily_volume, color=colors2, alpha=0.8, edgecolor='black')

    for bar, vol in zip(bars2, daily_volume):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                f'${vol}B', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlabel('Market', fontsize=11)
    ax2.set_ylabel('Daily Volume (Billions USD)', fontsize=11)
    ax2.set_title('Average Daily Trading Volume', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 7500)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Financial Market Segments Overview', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_segments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
