"""
Portfolio Optimization with ML
Efficient frontier and ML enhancements

Output: portfolio_optimization_ml.pdf
Module: module_03_ai_ml
Lesson: 33 - Robo-Advisors ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Portfolio Optimization ML',
    'module': 'module_03_ai_ml',
    'lesson': 33,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/portfolio_optimization_ml'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Efficient Frontier
    ax1 = axes[0]

    # Generate efficient frontier curve
    risk = np.linspace(0.08, 0.25, 100)
    # Traditional mean-variance
    return_mv = 0.02 + 0.6 * risk - 0.5 * risk**2
    # ML-enhanced
    return_ml = 0.025 + 0.65 * risk - 0.4 * risk**2

    ax1.plot(risk * 100, return_mv * 100, 'b-', linewidth=2.5, label='Mean-Variance')
    ax1.plot(risk * 100, return_ml * 100, 'g-', linewidth=2.5, label='ML-Enhanced')

    # Random portfolios
    rand_risk = np.random.uniform(0.08, 0.25, 50)
    rand_return = 0.015 + 0.5 * rand_risk - 0.3 * rand_risk**2 + np.random.randn(50) * 0.02
    ax1.scatter(rand_risk * 100, rand_return * 100, c='gray', alpha=0.4, s=30, label='Random Portfolios')

    # Optimal portfolio points
    ax1.scatter([15], [11], c='#D62728', s=200, marker='*', zorder=5, label='Max Sharpe (MV)')
    ax1.scatter([14], [12], c='#44A044', s=200, marker='*', zorder=5, label='Max Sharpe (ML)')

    ax1.set_xlabel('Portfolio Risk (Std Dev %)', fontsize=11)
    ax1.set_ylabel('Expected Return (%)', fontsize=11)
    ax1.set_title('Efficient Frontier: Traditional vs ML', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(5, 28)
    ax1.set_ylim(0, 16)

    # ML Enhancement Methods
    ax2 = axes[1]

    methods = ['Mean-Variance\n(Baseline)', 'Black-Litterman', 'Risk Parity', 'ML Covariance\nShrinkage', 'Deep Learning\nPortfolio']
    sharpe = [0.72, 0.85, 0.91, 0.95, 0.88]
    max_dd = [18, 15, 12, 11, 14]

    x = np.arange(len(methods))
    width = 0.35

    bars1 = ax2.bar(x - width/2, sharpe, width, label='Sharpe Ratio', color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x + width/2, [d/20 for d in max_dd], width, label='Max Drawdown (/20)', color='#D62728', alpha=0.8)

    ax2.set_xlabel('Optimization Method', fontsize=11)
    ax2.set_ylabel('Metric Value', fontsize=11)
    ax2.set_title('ML Portfolio Optimization Methods', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(methods, fontsize=8)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 1.2)
    ax2.yaxis.grid(True, alpha=0.3)

    # Highlight best
    ax2.annotate('Best\nRisk-Adjusted', xy=(3, 0.95), xytext=(3.5, 1.1),
                fontsize=9, fontweight='bold', color='#4A90E2',
                arrowprops=dict(arrowstyle='->', color='#4A90E2'))

    fig.suptitle('ML-Enhanced Portfolio Optimization', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'portfolio_optimization_ml.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
