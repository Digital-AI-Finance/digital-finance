"""
LIME Explanation Visualization
Local interpretable model explanations

Output: lime_explanation.pdf
Module: module_03_ai_ml
Lesson: 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'LIME Explanation',
    'module': 'module_03_ai_ml',
    'lesson': 35,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/lime_explanation'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # LIME Feature Weights
    ax1 = axes[0]

    features = ['DTI > 0.4', 'Credit Util > 0.8', 'Missed Payment = Yes',
                'Account Age < 2yr', 'Income > $80K', 'Inquiries > 3',
                'Employment < 1yr', 'Loan > $20K']
    weights = [0.25, 0.18, 0.15, 0.08, -0.12, 0.06, 0.05, 0.04]

    colors = ['#D62728' if w > 0 else '#4A90E2' for w in weights]
    y_pos = np.arange(len(features))

    bars = ax1.barh(y_pos, weights, color=colors, alpha=0.8, edgecolor='black')

    ax1.axvline(x=0, color='black', linewidth=1)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(features)
    ax1.set_xlabel('Feature Weight (Local Importance)', fontsize=11)
    ax1.set_title('LIME Explanation: Why This Applicant is High Risk', fontsize=12, fontweight='bold')
    ax1.set_xlim(-0.2, 0.35)
    ax1.xaxis.grid(True, alpha=0.3)

    # Add value labels
    for bar, weight in zip(bars, weights):
        x_pos = weight + 0.01 if weight > 0 else weight - 0.01
        ha = 'left' if weight > 0 else 'right'
        ax1.text(x_pos, bar.get_y() + bar.get_height()/2, f'{weight:.2f}',
                ha=ha, va='center', fontsize=9, fontweight='bold')

    # Prediction bar
    ax1.text(0.15, -1, f'Prediction: 72% Default Risk', fontsize=11, fontweight='bold',
            color='#D62728', ha='center')

    # Local vs Global comparison
    ax2 = axes[1]

    features_short = ['DTI', 'Credit Util', 'Payment Hist', 'Account Age',
                     'Income', 'Inquiries']
    global_importance = [0.18, 0.15, 0.22, 0.12, 0.10, 0.08]
    local_importance = [0.25, 0.18, 0.15, 0.08, 0.12, 0.06]

    x = np.arange(len(features_short))
    width = 0.35

    bars1 = ax2.bar(x - width/2, global_importance, width, label='Global (All Data)',
                   color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x + width/2, local_importance, width, label='Local (This Case)',
                   color='#FF7F0E', alpha=0.8)

    ax2.set_xlabel('Feature', fontsize=11)
    ax2.set_ylabel('Importance', fontsize=11)
    ax2.set_title('Global vs Local Feature Importance', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(features_short, rotation=20, ha='right')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 0.35)
    ax2.yaxis.grid(True, alpha=0.3)

    # Highlight differences
    ax2.annotate('DTI more\nimportant locally', xy=(0 + width/2, 0.25),
                xytext=(0.8, 0.30), fontsize=8, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#FF7F0E'))

    fig.suptitle('LIME: Local Interpretable Model Explanations', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'lime_explanation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
