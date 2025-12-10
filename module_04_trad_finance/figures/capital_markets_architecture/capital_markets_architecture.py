"""
Capital Markets Technology Architecture
Trading to settlement infrastructure

Output: capital_markets_architecture.pdf
Module: module_04_trad_finance
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Capital Markets Architecture',
    'module': 'module_04_trad_finance',
    'lesson': 44,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/capital_markets_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Layer boxes
    layers = [
        ('Front Office', 0.5, 7, 13, 1.5, '#4A90E2'),
        ('Middle Office', 0.5, 4.8, 13, 1.5, '#44A044'),
        ('Back Office', 0.5, 2.6, 13, 1.5, '#FF7F0E'),
        ('Infrastructure', 0.5, 0.5, 13, 1.5, '#9B59B6'),
    ]

    for name, x, y, w, h, color in layers:
        rect = mpatches.FancyBboxPatch((x, y), w, h,
                                        boxstyle="round,pad=0.02",
                                        facecolor=color, alpha=0.15, edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        ax.text(0.2, y + h/2, name, ha='left', va='center', fontsize=11,
                fontweight='bold', color=color, rotation=90)

    # Front Office components
    front_components = [
        ('Order\nManagement', 2, 7.5),
        ('Execution\nManagement', 4.5, 7.5),
        ('Algo\nTrading', 7, 7.5),
        ('Market\nData', 9.5, 7.5),
        ('Portfolio\nManagement', 12, 7.5),
    ]

    for name, x, y in front_components:
        rect = mpatches.FancyBboxPatch((x-0.9, y-0.4), 1.8, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#4A90E2', alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    # Middle Office components
    middle_components = [
        ('Risk\nManagement', 2.5, 5.3),
        ('P&L\nAttribution', 5, 5.3),
        ('Compliance', 7.5, 5.3),
        ('Trade\nCapture', 10, 5.3),
        ('Position\nKeeping', 12.5, 5.3),
    ]

    for name, x, y in middle_components:
        rect = mpatches.FancyBboxPatch((x-0.9, y-0.4), 1.8, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#44A044', alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    # Back Office components
    back_components = [
        ('Clearing', 2.5, 3.1),
        ('Settlement', 5, 3.1),
        ('Custody', 7.5, 3.1),
        ('Corporate\nActions', 10, 3.1),
        ('Reconciliation', 12.5, 3.1),
    ]

    for name, x, y in back_components:
        rect = mpatches.FancyBboxPatch((x-0.9, y-0.4), 1.8, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#FF7F0E', alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    # Infrastructure components
    infra_components = [
        ('Connectivity\n(FIX/SWIFT)', 2.5, 1),
        ('Data\nWarehouse', 5, 1),
        ('Message\nBus', 7.5, 1),
        ('Reference\nData', 10, 1),
        ('Security', 12.5, 1),
    ]

    for name, x, y in infra_components:
        rect = mpatches.FancyBboxPatch((x-0.9, y-0.4), 1.8, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#9B59B6', alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    # Title
    ax.text(7, 8.7, 'Capital Markets Technology Stack', ha='center', va='center',
            fontsize=14, fontweight='bold')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'capital_markets_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
