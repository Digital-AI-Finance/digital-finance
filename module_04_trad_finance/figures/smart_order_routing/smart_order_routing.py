"""
Smart Order Routing Logic
SOR algorithm decision tree

Output: smart_order_routing.pdf
Module: module_04_trad_finance
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Smart Order Routing',
    'module': 'module_04_trad_finance',
    'lesson': 40,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/smart_order_routing'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)

    # SOR Decision Flow
    nodes = [
        (8, 9, 'Order\nReceived', '#4A90E2', 'diamond'),
        (4, 7, 'Size >\nThreshold?', '#FF7F0E', 'diamond'),
        (12, 7, 'Urgent?', '#FF7F0E', 'diamond'),
        (2, 5, 'TWAP/VWAP\nAlgorithm', '#44A044', 'rect'),
        (6, 5, 'Dark Pool\nFirst', '#44A044', 'rect'),
        (10, 5, 'Lit Market\nDirect', '#44A044', 'rect'),
        (14, 5, 'Aggressive\nSweep', '#44A044', 'rect'),
        (8, 2.5, 'Execution\nComplete', '#9B59B6', 'rect'),
    ]

    for x, y, label, color, shape in nodes:
        if shape == 'diamond':
            diamond = mpatches.RegularPolygon((x, y), numVertices=4, radius=0.8,
                                               orientation=np.pi/4,
                                               facecolor=color, alpha=0.8,
                                               edgecolor='black', linewidth=2)
            ax.add_patch(diamond)
        else:
            rect = mpatches.FancyBboxPatch((x-1.2, y-0.6), 2.4, 1.2,
                                            boxstyle="round,pad=0.05",
                                            facecolor=color, alpha=0.8,
                                            edgecolor='black', linewidth=2)
            ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')

    # Connections with labels
    connections = [
        (8, 8.2, 8, 7, '', 'k'),
        (4, 6.2, 4, 5.7, 'No', 'k'),
        (12, 6.2, 12, 5.7, 'No', 'k'),
        (8, 7.5, 5, 7.5, 'Large', '#D62728'),
        (8, 6.5, 11, 6.5, 'Small', '#44A044'),
        (4.8, 7, 6, 5.6, 'Yes', 'k'),
        (11.2, 7, 10, 5.6, 'Yes', 'k'),
        (2, 4.4, 5, 3, '', 'gray'),
        (6, 4.4, 6.5, 3, '', 'gray'),
        (10, 4.4, 9.5, 3, '', 'gray'),
        (14, 4.4, 11, 3, '', 'gray'),
    ]

    for x1, y1, x2, y2, label, color in connections:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2 + 0.2, label, fontsize=8, fontweight='bold')

    ax.set_title('Smart Order Router Decision Flow', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'smart_order_routing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
