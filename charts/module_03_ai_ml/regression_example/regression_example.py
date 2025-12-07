"""
Linear Regression Example
Scatter plot with regression line demonstration

Required libraries: matplotlib, numpy
Output: regression_example.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Linear Regression Example',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_03_ai_ml/regression_example'
}

def create_regression_example():
    """Create a visualization of linear regression with scatter plot"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Generate synthetic data
    n_points = 50
    X = np.linspace(0, 10, n_points)
    true_slope = 2.5
    true_intercept = 5
    noise = np.random.normal(0, 3, n_points)
    y = true_slope * X + true_intercept + noise

    # Calculate regression line (least squares)
    coefficients = np.polyfit(X, y, 1)
    slope, intercept = coefficients
    y_pred = slope * X + intercept

    # Calculate R-squared
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # Left panel: Regression plot
    ax1.scatter(X, y, color='gray', s=30, alpha=0.6,
               edgecolor='black', linewidth=0.5, label='Data points')
    ax1.plot(X, y_pred, color='black', linewidth=2, label='Regression line')

    # Add residual lines for a few points
    sample_indices = [5, 15, 25, 35, 45]
    for idx in sample_indices:
        ax1.plot([X[idx], X[idx]], [y[idx], y_pred[idx]],
                'k--', linewidth=0.5, alpha=0.5)

    ax1.set_xlabel('Feature (X)', fontsize=8)
    ax1.set_ylabel('Target (y)', fontsize=8)
    ax1.set_title('Linear Regression Example [SYNTHETIC DATA]', fontsize=10, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=7)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Add equation and R-squared
    equation_text = f'y = {slope:.2f}x + {intercept:.2f}\nR² = {r_squared:.3f}'
    ax1.text(0.05, 0.95, equation_text,
            transform=ax1.transAxes,
            fontsize=8,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white',
                     edgecolor='black', linewidth=0.5))

    # Right panel: Residuals plot
    residuals = y - y_pred

    ax2.scatter(X, residuals, color='gray', s=30, alpha=0.6,
               edgecolor='black', linewidth=0.5)
    ax2.axhline(y=0, color='black', linewidth=1.5, linestyle='-')

    # Add confidence bands
    std_residuals = np.std(residuals)
    ax2.axhline(y=2*std_residuals, color='gray', linewidth=1,
               linestyle='--', label='±2σ')
    ax2.axhline(y=-2*std_residuals, color='gray', linewidth=1,
               linestyle='--')

    ax2.set_xlabel('Feature (X)', fontsize=8)
    ax2.set_ylabel('Residuals (y - ŷ)', fontsize=8)
    ax2.set_title('Residuals Plot', fontsize=10, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=7)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Add statistics
    stats_text = f'Mean: {np.mean(residuals):.2f}\nStd: {std_residuals:.2f}'
    ax2.text(0.05, 0.95, stats_text,
            transform=ax2.transAxes,
            fontsize=7,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white',
                     edgecolor='black', linewidth=0.5))

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'regression_example.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_regression_example()
