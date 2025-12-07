"""
Portfolio Efficient Frontier Visualization

This script demonstrates Modern Portfolio Theory by calculating and visualizing
the efficient frontier for a multi-asset portfolio.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set font size globally and random seed
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

def generate_asset_data(n_assets=4, n_days=252):
    """
    Generate synthetic return data for multiple assets.

    Parameters:
    -----------
    n_assets : int
        Number of assets
    n_days : int
        Number of trading days

    Returns:
    --------
    tuple
        (returns, asset_names, expected_returns, cov_matrix)
    """
    # Asset parameters (annual)
    asset_names = ['Stock A', 'Stock B', 'Bond', 'Gold']
    annual_returns = np.array([0.12, 0.10, 0.05, 0.07])  # Expected annual returns
    annual_vols = np.array([0.25, 0.20, 0.08, 0.15])  # Annual volatilities

    # Correlation matrix
    correlation = np.array([
        [1.00, 0.60, 0.10, -0.20],  # Stock A
        [0.60, 1.00, 0.15, -0.10],  # Stock B
        [0.10, 0.15, 1.00, 0.25],   # Bond
        [-0.20, -0.10, 0.25, 1.00]  # Gold (negative correlation with stocks)
    ])

    # Convert to covariance matrix
    cov_matrix = np.outer(annual_vols, annual_vols) * correlation

    return asset_names, annual_returns, cov_matrix

def portfolio_performance(weights, returns, cov_matrix):
    """
    Calculate portfolio return and risk.

    Parameters:
    -----------
    weights : np.array
        Portfolio weights
    returns : np.array
        Expected returns for each asset
    cov_matrix : np.array
        Covariance matrix

    Returns:
    --------
    tuple
        (portfolio_return, portfolio_risk)
    """
    portfolio_return = np.dot(weights, returns)
    portfolio_risk = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_risk

def generate_random_portfolios(n_portfolios, returns, cov_matrix):
    """Generate random portfolio allocations."""
    n_assets = len(returns)
    results = np.zeros((3, n_portfolios))

    for i in range(n_portfolios):
        # Generate random weights
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)  # Normalize to sum to 1

        # Calculate performance
        port_return, port_risk = portfolio_performance(weights, returns, cov_matrix)

        # Store results
        results[0, i] = port_risk
        results[1, i] = port_return
        results[2, i] = port_return / port_risk  # Sharpe ratio (assuming rf=0)

    return results

def optimize_portfolio(target_return, returns, cov_matrix):
    """
    Find minimum variance portfolio for a target return.
    Simplified optimization using random search.
    """
    n_assets = len(returns)
    best_risk = float('inf')
    best_weights = None

    # Random search
    for _ in range(10000):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)

        port_return, port_risk = portfolio_performance(weights, returns, cov_matrix)

        # Check if return matches target (within tolerance)
        if abs(port_return - target_return) < 0.001 and port_risk < best_risk:
            best_risk = port_risk
            best_weights = weights

    return best_weights, best_risk

def calculate_efficient_frontier(returns, cov_matrix, n_points=50):
    """Calculate the efficient frontier."""
    min_return = np.min(returns)
    max_return = np.max(returns)

    target_returns = np.linspace(min_return, max_return, n_points)
    efficient_risks = []

    for target in target_returns:
        weights, risk = optimize_portfolio(target, returns, cov_matrix)
        if risk != float('inf'):
            efficient_risks.append(risk)
        else:
            efficient_risks.append(np.nan)

    return target_returns, np.array(efficient_risks)

def main():
    # Generate asset data
    asset_names, expected_returns, cov_matrix = generate_asset_data()

    # Calculate individual asset risk-return
    individual_risks = np.sqrt(np.diag(cov_matrix))

    # Generate random portfolios
    n_portfolios = 5000
    random_portfolios = generate_random_portfolios(n_portfolios, expected_returns, cov_matrix)

    # Calculate efficient frontier
    frontier_returns, frontier_risks = calculate_efficient_frontier(
        expected_returns, cov_matrix, n_points=30
    )

    # Calculate minimum variance portfolio
    min_var_weights, min_var_risk = optimize_portfolio(
        np.mean(expected_returns), expected_returns, cov_matrix
    )
    min_var_return, _ = portfolio_performance(min_var_weights, expected_returns, cov_matrix)

    # Calculate maximum Sharpe ratio portfolio (assuming risk-free rate = 0)
    max_sharpe_idx = np.argmax(random_portfolios[2])
    max_sharpe_return = random_portfolios[1, max_sharpe_idx]
    max_sharpe_risk = random_portfolios[0, max_sharpe_idx]

    # Create visualization
    fig = plt.figure(figsize=(10, 7))
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1])
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])

    # Plot 1: Efficient Frontier
    # Random portfolios
    scatter = ax1.scatter(random_portfolios[0], random_portfolios[1],
                         c=random_portfolios[2], cmap='gray',
                         alpha=0.3, s=10, edgecolors='none')

    # Efficient frontier
    ax1.plot(frontier_risks, frontier_returns, 'k-', linewidth=2.5,
            label='Efficient Frontier')

    # Individual assets
    for i, name in enumerate(asset_names):
        ax1.scatter(individual_risks[i], expected_returns[i],
                   marker='s', s=100, color='white', edgecolor='black',
                   linewidth=1.5, zorder=5)
        ax1.annotate(name, (individual_risks[i], expected_returns[i]),
                    xytext=(10, 5), textcoords='offset points',
                    fontsize=7, bbox=dict(boxstyle='round', facecolor='white',
                                         alpha=0.7, edgecolor='gray'))

    # Mark special portfolios
    ax1.scatter(min_var_risk, min_var_return, marker='*', s=300,
               color='black', edgecolor='white', linewidth=1,
               label='Min Variance', zorder=5)

    ax1.scatter(max_sharpe_risk, max_sharpe_return, marker='D', s=150,
               color='black', edgecolor='white', linewidth=1,
               label='Max Sharpe Ratio', zorder=5)

    ax1.set_xlabel('Portfolio Risk (Annual Volatility)', fontsize=8)
    ax1.set_ylabel('Expected Return (Annual)', fontsize=8)
    ax1.set_title('Portfolio Efficient Frontier', fontsize=8)
    ax1.legend(fontsize=7, loc='lower right')
    ax1.grid(True, alpha=0.3)

    # Format axes as percentages
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))

    # Colorbar for Sharpe ratio
    cbar = plt.colorbar(scatter, ax=ax1)
    cbar.set_label('Sharpe Ratio', fontsize=7)
    cbar.ax.tick_params(labelsize=7)

    # Plot 2: Risk-Return by Asset
    bars = ax2.bar(asset_names, expected_returns * 100,
                   color=['darkgray', 'gray', 'lightgray', 'black'],
                   edgecolor='black', alpha=0.7)

    for bar, ret in zip(bars, expected_returns):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{ret*100:.1f}%', ha='center', va='bottom', fontsize=7)

    ax2.set_ylabel('Expected Return (%)', fontsize=8)
    ax2.set_title('Individual Asset Expected Returns', fontsize=8)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_xticklabels(asset_names, rotation=15, ha='right')

    # Plot 3: Portfolio weights for optimal portfolios
    portfolios_to_show = {
        'Min Variance': min_var_weights,
        'Equal Weight': np.ones(len(asset_names)) / len(asset_names),
    }

    x = np.arange(len(asset_names))
    width = 0.35

    weights_min_var = portfolios_to_show['Min Variance']
    weights_equal = portfolios_to_show['Equal Weight']

    bars1 = ax3.bar(x - width/2, weights_min_var * 100, width,
                   label='Min Variance', color='gray', edgecolor='black', alpha=0.7)
    bars2 = ax3.bar(x + width/2, weights_equal * 100, width,
                   label='Equal Weight', color='black', edgecolor='black', alpha=0.7)

    ax3.set_ylabel('Portfolio Weight (%)', fontsize=8)
    ax3.set_title('Portfolio Allocations', fontsize=8)
    ax3.set_xticks(x)
    ax3.set_xticklabels(asset_names, rotation=15, ha='right')
    ax3.legend(fontsize=7)
    ax3.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'portfolio_efficient_frontier.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print detailed results
    print("\nAsset Statistics:")
    print("-" * 70)
    print(f"{'Asset':<12} {'Expected Return':>15} {'Volatility':>15} {'Sharpe Ratio':>15}")
    print("-" * 70)

    for i, name in enumerate(asset_names):
        sharpe = expected_returns[i] / individual_risks[i]
        print(f"{name:<12} {expected_returns[i]*100:>14.2f}% "
              f"{individual_risks[i]*100:>14.2f}% {sharpe:>15.2f}")

    print("\n" + "-" * 70)
    print("Correlation Matrix:")
    print("-" * 70)

    # Print correlation matrix
    corr_matrix = cov_matrix / np.outer(individual_risks, individual_risks)
    print(f"{'':12}", end="")
    for name in asset_names:
        print(f"{name:>12}", end="")
    print()

    for i, name in enumerate(asset_names):
        print(f"{name:<12}", end="")
        for j in range(len(asset_names)):
            print(f"{corr_matrix[i,j]:>12.2f}", end="")
        print()

    print("\n" + "-" * 70)
    print("Optimal Portfolios:")
    print("-" * 70)
    print("\nMinimum Variance Portfolio:")
    print(f"Expected Return: {min_var_return*100:.2f}%")
    print(f"Volatility:      {min_var_risk*100:.2f}%")
    print(f"Sharpe Ratio:    {min_var_return/min_var_risk:.2f}")
    print("Weights:")
    for name, weight in zip(asset_names, min_var_weights):
        print(f"  {name:<12} {weight*100:>6.2f}%")

    print("\nMaximum Sharpe Ratio Portfolio:")
    print(f"Expected Return: {max_sharpe_return*100:.2f}%")
    print(f"Volatility:      {max_sharpe_risk*100:.2f}%")
    print(f"Sharpe Ratio:    {max_sharpe_return/max_sharpe_risk:.2f}")

if __name__ == '__main__':
    main()
