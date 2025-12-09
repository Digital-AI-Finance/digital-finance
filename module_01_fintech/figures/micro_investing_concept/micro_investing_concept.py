"""
Micro-Investing Concept
Shows how micro-investing works

Output: micro_investing_concept.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Micro-Investing Concept',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/micro_investing_concept'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create micro-investing concept diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Micro-Investing: Invest Your Spare Change', fontsize=20, fontweight='bold', ha='center')

    # Process flow
    steps = [
        {'name': 'Purchase\nUSD 3.75', 'x': 2, 'y': 6, 'color': '#4A90E2'},
        {'name': 'Round-Up\nto USD 4.00', 'x': 5, 'y': 6, 'color': '#44A044'},
        {'name': 'USD 0.25\nto Invest', 'x': 8, 'y': 6, 'color': '#FF7F0E'},
        {'name': 'Auto-Invest\nin ETF Portfolio', 'x': 11, 'y': 6, 'color': '#6B5B95'},
    ]

    for i, step in enumerate(steps):
        box = mpatches.FancyBboxPatch((step['x']-1.3, step['y']-1.2), 2.6, 2.4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y'], step['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=step['color'])

        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-1.4, 6), xytext=(step['x']+1.4, 6),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Example calculation
    example = """Example Monthly Impact:
    - 30 purchases/month avg
    - USD 0.50 avg round-up
    - = USD 15/month invested
    - = USD 180/year + returns"""

    ax.text(4, 2.5, example, ha='center', fontsize=12, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Benefits
    benefits = """Why It Works:
    - Removes investment friction
    - Automatic saving habit
    - Fractional share access
    - Gamification elements
    - Low barrier to entry"""

    ax.text(10, 2.5, benefits, ha='center', fontsize=12, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Target audience
    target = "Target: Gen Z/Millennials | 70% of users are first-time investors"
    ax.text(7, 0.8, target, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL DIAGRAM]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'micro_investing_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
