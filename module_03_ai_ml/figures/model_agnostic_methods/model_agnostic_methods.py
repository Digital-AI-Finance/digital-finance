"""
Model-Agnostic Explanation Methods
Overview of interpretability techniques

Output: model_agnostic_methods.pdf
Module: module_03_ai_ml
Lesson: 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Model Agnostic Methods',
    'module': 'module_03_ai_ml',
    'lesson': 35,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/model_agnostic_methods'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)

    # Categories and methods
    categories = [
        ('Global Methods', 3, '#4A90E2', [
            'Permutation Importance',
            'SHAP (Global)',
            'Partial Dependence',
            'Feature Interaction'
        ]),
        ('Local Methods', 8, '#44A044', [
            'LIME',
            'SHAP (Local)',
            'Counterfactual',
            'Anchors'
        ]),
        ('Intrinsic Methods', 13, '#FF7F0E', [
            'Decision Trees',
            'Linear Models',
            'Rule Lists',
            'GAMs'
        ])
    ]

    for cat_name, x, color, methods in categories:
        # Category header
        rect = mpatches.FancyBboxPatch((x-2, 7), 4, 1.2,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.9,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, 7.6, cat_name, ha='center', va='center', fontsize=12,
               fontweight='bold', color='white')

        # Methods
        for i, method in enumerate(methods):
            rect = mpatches.FancyBboxPatch((x-1.8, 5.5 - i*1.3), 3.6, 1,
                                            boxstyle="round,pad=0.05",
                                            facecolor=color, alpha=0.3,
                                            edgecolor=color, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x, 6 - i*1.3, method, ha='center', va='center', fontsize=10)

    # Add connecting concept
    ax.annotate('', xy=(5.5, 4), xytext=(5, 4),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=2))
    ax.annotate('', xy=(10.5, 4), xytext=(10, 4),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=2))

    # Trade-off explanation
    ax.text(8, 0.8, 'Trade-off: Interpretability vs. Predictive Power', ha='center',
           fontsize=12, fontweight='bold', style='italic')

    # Spectrum bar
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    ax.imshow(gradient, aspect='auto', cmap='RdYlGn', extent=[3, 13, 0.2, 0.5])
    ax.text(3, 0, 'Complex Models\n(High Accuracy)', fontsize=9, ha='center', color='#D62728')
    ax.text(13, 0, 'Simple Models\n(High Interpret.)', fontsize=9, ha='center', color='#44A044')

    ax.set_title('Model-Agnostic Explainability Methods', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'model_agnostic_methods.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
