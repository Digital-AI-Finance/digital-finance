"""
Order Book Visualization
Shows bid and ask orders in a limit order book

Output: order_book.pdf
Module: module_04_traditional
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simulated order book for a stock at ~$100
    bid_prices = [99.95, 99.90, 99.85, 99.80, 99.75, 99.70, 99.65, 99.60]
    bid_volumes = [500, 1200, 800, 2500, 1800, 3200, 1500, 2000]

    ask_prices = [100.00, 100.05, 100.10, 100.15, 100.20, 100.25, 100.30, 100.35]
    ask_volumes = [400, 900, 1500, 2100, 1200, 2800, 1900, 2500]

    # Cumulative volumes for depth chart
    bid_cumulative = np.cumsum(bid_volumes)
    ask_cumulative = np.cumsum(ask_volumes)

    # Plot bid side (green, left)
    ax.fill_betweenx(bid_prices, 0, bid_cumulative, color=MLGREEN, alpha=0.4, step='post')
    ax.step(bid_cumulative, bid_prices, where='post', color=MLGREEN, linewidth=2, label='Bids')

    # Plot ask side (red, right)
    ax.fill_betweenx(ask_prices, 0, -np.array(ask_cumulative), color=MLRED, alpha=0.4, step='post')
    ax.step(-np.array(ask_cumulative), ask_prices, where='post', color=MLRED, linewidth=2, label='Asks')

    # Add spread annotation
    spread = ask_prices[0] - bid_prices[0]
    ax.axhline(y=bid_prices[0], color=MLGREEN, linestyle='--', alpha=0.5)
    ax.axhline(y=ask_prices[0], color=MLRED, linestyle='--', alpha=0.5)
    ax.annotate(f'Spread: ${spread:.2f}', xy=(0, 99.975), fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    ax.set_xlabel('Cumulative Volume (shares)', fontsize=11)
    ax.set_ylabel('Price ($)', fontsize=11)
    ax.set_title('Limit Order Book Depth', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)

    ax.legend(loc='lower right', framealpha=0.9)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_xlim(-15000, 15000)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative order book]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'order_book.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
