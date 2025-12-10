"""
Expected Shortfall (CVaR)
Conditional VaR visualization

Output: expected_shortfall.pdf
Module: module_04_trad_finance
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Expected Shortfall',
    'module': 'module_04_trad_finance',
    'lesson': 42,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/expected_shortfall'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # ES vs VaR Comparison
    ax1 = axes[0]

    # Generate returns with fat tails
    returns = np.concatenate([
        np.random.normal(0, 0.015, 900),
        np.random.normal(-0.05, 0.02, 100)  # Fat tail
    ])
    returns = np.sort(returns)

    var_95 = np.percentile(returns, 5)
    var_99 = np.percentile(returns, 1)

    # Expected Shortfall = mean of returns below VaR
    es_95 = returns[returns <= var_95].mean()
    es_99 = returns[returns <= var_99].mean()

    # Plot
    ax1.hist(returns, bins=50, density=True, alpha=0.7, color='#4A90E2', label='Returns')

    # VaR and ES lines
    ax1.axvline(x=var_95, color='#FF7F0E', linestyle='--', linewidth=2, label=f'VaR 95%: {var_95*100:.1f}%')
    ax1.axvline(x=es_95, color='#D62728', linestyle='-', linewidth=2, label=f'ES 95%: {es_95*100:.1f}%')

    # Shade ES region
    mask = returns <= var_95
    ax1.fill_between(returns[mask], 0, 1, alpha=0.3, color='#D62728', transform=ax1.get_xaxis_transform())

    ax1.set_xlabel('Daily Return', fontsize=11)
    ax1.set_ylabel('Frequency', fontsize=11)
    ax1.set_title('VaR vs. Expected Shortfall', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(-0.12, 0.08)
    ax1.grid(True, alpha=0.3)

    # Add annotation
    ax1.annotate('ES captures\ntail risk better', xy=(es_95, 5), xytext=(-0.08, 15),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    # VaR vs ES Summary
    ax2 = axes[1]

    metrics = ['VaR 95%', 'ES 95%', 'VaR 99%', 'ES 99%']
    values = [abs(var_95)*100, abs(es_95)*100, abs(var_99)*100, abs(es_99)*100]
    colors = ['#FF7F0E', '#D62728', '#FF7F0E', '#D62728']

    bars = ax2.bar(metrics, values, color=colors, alpha=0.8, edgecolor='black')

    for bar, val in zip(bars, values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{val:.2f}%', ha='center', fontsize=11, fontweight='bold')

    ax2.set_xlabel('Risk Metric', fontsize=11)
    ax2.set_ylabel('Loss (%)', fontsize=11)
    ax2.set_title('Risk Metric Comparison', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 8)
    ax2.yaxis.grid(True, alpha=0.3)

    # Regulatory note
    ax2.text(1.5, 7, 'Basel III requires ES at 97.5%', fontsize=10,
            ha='center', style='italic', color='#666666')

    fig.suptitle('Expected Shortfall: Beyond VaR', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'expected_shortfall.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
