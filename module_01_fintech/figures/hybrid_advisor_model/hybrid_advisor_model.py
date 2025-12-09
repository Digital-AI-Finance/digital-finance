"""
Hybrid Advisor Model
Shows the combination of robo and human advisory

Output: hybrid_advisor_model.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Hybrid Advisor Model',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/hybrid_advisor_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create hybrid advisor model diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Hybrid Advisory Model', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Combining Robo Efficiency with Human Expertise', fontsize=12, ha='center',
           style='italic', color='#666666')

    # Robo Component (left)
    robo_box = mpatches.FancyBboxPatch((0.5, 3.5), 4, 4.5, boxstyle='round,pad=0.1',
                                        facecolor='#4A90E2', alpha=0.2,
                                        edgecolor='#4A90E2', lw=2)
    ax.add_patch(robo_box)
    ax.text(2.5, 7.5, 'ROBO COMPONENT', ha='center', fontsize=13, fontweight='bold', color='#4A90E2')

    robo_tasks = [
        'Portfolio construction',
        'Automated rebalancing',
        'Tax-loss harvesting',
        'Performance reporting',
        'Account management',
    ]
    for i, task in enumerate(robo_tasks):
        ax.text(2.5, 6.8-i*0.7, f'* {task}', ha='center', fontsize=11)

    # Human Component (right)
    human_box = mpatches.FancyBboxPatch((9.5, 3.5), 4, 4.5, boxstyle='round,pad=0.1',
                                         facecolor='#44A044', alpha=0.2,
                                         edgecolor='#44A044', lw=2)
    ax.add_patch(human_box)
    ax.text(11.5, 7.5, 'HUMAN COMPONENT', ha='center', fontsize=13, fontweight='bold', color='#44A044')

    human_tasks = [
        'Financial planning',
        'Goal setting/review',
        'Complex tax strategy',
        'Estate planning',
        'Behavioral coaching',
    ]
    for i, task in enumerate(human_tasks):
        ax.text(11.5, 6.8-i*0.7, f'* {task}', ha='center', fontsize=11)

    # Combined value (center)
    combined = mpatches.FancyBboxPatch((5, 4.5), 4, 3, boxstyle='round,pad=0.1',
                                        facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(combined)
    ax.text(7, 6.5, 'HYBRID', ha='center', fontsize=14, fontweight='bold', color='white')
    ax.text(7, 5.8, 'VALUE', ha='center', fontsize=14, fontweight='bold', color='white')
    ax.text(7, 5, 'Best of both', ha='center', fontsize=11, color='white')

    # Arrows
    ax.annotate('', xy=(4.9, 6), xytext=(4.6, 6),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))
    ax.annotate('', xy=(9.4, 6), xytext=(9.1, 6),
               arrowprops=dict(arrowstyle='<-', color='#44A044', lw=2))

    # Pricing comparison
    pricing = """Typical Hybrid Pricing:
    Betterment Premium: 0.40% + CFP access
    Vanguard Personal: 0.30% + advisors
    Schwab Intelligent: 0% + $300 planning fee
    Personal Capital: 0.89% (full service)"""

    ax.text(7, 2.5, pricing, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Company pricing pages (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'hybrid_advisor_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
