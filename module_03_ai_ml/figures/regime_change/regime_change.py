"""
Regime Change in Financial Markets
Impact on model performance

Output: regime_change.pdf
Module: module_03_ai_ml
Lesson: 34 - Prediction Limitations
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Regime Change',
    'module': 'module_03_ai_ml',
    'lesson': 34,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/regime_change'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), height_ratios=[1.5, 1])

    np.random.seed(42)

    # Market regimes
    ax1 = axes[0]

    days = np.arange(0, 500)

    # Generate price with different regimes
    price = [100]
    regimes = []
    for i in range(1, 500):
        if i < 150:  # Bull market
            ret = np.random.normal(0.001, 0.01)
            regimes.append('Bull')
        elif i < 250:  # High volatility
            ret = np.random.normal(0, 0.025)
            regimes.append('Crisis')
        elif i < 400:  # Range-bound
            ret = np.random.normal(0, 0.008)
            regimes.append('Sideways')
        else:  # Recovery
            ret = np.random.normal(0.0008, 0.012)
            regimes.append('Recovery')
        price.append(price[-1] * (1 + ret))
    regimes.insert(0, 'Bull')

    ax1.plot(days, price, 'k-', linewidth=1.5)

    # Color regimes
    regime_colors = {'Bull': '#44A044', 'Crisis': '#D62728', 'Sideways': '#888888', 'Recovery': '#4A90E2'}
    for regime, color in regime_colors.items():
        mask = np.array(regimes) == regime
        ax1.fill_between(days, min(price)*0.9, max(price)*1.1, where=mask,
                        alpha=0.2, color=color, label=regime)

    ax1.set_ylabel('Price', fontsize=11)
    ax1.set_title('Market Regimes and Price Dynamics', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9, ncol=4)
    ax1.set_xlim(0, 500)
    ax1.grid(True, alpha=0.3)

    # Model performance by regime
    ax2 = axes[1]

    regimes_list = ['Bull', 'Crisis', 'Sideways', 'Recovery']
    model_perf = {
        'Momentum': [0.8, -0.5, 0.1, 0.4],
        'Mean Reversion': [0.2, 0.6, 0.7, 0.3],
        'ML Ensemble': [0.6, 0.2, 0.5, 0.5],
        'Trend Following': [0.7, -0.3, -0.2, 0.5]
    }

    x = np.arange(len(regimes_list))
    width = 0.2
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6']

    for i, (model, perfs) in enumerate(model_perf.items()):
        ax2.bar(x + i*width - 1.5*width, perfs, width, label=model, color=colors[i], alpha=0.8)

    ax2.axhline(y=0, color='black', linewidth=1)
    ax2.set_xlabel('Market Regime', fontsize=11)
    ax2.set_ylabel('Strategy Performance', fontsize=11)
    ax2.set_title('Model Performance Varies by Regime', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(regimes_list)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(-0.8, 1)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Regime Change: ML Model Fragility', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'regime_change.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
