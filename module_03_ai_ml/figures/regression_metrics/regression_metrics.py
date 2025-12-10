"""
Regression Metrics Comparison
MSE, RMSE, MAE, R-squared

Output: regression_metrics.pdf
Module: module_03_ai_ml
Lesson: 27 - Regression
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Regression Metrics',
    'module': 'module_03_ai_ml',
    'lesson': 27,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/regression_metrics'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(12, 6))

    models = ['Linear\nRegression', 'Ridge\nRegression', 'Lasso\nRegression',
              'Random\nForest', 'XGBoost', 'Neural\nNetwork']
    mse = [0.045, 0.042, 0.048, 0.032, 0.028, 0.035]
    mae = [0.18, 0.17, 0.19, 0.14, 0.12, 0.15]
    r2 = [0.72, 0.74, 0.71, 0.82, 0.86, 0.79]

    x = np.arange(len(models))
    width = 0.25

    bars1 = ax.bar(x - width, [m * 10 for m in mse], width, label='MSE (x10)', color='#4A90E2', alpha=0.8)
    bars2 = ax.bar(x, mae, width, label='MAE', color='#FF7F0E', alpha=0.8)
    bars3 = ax.bar(x + width, r2, width, label='R²', color='#44A044', alpha=0.8)

    ax.set_xlabel('Model', fontsize=11)
    ax.set_ylabel('Metric Value', fontsize=11)
    ax.set_title('Regression Model Performance Comparison', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=9)
    ax.legend(loc='upper right', fontsize=9)
    ax.set_ylim(0, 1.1)

    # Highlight best model
    best_idx = r2.index(max(r2))
    ax.annotate('Best\nModel', xy=(x[best_idx] + width, r2[best_idx]),
               xytext=(x[best_idx] + width + 0.5, r2[best_idx] + 0.1),
               fontsize=9, fontweight='bold', color='#44A044',
               arrowprops=dict(arrowstyle='->', color='#44A044'))

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'regression_metrics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
