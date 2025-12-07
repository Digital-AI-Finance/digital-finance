"""
Order Book Depth Visualization
Bid/Ask order book with depth chart

Required libraries: matplotlib, numpy
Output: order_book_depth.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Order Book Depth Visualization',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_04_traditional/order_book_depth'
}

def create_order_book_depth():
    """Create visualization of order book with bid/ask depth"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig = plt.figure(figsize=(10, 7))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3,
                         height_ratios=[1.2, 1])

    # Generate synthetic order book data
    mid_price = 100.00

    # Bid prices (below mid price)
    n_levels = 10
    bid_prices = mid_price - np.arange(0.01, 0.11, 0.01)
    bid_sizes = np.random.exponential(scale=500, size=n_levels)
    bid_cumulative = np.cumsum(bid_sizes)

    # Ask prices (above mid price)
    ask_prices = mid_price + np.arange(0.01, 0.11, 0.01)
    ask_sizes = np.random.exponential(scale=500, size=n_levels)
    ask_cumulative = np.cumsum(ask_sizes)

    # Top left: Order book table
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.axis('off')

    # Create order book data
    book_data = [['Bid Size', 'Bid Price', 'Ask Price', 'Ask Size']]

    for i in range(min(8, n_levels)):
        book_data.append([
            f'{int(bid_sizes[i]):,}',
            f'${bid_prices[i]:.2f}',
            f'${ask_prices[i]:.2f}',
            f'{int(ask_sizes[i]):,}'
        ])

    table = ax1.table(cellText=book_data,
                     cellLoc='center',
                     loc='center',
                     bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(7)

    # Style header
    for i in range(4):
        cell = table[(0, i)]
        cell.set_facecolor('darkgray')
        cell.set_text_props(weight='bold', color='black')

    # Style bid columns (green tint with grayscale)
    for i in range(1, len(book_data)):
        # Bid size and price
        for j in [0, 1]:
            cell = table[(i, j)]
            cell.set_facecolor('lightgray')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

        # Ask price and size
        for j in [2, 3]:
            cell = table[(i, j)]
            cell.set_facecolor('white')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

    ax1.set_title('Order Book Snapshot', fontsize=10, fontweight='bold', pad=20)

    # Top right: Depth chart
    ax2 = fig.add_subplot(gs[0, 1])

    # Plot cumulative depth
    # Bids (step down from mid price)
    bid_prices_extended = np.concatenate([[mid_price], bid_prices])
    bid_cumulative_extended = np.concatenate([[0], bid_cumulative])

    ax2.fill_betweenx(bid_prices_extended, 0, bid_cumulative_extended,
                     step='post', alpha=0.5, color='lightgray',
                     edgecolor='black', linewidth=1, label='Bid Depth')

    # Asks (step up from mid price)
    ask_prices_extended = np.concatenate([[mid_price], ask_prices])
    ask_cumulative_extended = np.concatenate([[0], ask_cumulative])

    ax2.fill_betweenx(ask_prices_extended, 0, ask_cumulative_extended,
                     step='post', alpha=0.5, color='darkgray',
                     edgecolor='black', linewidth=1, label='Ask Depth')

    # Mark mid price
    ax2.axhline(y=mid_price, color='black', linestyle='--',
               linewidth=1.5, label=f'Mid Price: ${mid_price:.2f}')

    ax2.set_xlabel('Cumulative Size (shares)', fontsize=8)
    ax2.set_ylabel('Price ($)', fontsize=8)
    ax2.set_title('Market Depth Chart', fontsize=10, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=7)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Bottom left: Spread analysis
    ax3 = fig.add_subplot(gs[1, 0])

    # Calculate spreads
    best_bid = bid_prices[0]
    best_ask = ask_prices[0]
    spread = best_ask - best_bid
    spread_bps = (spread / mid_price) * 10000

    # Visualize spread
    price_range = np.linspace(best_bid - 0.02, best_ask + 0.02, 100)
    ax3.axvspan(best_bid, best_ask, alpha=0.3, color='gray', label='Bid-Ask Spread')

    ax3.axvline(x=best_bid, color='black', linewidth=2, label='Best Bid')
    ax3.axvline(x=best_ask, color='black', linewidth=2, linestyle='--',
               label='Best Ask')
    ax3.axvline(x=mid_price, color='red', linewidth=1.5, linestyle=':',
               label='Mid Price')

    ax3.set_xlabel('Price ($)', fontsize=8)
    ax3.set_ylabel('', fontsize=8)
    ax3.set_title('Bid-Ask Spread', fontsize=10, fontweight='bold')
    ax3.set_ylim(0, 1)
    ax3.set_yticks([])
    ax3.legend(loc='upper left', fontsize=7)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['left'].set_visible(False)

    # Add spread statistics
    stats_text = f'Spread: ${spread:.3f}\n({spread_bps:.1f} bps)\n\nBest Bid: ${best_bid:.2f}\nBest Ask: ${best_ask:.2f}\nMid: ${mid_price:.2f}'
    ax3.text(0.98, 0.95, stats_text,
            transform=ax3.transAxes,
            fontsize=7,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.4',
                     facecolor='white',
                     edgecolor='black',
                     linewidth=0.5))

    # Bottom right: Order flow metrics
    ax4 = fig.add_subplot(gs[1, 1])

    # Calculate metrics
    total_bid_size = np.sum(bid_sizes)
    total_ask_size = np.sum(ask_sizes)
    imbalance = (total_bid_size - total_ask_size) / (total_bid_size + total_ask_size)

    metrics = ['Total Bid\nVolume', 'Total Ask\nVolume', 'Order Book\nImbalance']
    values = [total_bid_size, total_ask_size, imbalance * 10000]  # Scale imbalance for visibility

    colors = ['lightgray', 'darkgray', 'gray']
    bars = ax4.bar(metrics, [total_bid_size, total_ask_size, abs(imbalance) * max(total_bid_size, total_ask_size)],
                   color=colors, edgecolor='black', linewidth=0.8)

    # Add value labels
    ax4.text(0, total_bid_size + 200, f'{int(total_bid_size):,}',
            ha='center', fontsize=7)
    ax4.text(1, total_ask_size + 200, f'{int(total_ask_size):,}',
            ha='center', fontsize=7)
    ax4.text(2, abs(imbalance) * max(total_bid_size, total_ask_size) + 200,
            f'{imbalance:.1%}',
            ha='center', fontsize=7)

    ax4.set_ylabel('Volume (shares)', fontsize=8)
    ax4.set_title('Order Book Metrics', fontsize=10, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)

    # Main title
    fig.suptitle('Order Book and Market Depth Analysis [SYNTHETIC DATA]',
                fontsize=12, fontweight='bold', y=0.98)

    # Save as PDF
    output_path = Path(__file__).parent / 'order_book_depth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_order_book_depth()
