"""
Model Governance Framework
ML model risk management

Output: model_governance.pdf
Module: module_03_ai_ml
Lesson: 36 - AI Regulation
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Model Governance',
    'module': 'module_03_ai_ml',
    'lesson': 36,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/model_governance'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)

    # Three Lines of Defense
    lines = [
        ('1st Line:\nBusiness', 3, '#4A90E2', [
            'Model Development',
            'Data Quality',
            'Ongoing Monitoring',
            'User Training'
        ]),
        ('2nd Line:\nRisk Management', 8, '#44A044', [
            'Model Validation',
            'Risk Assessment',
            'Policy Setting',
            'Compliance Check'
        ]),
        ('3rd Line:\nInternal Audit', 13, '#FF7F0E', [
            'Independent Review',
            'Framework Audit',
            'Regulatory Liaison',
            'Report to Board'
        ])
    ]

    for line_name, x, color, activities in lines:
        # Header
        rect = mpatches.FancyBboxPatch((x-2, 7), 4, 1.3,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.9,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 7.6, line_name, ha='center', va='center', fontsize=11,
               fontweight='bold', color='white')

        # Activities
        for i, act in enumerate(activities):
            rect = mpatches.FancyBboxPatch((x-1.8, 5.5 - i*1.2), 3.6, 0.9,
                                            boxstyle="round,pad=0.05",
                                            facecolor=color, alpha=0.25,
                                            edgecolor=color, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x, 6 - i*1.2, act, ha='center', va='center', fontsize=9)

    # Lifecycle arrow
    ax.annotate('', xy=(14.5, 1), xytext=(1.5, 1),
               arrowprops=dict(arrowstyle='->', color='black', lw=2))

    lifecycle = ['Develop', 'Validate', 'Deploy', 'Monitor', 'Retire']
    for i, stage in enumerate(lifecycle):
        ax.text(2.5 + i*2.5, 0.5, stage, ha='center', fontsize=9, fontweight='bold')
        ax.plot(2.5 + i*2.5, 1, 'ko', markersize=8)

    ax.text(8, 1.5, 'Model Lifecycle', ha='center', fontsize=11, fontweight='bold')

    ax.set_title('ML Model Governance: Three Lines of Defense', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'model_governance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
