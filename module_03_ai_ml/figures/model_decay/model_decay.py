"""
Model Decay Over Time
Performance degradation of ML models

Output: model_decay.pdf
Module: module_03_ai_ml
Lesson: 34 - Prediction Limitations
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Model Decay',
    'module': 'module_03_ai_ml',
    'lesson': 34,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/model_decay'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Model performance decay
    ax1 = axes[0]

    months = np.arange(0, 25)

    # Different models decay at different rates
    credit_model = 0.85 * np.exp(-0.02 * months) + 0.10 + np.random.randn(25) * 0.02
    fraud_model = 0.90 * np.exp(-0.05 * months) + 0.15 + np.random.randn(25) * 0.03
    trading_model = 0.80 * np.exp(-0.08 * months) + 0.20 + np.random.randn(25) * 0.04

    ax1.plot(months, credit_model, 'b-', linewidth=2.5, marker='o', markersize=4, label='Credit Scoring')
    ax1.plot(months, fraud_model, 'g-', linewidth=2.5, marker='s', markersize=4, label='Fraud Detection')
    ax1.plot(months, trading_model, 'r-', linewidth=2.5, marker='^', markersize=4, label='Trading Strategy')

    # Retraining threshold
    ax1.axhline(y=0.7, color='#FF7F0E', linestyle='--', linewidth=2, label='Retrain Threshold')
    ax1.fill_between(months, 0, 0.7, alpha=0.1, color='#D62728')

    ax1.set_xlabel('Months Since Training', fontsize=11)
    ax1.set_ylabel('Model Performance (AUC/Sharpe)', fontsize=11)
    ax1.set_title('Model Performance Decay Over Time', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(0, 24)
    ax1.set_ylim(0.4, 1)
    ax1.grid(True, alpha=0.3)

    # Retrain frequency vs performance
    ax2 = axes[1]

    retrain_freq = ['Never', 'Yearly', 'Quarterly', 'Monthly', 'Weekly']
    avg_performance = [0.58, 0.72, 0.82, 0.88, 0.90]
    retrain_cost = [0, 10, 40, 150, 700]

    x = np.arange(len(retrain_freq))

    ax2.bar(x, avg_performance, color='#4A90E2', alpha=0.8, label='Avg Performance')

    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, retrain_cost, 'ro-', linewidth=2, markersize=10, label='Retrain Cost ($K/yr)')
    ax2_twin.set_ylabel('Annual Retraining Cost ($K)', fontsize=10, color='#D62728')
    ax2_twin.tick_params(axis='y', labelcolor='#D62728')

    ax2.set_xlabel('Retraining Frequency', fontsize=11)
    ax2.set_ylabel('Average Performance', fontsize=11)
    ax2.set_title('Retraining Frequency Trade-off', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(retrain_freq)
    ax2.set_ylim(0.5, 1)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='center right', fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    # Optimal zone
    ax2.annotate('Optimal\nZone', xy=(2, 0.82), xytext=(2.5, 0.7),
                fontsize=10, fontweight='bold', color='#44A044',
                arrowprops=dict(arrowstyle='->', color='#44A044'))

    fig.suptitle('ML Model Decay and Retraining Strategy', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'model_decay.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
