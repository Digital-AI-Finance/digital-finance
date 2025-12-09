"""
LendingClub Evolution
Shows the transformation of LendingClub from P2P to bank

Output: lendingclub_evolution.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'LendingClub Evolution',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/lendingclub_evolution'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create LendingClub evolution timeline"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'LendingClub Evolution: P2P to Bank', fontsize=17, fontweight='bold', ha='center')

    # Timeline
    timeline_y = 6
    ax.plot([0.5, 12.5], [timeline_y, timeline_y], color='#333333', lw=3)

    # Milestones
    milestones = [
        {'year': '2007', 'x': 1.5, 'event': 'Founded\n(Facebook app)', 'color': '#4A90E2'},
        {'year': '2008', 'x': 3, 'event': 'SEC\nregistration', 'color': '#4A90E2'},
        {'year': '2014', 'x': 5, 'event': 'IPO\n($9B valuation)', 'color': '#44A044'},
        {'year': '2016', 'x': 7, 'event': 'CEO scandal\nStock -50%', 'color': '#D62728'},
        {'year': '2020', 'x': 9, 'event': 'Acquired\nRadius Bank', 'color': '#FF7F0E'},
        {'year': '2021+', 'x': 11.5, 'event': 'Full bank\nmodel', 'color': '#6B5B95'},
    ]

    for m in milestones:
        # Circle on timeline
        circle = mpatches.Circle((m['x'], timeline_y), 0.3, facecolor=m['color'],
                                  edgecolor='#333333', lw=2, zorder=3)
        ax.add_patch(circle)

        # Year above
        ax.text(m['x'], timeline_y + 0.8, m['year'], ha='center', fontsize=11, fontweight='bold')

        # Event below
        ax.text(m['x'], timeline_y - 0.8, m['event'], ha='center', fontsize=10, va='top')

    # Business model transition boxes
    # P2P Era
    p2p_box = mpatches.FancyBboxPatch((0.5, 1.5), 5.5, 2.5, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=2)
    ax.add_patch(p2p_box)
    ax.text(3.25, 3.7, 'P2P Marketplace Era (2007-2020)', ha='center',
           fontsize=12, fontweight='bold', color='#4A90E2')
    ax.text(3.25, 3, 'Pure marketplace connecting borrowers/investors', ha='center', fontsize=10)
    ax.text(3.25, 2.4, 'Originated $60B+ in loans | Peak: 98% retail investors', ha='center', fontsize=10)

    # Bank Era
    bank_box = mpatches.FancyBboxPatch((7, 1.5), 5.5, 2.5, boxstyle='round,pad=0.1',
                                        facecolor='#6B5B95', alpha=0.15,
                                        edgecolor='#6B5B95', lw=2)
    ax.add_patch(bank_box)
    ax.text(9.75, 3.7, 'Digital Bank Era (2021+)', ha='center',
           fontsize=12, fontweight='bold', color='#6B5B95')
    ax.text(9.75, 3, 'Full-service digital bank with lending', ha='center', fontsize=10)
    ax.text(9.75, 2.4, 'Balance sheet lending | Lower cost of capital', ha='center', fontsize=10)

    # Arrow showing transition
    ax.annotate('', xy=(6.9, 2.75), xytext=(6.1, 2.75),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Source
    fig.text(0.5, 0.02, 'Source: LendingClub SEC filings, company announcements',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'lendingclub_evolution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
