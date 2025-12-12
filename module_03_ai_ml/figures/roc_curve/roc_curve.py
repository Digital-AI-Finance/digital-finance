"""
ROC Curve - Receiver Operating Characteristic
Shows trade-off between TPR and FPR

Output: roc_curve.pdf
Module: module_03_ai_ml
Lesson: 28 - Classification
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simulated ROC curves for different models
    fpr = np.linspace(0, 1, 100)

    # Perfect model
    tpr_perfect = np.where(fpr < 0.01, 1.0, 1.0)

    # Good model (AUC ~0.92)
    tpr_good = 1 - (1 - fpr)**3

    # Medium model (AUC ~0.78)
    tpr_medium = 1 - (1 - fpr)**1.5

    # Random classifier
    tpr_random = fpr

    ax.plot(fpr, tpr_good, color=MLBLUE, linewidth=2, label='Good Model (AUC = 0.92)')
    ax.plot(fpr, tpr_medium, color=MLORANGE, linewidth=2, label='Baseline Model (AUC = 0.78)')
    ax.plot(fpr, tpr_random, color='gray', linewidth=1.5, linestyle='--', label='Random (AUC = 0.50)')

    # Fill AUC area for good model
    ax.fill_between(fpr, tpr_good, alpha=0.15, color=MLBLUE)

    # Add threshold annotation
    ax.annotate('Threshold = 0.5', xy=(0.15, 0.85), xytext=(0.35, 0.65),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555')

    ax.set_xlabel('False Positive Rate (FPR)', fontsize=11)
    ax.set_ylabel('True Positive Rate (TPR)', fontsize=11)
    ax.set_title('ROC Curve: Model Comparison', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)
    ax.legend(loc='lower right', framealpha=0.9)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative curves]', fontsize=7,
             color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'roc_curve.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
