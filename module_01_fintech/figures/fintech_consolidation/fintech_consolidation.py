"""
FinTech Consolidation
Shows FinTech market consolidation trends

Output: fintech_consolidation.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Consolidation',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_consolidation'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech consolidation diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'FinTech Market Consolidation', fontsize=20, fontweight='bold', ha='center')

    # Consolidation phases
    phases = [
        {
            'name': 'Fragmentation\n(2015-2019)',
            'x': 2.5, 'y': 6,
            'color': '#4A90E2',
            'features': ['1000s of startups', 'Point solutions', 'Easy VC funding'],
        },
        {
            'name': 'Maturation\n(2020-2022)',
            'x': 7, 'y': 6,
            'color': '#FF7F0E',
            'features': ['Winners emerge', 'Horizontal expansion', 'IPO wave'],
        },
        {
            'name': 'Consolidation\n(2023+)',
            'x': 11.5, 'y': 6,
            'color': '#44A044',
            'features': ['M&A activity', 'Profitability focus', 'Platform plays'],
        },
    ]

    for phase in phases:
        box = mpatches.FancyBboxPatch((phase['x']-1.8, phase['y']-1.8), 3.6, 3.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=phase['color'], alpha=0.2,
                                       edgecolor=phase['color'], lw=2)
        ax.add_patch(box)
        ax.text(phase['x'], phase['y']+1.4, phase['name'], ha='center',
               fontsize=12, fontweight='bold', color=phase['color'])

        for i, feat in enumerate(phase['features']):
            ax.text(phase['x'], phase['y']+0.4-i*0.6, f'* {feat}', ha='center', fontsize=11)

    # Arrows
    ax.annotate('', xy=(4.7, 6), xytext=(4, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.annotate('', xy=(9.2, 6), xytext=(8.5, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Survivor characteristics
    survivors = """Consolidation Survivors:
    - Strong unit economics
    - Regulatory moats
    - Platform/ecosystem strategy
    - Institutional customers
    - Path to profitability"""

    ax.text(4, 2, survivors, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # At risk
    at_risk = """At-Risk Categories:
    - Cash-burning B2C
    - Single-product
    - Crowded markets
    - Regulatory arbitrage
    - No differentiation"""

    ax.text(10, 2, at_risk, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFEBEB', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, '[MARKET ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_consolidation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
