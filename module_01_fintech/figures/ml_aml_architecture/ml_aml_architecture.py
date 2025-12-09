"""
ML AML Architecture
Shows machine learning approach to AML

Output: ml_aml_architecture.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'ML AML Architecture',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ml_aml_architecture'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create ML AML architecture diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'ML-Powered AML Architecture', fontsize=20, fontweight='bold', ha='center')

    # Data layer
    ax.text(2, 7.8, 'Data Layer', fontsize=14, fontweight='bold', color='#4A90E2')
    data_sources = ['Transactions', 'Customer\nProfiles', 'External\nData', 'Historical\nSARs']
    for i, src in enumerate(data_sources):
        box = mpatches.FancyBboxPatch((0.5+i*3.2, 6.5), 2.8, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.2,
                                       edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(box)
        ax.text(1.9+i*3.2, 7, src, ha='center', va='center', fontsize=11)

    # Arrow to ML layer
    ax.annotate('', xy=(7, 5.8), xytext=(7, 6.4),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # ML Layer
    ax.text(2, 5.6, 'ML Layer', fontsize=14, fontweight='bold', color='#44A044')
    ml_components = [
        {'name': 'Feature\nEngineering', 'x': 2.5},
        {'name': 'Anomaly\nDetection', 'x': 5.5},
        {'name': 'Risk\nScoring', 'x': 8.5},
        {'name': 'Network\nAnalysis', 'x': 11.5},
    ]
    for comp in ml_components:
        box = mpatches.FancyBboxPatch((comp['x']-1.3, 4.2), 2.6, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.2,
                                       edgecolor='#44A044', lw=1.5)
        ax.add_patch(box)
        ax.text(comp['x'], 4.8, comp['name'], ha='center', va='center', fontsize=11)

    # Arrow to output
    ax.annotate('', xy=(7, 3.5), xytext=(7, 4.1),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Output layer
    ax.text(2, 3.3, 'Output Layer', fontsize=14, fontweight='bold', color='#FF7F0E')
    outputs = [
        {'name': 'Prioritized\nAlerts', 'x': 3.5},
        {'name': 'Risk\nDashboard', 'x': 7},
        {'name': 'Auto SAR\nDrafting', 'x': 10.5},
    ]
    for out in outputs:
        box = mpatches.FancyBboxPatch((out['x']-1.5, 1.8), 3, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#FF7F0E', alpha=0.2,
                                       edgecolor='#FF7F0E', lw=1.5)
        ax.add_patch(box)
        ax.text(out['x'], 2.4, out['name'], ha='center', va='center', fontsize=11)

    # Benefits
    benefits = "Benefits: 50-70% fewer false positives | 80% faster investigation | Continuous learning"
    ax.text(7, 0.8, benefits, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL ARCHITECTURE]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_aml_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
