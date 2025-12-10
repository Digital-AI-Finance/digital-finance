"""
Trading System Architecture
Electronic trading infrastructure

Output: trading_system_architecture.pdf
Module: module_04_trad_finance
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Trading System Architecture',
    'module': 'module_04_trad_finance',
    'lesson': 40,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/trading_system_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)

    # System components
    components = [
        (3, 8, 'Order\nManagement', '#4A90E2', 2.5, 1.3),
        (8, 8, 'Execution\nManagement', '#44A044', 2.5, 1.3),
        (13, 8, 'Market\nConnectivity', '#FF7F0E', 2.5, 1.3),

        (3, 5, 'Risk\nEngine', '#D62728', 2.5, 1.3),
        (8, 5, 'Smart Order\nRouter', '#9B59B6', 2.5, 1.3),
        (13, 5, 'Market Data\nHandler', '#17BECF', 2.5, 1.3),

        (5.5, 2, 'Trade\nMatching', '#FF7F0E', 2.5, 1.3),
        (10.5, 2, 'Post-Trade\nProcessing', '#4A90E2', 2.5, 1.3),
    ]

    for x, y, label, color, w, h in components:
        rect = mpatches.FancyBboxPatch((x-w/2, y-h/2), w, h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')

    # Connections
    connections = [
        (4.3, 8, 6.7, 8), (9.3, 8, 11.7, 8),  # Horizontal top
        (4.3, 5, 6.7, 5), (9.3, 5, 11.7, 5),  # Horizontal middle
        (3, 7.3, 3, 5.7), (8, 7.3, 8, 5.7), (13, 7.3, 13, 5.7),  # Vertical
        (5.5, 4.3, 5.5, 2.7), (10.5, 4.3, 10.5, 2.7),  # To bottom
    ]

    for x1, y1, x2, y2 in connections:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

    ax.set_title('Electronic Trading System Architecture', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'trading_system_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
