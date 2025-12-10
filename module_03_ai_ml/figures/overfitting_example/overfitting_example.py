"""
Overfitting Example
Training vs test performance

Output: overfitting_example.pdf
Module: module_03_ai_ml
Lesson: 34 - Prediction Limitations
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Overfitting Example',
    'module': 'module_03_ai_ml',
    'lesson': 34,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/overfitting_example'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Learning Curves
    ax1 = axes[0]

    complexity = np.arange(1, 21)

    # Training error (decreases with complexity)
    train_error = 0.4 * np.exp(-0.3 * complexity) + 0.02

    # Test error (U-shaped)
    test_error = 0.4 * np.exp(-0.3 * complexity) + 0.05 * (complexity - 5)**2 / 100 + 0.05

    ax1.plot(complexity, train_error, 'b-', linewidth=2.5, marker='o', markersize=5, label='Training Error')
    ax1.plot(complexity, test_error, 'r-', linewidth=2.5, marker='s', markersize=5, label='Test Error')

    # Optimal complexity zone
    ax1.axvline(x=6, color='#44A044', linestyle='--', linewidth=2, alpha=0.7)
    ax1.fill_between([4, 8], [0, 0], [0.5, 0.5], alpha=0.1, color='#44A044')
    ax1.text(6, 0.45, 'Optimal\nComplexity', ha='center', fontsize=9, fontweight='bold', color='#44A044')

    # Zone labels
    ax1.text(2, 0.35, 'Underfitting', ha='center', fontsize=10, color='#D62728')
    ax1.text(16, 0.35, 'Overfitting', ha='center', fontsize=10, color='#D62728')

    ax1.set_xlabel('Model Complexity', fontsize=11)
    ax1.set_ylabel('Error', fontsize=11)
    ax1.set_title('Bias-Variance Trade-off', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(0, 21)
    ax1.set_ylim(0, 0.5)
    ax1.grid(True, alpha=0.3)

    # Backtest vs Live Performance
    ax2 = axes[1]

    strategies = ['Strategy A', 'Strategy B', 'Strategy C', 'Strategy D', 'Strategy E']
    backtest_sharpe = [2.5, 1.8, 1.2, 0.9, 0.7]
    live_sharpe = [0.3, 0.6, 0.8, 0.75, 0.65]

    x = np.arange(len(strategies))
    width = 0.35

    bars1 = ax2.bar(x - width/2, backtest_sharpe, width, label='Backtest Sharpe', color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x + width/2, live_sharpe, width, label='Live Sharpe', color='#D62728', alpha=0.8)

    # Performance degradation line
    degradation = [(b - l) / b * 100 for b, l in zip(backtest_sharpe, live_sharpe)]

    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, degradation, 'ko-', linewidth=2, markersize=8, label='Degradation %')
    ax2_twin.set_ylabel('Performance Degradation (%)', fontsize=10)
    ax2_twin.set_ylim(0, 100)

    ax2.set_xlabel('Trading Strategy', fontsize=11)
    ax2.set_ylabel('Sharpe Ratio', fontsize=11)
    ax2.set_title('Backtest vs. Live Performance', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(strategies)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 3)
    ax2.yaxis.grid(True, alpha=0.3)

    # Warning annotation
    ax2.annotate('Most overfit\nstrategy', xy=(0, 2.5), xytext=(1, 2.8),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    fig.suptitle('ML Overfitting in Financial Models', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'overfitting_example.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
