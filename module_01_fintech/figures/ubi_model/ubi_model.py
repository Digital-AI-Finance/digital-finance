"""
Usage-Based Insurance Model
Shows how UBI works with telematics

Output: ubi_model.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Usage-Based Insurance Model',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ubi_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create UBI model diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Usage-Based Insurance (UBI)', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Pay-How-You-Drive / Pay-As-You-Drive', fontsize=14, ha='center', color='#666666')

    # UBI Types
    types = [
        {'name': 'PAYD\n(Pay-As-You-Drive)', 'x': 3.5, 'y': 6.5, 'color': '#4A90E2',
         'basis': 'Miles driven', 'example': 'Metromile: $0.05/mile'},
        {'name': 'PHYD\n(Pay-How-You-Drive)', 'x': 10.5, 'y': 6.5, 'color': '#44A044',
         'basis': 'Driving behavior', 'example': 'Progressive: up to 30% discount'},
    ]

    for t in types:
        box = mpatches.FancyBboxPatch((t['x']-2, t['y']-1.5), 4, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=t['color'], alpha=0.2,
                                       edgecolor=t['color'], lw=2)
        ax.add_patch(box)
        ax.text(t['x'], t['y']+1, t['name'], ha='center', fontsize=13, fontweight='bold', color=t['color'])
        ax.text(t['x'], t['y'], f"Based on: {t['basis']}", ha='center', fontsize=12)
        ax.text(t['x'], t['y']-0.7, t['example'], ha='center', fontsize=11, style='italic')

    # Data collection methods
    ax.text(7, 4.3, 'Data Collection Methods', fontsize=14, fontweight='bold', ha='center')

    methods = [
        {'name': 'OBD-II\nDongle', 'x': 2.5, 'y': 3},
        {'name': 'Smartphone\nApp', 'x': 5.5, 'y': 3},
        {'name': 'Vehicle\nTelematics', 'x': 8.5, 'y': 3},
        {'name': 'Connected\nCar API', 'x': 11.5, 'y': 3},
    ]

    for m in methods:
        box = mpatches.FancyBboxPatch((m['x']-1.2, m['y']-0.8), 2.4, 1.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#FF7F0E', alpha=0.15,
                                       edgecolor='#FF7F0E', lw=1.5)
        ax.add_patch(box)
        ax.text(m['x'], m['y'], m['name'], ha='center', va='center', fontsize=11)

    # Market stats
    stats = "UBI Market: $35B (2024) | Growth: 25% CAGR | Adoption: 20% of US auto policies by 2025"
    ax.text(7, 1.2, stats, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Ptolemus Consulting, Allied Market Research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ubi_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
