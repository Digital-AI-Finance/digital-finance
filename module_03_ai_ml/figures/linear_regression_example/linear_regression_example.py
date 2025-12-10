"""
Linear Regression Example
Stock price prediction example

Output: linear_regression_example.pdf
Module: module_03_ai_ml
Lesson: 27 - Regression
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Linear Regression Example',
    'module': 'module_03_ai_ml',
    'lesson': 27,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/linear_regression_example'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)
    X = np.linspace(0, 10, 50)
    y = 2.5 * X + 10 + np.random.randn(50) * 3

    ax.scatter(X, y, color='#4A90E2', s=60, alpha=0.7, label='Data Points')

    # Regression line
    m, b = np.polyfit(X, y, 1)
    ax.plot(X, m * X + b, 'r-', linewidth=2.5, label=f'Regression Line: y = {m:.2f}x + {b:.2f}')

    # Confidence interval
    y_pred = m * X + b
    residuals = y - y_pred
    std_err = np.std(residuals)
    ax.fill_between(X, y_pred - 2*std_err, y_pred + 2*std_err, alpha=0.2, color='red', label='95% CI')

    ax.set_xlabel('Market Factor (X)', fontsize=11)
    ax.set_ylabel('Stock Returns (Y)', fontsize=11)
    ax.set_title('Linear Regression: Market Factor vs Returns', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=9)

    # R-squared annotation
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - ss_res/ss_tot
    ax.text(0.95, 0.05, f'R² = {r_squared:.3f}', transform=ax.transAxes,
            fontsize=11, fontweight='bold', ha='right', va='bottom',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.grid(True, alpha=0.3)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'linear_regression_example.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
