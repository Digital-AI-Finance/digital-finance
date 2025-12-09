"""
Incumbent WealthTech Response
Shows how traditional firms respond to WealthTech

Output: incumbent_wealthtech_response.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Incumbent WealthTech Response',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/incumbent_wealthtech_response'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create incumbent WealthTech response diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Traditional Firms: WealthTech Response', fontsize=20, fontweight='bold', ha='center')

    # Response strategies
    strategies = [
        {
            'name': 'Schwab',
            'x': 2.5, 'y': 6,
            'color': '#4A90E2',
            'response': 'Zero commissions (2019)\nSchwab Intelligent\nSlices (fractional)',
        },
        {
            'name': 'Fidelity',
            'x': 5.5, 'y': 6,
            'color': '#44A044',
            'response': 'Zero commissions\nYouth accounts\nFidelity Go robo',
        },
        {
            'name': 'Vanguard',
            'x': 8.5, 'y': 6,
            'color': '#FF7F0E',
            'response': 'Digital Advisor\nLower minimums\nMobile app upgrade',
        },
        {
            'name': 'Morgan Stanley',
            'x': 11.5, 'y': 6,
            'color': '#6B5B95',
            'response': 'E*TRADE acquisition\nMorgan Stanley Access\nDirect indexing',
        },
    ]

    for strat in strategies:
        box = mpatches.FancyBboxPatch((strat['x']-1.5, strat['y']-1.8), 3, 3.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=strat['color'], alpha=0.2,
                                       edgecolor=strat['color'], lw=2)
        ax.add_patch(box)
        ax.text(strat['x'], strat['y']+1.3, strat['name'], ha='center',
               fontsize=14, fontweight='bold', color=strat['color'])
        ax.text(strat['x'], strat['y']-0.2, strat['response'], ha='center', fontsize=10)

    # Common strategies
    common = """Common Incumbent Strategies:
    - Commission elimination (race to zero)
    - Mobile app modernization
    - Robo-advisor launches
    - Acquisitions (E*TRADE, TD Ameritrade)
    - Lower account minimums"""

    ax.text(4, 2, common, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Advantages
    advantages = """Incumbent Advantages:
    - Existing customer base
    - Brand trust
    - Regulatory expertise
    - Full product suite
    - Scale economics"""

    ax.text(10, 2, advantages, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Company announcements, investor presentations (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'incumbent_wealthtech_response.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
