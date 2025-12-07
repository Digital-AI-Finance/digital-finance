"""
Order Book Simulation and Visualization

This script simulates a limit order book and visualizes market depth,
demonstrating how bid-ask spreads and liquidity work in financial markets.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set font size globally and random seed
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

class OrderBook:
    """Simple limit order book implementation."""

    def __init__(self, mid_price=100.0):
        self.mid_price = mid_price
        self.bids = []  # (price, quantity) tuples
        self.asks = []  # (price, quantity) tuples

    def add_limit_order(self, side, price, quantity):
        """Add a limit order to the book."""
        if side == 'buy':
            self.bids.append((price, quantity))
            self.bids.sort(reverse=True)  # Highest bid first
        else:
            self.asks.append((price, quantity))
            self.asks.sort()  # Lowest ask first

    def get_best_bid(self):
        """Get the best (highest) bid price."""
        return self.bids[0][0] if self.bids else None

    def get_best_ask(self):
        """Get the best (lowest) ask price."""
        return self.asks[0][0] if self.asks else None

    def get_spread(self):
        """Calculate bid-ask spread."""
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid and best_ask:
            return best_ask - best_bid
        return None

def generate_order_book(mid_price=100.0, n_levels=20):
    """
    Generate a realistic order book with liquidity.

    Parameters:
    -----------
    mid_price : float
        Mid-market price
    n_levels : int
        Number of price levels on each side

    Returns:
    --------
    OrderBook
        Populated order book
    """
    book = OrderBook(mid_price)

    # Generate bid side (below mid price)
    for i in range(1, n_levels + 1):
        # Price decreases as we go deeper into the book
        price = mid_price - i * 0.10
        # Quantity increases with distance from mid (more liquidity at worse prices)
        quantity = 100 * (1 + i * 0.3) + np.random.normal(0, 20)
        quantity = max(50, quantity)  # Minimum 50 shares
        book.add_limit_order('buy', price, quantity)

    # Generate ask side (above mid price)
    for i in range(1, n_levels + 1):
        price = mid_price + i * 0.10
        quantity = 100 * (1 + i * 0.3) + np.random.normal(0, 20)
        quantity = max(50, quantity)
        book.add_limit_order('sell', price, quantity)

    return book

def calculate_cumulative_volume(orders):
    """Calculate cumulative volume at each price level."""
    if not orders:
        return [], []

    prices = [price for price, _ in orders]
    quantities = [qty for _, qty in orders]
    cumulative = np.cumsum(quantities)

    return prices, cumulative

def main():
    # Generate order book
    mid_price = 100.0
    book = generate_order_book(mid_price=mid_price, n_levels=20)

    # Calculate cumulative volumes
    bid_prices, bid_cumulative = calculate_cumulative_volume(book.bids)
    ask_prices, ask_cumulative = calculate_cumulative_volume(book.asks)

    # Get order quantities
    bid_quantities = [qty for _, qty in book.bids]
    ask_quantities = [qty for _, qty in book.asks]

    # Create visualization
    fig = plt.figure(figsize=(10, 7))
    gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1])
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[2, :])

    # Plot 1: Order book depth chart
    # Bids (buy orders)
    ax1.barh(bid_prices, bid_quantities, height=0.08, color='gray',
            edgecolor='black', alpha=0.7, label='Bid (Buy Orders)')

    # Asks (sell orders)
    ax1.barh(ask_prices, ask_quantities, height=0.08, color='black',
            edgecolor='black', alpha=0.7, label='Ask (Sell Orders)')

    # Mark mid price and best bid/ask
    best_bid = book.get_best_bid()
    best_ask = book.get_best_ask()
    spread = book.get_spread()

    ax1.axhline(y=mid_price, color='gray', linestyle='--', linewidth=1.5,
               label=f'Mid Price: ${mid_price:.2f}')
    ax1.axhline(y=best_bid, color='darkgray', linestyle=':', linewidth=1,
               label=f'Best Bid: ${best_bid:.2f}')
    ax1.axhline(y=best_ask, color='black', linestyle=':', linewidth=1,
               label=f'Best Ask: ${best_ask:.2f}')

    # Highlight spread
    ax1.axhspan(best_bid, best_ask, alpha=0.2, color='yellow',
               label=f'Spread: ${spread:.2f}')

    ax1.set_xlabel('Order Size (shares)', fontsize=8)
    ax1.set_ylabel('Price (USD)', fontsize=8)
    ax1.set_title('Limit Order Book Depth', fontsize=8)
    ax1.legend(fontsize=7, loc='upper right')
    ax1.grid(True, alpha=0.3, axis='x')

    # Plot 2: Cumulative bid depth
    ax2.step(bid_cumulative, bid_prices, where='post', color='gray',
            linewidth=2, label='Cumulative Bids')
    ax2.fill_betweenx(bid_prices, 0, bid_cumulative, step='post',
                     alpha=0.3, color='gray')

    ax2.set_xlabel('Cumulative Volume (shares)', fontsize=8)
    ax2.set_ylabel('Price (USD)', fontsize=8)
    ax2.set_title('Bid Side Liquidity', fontsize=8)
    ax2.axhline(y=best_bid, color='black', linestyle='--', linewidth=1)
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.3)

    # Plot 3: Cumulative ask depth
    ax3.step(ask_cumulative, ask_prices, where='post', color='black',
            linewidth=2, label='Cumulative Asks')
    ax3.fill_betweenx(ask_prices, 0, ask_cumulative, step='post',
                     alpha=0.3, color='black')

    ax3.set_xlabel('Cumulative Volume (shares)', fontsize=8)
    ax3.set_ylabel('Price (USD)', fontsize=8)
    ax3.set_title('Ask Side Liquidity', fontsize=8)
    ax3.axhline(y=best_ask, color='gray', linestyle='--', linewidth=1)
    ax3.legend(fontsize=7)
    ax3.grid(True, alpha=0.3)

    # Plot 4: Market impact simulation
    # Simulate different order sizes and their impact
    order_sizes = np.array([100, 250, 500, 1000, 2000, 5000])
    buy_impacts = []
    sell_impacts = []

    for size in order_sizes:
        # Buy order impact (consumes asks)
        remaining = size
        total_cost = 0
        for price, qty in book.asks:
            if remaining <= 0:
                break
            executed = min(remaining, qty)
            total_cost += executed * price
            remaining -= executed

        if remaining == 0:
            avg_price = total_cost / size
            buy_impacts.append((avg_price - best_ask) / best_ask * 10000)  # bps
        else:
            buy_impacts.append(np.nan)

        # Sell order impact (consumes bids)
        remaining = size
        total_proceeds = 0
        for price, qty in book.bids:
            if remaining <= 0:
                break
            executed = min(remaining, qty)
            total_proceeds += executed * price
            remaining -= executed

        if remaining == 0:
            avg_price = total_proceeds / size
            sell_impacts.append((best_bid - avg_price) / best_bid * 10000)  # bps
        else:
            sell_impacts.append(np.nan)

    # Plot market impact
    x_pos = np.arange(len(order_sizes))
    width = 0.35

    bars1 = ax4.bar(x_pos - width/2, buy_impacts, width,
                   label='Buy Impact', color='gray', edgecolor='black', alpha=0.7)
    bars2 = ax4.bar(x_pos + width/2, sell_impacts, width,
                   label='Sell Impact', color='black', edgecolor='black', alpha=0.7)

    ax4.set_xlabel('Order Size (shares)', fontsize=8)
    ax4.set_ylabel('Market Impact (basis points)', fontsize=8)
    ax4.set_title('Market Impact by Order Size', fontsize=8)
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels([f'{int(s)}' for s in order_sizes])
    ax4.legend(fontsize=7)
    ax4.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'order_book_simulation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print order book statistics
    print("\nOrder Book Statistics:")
    print("-" * 70)
    print(f"Mid Price:       ${mid_price:.2f}")
    print(f"Best Bid:        ${best_bid:.2f}")
    print(f"Best Ask:        ${best_ask:.2f}")
    print(f"Bid-Ask Spread:  ${spread:.2f} ({spread/mid_price*100:.3f}%)")
    print(f"\nTotal Bid Volume:   {sum(bid_quantities):,.0f} shares")
    print(f"Total Ask Volume:   {sum(ask_quantities):,.0f} shares")
    print(f"\nBid Levels: {len(book.bids)}")
    print(f"Ask Levels: {len(book.asks)}")

    print("\nTop 5 Bids:")
    for i, (price, qty) in enumerate(book.bids[:5]):
        print(f"  {i+1}. ${price:.2f} x {qty:,.0f} shares")

    print("\nTop 5 Asks:")
    for i, (price, qty) in enumerate(book.asks[:5]):
        print(f"  {i+1}. ${price:.2f} x {qty:,.0f} shares")

    # Calculate market impact for a sample order
    sample_order_size = 500
    print(f"\nMarket Impact Analysis (for {sample_order_size} share market order):")
    print("-" * 70)

    # Buy market order (consumes asks)
    remaining = sample_order_size
    total_cost = 0
    for price, qty in book.asks:
        if remaining <= 0:
            break
        executed = min(remaining, qty)
        total_cost += executed * price
        remaining -= executed

    avg_price_buy = total_cost / sample_order_size if remaining == 0 else None
    if avg_price_buy:
        slippage_buy = avg_price_buy - best_ask
        print(f"Buy {sample_order_size} shares:")
        print(f"  Average execution price: ${avg_price_buy:.2f}")
        print(f"  Slippage: ${slippage_buy:.2f} ({slippage_buy/best_ask*100:.3f}%)")

if __name__ == '__main__':
    main()
