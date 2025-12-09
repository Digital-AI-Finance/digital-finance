"""
Embedded Insurance
Shows embedded insurance distribution model

Output: embedded_insurance.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Embedded Insurance',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/embedded_insurance'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create embedded insurance diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Embedded Insurance: Insurance at Point of Sale', fontsize=20, fontweight='bold', ha='center')

    # Traditional vs Embedded
    ax.text(3.5, 8.2, 'Traditional Distribution', fontsize=14, fontweight='bold', ha='center', color='#666666')
    ax.text(10.5, 8.2, 'Embedded Insurance', fontsize=14, fontweight='bold', ha='center', color='#44A044')

    # Traditional path
    trad_steps = [
        {'name': 'Buy product', 'y': 7},
        {'name': 'Research insurance', 'y': 6},
        {'name': 'Visit insurer site', 'y': 5},
        {'name': 'Fill application', 'y': 4},
        {'name': 'Purchase separately', 'y': 3},
    ]
    for i, step in enumerate(trad_steps):
        ax.text(3.5, step['y'], step['name'], ha='center', fontsize=12)
        if i < len(trad_steps) - 1:
            ax.annotate('', xy=(3.5, step['y']-0.6), xytext=(3.5, step['y']-0.3),
                       arrowprops=dict(arrowstyle='->', color='#999999', lw=1.5))

    # Embedded path
    embed_steps = [
        {'name': 'Buy product', 'y': 7},
        {'name': 'Insurance offered\nat checkout', 'y': 5.5},
        {'name': 'One-click add', 'y': 4},
    ]
    for i, step in enumerate(embed_steps):
        ax.text(10.5, step['y'], step['name'], ha='center', fontsize=12, color='#44A044')
        if i < len(embed_steps) - 1:
            ax.annotate('', xy=(10.5, step['y']-0.8), xytext=(10.5, step['y']-0.3),
                       arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    # Examples
    examples = [
        {'platform': 'Tesla', 'insurance': 'Auto insurance at purchase', 'x': 2.5, 'y': 1.8},
        {'platform': 'Uber', 'insurance': 'Ride protection per trip', 'x': 7, 'y': 1.8},
        {'platform': 'Amazon', 'insurance': 'Product warranty extension', 'x': 11.5, 'y': 1.8},
    ]

    ax.text(7, 2.6, 'Examples:', fontsize=14, fontweight='bold', ha='center')
    for ex in examples:
        box = mpatches.FancyBboxPatch((ex['x']-1.8, ex['y']-0.6), 3.6, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(box)
        ax.text(ex['x'], ex['y']+0.2, ex['platform'], ha='center', fontsize=12, fontweight='bold')
        ax.text(ex['x'], ex['y']-0.2, ex['insurance'], ha='center', fontsize=10)

    # Market projection
    market = "Embedded Insurance Market: $70B (2024) | Projected: $720B by 2030 | CAGR: 35%"
    ax.text(7, 0.7, market, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: InsTech London, Simon-Kucher embedded insurance report (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'embedded_insurance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
