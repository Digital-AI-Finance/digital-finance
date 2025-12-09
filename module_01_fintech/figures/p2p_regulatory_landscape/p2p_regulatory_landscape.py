"""
P2P Regulatory Landscape
Shows global regulatory approaches to P2P lending

Output: p2p_regulatory_landscape.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P Regulatory Landscape',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_regulatory_landscape'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P regulatory landscape diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Lending Regulatory Landscape', fontsize=17, fontweight='bold', ha='center')

    # Regions
    regions = [
        {
            'name': 'United States',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'approach': 'SEC + State',
            'details': ['SEC securities registration', 'State lending licenses',
                       'CFPB consumer protection', 'Bank partnership model emerging'],
        },
        {
            'name': 'United Kingdom',
            'x': 6.5, 'y': 6.5,
            'color': '#44A044',
            'approach': 'FCA Regulated',
            'details': ['Full authorization required', 'Client money rules',
                       'Marketing restrictions', 'Investor appropriateness tests'],
        },
        {
            'name': 'European Union',
            'x': 10.8, 'y': 6.5,
            'color': '#FF7F0E',
            'approach': 'ECSP Regulation',
            'details': ['Harmonized framework (2022)', 'EUR 5M limit per project',
                       'Investor protection measures', 'Cross-border passporting'],
        },
        {
            'name': 'China',
            'x': 2.2, 'y': 2.5,
            'color': '#D62728',
            'approach': 'Banned (2020)',
            'details': ['Peak: 6,000+ platforms', 'Massive fraud/failures',
                       'All P2P lending banned', 'Shift to licensed microlenders'],
        },
        {
            'name': 'Asia-Pacific',
            'x': 10.8, 'y': 2.5,
            'color': '#6B5B95',
            'approach': 'Mixed',
            'details': ['Singapore: Licensed', 'Australia: Credit license',
                       'Indonesia: OJK regulated', 'India: NBFC framework'],
        },
    ]

    for region in regions:
        # Box
        box = mpatches.FancyBboxPatch((region['x']-1.8, region['y']-1.5), 3.6, 3.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=region['color'], alpha=0.15,
                                       edgecolor=region['color'], lw=2)
        ax.add_patch(box)
        ax.text(region['x'], region['y']+1.4, region['name'], ha='center',
               fontsize=12, fontweight='bold', color=region['color'])
        ax.text(region['x'], region['y']+0.9, f"({region['approach']})", ha='center',
               fontsize=10, color='#666666')

        for i, detail in enumerate(region['details']):
            ax.text(region['x'], region['y']+0.3-i*0.4, f'* {detail}', ha='center', fontsize=9)

    # Key trend
    trend = "Global Trend: Moving from self-regulation to formal licensing and capital requirements"
    ax.text(6.5, 0.5, trend, ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: FCA, SEC, PBOC, EU ECSP Regulation (2020/1503)',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_regulatory_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
