"""
Value at Risk (VaR) Visualization
Shows return distribution with VaR threshold

Output: var_histogram.pdf
Module: module_04_traditional
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)

    # Simulate portfolio daily returns (mean 0.05%, std 1.5%)
    returns = np.random.normal(0.0005, 0.015, 1000) * 100  # in percentage

    # Calculate VaR at different confidence levels
    var_95 = np.percentile(returns, 5)
    var_99 = np.percentile(returns, 1)

    # Plot histogram
    n, bins, patches = ax.hist(returns, bins=50, density=True, color=MLBLUE,
                                alpha=0.7, edgecolor='white')

    # Color the tail red (VaR region)
    for i, (patch, left, right) in enumerate(zip(patches, bins[:-1], bins[1:])):
        if right <= var_95:
            patch.set_facecolor(MLRED)
            patch.set_alpha(0.8)

    # Add VaR lines
    ax.axvline(x=var_95, color=MLORANGE, linewidth=2, linestyle='--',
               label=f'95% VaR: {var_95:.2f}%')
    ax.axvline(x=var_99, color=MLRED, linewidth=2, linestyle='-',
               label=f'99% VaR: {var_99:.2f}%')

    # Add normal distribution overlay
    x = np.linspace(-6, 6, 100)
    ax.plot(x, stats.norm.pdf(x, 0.05, 1.5), color=MLPURPLE, linewidth=2,
            linestyle=':', label='Normal Distribution')

    ax.set_xlabel('Daily Return (%)', fontsize=11)
    ax.set_ylabel('Probability Density', fontsize=11)
    ax.set_title('Portfolio Return Distribution with Value at Risk', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xlim(-6, 6)

    # Add annotation
    ax.annotate('5% worst\noutcomes', xy=(var_95/2, 0.02), fontsize=9,
                ha='center', color='white', fontweight='bold')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Monte Carlo simulation]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'var_histogram.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
