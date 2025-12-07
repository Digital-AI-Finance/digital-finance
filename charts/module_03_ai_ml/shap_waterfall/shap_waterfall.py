"""
SHAP Waterfall Chart
Visualization of SHAP values for model explainability

Required libraries: matplotlib, numpy
Output: shap_waterfall.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'SHAP Waterfall Chart',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_03_ai_ml/shap_waterfall'
}

def create_shap_waterfall():
    """Create a SHAP-style waterfall chart for feature importance explanation"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # Synthetic SHAP values for a credit risk prediction example
    features = [
        'Income',
        'Credit Score',
        'Debt-to-Income',
        'Employment Years',
        'Loan Amount',
        'Age',
        'Previous Defaults',
        'Num. Credit Cards'
    ]

    # SHAP values (impact on prediction)
    shap_values = np.array([0.25, 0.18, -0.22, 0.12, -0.15, 0.08, -0.28, 0.05])
    base_value = 0.5  # Base prediction (e.g., average default probability)
    prediction = base_value + np.sum(shap_values)

    # Sort by absolute SHAP value
    sorted_indices = np.argsort(np.abs(shap_values))[::-1]
    features_sorted = [features[i] for i in sorted_indices]
    shap_sorted = shap_values[sorted_indices]

    # Left panel: SHAP waterfall chart
    n_features = len(features_sorted)
    y_pos = np.arange(n_features)

    # Create waterfall
    cumulative = base_value
    positions = [cumulative]

    for val in shap_sorted:
        cumulative += val
        positions.append(cumulative)

    # Plot bars
    for i, (feature, shap_val) in enumerate(zip(features_sorted, shap_sorted)):
        start = positions[i]
        color = 'darkgray' if shap_val > 0 else 'lightgray'

        # Draw bar
        ax1.barh(i, shap_val, left=start, height=0.6,
                color=color, edgecolor='black', linewidth=0.8)

        # Add value label
        label_x = start + shap_val/2
        ax1.text(label_x, i, f'{shap_val:+.3f}',
                ha='center', va='center', fontsize=6, fontweight='bold')

        # Draw connecting line to next feature
        if i < n_features - 1:
            ax1.plot([positions[i+1], positions[i+1]],
                    [i - 0.4, i + 0.6],
                    'k--', linewidth=0.5, alpha=0.5)

    # Add base value marker
    ax1.axvline(x=base_value, color='black', linestyle=':',
               linewidth=1.5, label='Base Value')
    ax1.text(base_value, n_features - 0.5, f'Base: {base_value:.2f}',
            ha='center', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                     edgecolor='black', linewidth=0.5))

    # Add final prediction marker
    ax1.axvline(x=prediction, color='red', linestyle='-',
               linewidth=2, label='Prediction')
    ax1.text(prediction, n_features - 0.5, f'Pred: {prediction:.2f}',
            ha='center', fontsize=7, color='red',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                     edgecolor='red', linewidth=0.5))

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(features_sorted, fontsize=8)
    ax1.set_xlabel('Model Output (Default Probability)', fontsize=8)
    ax1.set_title('SHAP Waterfall Chart: Feature Contributions',
                 fontsize=10, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=7)
    ax1.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.set_xlim(0, 1)

    # Add legend for colors
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, fc='darkgray', edgecolor='black',
                     label='Positive Impact (increases risk)'),
        plt.Rectangle((0, 0), 1, 1, fc='lightgray', edgecolor='black',
                     label='Negative Impact (decreases risk)')
    ]
    ax1.legend(handles=legend_elements, loc='upper left', fontsize=6)

    # Right panel: SHAP summary plot (feature importance)
    ax2.barh(features_sorted, np.abs(shap_sorted),
            color=['darkgray' if v > 0 else 'lightgray' for v in shap_sorted],
            edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (feature, val) in enumerate(zip(features_sorted, shap_sorted)):
        label = f'{np.abs(val):.3f}'
        ax2.text(np.abs(val) + 0.01, i, label,
                va='center', fontsize=6)

    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(features_sorted, fontsize=8)
    ax2.set_xlabel('Mean |SHAP Value| (Feature Importance)', fontsize=8)
    ax2.set_title('Feature Importance Ranking', fontsize=10, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Add interpretation box
    interpretation = """
    Interpretation:
    • Previous Defaults: Strong negative impact (reduces default probability)
    • Income: Strong positive impact (increases approval likelihood)
    • Debt-to-Income: Negative impact (higher ratio = higher risk)
    • SHAP values show how each feature pushes prediction away from base value
    """

    fig.text(0.5, -0.05, interpretation,
            ha='center', fontsize=7,
            bbox=dict(boxstyle='round,pad=0.5',
                     facecolor='white',
                     edgecolor='black',
                     linewidth=0.5))

    plt.suptitle('SHAP (SHapley Additive exPlanations) Feature Attribution [SYNTHETIC DATA]',
                fontsize=11, fontweight='bold', y=0.98)

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'shap_waterfall.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_shap_waterfall()
