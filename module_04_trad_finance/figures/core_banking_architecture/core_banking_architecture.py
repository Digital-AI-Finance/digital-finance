"""
Core Banking Architecture
Traditional bank system structure

Output: core_banking_architecture.pdf
Module: module_04_trad_finance
Lesson: 38 - Core Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Core Banking Architecture',
    'module': 'module_04_trad_finance',
    'lesson': 38,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/core_banking_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)

    # Layers of architecture
    layers = [
        (8, 8.5, 'Channels', '#4A90E2', 14, 1,
         ['Branch', 'ATM', 'Mobile', 'Web', 'API']),
        (8, 6.5, 'Integration Layer', '#44A044', 14, 1,
         ['ESB', 'API Gateway', 'Message Queue', 'SOA']),
        (8, 4.5, 'Core Banking System', '#FF7F0E', 14, 1.5,
         ['Deposits', 'Loans', 'Payments', 'GL', 'Customer']),
        (8, 2.5, 'Infrastructure', '#9B59B6', 14, 1,
         ['Database', 'Mainframe', 'Cloud', 'Security']),
    ]

    for x, y, label, color, w, h, components in layers:
        rect = mpatches.FancyBboxPatch((x-w/2, y-h/2), w, h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.7,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.5, y, label, ha='center', va='center', fontsize=11,
               fontweight='bold', rotation=90)

        # Components
        comp_width = w / len(components) - 0.3
        start_x = x - w/2 + 0.5
        for i, comp in enumerate(components):
            comp_x = start_x + i * (w / len(components))
            ax.text(comp_x + comp_width/2, y, comp, ha='center', va='center',
                   fontsize=9, fontweight='bold', color='white')

    # Connecting lines
    for i in range(3):
        ax.annotate('', xy=(8, 7.9 - i*2), xytext=(8, 7.1 - i*2),
                   arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))

    ax.set_title('Core Banking System Architecture', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'core_banking_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
