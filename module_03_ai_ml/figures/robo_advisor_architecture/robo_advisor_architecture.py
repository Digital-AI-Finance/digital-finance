"""
Robo-Advisor Architecture
ML components in automated investment

Output: robo_advisor_architecture.pdf
Module: module_03_ai_ml
Lesson: 33 - Robo-Advisors ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Robo Advisor Architecture',
    'module': 'module_03_ai_ml',
    'lesson': 33,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/robo_advisor_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)

    # Core components
    components = [
        # Client layer
        (3, 8.5, 'Client Onboarding', '#4A90E2', 2.5, 1),
        (8, 8.5, 'Risk Profiling', '#4A90E2', 2.5, 1),
        (13, 8.5, 'Goal Setting', '#4A90E2', 2.5, 1),

        # ML Engine layer
        (5.5, 6, 'Portfolio\nOptimization\n(Mean-Variance)', '#44A044', 3, 1.5),
        (10.5, 6, 'Asset\nAllocation\nModel', '#44A044', 3, 1.5),

        # Execution layer
        (3, 3, 'Trade\nExecution', '#FF7F0E', 2.5, 1.2),
        (8, 3, 'Tax-Loss\nHarvesting', '#FF7F0E', 2.5, 1.2),
        (13, 3, 'Rebalancing\nEngine', '#FF7F0E', 2.5, 1.2),

        # Data layer
        (8, 0.8, 'Market Data & Analytics', '#9B59B6', 8, 1),
    ]

    for x, y, label, color, w, h in components:
        rect = mpatches.FancyBboxPatch((x-w/2, y-h/2), w, h,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')

    # Layer labels
    ax.text(0.5, 8.5, 'Client\nLayer', fontsize=10, fontweight='bold', va='center')
    ax.text(0.5, 6, 'ML\nEngine', fontsize=10, fontweight='bold', va='center')
    ax.text(0.5, 3, 'Execution\nLayer', fontsize=10, fontweight='bold', va='center')
    ax.text(0.5, 0.8, 'Data\nLayer', fontsize=10, fontweight='bold', va='center')

    # Arrows
    arrows = [
        ((3, 7.9), (5, 6.8)),
        ((8, 7.9), (5.5, 6.8)),
        ((8, 7.9), (10.5, 6.8)),
        ((13, 7.9), (11, 6.8)),
        ((5.5, 5.2), (3, 3.7)),
        ((5.5, 5.2), (8, 3.7)),
        ((10.5, 5.2), (8, 3.7)),
        ((10.5, 5.2), (13, 3.7)),
        ((8, 1.8), (5.5, 5.2)),
        ((8, 1.8), (10.5, 5.2)),
    ]

    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    ax.set_title('Robo-Advisor ML Architecture', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'robo_advisor_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
