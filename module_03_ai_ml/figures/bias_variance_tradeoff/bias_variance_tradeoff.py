"""
Bias-Variance Tradeoff
Shows the U-shaped curve of total error

Output: bias_variance_tradeoff.pdf
Module: module_03_ai_ml
Lesson: 27 - Regression / 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

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

    # Model complexity (x-axis)
    complexity = np.linspace(0.5, 10, 100)

    # Bias decreases with complexity
    bias_squared = 5 / complexity

    # Variance increases with complexity
    variance = 0.3 * (complexity - 0.5)**1.5

    # Total error = bias^2 + variance + irreducible error
    irreducible = 0.5
    total_error = bias_squared + variance + irreducible

    ax.plot(complexity, bias_squared, color=MLBLUE, linewidth=2, label='Bias²')
    ax.plot(complexity, variance, color=MLORANGE, linewidth=2, label='Variance')
    ax.plot(complexity, total_error, color=MLRED, linewidth=2.5, label='Total Error')
    ax.axhline(y=irreducible, color='gray', linestyle='--', linewidth=1, label='Irreducible Error')

    # Mark optimal point
    optimal_idx = np.argmin(total_error)
    ax.scatter([complexity[optimal_idx]], [total_error[optimal_idx]], color=MLGREEN, s=100, zorder=5)
    ax.annotate('Optimal\nComplexity', xy=(complexity[optimal_idx], total_error[optimal_idx]),
                xytext=(complexity[optimal_idx]+1.5, total_error[optimal_idx]+0.8),
                fontsize=9, arrowprops=dict(arrowstyle='->', color=MLGREEN),
                color=MLGREEN, fontweight='bold')

    # Add underfitting/overfitting regions
    ax.text(1.5, 4.5, 'Underfitting\n(High Bias)', fontsize=10, ha='center', color='#666666')
    ax.text(8.5, 4.5, 'Overfitting\n(High Variance)', fontsize=10, ha='center', color='#666666')

    ax.set_xlabel('Model Complexity', fontsize=11)
    ax.set_ylabel('Error', fontsize=11)
    ax.set_title('Bias-Variance Tradeoff', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)
    ax.legend(loc='upper center', ncol=4, framealpha=0.9)

    ax.set_xlim(0.5, 10)
    ax.set_ylim(0, 6)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[CONCEPTUAL ILLUSTRATION]', fontsize=7,
             color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'bias_variance_tradeoff.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
