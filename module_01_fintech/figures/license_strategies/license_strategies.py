"""
Neobank License Strategies
Compares different regulatory approaches neobanks take

Output: license_strategies.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank License Strategies',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/license_strategies'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank license strategies comparison chart"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis('off')

    # Three strategy columns
    strategies = [
        {
            'title': 'Own Banking License',
            'x': 2,
            'color': '#333333',
            'examples': 'N26, Monzo, Starling',
            'pros': ['Full control', 'Direct deposits', 'Credit products', 'Higher trust'],
            'cons': ['High capital req.', 'Long approval', 'Regulatory burden', 'Expensive'],
            'timeline': '2-4 years',
            'cost': '$10-50M+'
        },
        {
            'title': 'E-Money License',
            'x': 6.5,
            'color': '#4A90E2',
            'examples': 'Revolut (EU), Wise',
            'pros': ['Faster approval', 'Lower capital', 'EU passporting', 'Payment focus'],
            'cons': ['No lending', 'No FDIC/FSCS', 'Deposit limits', 'Trust issues'],
            'timeline': '6-12 months',
            'cost': '$1-5M'
        },
        {
            'title': 'BaaS Partnership',
            'x': 11,
            'color': '#44A044',
            'examples': 'Chime, Current, Dave',
            'pros': ['Fast launch', 'Low cost', 'FDIC via partner', 'Focus on UX'],
            'cons': ['Revenue share', 'Less control', 'Partner risk', 'Scaling limits'],
            'timeline': '3-6 months',
            'cost': '$100K-1M'
        }
    ]

    for strat in strategies:
        x = strat['x']

        # Header box
        header = mpatches.FancyBboxPatch((x-1.5, 8), 3, 1.2,
                                          boxstyle='round,pad=0.05',
                                          facecolor=strat['color'], edgecolor='none')
        ax.add_patch(header)
        ax.text(x, 8.6, strat['title'], ha='center', va='center',
               fontsize=11, fontweight='bold', color='white')

        # Examples
        ax.text(x, 7.5, strat['examples'], ha='center', fontsize=8,
               style='italic', color='#666666')

        # Pros
        ax.text(x, 6.8, 'Advantages:', ha='center', fontsize=9, fontweight='bold',
               color='#44A044')
        for i, pro in enumerate(strat['pros']):
            ax.text(x, 6.4 - i*0.35, f'+ {pro}', ha='center', fontsize=8, color='#44A044')

        # Cons
        ax.text(x, 4.8, 'Disadvantages:', ha='center', fontsize=9, fontweight='bold',
               color='#D62728')
        for i, con in enumerate(strat['cons']):
            ax.text(x, 4.4 - i*0.35, f'- {con}', ha='center', fontsize=8, color='#D62728')

        # Metrics boxes
        metrics_box = mpatches.FancyBboxPatch((x-1.3, 1.5), 2.6, 1.3,
                                               boxstyle='round,pad=0.03',
                                               facecolor='#F5F5F5', edgecolor='#CCCCCC')
        ax.add_patch(metrics_box)
        ax.text(x, 2.5, f'Time: {strat["timeline"]}', ha='center', fontsize=8)
        ax.text(x, 2.1, f'Cost: {strat["cost"]}', ha='center', fontsize=8)

    # Arrows showing progression
    ax.annotate('', xy=(4.3, 5), xytext=(3.8, 5),
               arrowprops=dict(arrowstyle='->', color='#999999', lw=2))
    ax.annotate('', xy=(8.8, 5), xytext=(8.3, 5),
               arrowprops=dict(arrowstyle='->', color='#999999', lw=2))

    ax.text(4.05, 4.5, 'Less\nControl', ha='center', fontsize=7, color='#999999')
    ax.text(8.55, 4.5, 'Less\nControl', ha='center', fontsize=7, color='#999999')

    # Title
    ax.text(6.5, 9.7, 'Neobank Regulatory Strategies', fontsize=14, fontweight='bold', ha='center')

    # Note
    ax.text(6.5, 0.8, 'Note: Many neobanks start with BaaS/E-Money and later obtain full banking licenses',
           ha='center', fontsize=8, style='italic', color='#666666')

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)

    # Source
    fig.text(0.5, 0.02, 'Source: Regulatory filings, company announcements',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'license_strategies.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
