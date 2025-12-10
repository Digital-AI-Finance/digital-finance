"""
Residual Analysis
Diagnostic plots for regression

Output: residual_analysis.pdf
Module: module_03_ai_ml
Lesson: 27 - Regression
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

CHART_METADATA = {
    'title': 'Residual Analysis',
    'module': 'module_03_ai_ml',
    'lesson': 27,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/residual_analysis'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    np.random.seed(42)
    n = 100
    X = np.linspace(0, 10, n)
    y_true = 2 * X + 5
    residuals = np.random.randn(n) * 2

    # Residuals vs Fitted
    ax1 = axes[0, 0]
    ax1.scatter(y_true, residuals, color='#4A90E2', alpha=0.6, s=40)
    ax1.axhline(y=0, color='#D62728', linestyle='--', linewidth=2)
    ax1.set_xlabel('Fitted Values')
    ax1.set_ylabel('Residuals')
    ax1.set_title('Residuals vs Fitted', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Q-Q Plot
    ax2 = axes[0, 1]
    stats.probplot(residuals, dist="norm", plot=ax2)
    ax2.set_title('Normal Q-Q Plot', fontsize=12, fontweight='bold')
    ax2.get_lines()[0].set_color('#4A90E2')
    ax2.get_lines()[1].set_color('#D62728')

    # Scale-Location
    ax3 = axes[1, 0]
    standardized_residuals = (residuals - np.mean(residuals)) / np.std(residuals)
    ax3.scatter(y_true, np.sqrt(np.abs(standardized_residuals)), color='#4A90E2', alpha=0.6, s=40)
    ax3.set_xlabel('Fitted Values')
    ax3.set_ylabel('√|Standardized Residuals|')
    ax3.set_title('Scale-Location', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)

    # Histogram of Residuals
    ax4 = axes[1, 1]
    ax4.hist(residuals, bins=20, color='#4A90E2', alpha=0.7, edgecolor='white')
    ax4.axvline(x=0, color='#D62728', linestyle='--', linewidth=2)
    ax4.set_xlabel('Residuals')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Residual Distribution', fontsize=12, fontweight='bold')

    fig.suptitle('Regression Diagnostic Plots', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'residual_analysis.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
