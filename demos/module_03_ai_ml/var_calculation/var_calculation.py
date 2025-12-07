"""
Value at Risk (VaR) Calculation and Visualization

This script demonstrates historical VaR calculation on simulated asset returns,
showing the distribution and VaR threshold visualization.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# Set font size globally and random seed
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

def generate_returns(n_days=1000, annual_return=0.08, annual_vol=0.20):
    """
    Generate synthetic daily returns using geometric Brownian motion.

    Parameters:
    -----------
    n_days : int
        Number of trading days
    annual_return : float
        Expected annual return
    annual_vol : float
        Annual volatility

    Returns:
    --------
    np.array
        Daily returns
    """
    # Convert to daily parameters
    daily_return = annual_return / 252
    daily_vol = annual_vol / np.sqrt(252)

    # Generate returns with fat tails (Student's t-distribution)
    df = 5  # Degrees of freedom (lower = fatter tails)
    returns = stats.t.rvs(df, loc=daily_return, scale=daily_vol, size=n_days)

    return returns

def calculate_var(returns, confidence_level=0.95):
    """
    Calculate historical VaR at specified confidence level.

    Parameters:
    -----------
    returns : np.array
        Historical returns
    confidence_level : float
        Confidence level (e.g., 0.95 for 95%)

    Returns:
    --------
    float
        VaR value (positive number representing potential loss)
    """
    var = -np.percentile(returns, (1 - confidence_level) * 100)
    return var

def calculate_cvar(returns, confidence_level=0.95):
    """
    Calculate Conditional VaR (Expected Shortfall).

    Parameters:
    -----------
    returns : np.array
        Historical returns
    confidence_level : float
        Confidence level

    Returns:
    --------
    float
        CVaR value
    """
    var = -calculate_var(returns, confidence_level)
    cvar = -returns[returns <= var].mean()
    return cvar

def main():
    # Generate returns
    returns = generate_returns(n_days=1000)

    # Calculate VaR at different confidence levels
    confidence_levels = [0.90, 0.95, 0.99]
    vars = {cl: calculate_var(returns, cl) for cl in confidence_levels}
    cvars = {cl: calculate_cvar(returns, cl) for cl in confidence_levels}

    # Portfolio value
    portfolio_value = 1_000_000  # $1 million

    # Create visualization
    fig = plt.figure(figsize=(10, 7))
    gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1])
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[2, :])

    # Plot 1: Returns distribution with VaR thresholds
    n, bins, patches = ax1.hist(returns * 100, bins=50, color='gray',
                                 edgecolor='black', alpha=0.7, density=True)

    # Overlay normal distribution for comparison
    mu, sigma = returns.mean() * 100, returns.std() * 100
    x = np.linspace(returns.min() * 100, returns.max() * 100, 100)
    ax1.plot(x, stats.norm.pdf(x, mu, sigma), 'k--', linewidth=1.5,
            label='Normal distribution', alpha=0.7)

    # Mark VaR levels
    colors_var = ['darkgray', 'gray', 'black']
    linestyles = [':', '--', '-']
    for (cl, var), color, ls in zip(vars.items(), colors_var, linestyles):
        ax1.axvline(x=-var * 100, color=color, linestyle=ls, linewidth=1.5,
                   label=f'VaR {cl*100:.0f}%: {var*100:.2f}%')

    ax1.set_xlabel('Daily Return (%)', fontsize=8)
    ax1.set_ylabel('Density', fontsize=8)
    ax1.set_title('Distribution of Daily Returns with VaR Thresholds', fontsize=8)
    ax1.legend(fontsize=7, loc='upper left')
    ax1.grid(True, alpha=0.3, axis='y')

    # Plot 2: VaR comparison
    cl_labels = [f'{cl*100:.0f}%' for cl in confidence_levels]
    var_values = [vars[cl] * 100 for cl in confidence_levels]

    bars = ax2.bar(range(len(confidence_levels)), var_values,
                   color=['darkgray', 'gray', 'black'], edgecolor='black', alpha=0.7)

    for bar, val in zip(bars, var_values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{val:.2f}%', ha='center', va='bottom', fontsize=7)

    ax2.set_ylabel('VaR (%)', fontsize=8)
    ax2.set_xlabel('Confidence Level', fontsize=8)
    ax2.set_title('Value at Risk Comparison', fontsize=8)
    ax2.set_xticks(range(len(confidence_levels)))
    ax2.set_xticklabels(cl_labels)
    ax2.grid(True, alpha=0.3, axis='y')

    # Plot 3: VaR vs CVaR
    x_pos = np.arange(len(confidence_levels))
    width = 0.35

    var_values = [vars[cl] * 100 for cl in confidence_levels]
    cvar_values = [cvars[cl] * 100 for cl in confidence_levels]

    bars1 = ax3.bar(x_pos - width/2, var_values, width, label='VaR',
                   color='gray', edgecolor='black', alpha=0.7)
    bars2 = ax3.bar(x_pos + width/2, cvar_values, width, label='CVaR',
                   color='black', edgecolor='black', alpha=0.7)

    ax3.set_ylabel('Risk Metric (%)', fontsize=8)
    ax3.set_xlabel('Confidence Level', fontsize=8)
    ax3.set_title('VaR vs CVaR (Expected Shortfall)', fontsize=8)
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(cl_labels)
    ax3.legend(fontsize=7)
    ax3.grid(True, alpha=0.3, axis='y')

    # Plot 4: Portfolio value scenarios
    days_forward = 252  # One year
    n_scenarios = 5

    for i in range(n_scenarios):
        scenario_returns = generate_returns(n_days=days_forward)
        cumulative_returns = np.cumprod(1 + scenario_returns)
        portfolio_path = portfolio_value * cumulative_returns

        color = 'black' if i == 0 else 'gray'
        alpha = 0.8 if i == 0 else 0.3
        linewidth = 1.5 if i == 0 else 0.8

        ax4.plot(range(days_forward), portfolio_path, color=color,
                alpha=alpha, linewidth=linewidth)

    # Add 95% VaR line
    daily_var_95 = vars[0.95]
    var_portfolio_value = portfolio_value * (1 - daily_var_95)
    ax4.axhline(y=var_portfolio_value, color='black', linestyle='--',
               linewidth=1.5, label=f'Daily VaR 95% threshold')

    ax4.set_xlabel('Trading Days', fontsize=8)
    ax4.set_ylabel('Portfolio Value (USD)', fontsize=8)
    ax4.set_title(f'Portfolio Scenarios (Initial: ${portfolio_value:,.0f})', fontsize=8)
    ax4.legend(fontsize=7)
    ax4.grid(True, alpha=0.3)
    ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.2f}M'))

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'var_calculation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print detailed results
    print("\nValue at Risk Analysis:")
    print("-" * 70)
    print(f"Portfolio value: ${portfolio_value:,.0f}")
    print(f"Sample size: {len(returns)} trading days")
    print(f"Mean daily return: {returns.mean()*100:.3f}%")
    print(f"Daily volatility: {returns.std()*100:.3f}%")
    print("\n" + "-" * 70)
    print(f"{'Confidence':>12} {'VaR (%)':>12} {'VaR ($)':>15} {'CVaR (%)':>12} {'CVaR ($)':>15}")
    print("-" * 70)

    for cl in confidence_levels:
        var_pct = vars[cl] * 100
        var_usd = vars[cl] * portfolio_value
        cvar_pct = cvars[cl] * 100
        cvar_usd = cvars[cl] * portfolio_value

        print(f"{cl*100:>11.0f}% {var_pct:>12.3f} ${var_usd:>14,.0f} "
              f"{cvar_pct:>12.3f} ${cvar_usd:>14,.0f}")

    print("-" * 70)
    print("\nInterpretation:")
    print(f"With 95% confidence, the portfolio will not lose more than")
    print(f"${vars[0.95] * portfolio_value:,.0f} ({vars[0.95]*100:.2f}%) in one day.")
    print(f"\nIf losses exceed VaR 95%, the expected loss is ${cvars[0.95] * portfolio_value:,.0f} (CVaR).")

if __name__ == '__main__':
    main()
