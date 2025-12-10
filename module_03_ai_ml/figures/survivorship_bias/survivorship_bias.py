"""
Survivorship Bias in Finance
Impact on backtesting and analysis

Output: survivorship_bias.pdf
Module: module_03_ai_ml
Lesson: 34 - Prediction Limitations
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Survivorship Bias',
    'module': 'module_03_ai_ml',
    'lesson': 34,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/survivorship_bias'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Survivorship bias in stock returns
    ax1 = axes[0]

    years = np.arange(2010, 2024)

    # S&P 500 with and without survivorship
    sp500_biased = [100]
    sp500_unbiased = [100]

    for i in range(len(years) - 1):
        # Biased only includes survivors (higher returns)
        sp500_biased.append(sp500_biased[-1] * (1 + np.random.uniform(0.08, 0.15)))
        # Unbiased includes all stocks including failures
        sp500_unbiased.append(sp500_unbiased[-1] * (1 + np.random.uniform(0.04, 0.10)))

    ax1.plot(years, sp500_biased, 'b-', linewidth=2.5, marker='o', label='Survivor-Only Index')
    ax1.plot(years, sp500_unbiased, 'r-', linewidth=2.5, marker='s', label='Complete Index')

    # Difference annotation
    final_diff = sp500_biased[-1] - sp500_unbiased[-1]
    ax1.annotate(f'Bias: +{final_diff:.0f}%', xy=(2023, sp500_biased[-1]),
                xytext=(2020, sp500_biased[-1] + 50), fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'))

    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Index Value (Base=100)', fontsize=11)
    ax1.set_title('Survivorship Bias in Stock Index', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Fund performance distribution
    ax2 = axes[1]

    # With survivorship bias (only successful funds shown)
    biased_returns = np.random.normal(12, 8, 100)
    biased_returns = biased_returns[biased_returns > 0]  # Remove "failed" funds

    # Without bias (all funds)
    unbiased_returns = np.random.normal(6, 12, 150)

    ax2.hist(biased_returns, bins=20, alpha=0.6, color='#4A90E2', label='Survivor Funds Only', density=True)
    ax2.hist(unbiased_returns, bins=25, alpha=0.6, color='#D62728', label='All Funds (incl. closed)', density=True)

    # Mean lines
    ax2.axvline(x=np.mean(biased_returns), color='#4A90E2', linestyle='--', linewidth=2)
    ax2.axvline(x=np.mean(unbiased_returns), color='#D62728', linestyle='--', linewidth=2)

    ax2.text(np.mean(biased_returns) + 1, 0.06, f'Mean: {np.mean(biased_returns):.1f}%',
            fontsize=9, color='#4A90E2', fontweight='bold')
    ax2.text(np.mean(unbiased_returns) - 8, 0.06, f'Mean: {np.mean(unbiased_returns):.1f}%',
            fontsize=9, color='#D62728', fontweight='bold')

    ax2.set_xlabel('Annual Return (%)', fontsize=11)
    ax2.set_ylabel('Density', fontsize=11)
    ax2.set_title('Fund Return Distribution: Bias Impact', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_xlim(-40, 40)

    fig.suptitle('Survivorship Bias in Financial Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'survivorship_bias.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
