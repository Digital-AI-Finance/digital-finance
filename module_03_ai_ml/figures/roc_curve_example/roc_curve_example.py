"""
ROC Curve Example
Classification performance visualization

Output: roc_curve_example.pdf
Module: module_03_ai_ml
Lesson: 28 - Classification
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'ROC Curve Example',
    'module': 'module_03_ai_ml',
    'lesson': 28,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/roc_curve_example'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Generate ROC curves
    fpr = np.linspace(0, 1, 100)

    # Random classifier
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1.5, label='Random (AUC = 0.50)')

    # Model curves
    tpr_good = 1 - (1 - fpr) ** 3
    tpr_better = 1 - (1 - fpr) ** 5
    tpr_best = 1 - (1 - fpr) ** 8

    ax.plot(fpr, tpr_good, 'b-', linewidth=2.5, label='Logistic Reg (AUC = 0.78)')
    ax.plot(fpr, tpr_better, 'g-', linewidth=2.5, label='Random Forest (AUC = 0.85)')
    ax.plot(fpr, tpr_best, 'r-', linewidth=2.5, label='XGBoost (AUC = 0.92)')

    # Perfect classifier
    ax.plot([0, 0, 1], [0, 1, 1], 'purple', linewidth=1.5, linestyle=':', label='Perfect (AUC = 1.00)')

    ax.set_xlabel('False Positive Rate', fontsize=11)
    ax.set_ylabel('True Positive Rate', fontsize=11)
    ax.set_title('ROC Curves: Credit Default Classification', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='lower right', fontsize=9)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'roc_curve_example.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
