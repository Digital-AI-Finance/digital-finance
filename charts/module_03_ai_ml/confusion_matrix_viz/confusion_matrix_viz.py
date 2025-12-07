"""
Confusion Matrix Visualization
Visual representation of TP/TN/FP/FN classification metrics

Required libraries: matplotlib, numpy
Output: confusion_matrix_viz.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Confusion Matrix Visualization',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_03_ai_ml/confusion_matrix_viz'
}

def create_confusion_matrix_viz():
    """Create a comprehensive confusion matrix visualization"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig = plt.figure(figsize=(10, 8))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Sample confusion matrix values
    TP = 85  # True Positives
    TN = 90  # True Negatives
    FP = 10  # False Positives
    FN = 15  # False Negatives

    total = TP + TN + FP + FN

    # Top left: Main confusion matrix
    ax1 = fig.add_subplot(gs[0, 0])

    # Create matrix
    conf_matrix = np.array([[TN, FP],
                           [FN, TP]])

    # Plot heatmap with grayscale
    im = ax1.imshow(conf_matrix, cmap='Greys', aspect='auto',
                    vmin=0, vmax=max(TN, TP))

    # Add text annotations
    for i in range(2):
        for j in range(2):
            value = conf_matrix[i, j]
            percentage = (value / total) * 100
            text = ax1.text(j, i, f'{value}\n({percentage:.1f}%)',
                          ha='center', va='center',
                          fontsize=10, fontweight='bold',
                          color='white' if value > 70 else 'black')

    # Set labels
    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])
    ax1.set_xticklabels(['Negative (0)', 'Positive (1)'], fontsize=8)
    ax1.set_yticklabels(['Negative (0)', 'Positive (1)'], fontsize=8)
    ax1.set_xlabel('Predicted Class', fontsize=9, fontweight='bold')
    ax1.set_ylabel('Actual Class', fontsize=9, fontweight='bold')
    ax1.set_title('Confusion Matrix', fontsize=10, fontweight='bold')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)
    cbar.set_label('Count', fontsize=7)

    # Add labels for each cell
    cell_labels = [['TN\n(True Negative)', 'FP\n(False Positive)'],
                  ['FN\n(False Negative)', 'TP\n(True Positive)']]

    for i in range(2):
        for j in range(2):
            ax1.text(j, i + 0.35, cell_labels[i][j],
                    ha='center', va='center',
                    fontsize=6, style='italic',
                    color='white' if conf_matrix[i, j] > 70 else 'gray')

    # Top right: Performance metrics
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis('off')

    # Calculate metrics
    accuracy = (TP + TN) / total
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) > 0 else 0

    metrics_data = [
        ['Metric', 'Formula', 'Value'],
        ['Accuracy', '(TP+TN)/Total', f'{accuracy:.3f}'],
        ['Precision', 'TP/(TP+FP)', f'{precision:.3f}'],
        ['Recall (Sensitivity)', 'TP/(TP+FN)', f'{recall:.3f}'],
        ['Specificity', 'TN/(TN+FP)', f'{specificity:.3f}'],
        ['F1 Score', '2×(P×R)/(P+R)', f'{f1_score:.3f}']
    ]

    table = ax2.table(cellText=metrics_data,
                     cellLoc='left',
                     loc='center',
                     bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(7)

    # Style header
    for i in range(3):
        cell = table[(0, i)]
        cell.set_facecolor('darkgray')
        cell.set_text_props(weight='bold', color='black')

    # Style rows
    for i in range(1, len(metrics_data)):
        for j in range(3):
            cell = table[(i, j)]
            cell.set_facecolor('lightgray' if i % 2 == 0 else 'white')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

            # Make formula monospace
            if j == 1:
                cell.set_text_props(family='monospace', fontsize=6)

    ax2.set_title('Performance Metrics', fontsize=10, fontweight='bold', pad=20)

    # Bottom left: Visual interpretation
    ax3 = fig.add_subplot(gs[1, 0])

    # Create bar chart for metrics
    metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
    metrics_values = [accuracy, precision, recall, f1_score]

    bars = ax3.barh(metrics_names, metrics_values,
                   color=['darkgray', 'gray', 'lightgray', 'white'],
                   edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, metrics_values)):
        ax3.text(value + 0.02, i, f'{value:.3f}',
                va='center', fontsize=7)

    ax3.set_xlim(0, 1.1)
    ax3.set_xlabel('Score', fontsize=8)
    ax3.set_title('Metrics Comparison', fontsize=10, fontweight='bold')
    ax3.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)

    # Bottom right: Explanation
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')

    explanation_text = """
    Key Concepts:

    True Positive (TP): Correctly predicted positive
    True Negative (TN): Correctly predicted negative
    False Positive (FP): Incorrectly predicted positive (Type I Error)
    False Negative (FN): Incorrectly predicted negative (Type II Error)

    Trade-offs:
    • High Precision: Few false alarms (minimize FP)
    • High Recall: Catch all positives (minimize FN)
    • F1 Score: Balance between Precision and Recall

    Example: Fraud Detection
    • High Recall: Don't miss fraudulent transactions
    • High Precision: Don't flag legitimate transactions
    """

    ax4.text(0.05, 0.95, explanation_text,
            transform=ax4.transAxes,
            fontsize=7,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=dict(boxstyle='round,pad=0.5',
                     facecolor='white',
                     edgecolor='black',
                     linewidth=0.5))

    ax4.set_title('Interpretation Guide', fontsize=10, fontweight='bold')

    # Main title
    fig.suptitle('Confusion Matrix and Classification Metrics [SYNTHETIC DATA]',
                fontsize=12, fontweight='bold', y=0.98)

    # Save as PDF
    output_path = Path(__file__).parent / 'confusion_matrix_viz.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_confusion_matrix_viz()
