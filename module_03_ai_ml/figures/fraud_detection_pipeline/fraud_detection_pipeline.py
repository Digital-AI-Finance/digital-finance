"""
Fraud Detection Pipeline
End-to-end fraud detection system architecture

Output: fraud_detection_pipeline.pdf
Module: module_03_ai_ml
Lesson: 31 - Fraud Detection
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Fraud Detection Pipeline',
    'module': 'module_03_ai_ml',
    'lesson': 31,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/fraud_detection_pipeline'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    # Pipeline stages
    stages = [
        (1, 4, 'Data\nIngestion', '#4A90E2', ['Transaction Data', 'User Behavior', 'Device Info']),
        (4, 4, 'Feature\nEngineering', '#44A044', ['Velocity Features', 'Aggregations', 'Anomaly Flags']),
        (7, 4, 'ML\nModels', '#FF7F0E', ['Random Forest', 'Neural Network', 'Ensemble']),
        (10, 4, 'Rule\nEngine', '#9B59B6', ['Business Rules', 'Velocity Checks', 'Blacklists']),
        (13, 4, 'Decision', '#D62728', ['Approve', 'Decline', 'Review'])
    ]

    for x, y, label, color, details in stages:
        # Main box
        rect = mpatches.FancyBboxPatch((x-0.8, y-0.8), 1.6, 1.6,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')

        # Details below
        for i, detail in enumerate(details):
            ax.text(x, y - 1.5 - i*0.4, f'- {detail}', ha='center', va='top',
                   fontsize=8, color='#333333')

        # Arrows
        if x < 13:
            ax.annotate('', xy=(x+1.3, y), xytext=(x+0.9, y),
                       arrowprops=dict(arrowstyle='->', color='black', lw=2))

    # Real-time indicator
    ax.annotate('Real-time (<100ms)', xy=(7, 6.5), fontsize=12, fontweight='bold',
               ha='center', color='#4A90E2')
    ax.plot([1, 13], [6.2, 6.2], 'b--', linewidth=2, alpha=0.5)

    # Feedback loop
    ax.annotate('', xy=(1, 2), xytext=(13, 2),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2,
                             connectionstyle='arc3,rad=0.3'))
    ax.text(7, 1, 'Model Retraining Feedback Loop', ha='center', va='center',
           fontsize=10, fontweight='bold', color='#44A044')

    ax.set_title('Fraud Detection Pipeline Architecture', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'fraud_detection_pipeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
