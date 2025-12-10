"""
Price Discovery Process
Information incorporation into prices

Output: price_discovery.pdf
Module: module_04_trad_finance
Lesson: 41 - Market Microstructure
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Price Discovery',
    'module': 'module_04_trad_finance',
    'lesson': 41,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/price_discovery'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Price Response to News
    ax1 = axes[0]

    time = np.arange(-10, 60)  # Minutes around news event

    # Price before news
    price = np.ones(70) * 100
    price[:10] += np.random.randn(10) * 0.05

    # News impact at t=0: gradual incorporation
    news_impact = 2.0  # +2% fundamental change
    for i in range(10, 70):
        t = i - 10
        # Price gradually moves to new fundamental value
        adjustment = news_impact * (1 - np.exp(-0.2 * t))
        price[i] = 100 + adjustment + np.random.randn() * 0.1

    ax1.plot(time, price, 'b-', linewidth=2)
    ax1.axvline(x=0, color='red', linestyle='--', linewidth=2, label='News Release')
    ax1.axhline(y=102, color='green', linestyle='--', linewidth=1.5, label='New Fundamental')
    ax1.axhline(y=100, color='gray', linestyle='--', linewidth=1, label='Old Price')

    ax1.fill_between(time[10:], 100, price[10:], alpha=0.2, color='blue')

    ax1.set_xlabel('Time (minutes)', fontsize=11)
    ax1.set_ylabel('Price ($)', fontsize=11)
    ax1.set_title('Price Response to Information', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-10, 50)
    ax1.set_ylim(99, 103)

    # Information Share by Venue
    ax2 = axes[1]

    venues = ['NYSE', 'NASDAQ', 'BATS', 'Dark Pools', 'Other ATSs']
    info_share = [32, 28, 18, 12, 10]
    trade_share = [22, 25, 18, 25, 10]

    x = np.arange(len(venues))
    width = 0.35

    bars1 = ax2.bar(x - width/2, info_share, width, label='Information Share (%)', color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x + width/2, trade_share, width, label='Trade Volume Share (%)', color='#44A044', alpha=0.8)

    ax2.set_xlabel('Trading Venue', fontsize=11)
    ax2.set_ylabel('Share (%)', fontsize=11)
    ax2.set_title('Price Discovery Contribution by Venue', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(venues, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 40)
    ax2.yaxis.grid(True, alpha=0.3)

    # Annotation
    ax2.annotate('Lit markets lead\nprice discovery', xy=(0.5, 30), xytext=(2, 35),
                fontsize=9, fontweight='bold', color='#4A90E2',
                arrowprops=dict(arrowstyle='->', color='#4A90E2'))

    fig.suptitle('Price Discovery in Financial Markets', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'price_discovery.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
