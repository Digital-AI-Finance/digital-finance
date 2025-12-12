"""
Confusion Matrix - Visual explanation for classification
Shows TP, TN, FP, FN with example

Output: confusion_matrix.pdf
Module: module_03_ai_ml
Lesson: 28 - Classification
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Example confusion matrix (fraud detection scenario)
    cm = np.array([[950, 20],   # TN, FP
                   [30, 100]])  # FN, TP

    # Create heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Predicted: Not Fraud', 'Predicted: Fraud'],
                yticklabels=['Actual: Not Fraud', 'Actual: Fraud'],
                annot_kws={'size': 14, 'weight': 'bold'},
                cbar_kws={'label': 'Count'})

    # Add cell labels
    ax.text(0.5, 0.2, 'True Negative\n(TN)', ha='center', va='center',
            fontsize=9, color='#333333', transform=ax.transAxes)
    ax.text(0.5, 0.7, 'False Negative\n(FN)', ha='center', va='center',
            fontsize=9, color='white', transform=ax.transAxes)

    ax.set_title('Confusion Matrix: Fraud Detection Example', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=15)

    # Add metrics text box
    accuracy = (950 + 100) / 1100 * 100
    precision = 100 / (100 + 20) * 100
    recall = 100 / (100 + 30) * 100
    f1 = 2 * precision * recall / (precision + recall)

    metrics_text = f'Accuracy: {accuracy:.1f}%\nPrecision: {precision:.1f}%\nRecall: {recall:.1f}%\nF1 Score: {f1:.1f}%'
    ax.text(1.25, 0.5, metrics_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='center', bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative example]', fontsize=7,
             color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'confusion_matrix.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
