"""
SHAP Values Visualization
Feature importance explanation

Output: shap_values.pdf
Module: module_03_ai_ml
Lesson: 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'SHAP Values',
    'module': 'module_03_ai_ml',
    'lesson': 35,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/shap_values'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    np.random.seed(42)

    # SHAP Summary Plot (simulated)
    ax1 = axes[0]

    features = ['Debt-to-Income', 'Credit Utilization', 'Payment History',
                'Account Age', 'Number of Inquiries', 'Annual Income',
                'Employment Length', 'Loan Amount']

    # Generate SHAP-like values for each feature
    n_samples = 100
    shap_data = {}
    feature_values = {}

    for feat in features:
        shap_data[feat] = np.random.randn(n_samples) * np.random.uniform(0.1, 0.5)
        feature_values[feat] = np.random.uniform(0, 1, n_samples)

    # Plot as beeswarm-like
    for i, feat in enumerate(features):
        y = np.ones(n_samples) * i + np.random.randn(n_samples) * 0.15
        colors = plt.cm.RdYlBu_r(feature_values[feat])
        ax1.scatter(shap_data[feat], y, c=colors, s=15, alpha=0.6)

    ax1.axvline(x=0, color='gray', linewidth=1)
    ax1.set_yticks(range(len(features)))
    ax1.set_yticklabels(features)
    ax1.set_xlabel('SHAP Value (Impact on Model Output)', fontsize=11)
    ax1.set_title('SHAP Summary Plot: Credit Default Model', fontsize=12, fontweight='bold')
    ax1.set_xlim(-1, 1)

    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap='RdYlBu_r', norm=plt.Normalize(0, 1))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax1, shrink=0.5)
    cbar.set_label('Feature Value', fontsize=10)

    # Force Plot (single prediction)
    ax2 = axes[1]

    # Simulated force plot
    base_value = 0.15
    contributions = {
        'Debt-to-Income': 0.12,
        'Credit Util': 0.08,
        'Payment Hist': -0.06,
        'Account Age': -0.04,
        'Inquiries': 0.03,
        'Income': -0.02
    }

    # Build waterfall
    y_pos = 0.5
    current = base_value
    positive_x = []
    negative_x = []

    ax2.barh(y_pos, base_value, height=0.3, left=0, color='gray', alpha=0.5)
    ax2.text(base_value/2, y_pos, f'Base\n{base_value:.2f}', ha='center', va='center', fontsize=9)

    pos_start = base_value
    neg_start = base_value

    for feat, contrib in contributions.items():
        if contrib > 0:
            ax2.barh(y_pos + 0.35, contrib, height=0.25, left=pos_start, color='#D62728', alpha=0.7)
            ax2.text(pos_start + contrib/2, y_pos + 0.35, f'{feat}\n+{contrib:.2f}',
                    ha='center', va='center', fontsize=7, color='white')
            pos_start += contrib
        else:
            ax2.barh(y_pos - 0.35, -contrib, height=0.25, left=neg_start + contrib, color='#4A90E2', alpha=0.7)
            ax2.text(neg_start + contrib/2, y_pos - 0.35, f'{feat}\n{contrib:.2f}',
                    ha='center', va='center', fontsize=7, color='white')
            neg_start += contrib

    final_value = base_value + sum(contributions.values())
    ax2.axvline(x=final_value, color='black', linewidth=2, linestyle='--')
    ax2.text(final_value + 0.02, y_pos, f'Prediction\n{final_value:.2f}', fontsize=10, fontweight='bold')

    ax2.set_xlim(-0.1, 0.5)
    ax2.set_ylim(0, 1)
    ax2.set_xlabel('Model Output (Default Probability)', fontsize=11)
    ax2.set_title('SHAP Force Plot: Single Prediction', fontsize=12, fontweight='bold')
    ax2.set_yticks([])

    # Legend
    ax2.barh([], [], color='#D62728', alpha=0.7, label='Increases Risk')
    ax2.barh([], [], color='#4A90E2', alpha=0.7, label='Decreases Risk')
    ax2.legend(loc='upper right', fontsize=9)

    fig.suptitle('SHAP: Explaining ML Model Predictions', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'shap_values.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
