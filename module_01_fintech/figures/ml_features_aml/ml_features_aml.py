"""
ML Features for AML
Shows features used in ML-based AML systems

Output: ml_features_aml.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'ML Features for AML',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ml_features_aml'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create ML features for AML diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'ML Features for AML Detection', fontsize=20, fontweight='bold', ha='center')

    # Feature categories
    categories = [
        {
            'name': 'Transaction Features',
            'x': 2.5, 'y': 6.5,
            'color': '#4A90E2',
            'features': ['Amount, frequency, timing', 'Counterparty patterns', 'Channel (ATM, wire, ACH)', 'Geographic spread']
        },
        {
            'name': 'Behavioral Features',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'features': ['Deviation from baseline', 'Velocity changes', 'Product usage shifts', 'Login patterns']
        },
        {
            'name': 'Network Features',
            'x': 11.5, 'y': 6.5,
            'color': '#FF7F0E',
            'features': ['Degree centrality', 'Community detection', 'Path analysis', 'Entity resolution']
        },
        {
            'name': 'Customer Features',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'features': ['Risk score', 'KYC data quality', 'Account age', 'Product holdings']
        },
        {
            'name': 'External Features',
            'x': 9.25, 'y': 2.5,
            'color': '#D62728',
            'features': ['Adverse media', 'Sanctions lists', 'PEP databases', 'Corporate registries']
        },
    ]

    for cat in categories:
        # Box
        box = mpatches.FancyBboxPatch((cat['x']-1.8, cat['y']-1.6), 3.6, 3.3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(cat['x'], cat['y']+1.3, cat['name'], ha='center',
               fontsize=12, fontweight='bold', color=cat['color'])

        for i, feat in enumerate(cat['features']):
            ax.text(cat['x'], cat['y']+0.5-i*0.5, f'* {feat}', ha='center', fontsize=10)

    # Feature count note
    note = "Typical ML AML model: 200-500 features | Updated monthly | Continuous retraining"
    ax.text(7, 0.8, note, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[TYPICAL FEATURE ENGINEERING]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_features_aml.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
