"""
Credit Model Comparison
Traditional vs ML credit scoring models

Output: credit_model_comparison.pdf
Module: module_03_ai_ml
Lesson: 30 - Credit Scoring
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Credit Model Comparison',
    'module': 'module_03_ai_ml',
    'lesson': 30,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/credit_model_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Model Performance Comparison
    ax1 = axes[0]
    models = ['Traditional\nScorecard', 'Logistic\nRegression', 'Random\nForest',
              'Gradient\nBoosting', 'Neural\nNetwork']
    gini = [0.45, 0.52, 0.62, 0.68, 0.65]
    ks = [0.38, 0.44, 0.54, 0.58, 0.55]
    auc = [0.72, 0.76, 0.81, 0.84, 0.82]

    x = np.arange(len(models))
    width = 0.25

    bars1 = ax1.bar(x - width, gini, width, label='Gini Coefficient', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x, ks, width, label='KS Statistic', color='#44A044', alpha=0.8)
    bars3 = ax1.bar(x + width, auc, width, label='AUC-ROC', color='#FF7F0E', alpha=0.8)

    ax1.set_xlabel('Model Type', fontsize=11)
    ax1.set_ylabel('Score', fontsize=11)
    ax1.set_title('Credit Model Performance Metrics', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, fontsize=9)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_ylim(0, 1)
    ax1.yaxis.grid(True, alpha=0.3)

    # Highlight best
    ax1.annotate('Best\nPerformance', xy=(3, 0.68), xytext=(3.5, 0.78),
                fontsize=9, fontweight='bold', color='#4A90E2',
                arrowprops=dict(arrowstyle='->', color='#4A90E2'))

    # Trade-off: Accuracy vs Interpretability
    ax2 = axes[1]
    models_short = ['Scorecard', 'Log. Reg.', 'RF', 'XGBoost', 'NN']
    accuracy = [72, 76, 81, 84, 82]
    interpretability = [95, 85, 45, 35, 20]

    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728']

    for i, (model, acc, interp) in enumerate(zip(models_short, accuracy, interpretability)):
        ax2.scatter(acc, interp, s=300, c=colors[i], alpha=0.7, edgecolors='black', linewidth=2)
        ax2.annotate(model, xy=(acc, interp), xytext=(5, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold')

    ax2.set_xlabel('Predictive Accuracy (%)', fontsize=11)
    ax2.set_ylabel('Interpretability Score', fontsize=11)
    ax2.set_title('Accuracy vs. Interpretability Trade-off', fontsize=12, fontweight='bold')
    ax2.set_xlim(68, 88)
    ax2.set_ylim(10, 100)
    ax2.grid(True, alpha=0.3)

    # Add quadrant labels
    ax2.axhline(y=55, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=78, color='gray', linestyle='--', alpha=0.5)
    ax2.text(73, 80, 'High Interpretability\nLow Accuracy', fontsize=8, alpha=0.7, ha='center')
    ax2.text(83, 80, 'High Interpretability\nHigh Accuracy', fontsize=8, alpha=0.7, ha='center')
    ax2.text(73, 30, 'Low Interpretability\nLow Accuracy', fontsize=8, alpha=0.7, ha='center')
    ax2.text(83, 30, 'Low Interpretability\nHigh Accuracy', fontsize=8, alpha=0.7, ha='center')

    fig.suptitle('Credit Scoring Model Comparison', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'credit_model_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
