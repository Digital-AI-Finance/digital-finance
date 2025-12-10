"""
Order Book Depth Visualization
Limit order book structure

Output: order_book_depth.pdf
Module: module_04_trad_finance
Lesson: 41 - Market Microstructure
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Order Book Depth',
    'module': 'module_04_trad_finance',
    'lesson': 41,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/order_book_depth'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Order Book Visualization
    ax1 = axes[0]

    mid_price = 100.00
    tick = 0.01

    # Bid side
    bid_prices = np.array([mid_price - tick * i for i in range(1, 11)])
    bid_sizes = np.array([500, 1200, 800, 2500, 1500, 900, 600, 1800, 1100, 700])

    # Ask side
    ask_prices = np.array([mid_price + tick * i for i in range(1, 11)])
    ask_sizes = np.array([400, 900, 1500, 2000, 1200, 800, 1400, 600, 950, 500])

    ax1.barh(bid_prices, bid_sizes, height=0.008, color='#44A044', alpha=0.7, label='Bids')
    ax1.barh(ask_prices, -ask_sizes, height=0.008, color='#D62728', alpha=0.7, label='Asks')

    ax1.axhline(y=mid_price, color='black', linestyle='--', linewidth=2, label=f'Mid: ${mid_price}')

    ax1.set_xlabel('Size (shares)', fontsize=11)
    ax1.set_ylabel('Price ($)', fontsize=11)
    ax1.set_title('Limit Order Book', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=9)
    ax1.set_xlim(-3000, 3000)
    ax1.grid(True, alpha=0.3, axis='x')

    # Depth Chart
    ax2 = axes[1]

    bid_cumsum = np.cumsum(bid_sizes[::-1])[::-1]
    ask_cumsum = np.cumsum(ask_sizes)

    ax2.fill_between(bid_prices, bid_cumsum, step='post', alpha=0.3, color='#44A044')
    ax2.step(bid_prices, bid_cumsum, where='post', color='#44A044', linewidth=2, label='Bid Depth')

    ax2.fill_between(ask_prices, ask_cumsum, step='post', alpha=0.3, color='#D62728')
    ax2.step(ask_prices, ask_cumsum, where='post', color='#D62728', linewidth=2, label='Ask Depth')

    ax2.axvline(x=mid_price, color='black', linestyle='--', linewidth=2)

    # Mark spread
    ax2.annotate('', xy=(ask_prices[0], 500), xytext=(bid_prices[0], 500),
                arrowprops=dict(arrowstyle='<->', color='#FF7F0E', lw=2))
    ax2.text(mid_price, 700, f'Spread: ${(ask_prices[0]-bid_prices[0]):.2f}',
            ha='center', fontsize=9, fontweight='bold', color='#FF7F0E')

    ax2.set_xlabel('Price ($)', fontsize=11)
    ax2.set_ylabel('Cumulative Size', fontsize=11)
    ax2.set_title('Market Depth Chart', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_xlim(99.85, 100.15)
    ax2.grid(True, alpha=0.3)

    fig.suptitle('Market Microstructure: Order Book Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'order_book_depth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
