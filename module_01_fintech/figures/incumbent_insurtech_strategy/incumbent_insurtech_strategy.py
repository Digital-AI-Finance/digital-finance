"""
Incumbent InsurTech Strategy
Shows how traditional insurers respond to InsurTech

Output: incumbent_insurtech_strategy.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Incumbent InsurTech Strategy',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/incumbent_insurtech_strategy'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create incumbent InsurTech strategy diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Incumbent Response to InsurTech Disruption', fontsize=20, fontweight='bold', ha='center')

    # Strategies
    strategies = [
        {
            'name': 'Build',
            'x': 2, 'y': 6,
            'color': '#4A90E2',
            'desc': 'Internal digital\ntransformation',
            'examples': 'Allianz Direct,\nAXA digital units'
        },
        {
            'name': 'Partner',
            'x': 5, 'y': 6,
            'color': '#44A044',
            'desc': 'API & distribution\nagreements',
            'examples': 'Munich Re + Next,\nSwiss Re + Lemonade'
        },
        {
            'name': 'Invest',
            'x': 8, 'y': 6,
            'color': '#FF7F0E',
            'desc': 'VC arms & strategic\ninvestments',
            'examples': 'AXA Venture,\nMassMutual Ventures'
        },
        {
            'name': 'Acquire',
            'x': 11, 'y': 6,
            'color': '#6B5B95',
            'desc': 'Buy InsurTech\ncompanies',
            'examples': 'Hartford + Navigators,\nChubb acquisitions'
        },
    ]

    for strat in strategies:
        # Box
        box = mpatches.FancyBboxPatch((strat['x']-1.4, strat['y']-2), 2.8, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=strat['color'], alpha=0.2,
                                       edgecolor=strat['color'], lw=2)
        ax.add_patch(box)
        ax.text(strat['x'], strat['y']+1.5, strat['name'], ha='center',
               fontsize=15, fontweight='bold', color=strat['color'])
        ax.text(strat['x'], strat['y']+0.5, strat['desc'], ha='center', fontsize=11, va='center')
        ax.text(strat['x'], strat['y']-1, strat['examples'], ha='center', fontsize=10,
               style='italic', va='center')

    # Key stats
    stats = """Incumbent Digital Investment (2024):
    - Global insurers spent $15B+ on digital transformation
    - 70% have dedicated innovation labs
    - 50%+ use AI in claims processing
    - Average IT spend: 3-5% of premiums"""

    ax.text(7, 1.8, stats, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Deloitte Insurance Outlook, Accenture Insurance Technology (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'incumbent_insurtech_strategy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
