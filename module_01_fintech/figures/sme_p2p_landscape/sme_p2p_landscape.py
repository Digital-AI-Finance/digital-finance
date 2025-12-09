"""
SME P2P Lending Landscape
Shows P2P platforms focused on small business lending

Output: sme_p2p_landscape.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'SME P2P Lending Landscape',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/sme_p2p_landscape'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create SME P2P landscape diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'SME P2P Lending Landscape', fontsize=17, fontweight='bold', ha='center')

    # Loan types
    loan_types = [
        {
            'name': 'Invoice Finance',
            'x': 2, 'y': 6.5,
            'color': '#4A90E2',
            'desc': 'Advance on receivables',
            'players': ['Fundbox', 'BlueVine', 'MarketInvoice'],
            'terms': '30-90 days, 1-3% fee',
        },
        {
            'name': 'Term Loans',
            'x': 6.5, 'y': 6.5,
            'color': '#44A044',
            'desc': 'Fixed amount, fixed term',
            'players': ['Funding Circle', 'OnDeck', 'Kabbage'],
            'terms': '6-60 months, 10-30% APR',
        },
        {
            'name': 'Revenue-Based',
            'x': 11, 'y': 6.5,
            'color': '#FF7F0E',
            'desc': 'Repay as % of revenue',
            'players': ['Clearco', 'Pipe', 'Capchase'],
            'terms': 'Variable, 6-18% fee',
        },
    ]

    for lt in loan_types:
        # Box
        box = mpatches.FancyBboxPatch((lt['x']-1.6, lt['y']-1.8), 3.2, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=lt['color'], alpha=0.15,
                                       edgecolor=lt['color'], lw=2)
        ax.add_patch(box)
        ax.text(lt['x'], lt['y']+1.8, lt['name'], ha='center',
               fontsize=12, fontweight='bold', color=lt['color'])
        ax.text(lt['x'], lt['y']+1.2, lt['desc'], ha='center', fontsize=10)

        ax.text(lt['x'], lt['y']+0.5, 'Key Players:', ha='center', fontsize=9, fontweight='bold')
        for i, player in enumerate(lt['players']):
            ax.text(lt['x'], lt['y']-i*0.35, player, ha='center', fontsize=10)

        ax.text(lt['x'], lt['y']-1.4, lt['terms'], ha='center', fontsize=9,
               style='italic', color='#666666')

    # Market stats
    stats = """SME Online Lending Market:
    - Global: $100B+ annually
    - Growth: 15-20% CAGR
    - Fills $5T credit gap for SMEs
    Source: World Bank SME Finance Forum"""

    ax.text(6.5, 2.3, stats, ha='center', fontsize=10, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Value prop
    value = "Key Advantage: Faster decisions (minutes vs weeks) | Less documentation | Technology-driven underwriting"
    ax.text(6.5, 0.5, value, ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'sme_p2p_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
