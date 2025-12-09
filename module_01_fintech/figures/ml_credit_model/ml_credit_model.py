"""
ML Credit Scoring Model Architecture
Shows the machine learning pipeline for credit scoring

Output: ml_credit_model.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'ML Credit Model Architecture',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ml_credit_model'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create ML credit model architecture diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'ML Credit Scoring Pipeline', fontsize=17, fontweight='bold', ha='center')

    # Pipeline stages
    stages = [
        {'name': 'Data\nIngestion', 'x': 1.5, 'y': 6, 'color': '#4A90E2',
         'desc': '100+ features\nfrom 10+ sources'},
        {'name': 'Feature\nEngineering', 'x': 4, 'y': 6, 'color': '#44A044',
         'desc': 'Transformations\nInteractions'},
        {'name': 'Model\nTraining', 'x': 6.5, 'y': 6, 'color': '#FF7F0E',
         'desc': 'XGBoost/Neural\nEnsembles'},
        {'name': 'Risk\nScoring', 'x': 9, 'y': 6, 'color': '#6B5B95',
         'desc': 'PD estimation\n0-100 score'},
        {'name': 'Decision\nOutput', 'x': 11.5, 'y': 6, 'color': '#333333',
         'desc': 'Approve/Decline\nRate/Limit'},
    ]

    for stage in stages:
        box = mpatches.FancyBboxPatch((stage['x']-1, stage['y']-0.8), 2, 1.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=stage['color'], edgecolor='#333333', lw=2)
        ax.add_patch(box)
        ax.text(stage['x'], stage['y']+0.3, stage['name'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')
        ax.text(stage['x'], stage['y']-1.5, stage['desc'], ha='center', fontsize=9)

    # Arrows
    for i in range(len(stages)-1):
        ax.annotate('', xy=(stages[i+1]['x']-1.1, stages[i+1]['y']),
                   xytext=(stages[i]['x']+1.1, stages[i]['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Model details box
    details_box = mpatches.FancyBboxPatch((1, 1.5), 11, 2.5, boxstyle='round,pad=0.1',
                                           facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(details_box)
    ax.text(6.5, 3.7, 'Model Components', ha='center', fontsize=12, fontweight='bold')

    components = [
        ('Algorithms', 'Gradient Boosting, Random Forest, Neural Networks, Logistic Regression'),
        ('Validation', 'K-fold CV, Out-of-time testing, Stability analysis'),
        ('Explainability', 'SHAP values, Feature importance, Adverse action reasons'),
        ('Monitoring', 'PSI drift detection, Performance tracking, Bias testing'),
    ]
    for i, (name, desc) in enumerate(components):
        ax.text(1.3, 3.1-i*0.45, f'{name}:', fontsize=10, fontweight='bold')
        ax.text(3.5, 3.1-i*0.45, desc, fontsize=9)

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL ARCHITECTURE]',
            fontsize=9, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_credit_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
