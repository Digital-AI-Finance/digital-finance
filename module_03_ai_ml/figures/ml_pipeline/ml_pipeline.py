"""
Machine Learning Pipeline Overview
Shows the typical ML workflow in finance

Output: ml_pipeline.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Machine Learning Pipeline',
    'module': 'module_03_ai_ml',
    'lesson': 25,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/ml_pipeline'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create ML pipeline visualization"""
    fig, ax = plt.subplots(figsize=(12, 6))

    # Pipeline stages
    stages = ['Data\nCollection', 'Data\nPreprocessing', 'Feature\nEngineering',
              'Model\nTraining', 'Model\nValidation', 'Deployment']
    colors = ['#4A90E2', '#5BA0E2', '#6BB0E2', '#7BC0E2', '#8BD0E2', '#44A044']

    # Draw boxes
    box_width = 0.12
    box_height = 0.3
    y_center = 0.5

    for i, (stage, color) in enumerate(zip(stages, colors)):
        x = 0.08 + i * 0.15
        rect = mpatches.FancyBboxPatch((x, y_center - box_height/2), box_width, box_height,
                                        boxstyle="round,pad=0.02", facecolor=color,
                                        edgecolor='#333333', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + box_width/2, y_center, stage, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

        # Draw arrow to next stage
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + box_width + 0.025, y_center),
                       xytext=(x + box_width + 0.005, y_center),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Add feedback loop
    ax.annotate('', xy=(0.14, y_center - box_height/2 - 0.08),
               xytext=(0.83, y_center - box_height/2 - 0.08),
               arrowprops=dict(arrowstyle='<-', color='#666666', lw=1.5,
                             connectionstyle='arc3,rad=0.3'))
    ax.text(0.5, y_center - box_height/2 - 0.15, 'Feedback & Iteration',
            ha='center', va='center', fontsize=9, color='#666666', style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Machine Learning Pipeline in Finance', fontsize=14, fontweight='bold', pad=20)

    # Synthetic label
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_pipeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
