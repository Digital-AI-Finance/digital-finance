"""
WealthTech Segments
Shows WealthTech market segmentation by customer type

Output: wealthtech_segments.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Segments',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wealthtech_segments'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create WealthTech segments by customer diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'WealthTech by Customer Segment', fontsize=20, fontweight='bold', ha='center')

    # Pyramid structure
    segments = [
        {
            'name': 'Ultra-High Net Worth (>USD 30M)',
            'y': 8, 'width': 4, 'color': '#4A90E2',
            'solutions': 'Family offices, private banking tech, alternative investments',
            'providers': 'Addepar, iCapital'
        },
        {
            'name': 'High Net Worth (USD 1-30M)',
            'y': 6.5, 'width': 7, 'color': '#44A044',
            'solutions': 'Hybrid advisory, tax optimization, estate planning',
            'providers': 'Vanguard Personal, Schwab'
        },
        {
            'name': 'Affluent (USD 100K-1M)',
            'y': 5, 'width': 9, 'color': '#FF7F0E',
            'solutions': 'Robo-advisors, digital planning, ETF portfolios',
            'providers': 'Betterment, Wealthfront'
        },
        {
            'name': 'Mass Market (<USD 100K)',
            'y': 3.5, 'width': 12, 'color': '#D62728',
            'solutions': 'Micro-investing, savings apps, commission-free trading',
            'providers': 'Robinhood, Acorns, Stash'
        },
    ]

    for seg in segments:
        # Trapezoid-like box
        box = mpatches.FancyBboxPatch((7-seg['width']/2, seg['y']-0.6), seg['width'], 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=seg['color'], alpha=0.2,
                                       edgecolor=seg['color'], lw=2)
        ax.add_patch(box)
        ax.text(7, seg['y']+0.3, seg['name'], ha='center',
               fontsize=12, fontweight='bold', color=seg['color'])
        ax.text(7, seg['y']-0.2, seg['solutions'], ha='center', fontsize=10)

    # Key insight
    insight = "WealthTech Democratization: Services once reserved for UHNW now available to all segments"
    ax.text(7, 2.2, insight, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Stats
    stats = "Mass Market Growth: 85% of new WealthTech users | USD 100K avg user growth rate: 25% YoY"
    ax.text(7, 1.4, stats, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[MARKET SEGMENTATION]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealthtech_segments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
