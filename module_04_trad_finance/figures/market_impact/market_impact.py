"""
Market Impact Analysis
Price impact of large orders

Output: market_impact.pdf
Module: module_04_trad_finance
Lesson: 41 - Market Microstructure
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Market Impact',
    'module': 'module_04_trad_finance',
    'lesson': 41,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/market_impact'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Market Impact Model
    ax1 = axes[0]

    order_size_pct = np.linspace(0, 5, 50)  # % of ADV
    # Square root model: impact = sigma * sqrt(size/ADV)
    temporary_impact = 0.1 * np.sqrt(order_size_pct)
    permanent_impact = 0.05 * np.sqrt(order_size_pct)
    total_impact = temporary_impact + permanent_impact

    ax1.plot(order_size_pct, temporary_impact * 100, 'b-', linewidth=2.5, label='Temporary Impact')
    ax1.plot(order_size_pct, permanent_impact * 100, 'r-', linewidth=2.5, label='Permanent Impact')
    ax1.plot(order_size_pct, total_impact * 100, 'k--', linewidth=2, label='Total Impact')

    ax1.fill_between(order_size_pct, 0, temporary_impact * 100, alpha=0.2, color='blue')
    ax1.fill_between(order_size_pct, temporary_impact * 100, total_impact * 100, alpha=0.2, color='red')

    ax1.set_xlabel('Order Size (% of ADV)', fontsize=11)
    ax1.set_ylabel('Price Impact (%)', fontsize=11)
    ax1.set_title('Market Impact Model (Square Root)', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, 0.5)

    # Impact over time
    ax2 = axes[1]

    time = np.arange(0, 60)  # minutes
    # Large buy order at t=10
    order_start = 10
    order_end = 30

    price = np.ones(60) * 100
    # During execution: temporary + permanent impact
    price[order_start:order_end] = 100 + 0.3 * np.sqrt(np.arange(order_end-order_start) / (order_end-order_start))
    # After execution: only permanent remains
    price[order_end:] = 100.15 + np.random.randn(60-order_end) * 0.02

    ax2.plot(time, price, 'b-', linewidth=2)

    # Mark order period
    ax2.axvspan(order_start, order_end, alpha=0.2, color='orange', label='Order Execution')
    ax2.axhline(y=100, color='gray', linestyle='--', linewidth=1, label='Pre-trade Price')
    ax2.axhline(y=100.15, color='red', linestyle='--', linewidth=1, label='Post-trade (Permanent)')

    ax2.annotate('Temporary\nImpact', xy=(20, 100.25), xytext=(25, 100.35),
                fontsize=9, fontweight='bold', arrowprops=dict(arrowstyle='->', color='blue'))
    ax2.annotate('Permanent\nImpact', xy=(45, 100.15), xytext=(50, 100.25),
                fontsize=9, fontweight='bold', arrowprops=dict(arrowstyle='->', color='red'))

    ax2.set_xlabel('Time (minutes)', fontsize=11)
    ax2.set_ylabel('Price ($)', fontsize=11)
    ax2.set_title('Price Impact Over Time', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=8)
    ax2.grid(True, alpha=0.3)

    fig.suptitle('Market Impact: Large Order Execution', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_impact.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
