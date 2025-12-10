"""
Feature Attribution Methods
Comparison of explanation techniques

Output: feature_attribution.pdf
Module: module_03_ai_ml
Lesson: 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Feature Attribution',
    'module': 'module_03_ai_ml',
    'lesson': 35,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/feature_attribution'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))

    methods = ['Permutation\nImportance', 'SHAP', 'LIME', 'Integrated\nGradients',
               'Attention\nWeights', 'Grad-CAM']

    # Characteristics scores (0-10)
    characteristics = {
        'Model Agnostic': [10, 10, 10, 5, 3, 3],
        'Consistency': [6, 9, 7, 8, 5, 6],
        'Speed': [3, 5, 6, 7, 9, 8],
        'Local Explanations': [2, 9, 10, 8, 7, 8],
        'Global Explanations': [9, 8, 3, 5, 6, 4]
    }

    x = np.arange(len(methods))
    width = 0.15
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6']

    for i, (char, values) in enumerate(characteristics.items()):
        ax.bar(x + i*width - 2*width, values, width, label=char, color=colors[i], alpha=0.8)

    ax.set_xlabel('Attribution Method', fontsize=11)
    ax.set_ylabel('Score (0-10)', fontsize=11)
    ax.set_title('Feature Attribution Methods Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=10)
    ax.legend(loc='upper right', fontsize=9, ncol=2)
    ax.set_ylim(0, 12)
    ax.yaxis.grid(True, alpha=0.3)

    # Best use case annotations
    use_cases = ['Tabular Data', 'All Models', 'Quick Debug', 'Deep Learning', 'NLP/Transform.', 'Computer Vision']
    for i, (method, use) in enumerate(zip(methods, use_cases)):
        ax.text(i, 11, use, ha='center', fontsize=8, style='italic', color='#666666')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'feature_attribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
