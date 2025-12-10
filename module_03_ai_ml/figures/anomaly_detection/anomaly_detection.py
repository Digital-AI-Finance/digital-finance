"""
Anomaly Detection Visualization
Normal vs anomalous transactions

Output: anomaly_detection.pdf
Module: module_03_ai_ml
Lesson: 31 - Fraud Detection
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Anomaly Detection',
    'module': 'module_03_ai_ml',
    'lesson': 31,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/anomaly_detection'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Scatter plot of transactions
    ax1 = axes[0]

    # Normal transactions
    normal_amount = np.random.lognormal(4, 0.8, 500)
    normal_freq = np.random.poisson(5, 500)
    normal_amount = np.clip(normal_amount, 0, 1000)

    # Anomalous transactions
    anomaly_amount = np.random.uniform(500, 2000, 20)
    anomaly_freq = np.random.uniform(15, 30, 20)

    ax1.scatter(normal_freq, normal_amount, c='#4A90E2', alpha=0.5, s=30, label='Normal')
    ax1.scatter(anomaly_freq, anomaly_amount, c='#D62728', alpha=0.8, s=100,
               marker='X', label='Anomaly', edgecolors='black')

    # Decision boundary (simplified ellipse)
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(5 + 8*np.cos(theta), 300 + 300*np.sin(theta), 'g--', linewidth=2,
            label='Decision Boundary')

    ax1.set_xlabel('Transaction Frequency (per day)', fontsize=11)
    ax1.set_ylabel('Transaction Amount ($)', fontsize=11)
    ax1.set_title('Anomaly Detection: Transaction Patterns', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(-2, 35)
    ax1.set_ylim(0, 2500)
    ax1.grid(True, alpha=0.3)

    # Isolation Forest Score Distribution
    ax2 = axes[1]

    # Generate anomaly scores
    normal_scores = np.random.beta(2, 5, 1000) * 0.5
    fraud_scores = np.random.beta(5, 2, 50) * 0.5 + 0.5

    ax2.hist(normal_scores, bins=30, alpha=0.7, color='#4A90E2', label='Normal', density=True)
    ax2.hist(fraud_scores, bins=15, alpha=0.7, color='#D62728', label='Fraud', density=True)

    # Threshold line
    threshold = 0.5
    ax2.axvline(x=threshold, color='#44A044', linestyle='--', linewidth=2, label='Threshold')

    ax2.set_xlabel('Anomaly Score', fontsize=11)
    ax2.set_ylabel('Density', fontsize=11)
    ax2.set_title('Anomaly Score Distribution', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=9)

    # Add annotations
    ax2.annotate('Flag as\nSuspicious', xy=(0.7, 1), xytext=(0.8, 2),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    fig.suptitle('Fraud Anomaly Detection System', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'anomaly_detection.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
