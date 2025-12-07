"""
Classification with Confusion Matrix Visualization

This script demonstrates binary classification for credit default prediction
and visualizes results using a confusion matrix.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set font size globally and random seed
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

def generate_credit_data(n=500):
    """
    Generate synthetic credit default data.

    Features: Credit score, Debt-to-income ratio
    Target: Default (1) or No default (0)
    """
    # Non-defaulters (80%)
    n_good = int(n * 0.8)
    credit_score_good = np.random.normal(720, 50, n_good)
    debt_ratio_good = np.random.normal(0.3, 0.1, n_good)
    y_good = np.zeros(n_good)

    # Defaulters (20%)
    n_bad = n - n_good
    credit_score_bad = np.random.normal(620, 60, n_bad)
    debt_ratio_bad = np.random.normal(0.5, 0.15, n_bad)
    y_bad = np.ones(n_bad)

    # Combine data
    credit_score = np.concatenate([credit_score_good, credit_score_bad])
    debt_ratio = np.concatenate([debt_ratio_good, debt_ratio_bad])
    y = np.concatenate([y_good, y_bad])

    return credit_score, debt_ratio, y

def simple_classifier(credit_score, debt_ratio):
    """
    Simple rule-based classifier:
    Default if credit_score < 680 OR debt_ratio > 0.45
    """
    predictions = ((credit_score < 680) | (debt_ratio > 0.45)).astype(int)
    return predictions

def calculate_confusion_matrix(y_true, y_pred):
    """Calculate confusion matrix components."""
    tp = np.sum((y_true == 1) & (y_pred == 1))  # True Positives
    tn = np.sum((y_true == 0) & (y_pred == 0))  # True Negatives
    fp = np.sum((y_true == 0) & (y_pred == 1))  # False Positives
    fn = np.sum((y_true == 1) & (y_pred == 0))  # False Negatives

    return np.array([[tn, fp], [fn, tp]])

def calculate_metrics(confusion_matrix):
    """Calculate classification metrics from confusion matrix."""
    tn, fp, fn, tp = confusion_matrix.ravel()

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return accuracy, precision, recall, f1_score

def main():
    # Generate data
    credit_score, debt_ratio, y_true = generate_credit_data(n=500)

    # Make predictions
    y_pred = simple_classifier(credit_score, debt_ratio)

    # Calculate confusion matrix
    cm = calculate_confusion_matrix(y_true, y_pred)

    # Calculate metrics
    accuracy, precision, recall, f1 = calculate_metrics(cm)

    # Create visualization
    fig = plt.figure(figsize=(10, 4))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    # Plot 1: Decision boundary visualization
    # Create decision boundary
    credit_score_range = np.linspace(500, 850, 300)
    debt_ratio_boundary_vertical = np.full_like(credit_score_range, 0.45)

    # Plot data points
    default_mask = y_true == 1
    no_default_mask = y_true == 0

    # Correct predictions
    correct_default = (y_true == 1) & (y_pred == 1)
    correct_no_default = (y_true == 0) & (y_pred == 0)

    # Incorrect predictions
    incorrect_default = (y_true == 1) & (y_pred == 0)
    incorrect_no_default = (y_true == 0) & (y_pred == 1)

    # Plot points with different markers for correct/incorrect
    ax1.scatter(credit_score[correct_no_default], debt_ratio[correct_no_default],
               c='white', edgecolor='black', s=30, marker='o', label='True Negative', linewidth=0.5)
    ax1.scatter(credit_score[correct_default], debt_ratio[correct_default],
               c='black', edgecolor='black', s=30, marker='s', label='True Positive', linewidth=0.5)
    ax1.scatter(credit_score[incorrect_no_default], debt_ratio[incorrect_no_default],
               c='white', edgecolor='red', s=30, marker='o', label='False Positive', linewidth=1.5)
    ax1.scatter(credit_score[incorrect_default], debt_ratio[incorrect_default],
               c='black', edgecolor='red', s=30, marker='s', label='False Negative', linewidth=1.5)

    # Plot decision boundaries
    ax1.axvline(x=680, color='gray', linestyle='--', linewidth=1.5, label='Decision boundary')
    ax1.axhline(y=0.45, color='gray', linestyle='--', linewidth=1.5)

    # Add shaded regions
    ax1.axvspan(500, 680, alpha=0.1, color='gray')
    ax1.axhspan(0.45, 1.0, alpha=0.1, color='gray')

    ax1.set_xlabel('Credit Score', fontsize=8)
    ax1.set_ylabel('Debt-to-Income Ratio', fontsize=8)
    ax1.set_title('Credit Default Classification', fontsize=8)
    ax1.legend(fontsize=6, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(500, 850)
    ax1.set_ylim(0, 1)

    # Plot 2: Confusion Matrix
    im = ax2.imshow(cm, cmap='gray_r', aspect='auto', vmin=0, vmax=cm.max())

    # Add text annotations
    for i in range(2):
        for j in range(2):
            text_color = 'white' if cm[i, j] > cm.max()/2 else 'black'
            ax2.text(j, i, str(cm[i, j]), ha='center', va='center',
                    fontsize=20, color=text_color, weight='bold')

    # Labels
    ax2.set_xticks([0, 1])
    ax2.set_yticks([0, 1])
    ax2.set_xticklabels(['No Default\n(Predicted)', 'Default\n(Predicted)'], fontsize=8)
    ax2.set_yticklabels(['No Default\n(Actual)', 'Default\n(Actual)'], fontsize=8)
    ax2.set_title('Confusion Matrix', fontsize=8, pad=10)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)
    cbar.set_label('Count', fontsize=7)
    cbar.ax.tick_params(labelsize=7)

    # Add metrics text
    metrics_text = (
        f'Accuracy:  {accuracy:.3f}\n'
        f'Precision: {precision:.3f}\n'
        f'Recall:    {recall:.3f}\n'
        f'F1 Score:  {f1:.3f}'
    )
    ax2.text(1.5, 0.5, metrics_text, transform=ax2.transData,
            fontsize=7, verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'classification_demo.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print detailed metrics
    print("\nClassification Results:")
    print("-" * 50)
    print(f"Total samples: {len(y_true)}")
    print(f"Actual defaults: {np.sum(y_true)}")
    print(f"Predicted defaults: {np.sum(y_pred)}")
    print("\nConfusion Matrix:")
    print(f"True Negatives:  {cm[0,0]}")
    print(f"False Positives: {cm[0,1]}")
    print(f"False Negatives: {cm[1,0]}")
    print(f"True Positives:  {cm[1,1]}")
    print("\nMetrics:")
    print(f"Accuracy:  {accuracy:.3f}")
    print(f"Precision: {precision:.3f} (of predicted defaults, how many were correct?)")
    print(f"Recall:    {recall:.3f} (of actual defaults, how many did we catch?)")
    print(f"F1 Score:  {f1:.3f} (harmonic mean of precision and recall)")

if __name__ == '__main__':
    main()
