"""
Direct Indexing
Shows direct indexing concept vs ETFs

Output: direct_indexing.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Direct Indexing',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/direct_indexing'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create direct indexing comparison diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Direct Indexing vs Traditional ETFs', fontsize=20, fontweight='bold', ha='center')

    # ETF approach
    ax.text(3.5, 8.2, 'Traditional ETF', fontsize=16, fontweight='bold', ha='center', color='#4A90E2')
    etf_box = mpatches.FancyBboxPatch((1, 5), 5, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=2)
    ax.add_patch(etf_box)
    ax.text(3.5, 7.3, 'Buy ETF shares', ha='center', fontsize=12)
    ax.text(3.5, 6.7, 'Own fund, not stocks', ha='center', fontsize=12)
    ax.text(3.5, 6.1, 'Standard index exposure', ha='center', fontsize=12)
    ax.text(3.5, 5.5, 'Limited tax control', ha='center', fontsize=12)

    # Direct indexing approach
    ax.text(10.5, 8.2, 'Direct Indexing', fontsize=16, fontweight='bold', ha='center', color='#44A044')
    di_box = mpatches.FancyBboxPatch((8, 5), 5, 2.8,
                                      boxstyle='round,pad=0.1',
                                      facecolor='#44A044', alpha=0.15,
                                      edgecolor='#44A044', lw=2)
    ax.add_patch(di_box)
    ax.text(10.5, 7.3, 'Buy individual stocks', ha='center', fontsize=12)
    ax.text(10.5, 6.7, 'Own 500+ stocks directly', ha='center', fontsize=12)
    ax.text(10.5, 6.1, 'Customizable (ESG, sectors)', ha='center', fontsize=12)
    ax.text(10.5, 5.5, 'Tax-loss harvesting at stock level', ha='center', fontsize=12)

    # Benefits of direct indexing
    benefits = """Direct Indexing Benefits:
    - Tax alpha: 1-2%+ annual benefit
    - Personalization: Exclude stocks
    - ESG alignment
    - Factor tilts
    - No fund expenses"""

    ax.text(4, 2.5, benefits, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Providers
    providers = """Major Providers:
    - Parametric (Morgan Stanley)
    - Aperio (BlackRock)
    - Wealthfront Direct
    - Fidelity FidFolios
    - Schwab Personalized"""

    ax.text(10, 2.5, providers, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Market size
    market = "Direct Indexing AUM: USD 500B+ (2024) | Fastest growing wealth segment | CAGR: 20%+"
    ax.text(7, 0.8, market, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Cerulli Associates, Morgan Stanley research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'direct_indexing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
