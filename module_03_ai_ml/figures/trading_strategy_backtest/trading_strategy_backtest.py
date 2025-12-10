"""
Trading Strategy Backtest Results
Performance comparison of ML strategies

Output: trading_strategy_backtest.pdf
Module: module_03_ai_ml
Lesson: 29 - Algorithmic Trading Concepts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Trading Strategy Backtest',
    'module': 'module_03_ai_ml',
    'lesson': 29,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/trading_strategy_backtest'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)
    days = np.arange(252)  # One trading year

    # Cumulative returns
    ax1 = axes[0]
    benchmark = np.cumsum(np.random.randn(252) * 0.01)
    ml_strategy = np.cumsum(np.random.randn(252) * 0.012 + 0.0005)
    momentum = np.cumsum(np.random.randn(252) * 0.011 + 0.0003)

    ax1.plot(days, benchmark * 100, 'k-', linewidth=2, label='S&P 500 Benchmark')
    ax1.plot(days, ml_strategy * 100, 'b-', linewidth=2, label='ML Strategy')
    ax1.plot(days, momentum * 100, 'g-', linewidth=2, label='Momentum Strategy')

    ax1.set_xlabel('Trading Days', fontsize=11)
    ax1.set_ylabel('Cumulative Return (%)', fontsize=11)
    ax1.set_title('Strategy Backtest: Cumulative Returns', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='#999999', linestyle='--', linewidth=1)

    # Performance metrics
    ax2 = axes[1]
    strategies = ['Benchmark', 'ML Strategy', 'Momentum']
    sharpe = [0.95, 1.45, 1.15]
    max_dd = [-0.18, -0.12, -0.15]
    annual_ret = [0.12, 0.18, 0.14]

    x = np.arange(len(strategies))
    width = 0.25

    bars1 = ax2.bar(x - width, sharpe, width, label='Sharpe Ratio', color='#4A90E2')
    bars2 = ax2.bar(x, [r * 100 for r in annual_ret], width, label='Annual Return (%/10)', color='#44A044')
    bars3 = ax2.bar(x + width, [-d * 100 for d in max_dd], width, label='Max Drawdown (%)', color='#D62728')

    ax2.set_xlabel('Strategy', fontsize=11)
    ax2.set_ylabel('Metric Value', fontsize=11)
    ax2.set_title('Performance Metrics Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(strategies)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Algorithmic Trading Strategy Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'trading_strategy_backtest.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
