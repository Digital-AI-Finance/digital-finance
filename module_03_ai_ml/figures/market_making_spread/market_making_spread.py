"""
Market Making and Bid-Ask Spread
Visualization of market maker strategy

Output: market_making_spread.pdf
Module: module_03_ai_ml
Lesson: 29 - Algorithmic Trading Concepts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Market Making Spread',
    'module': 'module_03_ai_ml',
    'lesson': 29,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/market_making_spread'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Bid-Ask Spread Visualization
    ax1 = axes[0]
    time = np.arange(50)
    mid_price = 100 + np.cumsum(np.random.randn(50) * 0.2)
    spread = 0.5 + np.abs(np.random.randn(50) * 0.1)
    bid = mid_price - spread/2
    ask = mid_price + spread/2

    ax1.fill_between(time, bid, ask, alpha=0.3, color='#4A90E2', label='Spread')
    ax1.plot(time, mid_price, 'k-', linewidth=2, label='Mid Price')
    ax1.plot(time, bid, 'g-', linewidth=1.5, label='Bid (Buy)')
    ax1.plot(time, ask, 'r-', linewidth=1.5, label='Ask (Sell)')

    ax1.annotate('Profit = Spread', xy=(25, mid_price[25]),
                xytext=(30, mid_price[25]+1.5), fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'))

    ax1.set_xlabel('Time', fontsize=11)
    ax1.set_ylabel('Price ($)', fontsize=11)
    ax1.set_title('Bid-Ask Spread: Market Maker Profit Zone', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Order Book Depth
    ax2 = axes[1]
    price_levels = np.arange(98, 102.5, 0.5)
    mid = 100

    # Generate order book volumes
    bids = np.array([150, 280, 420, 350])  # Below mid
    asks = np.array([180, 320, 380, 290])  # Above mid

    bid_prices = [99.5, 99.0, 98.5, 98.0]
    ask_prices = [100.5, 101.0, 101.5, 102.0]

    ax2.barh(bid_prices, bids, height=0.35, color='#44A044', alpha=0.7, label='Bids (Buy Orders)')
    ax2.barh(ask_prices, -asks, height=0.35, color='#D62728', alpha=0.7, label='Asks (Sell Orders)')
    ax2.axhline(y=mid, color='k', linestyle='--', linewidth=2, label='Mid Price')

    ax2.set_xlabel('Volume (negative = asks)', fontsize=11)
    ax2.set_ylabel('Price Level ($)', fontsize=11)
    ax2.set_title('Order Book Depth', fontsize=12, fontweight='bold')
    ax2.legend(loc='lower right', fontsize=9)
    ax2.grid(True, alpha=0.3, axis='x')

    # Add annotations
    ax2.annotate('Market Maker\nplaces orders\non both sides', xy=(0, 100),
                xytext=(250, 100.5), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='#4A90E2'))

    fig.suptitle('Market Making Strategy: Capturing the Spread', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_making_spread.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
