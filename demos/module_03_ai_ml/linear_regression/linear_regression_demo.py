"""
Linear Regression Demonstration

This script demonstrates simple linear regression on synthetic financial data,
showing the relationship between market cap and stock returns.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set font size globally and random seed for reproducibility
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

def generate_synthetic_data(n=100):
    """
    Generate synthetic financial data: market cap vs returns.

    Parameters:
    -----------
    n : int
        Number of data points

    Returns:
    --------
    tuple
        (market_cap, returns) arrays
    """
    # Market cap in billions (log-normal distribution)
    market_cap = np.exp(np.random.normal(5, 1.5, n))

    # Returns with negative correlation to size (size effect)
    # Smaller companies tend to have higher returns (with noise)
    true_relationship = 15 - 2 * np.log(market_cap)
    noise = np.random.normal(0, 3, n)
    returns = true_relationship + noise

    return market_cap, returns

def linear_regression(x, y):
    """
    Perform simple linear regression.

    Parameters:
    -----------
    x, y : array-like
        Input and output variables

    Returns:
    --------
    tuple
        (slope, intercept, r_squared)
    """
    # Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate slope and intercept
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    # Calculate R-squared
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    return slope, intercept, r_squared

def main():
    # Generate data
    market_cap, returns = generate_synthetic_data(n=100)

    # Transform market cap to log scale for better linear relationship
    log_market_cap = np.log(market_cap)

    # Perform regression
    slope, intercept, r_squared = linear_regression(log_market_cap, returns)

    # Create predictions
    x_line = np.linspace(log_market_cap.min(), log_market_cap.max(), 100)
    y_line = slope * x_line + intercept

    # Calculate residuals for a few points
    y_pred = slope * log_market_cap + intercept
    residuals = returns - y_pred

    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Plot 1: Scatter plot with regression line
    ax1.scatter(log_market_cap, returns, color='gray', alpha=0.6, s=30,
               edgecolor='black', linewidth=0.5, label='Observed data')
    ax1.plot(x_line, y_line, 'k-', linewidth=2, label='Regression line')

    # Show residuals for a few points
    sample_indices = np.random.choice(len(log_market_cap), 10, replace=False)
    for idx in sample_indices:
        ax1.plot([log_market_cap[idx], log_market_cap[idx]],
                [returns[idx], y_pred[idx]],
                'k--', linewidth=0.5, alpha=0.3)

    # Add regression equation
    equation_text = f'Return = {intercept:.2f} + {slope:.2f} * ln(MarketCap)\n$R^2$ = {r_squared:.3f}'
    ax1.text(0.05, 0.95, equation_text, transform=ax1.transAxes,
            fontsize=7, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax1.set_xlabel('ln(Market Cap in Billion USD)', fontsize=8)
    ax1.set_ylabel('Annual Return (%)', fontsize=8)
    ax1.set_title('Linear Regression: Market Cap vs Returns', fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=7, loc='lower left')

    # Plot 2: Residuals plot
    ax2.scatter(y_pred, residuals, color='gray', alpha=0.6, s=30,
               edgecolor='black', linewidth=0.5)
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=1)

    # Add horizontal lines at +/- 2 standard deviations
    std_residuals = np.std(residuals)
    ax2.axhline(y=2*std_residuals, color='gray', linestyle=':', linewidth=0.5)
    ax2.axhline(y=-2*std_residuals, color='gray', linestyle=':', linewidth=0.5)
    ax2.text(y_pred.min(), 2*std_residuals + 0.5, '+2 SD', fontsize=6, color='gray')
    ax2.text(y_pred.min(), -2*std_residuals - 0.5, '-2 SD', fontsize=6, color='gray')

    ax2.set_xlabel('Fitted Values', fontsize=8)
    ax2.set_ylabel('Residuals', fontsize=8)
    ax2.set_title('Residual Plot (Model Diagnostics)', fontsize=8)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'linear_regression_demo.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print regression statistics
    print("\nRegression Results:")
    print("-" * 50)
    print(f"Slope (beta):      {slope:.4f}")
    print(f"Intercept (alpha): {intercept:.4f}")
    print(f"R-squared:         {r_squared:.4f}")
    print(f"RMSE:              {np.sqrt(np.mean(residuals**2)):.4f}")
    print("\nInterpretation:")
    print(f"For each 1-unit increase in ln(Market Cap),")
    print(f"expected return changes by {slope:.2f} percentage points.")

if __name__ == '__main__':
    main()
