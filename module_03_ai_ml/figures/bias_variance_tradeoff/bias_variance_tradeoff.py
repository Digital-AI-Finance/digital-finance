"""
Bias-Variance Tradeoff
Fundamental ML concept

Output: bias_variance_tradeoff.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Bias-Variance Tradeoff',
    'module': 'module_03_ai_ml',
    'lesson': 25,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/bias_variance_tradeoff'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    complexity = np.linspace(0.5, 10, 100)
    bias_squared = 5 / complexity
    variance = 0.1 * complexity ** 1.5
    total_error = bias_squared + variance + 0.5  # irreducible error

    ax.plot(complexity, bias_squared, 'b-', linewidth=2.5, label='Bias²')
    ax.plot(complexity, variance, 'r-', linewidth=2.5, label='Variance')
    ax.plot(complexity, total_error, 'k--', linewidth=2.5, label='Total Error')
    ax.axhline(y=0.5, color='#999999', linestyle=':', linewidth=1.5, label='Irreducible Error')

    # Optimal point
    optimal_idx = np.argmin(total_error)
    ax.scatter(complexity[optimal_idx], total_error[optimal_idx], s=150, color='#44A044', zorder=5)
    ax.annotate('Optimal\nComplexity', xy=(complexity[optimal_idx], total_error[optimal_idx]),
               xytext=(complexity[optimal_idx] + 1.5, total_error[optimal_idx] + 1),
               fontsize=10, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='#333333'))

    # Regions
    ax.axvspan(0.5, 3, alpha=0.1, color='blue', label='_nolegend_')
    ax.axvspan(7, 10, alpha=0.1, color='red', label='_nolegend_')
    ax.text(1.5, 6, 'Underfitting\n(High Bias)', ha='center', fontsize=10, color='#4A90E2')
    ax.text(8.5, 6, 'Overfitting\n(High Variance)', ha='center', fontsize=10, color='#D62728')

    ax.set_xlabel('Model Complexity', fontsize=11)
    ax.set_ylabel('Error', fontsize=11)
    ax.set_title('Bias-Variance Tradeoff', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper center', fontsize=9)
    ax.set_xlim(0.5, 10)
    ax.set_ylim(0, 8)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'bias_variance_tradeoff.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
