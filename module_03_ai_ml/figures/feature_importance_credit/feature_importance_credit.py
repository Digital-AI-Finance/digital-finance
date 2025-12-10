"""
Feature Importance in Credit Scoring
Key factors in credit risk models

Output: feature_importance_credit.pdf
Module: module_03_ai_ml
Lesson: 30 - Credit Scoring
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Feature Importance Credit',
    'module': 'module_03_ai_ml',
    'lesson': 30,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/feature_importance_credit'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Feature Importance (FICO model factors)
    ax1 = axes[0]
    features = ['Payment History', 'Amounts Owed', 'Length of Credit History',
                'New Credit', 'Credit Mix']
    importance = [35, 30, 15, 10, 10]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#E74C3C']

    wedges, texts, autotexts = ax1.pie(importance, labels=features, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0.02, 0, 0, 0],
                                        textprops={'fontsize': 9})

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    ax1.set_title('FICO Score Components', fontsize=12, fontweight='bold')

    # ML Model Feature Importance
    ax2 = axes[1]
    ml_features = [
        'Debt-to-Income Ratio',
        'Credit Utilization',
        'Payment History (24mo)',
        'Account Age',
        'Number of Inquiries',
        'Employment Length',
        'Annual Income',
        'Number of Accounts',
        'Recent Delinquencies',
        'Loan Amount Requested'
    ]
    ml_importance = [0.18, 0.16, 0.14, 0.12, 0.09, 0.08, 0.07, 0.06, 0.05, 0.05]

    colors = plt.cm.Blues(np.linspace(0.3, 0.9, len(ml_features)))[::-1]
    bars = ax2.barh(ml_features, ml_importance, color=colors, edgecolor='black', alpha=0.8)

    for bar, imp in zip(bars, ml_importance):
        ax2.text(imp + 0.005, bar.get_y() + bar.get_height()/2,
                f'{imp:.0%}', va='center', fontsize=9, fontweight='bold')

    ax2.set_xlabel('Feature Importance', fontsize=11)
    ax2.set_title('ML Credit Model: Feature Importance', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 0.25)
    ax2.xaxis.grid(True, alpha=0.3)
    ax2.invert_yaxis()

    fig.suptitle('Credit Scoring: Key Risk Factors', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'feature_importance_credit.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
