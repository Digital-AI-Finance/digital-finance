"""
Fairness Metrics in ML
Algorithmic fairness measurement

Output: fairness_metrics.pdf
Module: module_03_ai_ml
Lesson: 36 - AI Regulation
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Fairness Metrics',
    'module': 'module_03_ai_ml',
    'lesson': 36,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/fairness_metrics'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Fairness metrics comparison
    ax1 = axes[0]

    groups = ['Group A', 'Group B', 'Group C', 'Group D']
    approval_rate = [72, 58, 65, 45]
    fpr = [8, 15, 12, 22]  # False Positive Rate
    fnr = [12, 18, 15, 25]  # False Negative Rate

    x = np.arange(len(groups))
    width = 0.25

    bars1 = ax1.bar(x - width, approval_rate, width, label='Approval Rate (%)', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x, fpr, width, label='False Positive Rate (%)', color='#FF7F0E', alpha=0.8)
    bars3 = ax1.bar(x + width, fnr, width, label='False Negative Rate (%)', color='#D62728', alpha=0.8)

    ax1.set_xlabel('Demographic Group', fontsize=11)
    ax1.set_ylabel('Rate (%)', fontsize=11)
    ax1.set_title('Fairness Metrics Across Groups', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(groups)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 85)
    ax1.yaxis.grid(True, alpha=0.3)

    # Fairness threshold lines
    ax1.axhline(y=np.mean(approval_rate) * 0.8, color='#4A90E2', linestyle='--', alpha=0.5)
    ax1.text(3.5, np.mean(approval_rate) * 0.8 + 2, '80% rule', fontsize=8, color='#4A90E2')

    # Fairness-Accuracy Trade-off
    ax2 = axes[1]

    # Different fairness constraints
    constraints = ['No Constraint', 'Demographic\nParity', 'Equal\nOpportunity',
                  'Equalized\nOdds', 'Calibration']
    accuracy = [0.85, 0.78, 0.82, 0.80, 0.83]
    fairness_score = [0.45, 0.92, 0.78, 0.85, 0.72]

    colors = plt.cm.RdYlGn(np.array(fairness_score))

    for i, (const, acc, fair) in enumerate(zip(constraints, accuracy, fairness_score)):
        ax2.scatter(acc, fair, s=300, c=[colors[i]], edgecolors='black', linewidth=2, zorder=5)
        ax2.annotate(const, xy=(acc, fair), xytext=(5, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold')

    ax2.set_xlabel('Model Accuracy', fontsize=11)
    ax2.set_ylabel('Fairness Score', fontsize=11)
    ax2.set_title('Accuracy vs. Fairness Trade-off', fontsize=12, fontweight='bold')
    ax2.set_xlim(0.75, 0.88)
    ax2.set_ylim(0.4, 1)
    ax2.grid(True, alpha=0.3)

    # Optimal zone
    ax2.fill_between([0.78, 0.85], [0.75, 0.75], [1, 1], alpha=0.1, color='#44A044')
    ax2.text(0.815, 0.95, 'Acceptable\nZone', fontsize=9, ha='center', color='#44A044', fontweight='bold')

    fig.suptitle('Algorithmic Fairness in Financial AI', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'fairness_metrics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
