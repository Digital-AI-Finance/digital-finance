"""
Confusion Matrix for Financial Classification
Default prediction example

Output: confusion_matrix_finance.pdf
Module: module_03_ai_ml
Lesson: 28 - Classification
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

CHART_METADATA = {
    'title': 'Confusion Matrix Finance',
    'module': 'module_03_ai_ml',
    'lesson': 28,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/confusion_matrix_finance'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Confusion Matrix
    ax1 = axes[0]
    cm = np.array([[8500, 350], [420, 730]])
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax1,
                xticklabels=['No Default', 'Default'],
                yticklabels=['No Default', 'Default'],
                annot_kws={'size': 14, 'weight': 'bold'})
    ax1.set_xlabel('Predicted', fontsize=11)
    ax1.set_ylabel('Actual', fontsize=11)
    ax1.set_title('Confusion Matrix: Credit Default', fontsize=12, fontweight='bold')

    # Metrics
    ax2 = axes[1]
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'Specificity']
    values = [0.923, 0.676, 0.635, 0.655, 0.960]
    colors = ['#4A90E2' if v > 0.7 else '#FF7F0E' if v > 0.6 else '#D62728' for v in values]

    bars = ax2.barh(metrics, values, color=colors, height=0.6)
    ax2.set_xlabel('Score', fontsize=11)
    ax2.set_title('Classification Metrics', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1.1)

    for bar, val in zip(bars, values):
        ax2.text(val + 0.02, bar.get_y() + bar.get_height()/2, f'{val:.3f}',
                va='center', fontsize=10, fontweight='bold')

    ax2.axvline(x=0.7, color='#999999', linestyle='--', linewidth=1, alpha=0.5)
    ax2.text(0.71, 4.5, 'Target', fontsize=9, color='#999999')
    ax2.xaxis.grid(True, alpha=0.3)

    fig.suptitle('Credit Default Classification Performance', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'confusion_matrix_finance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
