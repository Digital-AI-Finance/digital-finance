"""
Financial Market Structure
Overview of market organization

Output: market_structure.pdf
Module: module_04_trad_finance
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Market Structure',
    'module': 'module_04_trad_finance',
    'lesson': 37,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/market_structure'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)

    # Market layers
    layers = [
        (8, 7.5, 'Primary Market', '#4A90E2', 14, 1.2,
         'IPOs, Bond Issuance, Direct Offerings'),
        (8, 5.5, 'Secondary Market', '#44A044', 14, 1.2,
         'Exchanges, OTC Markets, Dark Pools'),
        (8, 3.5, 'Derivatives Market', '#FF7F0E', 14, 1.2,
         'Futures, Options, Swaps'),
        (8, 1.5, 'Money Market', '#9B59B6', 14, 1.2,
         'T-Bills, Commercial Paper, Repos'),
    ]

    for x, y, label, color, w, h, desc in layers:
        rect = mpatches.FancyBboxPatch((x-w/2, y-h/2), w, h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.7,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.1, label, ha='center', va='center', fontsize=12,
               fontweight='bold', color='white')
        ax.text(x, y - 0.3, desc, ha='center', va='center', fontsize=9,
               color='white')

    # Connecting arrows
    for i in range(3):
        ax.annotate('', xy=(8, 6.8 - i*2), xytext=(8, 6.2 - i*2),
                   arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))

    ax.set_title('Financial Market Structure: Layers and Functions', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'market_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
