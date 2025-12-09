"""
Incumbent Robo Offerings
Shows traditional firms' robo-advisory products

Output: incumbent_robo_offerings.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Incumbent Robo Offerings',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/incumbent_robo_offerings'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create incumbent robo offerings comparison"""
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'Traditional Firms: Robo-Advisory Products', fontsize=20, fontweight='bold', ha='center')

    # Firms data
    firms = [
        {'name': 'Vanguard Digital', 'fee': '0.20%', 'min': '$3K', 'aum': '$350B+', 'x': 2},
        {'name': 'Schwab Intelligent', 'fee': '0%*', 'min': '$5K', 'aum': '$80B+', 'x': 5},
        {'name': 'Fidelity Go', 'fee': '0%**', 'min': '$0', 'aum': '$20B+', 'x': 8},
        {'name': 'Merrill Edge', 'fee': '0.45%', 'min': '$1K', 'aum': '$10B+', 'x': 11},
    ]

    for firm in firms:
        # Box
        box = mpatches.FancyBboxPatch((firm['x']-1.3, 4.5), 2.6, 4, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=2)
        ax.add_patch(box)
        ax.text(firm['x'], 8.1, firm['name'], ha='center', fontsize=11, fontweight='bold')
        ax.text(firm['x'], 7.3, f"Fee: {firm['fee']}", ha='center', fontsize=12, fontweight='bold', color='#44A044')
        ax.text(firm['x'], 6.6, f"Min: {firm['min']}", ha='center', fontsize=11)
        ax.text(firm['x'], 5.9, f"AUM: {firm['aum']}", ha='center', fontsize=11)

    # Notes
    notes = """* Schwab: No advisory fee, but holds cash allocation (earns interest spread)
    ** Fidelity: Free under $25K, then 0.35%"""

    ax.text(6.5, 3.8, notes, ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Key insight
    insight = """Incumbent Advantage: Existing customer base, brand trust, cross-sell opportunities
    Challenge: Legacy systems, advisor channel conflict, lower margins"""

    ax.text(6.5, 2, insight, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Company websites, SEC filings (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'incumbent_robo_offerings.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
