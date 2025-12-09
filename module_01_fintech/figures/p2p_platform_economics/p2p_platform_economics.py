"""
P2P Platform Economics
Shows the unit economics of P2P lending platforms

Output: p2p_platform_economics.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P Platform Economics',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_platform_economics'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P platform economics diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Platform Unit Economics', fontsize=17, fontweight='bold', ha='center')
    ax.text(6.5, 8.7, '(Per $10,000 loan originated)', fontsize=12, ha='center',
           style='italic', color='#666666')

    # Revenue side (left)
    rev_box = mpatches.FancyBboxPatch((0.5, 3), 5.5, 5, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.15,
                                       edgecolor='#44A044', lw=2)
    ax.add_patch(rev_box)
    ax.text(3.25, 7.5, 'REVENUE', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    revenues = [
        ('Origination fee', '3-5%', '$300-500'),
        ('Servicing fee', '1% annually', '$100/year'),
        ('Late fees', 'Variable', '$20-50'),
        ('Investor fees', '0-1%', '$0-100'),
    ]
    for i, (item, rate, amount) in enumerate(revenues):
        ax.text(0.8, 6.8-i*0.8, f'{item}:', fontsize=11, fontweight='bold')
        ax.text(3, 6.8-i*0.8, rate, fontsize=11)
        ax.text(5.2, 6.8-i*0.8, amount, fontsize=11, color='#44A044')

    ax.text(3.25, 3.6, 'Total Revenue: $420-750', ha='center', fontsize=12, fontweight='bold',
           color='#44A044')

    # Cost side (right)
    cost_box = mpatches.FancyBboxPatch((7, 3), 5.5, 5, boxstyle='round,pad=0.1',
                                        facecolor='#D62728', alpha=0.15,
                                        edgecolor='#D62728', lw=2)
    ax.add_patch(cost_box)
    ax.text(9.75, 7.5, 'COSTS', ha='center', fontsize=14, fontweight='bold', color='#D62728')

    costs = [
        ('Customer acquisition', '-', '$150-300'),
        ('Credit underwriting', '-', '$30-50'),
        ('Servicing costs', '-', '$50-100'),
        ('Default losses', '3-8%', '$300-800'),
    ]
    for i, (item, rate, amount) in enumerate(costs):
        ax.text(7.3, 6.8-i*0.8, f'{item}:', fontsize=11, fontweight='bold')
        ax.text(9.5, 6.8-i*0.8, rate, fontsize=11)
        ax.text(11.7, 6.8-i*0.8, amount, fontsize=11, color='#D62728')

    ax.text(9.75, 3.6, 'Total Costs: $530-1,250', ha='center', fontsize=12, fontweight='bold',
           color='#D62728')

    # Margin analysis
    margin = """Margin Analysis:
    Break-even requires: Low CAC + Low defaults + Scale
    Profitable loans: Prime borrowers, repeat customers
    Challenging: Subprime, high marketing spend"""

    ax.text(6.5, 1.8, margin, ha='center', fontsize=10, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: Industry analysis, LendingClub/Prosper disclosures [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_platform_economics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
