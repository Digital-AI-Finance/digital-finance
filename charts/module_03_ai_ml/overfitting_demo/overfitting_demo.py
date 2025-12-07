"""
Overfitting Demonstration
Visualization of underfitting, good fit, and overfitting with train/test error curves

Required libraries: matplotlib, numpy
Output: overfitting_demo.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Overfitting Demonstration',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_03_ai_ml/overfitting_demo'
}

def create_overfitting_demo():
    """Create visualization demonstrating overfitting vs good fit vs underfitting"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig = plt.figure(figsize=(10, 8))
    gs = fig.add_gridspec(2, 3, hspace=0.35, wspace=0.3)

    # Generate synthetic data
    n_points = 20
    X = np.linspace(0, 10, n_points)
    true_function = lambda x: 2 * np.sin(x) + 0.5 * x
    noise = np.random.normal(0, 0.8, n_points)
    y = true_function(X) + noise

    X_smooth = np.linspace(0, 10, 200)
    y_true = true_function(X_smooth)

    # Three models with different complexity
    # Underfitting: linear (degree 1)
    # Good fit: polynomial degree 3
    # Overfitting: polynomial degree 15

    models = [
        {'name': 'Underfitting', 'degree': 1, 'ax_idx': 0},
        {'name': 'Good Fit', 'degree': 3, 'ax_idx': 1},
        {'name': 'Overfitting', 'degree': 15, 'ax_idx': 2}
    ]

    # Top row: Fit visualizations
    for model in models:
        ax = fig.add_subplot(gs[0, model['ax_idx']])

        # Fit polynomial
        coeffs = np.polyfit(X, y, model['degree'])
        y_pred = np.polyval(coeffs, X_smooth)

        # Plot
        ax.scatter(X, y, color='gray', s=30, alpha=0.6,
                  edgecolor='black', linewidth=0.5, label='Data', zorder=3)
        ax.plot(X_smooth, y_true, 'k--', linewidth=1.5,
               label='True Function', alpha=0.5, zorder=1)
        ax.plot(X_smooth, y_pred, 'k-', linewidth=2,
               label=f'Model (deg={model["degree"]})', zorder=2)

        ax.set_xlabel('X', fontsize=8)
        ax.set_ylabel('y', fontsize=8)
        ax.set_title(model['name'], fontsize=10, fontweight='bold')
        ax.legend(loc='upper left', fontsize=6)
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
        ax.set_ylim(-5, 12)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Calculate and display error
        train_error = np.mean((y - np.polyval(coeffs, X))**2)
        ax.text(0.98, 0.02, f'Train MSE: {train_error:.2f}',
               transform=ax.transAxes,
               fontsize=7,
               verticalalignment='bottom',
               horizontalalignment='right',
               bbox=dict(boxstyle='round,pad=0.3',
                        facecolor='white',
                        edgecolor='black',
                        linewidth=0.5))

    # Bottom row: Learning curves
    ax_curve = fig.add_subplot(gs[1, :])

    # Simulate learning curves
    model_complexity = np.linspace(1, 20, 50)

    # Training error decreases with complexity
    train_error = 5 * np.exp(-0.3 * model_complexity) + 0.1

    # Validation error: U-shaped
    # Decreases initially, then increases due to overfitting
    val_error = 5 * np.exp(-0.15 * model_complexity) + 0.3 * (model_complexity - 5)**2 / 50 + 0.5

    ax_curve.plot(model_complexity, train_error, 'k-', linewidth=2,
                 label='Training Error', marker='o', markersize=3,
                 markevery=5)
    ax_curve.plot(model_complexity, val_error, 'k--', linewidth=2,
                 label='Validation Error', marker='s', markersize=3,
                 markevery=5)

    # Mark the three zones
    # Underfitting zone
    ax_curve.axvspan(0, 5, alpha=0.1, color='red', label='Underfitting')
    ax_curve.text(2.5, 4, 'Underfitting\n(High Bias)', ha='center',
                 fontsize=7, bbox=dict(boxstyle='round,pad=0.3',
                                      facecolor='white',
                                      edgecolor='red',
                                      linewidth=0.5))

    # Good fit zone
    optimal_idx = np.argmin(val_error)
    optimal_complexity = model_complexity[optimal_idx]
    ax_curve.axvline(x=optimal_complexity, color='green', linestyle=':',
                    linewidth=1.5, label='Optimal Complexity')
    ax_curve.text(optimal_complexity, 4, 'Good Fit\n(Balanced)', ha='center',
                 fontsize=7, bbox=dict(boxstyle='round,pad=0.3',
                                      facecolor='white',
                                      edgecolor='green',
                                      linewidth=0.5))

    # Overfitting zone
    ax_curve.axvspan(15, 20, alpha=0.1, color='blue', label='Overfitting')
    ax_curve.text(17.5, 4, 'Overfitting\n(High Variance)', ha='center',
                 fontsize=7, bbox=dict(boxstyle='round,pad=0.3',
                                      facecolor='white',
                                      edgecolor='blue',
                                      linewidth=0.5))

    ax_curve.set_xlabel('Model Complexity', fontsize=9)
    ax_curve.set_ylabel('Error (MSE)', fontsize=9)
    ax_curve.set_title('Bias-Variance Trade-off: Learning Curves', fontsize=10, fontweight='bold')
    ax_curve.legend(loc='upper right', fontsize=7, ncol=2)
    ax_curve.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax_curve.set_xlim(0, 20)
    ax_curve.set_ylim(0, 5)
    ax_curve.spines['top'].set_visible(False)
    ax_curve.spines['right'].set_visible(False)

    # Add key insight
    insight_text = 'Key Insight: Optimal model minimizes validation error. Training error alone is misleading.'
    ax_curve.text(0.5, -0.2, insight_text,
                 transform=ax_curve.transAxes,
                 fontsize=7, style='italic',
                 ha='center',
                 bbox=dict(boxstyle='round,pad=0.4',
                          facecolor='lightyellow',
                          edgecolor='black',
                          linewidth=0.5))

    # Main title
    fig.suptitle('Overfitting vs Underfitting Demonstration [SYNTHETIC DATA]',
                fontsize=12, fontweight='bold', y=0.98)

    # Save as PDF
    output_path = Path(__file__).parent / 'overfitting_demo.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_overfitting_demo()
