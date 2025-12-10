"""
Fraud Detection Cost-Benefit Analysis
Trade-offs in fraud prevention

Output: fraud_cost_benefit.pdf
Module: module_03_ai_ml
Lesson: 31 - Fraud Detection
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Fraud Cost Benefit',
    'module': 'module_03_ai_ml',
    'lesson': 31,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/fraud_cost_benefit'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Cost-Benefit Matrix
    ax1 = axes[0]

    categories = ['True Positive\n(Caught Fraud)', 'False Positive\n(False Alarm)',
                  'False Negative\n(Missed Fraud)', 'True Negative\n(Good Transaction)']
    costs = [50, -25, -500, 2]  # Positive = benefit, Negative = cost
    colors = ['#44A044', '#FF7F0E', '#D62728', '#4A90E2']

    bars = ax1.bar(categories, costs, color=colors, edgecolor='black', alpha=0.8)

    for bar, cost in zip(bars, costs):
        label = f'+${cost}' if cost > 0 else f'-${abs(cost)}'
        y_pos = bar.get_height() + 10 if cost > 0 else bar.get_height() - 30
        ax1.text(bar.get_x() + bar.get_width()/2, y_pos, label,
                ha='center', fontsize=11, fontweight='bold')

    ax1.axhline(y=0, color='black', linewidth=1)
    ax1.set_ylabel('Net Value per Transaction ($)', fontsize=11)
    ax1.set_title('Cost-Benefit Analysis per Outcome', fontsize=12, fontweight='bold')
    ax1.set_ylim(-600, 100)
    ax1.yaxis.grid(True, alpha=0.3)

    # Precision-Recall Trade-off
    ax2 = axes[1]

    # Generate trade-off curve
    recall = np.linspace(0.1, 0.99, 50)
    precision = 0.95 - 0.6 * recall + 0.3 * recall**2  # Simulated trade-off

    ax2.plot(recall, precision, 'b-', linewidth=3)

    # Mark operating points
    points = [(0.6, 0.78, 'Conservative'), (0.8, 0.65, 'Balanced'), (0.95, 0.48, 'Aggressive')]
    for r, p, label in points:
        ax2.scatter([r], [p], s=150, zorder=5, edgecolors='black', linewidth=2)
        ax2.annotate(label, xy=(r, p), xytext=(r+0.05, p+0.05),
                    fontsize=9, fontweight='bold')

    ax2.fill_between(recall, precision, alpha=0.2, color='#4A90E2')

    ax2.set_xlabel('Recall (Fraud Caught Rate)', fontsize=11)
    ax2.set_ylabel('Precision (Accuracy of Alerts)', fontsize=11)
    ax2.set_title('Precision-Recall Trade-off', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1.1)
    ax2.set_ylim(0.3, 1)
    ax2.grid(True, alpha=0.3)

    # Add business context
    ax2.text(0.3, 0.9, 'Fewer false\nalarms', fontsize=9, ha='center', color='#44A044')
    ax2.text(0.85, 0.4, 'Catch more\nfraud', fontsize=9, ha='center', color='#D62728')

    fig.suptitle('Fraud Detection: Cost-Benefit Trade-offs', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'fraud_cost_benefit.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
