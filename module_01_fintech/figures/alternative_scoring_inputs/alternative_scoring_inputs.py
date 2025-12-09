"""
Alternative Credit Scoring Inputs
Shows non-traditional data sources used in P2P credit scoring

Output: alternative_scoring_inputs.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Alternative Credit Scoring Inputs',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/alternative_scoring_inputs'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create alternative scoring inputs diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'Alternative Credit Scoring Data Sources', fontsize=17, fontweight='bold', ha='center')

    # Center: ML Model
    model_circle = mpatches.Circle((6.5, 5), 1.5, facecolor='#4A90E2',
                                    edgecolor='#333333', lw=3)
    ax.add_patch(model_circle)
    ax.text(6.5, 5.2, 'ML Credit', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(6.5, 4.6, 'Model', ha='center', fontsize=12, fontweight='bold', color='white')

    # Data categories around the model
    categories = [
        {'name': 'Traditional', 'x': 2, 'y': 8, 'color': '#44A044',
         'items': ['FICO score', 'Credit history', 'Income verification', 'Employment']},
        {'name': 'Financial Behavior', 'x': 11, 'y': 8, 'color': '#FF7F0E',
         'items': ['Bank transactions', 'Spending patterns', 'Savings habits', 'Bill payments']},
        {'name': 'Digital Footprint', 'x': 2, 'y': 2, 'color': '#6B5B95',
         'items': ['Device data', 'Browser behavior', 'App usage', 'Location patterns']},
        {'name': 'Social/Alternative', 'x': 11, 'y': 2, 'color': '#D62728',
         'items': ['Education history', 'Professional network', 'Social connections', 'Reviews/reputation']},
    ]

    for cat in categories:
        # Category box
        box = mpatches.FancyBboxPatch((cat['x']-1.5, cat['y']-1.5), 3, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(cat['x'], cat['y']+0.7, cat['name'], ha='center',
               fontsize=11, fontweight='bold', color=cat['color'])

        for i, item in enumerate(cat['items']):
            ax.text(cat['x'], cat['y']-i*0.4, f'* {item}', ha='center', fontsize=9)

        # Arrow to center
        dx = 6.5 - cat['x']
        dy = 5 - cat['y']
        length = np.sqrt(dx**2 + dy**2)
        ax.annotate('', xy=(6.5 - dx/length*1.6, 5 - dy/length*1.6),
                   xytext=(cat['x'] + dx/length*1.6, cat['y'] + dy/length*1.6),
                   arrowprops=dict(arrowstyle='->', color=cat['color'], lw=2))

    # Impact note
    impact = "Alternative data can increase approval rates by 20-30% for thin-file borrowers"
    ax.text(6.5, 0.5, impact, ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CFPB alternative data research, industry practices',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'alternative_scoring_inputs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
