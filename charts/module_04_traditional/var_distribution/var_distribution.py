"""
Value at Risk (VaR) Distribution Visualization
VaR on return distribution with confidence levels

Required libraries: matplotlib, numpy, scipy
Output: var_distribution.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Value at Risk (VaR) Distribution Visualization',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_04_traditional/var_distribution'
}

def create_var_distribution():
    """Create visualization of VaR on return distribution"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig = plt.figure(figsize=(10, 8))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Generate synthetic return distribution
    mu = 0.0005  # Daily mean return (0.05%)
    sigma = 0.02  # Daily volatility (2%)
    n_samples = 10000

    returns = np.random.normal(mu, sigma, n_samples)

    # Calculate VaR at different confidence levels
    confidence_levels = [0.90, 0.95, 0.99]
    var_values = {}

    for conf in confidence_levels:
        alpha = 1 - conf
        var_values[conf] = -np.percentile(returns, alpha * 100)

    # Top left: Return distribution with VaR
    ax1 = fig.add_subplot(gs[0, :])

    # Plot histogram
    n, bins, patches = ax1.hist(returns, bins=50, density=True,
                                color='lightgray', edgecolor='black',
                                linewidth=0.5, alpha=0.7, label='Empirical Distribution')

    # Plot theoretical normal distribution
    x = np.linspace(returns.min(), returns.max(), 1000)
    theoretical = stats.norm.pdf(x, mu, sigma)
    ax1.plot(x, theoretical, 'k-', linewidth=2, label='Normal Distribution')

    # Mark VaR levels
    colors_var = ['black', 'darkgray', 'gray']
    for i, (conf, color) in enumerate(zip(confidence_levels, colors_var)):
        var = var_values[conf]
        ax1.axvline(x=-var, color=color, linestyle='--',
                   linewidth=1.5, label=f'VaR {conf:.0%}: {var*100:.2f}%')

        # Shade tail area
        if i == 1:  # Shade 95% VaR for visibility
            tail_x = x[x <= -var]
            tail_y = stats.norm.pdf(tail_x, mu, sigma)
            ax1.fill_between(tail_x, 0, tail_y, alpha=0.3,
                           color='gray', label=f'{(1-conf)*100:.0f}% Tail')

    ax1.set_xlabel('Daily Return', fontsize=8)
    ax1.set_ylabel('Probability Density', fontsize=8)
    ax1.set_title('Return Distribution and Value at Risk (VaR)', fontsize=10, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=7, ncol=2)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Add statistics box
    stats_text = f'Mean: {mu*100:.3f}%\nStd Dev: {sigma*100:.2f}%\nSkewness: {stats.skew(returns):.3f}\nKurtosis: {stats.kurtosis(returns):.3f}'
    ax1.text(0.02, 0.98, stats_text,
            transform=ax1.transAxes,
            fontsize=7,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.4',
                     facecolor='white',
                     edgecolor='black',
                     linewidth=0.5))

    # Bottom left: VaR comparison table
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.axis('off')

    # Portfolio value
    portfolio_value = 10000000  # $10 million

    var_data = [['Confidence Level', 'VaR (%)', 'VaR ($)', 'Expected Loss']]

    for conf in confidence_levels:
        var_pct = var_values[conf]
        var_dollar = var_pct * portfolio_value
        expected_shortfall = -np.mean(returns[returns <= -var_pct])

        var_data.append([
            f'{conf:.0%}',
            f'{var_pct*100:.3f}%',
            f'${var_dollar:,.0f}',
            f'{expected_shortfall*100:.3f}%'
        ])

    table = ax2.table(cellText=var_data,
                     cellLoc='center',
                     loc='center',
                     bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(7)

    # Style header
    for i in range(4):
        cell = table[(0, i)]
        cell.set_facecolor('darkgray')
        cell.set_text_props(weight='bold', color='black')

    # Style rows
    for i in range(1, len(var_data)):
        for j in range(4):
            cell = table[(i, j)]
            cell.set_facecolor('lightgray' if i % 2 == 0 else 'white')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

    ax2.set_title(f'VaR Summary (Portfolio: ${portfolio_value/1e6:.0f}M)', fontsize=10, fontweight='bold', pad=20)

    # Bottom right: VaR interpretation
    ax3 = fig.add_subplot(gs[1, 1])

    # Bar chart of VaR values
    conf_labels = [f'{c:.0%}' for c in confidence_levels]
    var_percentages = [var_values[c] * 100 for c in confidence_levels]

    bars = ax3.barh(conf_labels, var_percentages,
                   color=['lightgray', 'gray', 'darkgray'],
                   edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, var_percentages)):
        ax3.text(val + 0.05, i, f'{val:.3f}%',
                va='center', fontsize=7)

    ax3.set_xlabel('VaR (%)', fontsize=8)
    ax3.set_ylabel('Confidence Level', fontsize=8)
    ax3.set_title('VaR by Confidence Level', fontsize=10, fontweight='bold')
    ax3.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)

    # Add interpretation
    interpretation = """
    VaR Interpretation:

    95% VaR = 3.14% means:
    • 95% confidence that daily loss
      will not exceed 3.14%
    • OR: 5% chance of losing more
      than $314,000 in one day

    Limitations:
    • Assumes normal distribution
    • Ignores tail risk (fat tails)
    • No info about magnitude
      beyond VaR threshold
    """

    ax3.text(1.02, 0.5, interpretation,
            transform=ax3.transAxes,
            fontsize=6,
            verticalalignment='center',
            bbox=dict(boxstyle='round,pad=0.4',
                     facecolor='white',
                     edgecolor='black',
                     linewidth=0.5))

    # Main title
    fig.suptitle('Value at Risk (VaR) Analysis [SYNTHETIC DATA]',
                fontsize=12, fontweight='bold', y=0.98)

    # Save as PDF
    output_path = Path(__file__).parent / 'var_distribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_var_distribution()
