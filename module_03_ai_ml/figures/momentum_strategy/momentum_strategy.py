"""
Momentum Trading Strategy
Price momentum and moving average crossover

Output: momentum_strategy.pdf
Module: module_03_ai_ml
Lesson: 29 - Algorithmic Trading Concepts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Momentum Strategy',
    'module': 'module_03_ai_ml',
    'lesson': 29,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/momentum_strategy'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), height_ratios=[2, 1])

    np.random.seed(123)
    days = 200
    time = np.arange(days)

    # Generate price with trend
    returns = np.random.randn(days) * 0.015
    returns[50:100] += 0.005  # Bull period
    returns[120:160] -= 0.003  # Bear period
    price = 100 * np.exp(np.cumsum(returns))

    # Calculate moving averages
    def moving_average(x, window):
        return np.convolve(x, np.ones(window)/window, mode='valid')

    ma_short = np.pad(moving_average(price, 10), (9, 0), mode='edge')
    ma_long = np.pad(moving_average(price, 50), (49, 0), mode='edge')

    # Price and MAs
    ax1 = axes[0]
    ax1.plot(time, price, 'gray', linewidth=1, alpha=0.7, label='Price')
    ax1.plot(time, ma_short, 'b-', linewidth=2, label='10-day MA (Fast)')
    ax1.plot(time, ma_long, 'r-', linewidth=2, label='50-day MA (Slow)')

    # Mark crossover signals
    buy_signals = []
    sell_signals = []
    for i in range(51, days):
        if ma_short[i] > ma_long[i] and ma_short[i-1] <= ma_long[i-1]:
            buy_signals.append(i)
        elif ma_short[i] < ma_long[i] and ma_short[i-1] >= ma_long[i-1]:
            sell_signals.append(i)

    for bs in buy_signals:
        ax1.scatter([bs], [price[bs]], color='#44A044', s=150, marker='^', zorder=5)
        ax1.annotate('BUY', xy=(bs, price[bs]), xytext=(bs, price[bs]*1.05),
                    fontsize=8, color='#44A044', fontweight='bold', ha='center')

    for ss in sell_signals:
        ax1.scatter([ss], [price[ss]], color='#D62728', s=150, marker='v', zorder=5)
        ax1.annotate('SELL', xy=(ss, price[ss]), xytext=(ss, price[ss]*0.95),
                    fontsize=8, color='#D62728', fontweight='bold', ha='center')

    ax1.set_ylabel('Price ($)', fontsize=11)
    ax1.set_title('Moving Average Crossover Strategy', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, days)

    # Momentum indicator
    ax2 = axes[1]
    momentum = (price[10:] / price[:-10] - 1) * 100
    momentum = np.pad(momentum, (10, 0), mode='edge')

    colors = ['#44A044' if m > 0 else '#D62728' for m in momentum]
    ax2.bar(time, momentum, color=colors, alpha=0.7, width=1)
    ax2.axhline(y=0, color='k', linestyle='-', linewidth=1)
    ax2.axhline(y=5, color='#44A044', linestyle='--', linewidth=1, alpha=0.5)
    ax2.axhline(y=-5, color='#D62728', linestyle='--', linewidth=1, alpha=0.5)

    ax2.set_xlabel('Trading Days', fontsize=11)
    ax2.set_ylabel('10-day Momentum (%)', fontsize=11)
    ax2.set_title('Price Momentum Indicator', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, days)

    fig.suptitle('Momentum Trading Strategy Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'momentum_strategy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
