"""
BaaS Ecosystem
Shows Banking-as-a-Service ecosystem

Output: baas_ecosystem.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'BaaS Ecosystem',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/baas_ecosystem'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create BaaS ecosystem diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Banking-as-a-Service (BaaS) Ecosystem', fontsize=20, fontweight='bold', ha='center')

    # Layers
    layers = [
        {
            'name': 'Licensed Banks',
            'y': 7.5, 'color': '#4A90E2',
            'examples': 'Cross River, Sutton, Green Dot, Bancorp',
            'role': 'Hold charter, provide compliance'
        },
        {
            'name': 'BaaS Platforms',
            'y': 5.5, 'color': '#44A044',
            'examples': 'Galileo, Synapse, Unit, Treasury Prime',
            'role': 'APIs, orchestration, program mgmt'
        },
        {
            'name': 'FinTech/Brands',
            'y': 3.5, 'color': '#FF7F0E',
            'examples': 'Chime, Dave, Current, Shopify Balance',
            'role': 'Customer experience, distribution'
        },
        {
            'name': 'End Customers',
            'y': 1.5, 'color': '#6B5B95',
            'examples': 'Consumers, SMBs, enterprises',
            'role': 'Use financial products'
        },
    ]

    for layer in layers:
        box = mpatches.FancyBboxPatch((2, layer['y']-0.6), 10, 1.3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=layer['color'], alpha=0.2,
                                       edgecolor=layer['color'], lw=2)
        ax.add_patch(box)
        ax.text(3.5, layer['y'], layer['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=layer['color'])
        ax.text(7.5, layer['y']+0.2, layer['examples'], ha='center', va='center', fontsize=10)
        ax.text(7.5, layer['y']-0.25, layer['role'], ha='center', va='center',
               fontsize=10, style='italic', color='#666666')

    # Arrows between layers
    for i in range(len(layers)-1):
        ax.annotate('', xy=(7, layers[i+1]['y']+0.6), xytext=(7, layers[i]['y']-0.6),
                   arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5))

    # Benefits
    ax.text(13.5, 5.5, 'Benefits:', fontsize=12, fontweight='bold', ha='right')
    benefits = ['Fast launch', 'No charter needed', 'Focus on UX', 'Scalable']
    for i, b in enumerate(benefits):
        ax.text(13.5, 5-i*0.4, f'* {b}', fontsize=10, ha='right')

    # Source
    fig.text(0.5, 0.02, 'Source: a]6z BaaS report, company documentation (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'baas_ecosystem.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
