"""
Value at Risk Calculation
VaR methods and visualization

Output: var_calculation.pdf
Module: module_04_trad_finance
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

CHART_METADATA = {
    'title': 'VaR Calculation',
    'module': 'module_04_trad_finance',
    'lesson': 42,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/var_calculation'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # VaR Distribution
    ax1 = axes[0]

    # Generate return distribution
    returns = np.random.normal(0.0005, 0.02, 1000)

    # Calculate VaR levels
    var_95 = np.percentile(returns, 5)
    var_99 = np.percentile(returns, 1)

    # Plot histogram
    n, bins, patches = ax1.hist(returns, bins=50, density=True, alpha=0.7, color='#4A90E2')

    # Color VaR tail
    for i, (patch, left_edge) in enumerate(zip(patches, bins[:-1])):
        if left_edge < var_99:
            patch.set_facecolor('#D62728')
        elif left_edge < var_95:
            patch.set_facecolor('#FF7F0E')

    # VaR lines
    ax1.axvline(x=var_95, color='#FF7F0E', linestyle='--', linewidth=2, label=f'VaR 95%: {var_95*100:.2f}%')
    ax1.axvline(x=var_99, color='#D62728', linestyle='--', linewidth=2, label=f'VaR 99%: {var_99*100:.2f}%')

    ax1.set_xlabel('Daily Return', fontsize=11)
    ax1.set_ylabel('Frequency', fontsize=11)
    ax1.set_title('VaR: Return Distribution', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)

    # VaR Methods Comparison
    ax2 = axes[1]

    methods = ['Historical\nSimulation', 'Parametric\n(Normal)', 'Monte Carlo', 'GARCH', 'EVT\n(Extreme)']
    var_values = [3.2, 2.8, 3.1, 3.5, 4.2]  # 99% VaR as % of portfolio
    accuracy = [75, 65, 80, 85, 90]

    x = np.arange(len(methods))
    width = 0.35

    bars1 = ax2.bar(x - width/2, var_values, width, label='VaR Estimate (%)', color='#4A90E2', alpha=0.8)

    ax2_twin = ax2.twinx()
    ax2_twin.bar(x + width/2, accuracy, width, label='Backtest Accuracy (%)', color='#44A044', alpha=0.8)
    ax2_twin.set_ylabel('Backtest Accuracy (%)', fontsize=10, color='#44A044')
    ax2_twin.tick_params(axis='y', labelcolor='#44A044')
    ax2_twin.set_ylim(50, 100)

    ax2.set_xlabel('VaR Method', fontsize=11)
    ax2.set_ylabel('VaR Estimate (%)', fontsize=11)
    ax2.set_title('VaR Methods Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(methods, fontsize=9)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 5)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Value at Risk (VaR) Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'var_calculation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
