"""
FinTech Sustainability
Shows sustainable/green FinTech trends

Output: fintech_sustainability.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Sustainability',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_sustainability'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech sustainability diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Sustainable FinTech / Green Finance', fontsize=20, fontweight='bold', ha='center')

    # Categories
    categories = [
        {
            'name': 'Green\nInvesting',
            'x': 2.2, 'y': 6.5,
            'color': '#44A044',
            'examples': ['ESG portfolios', 'Impact investing', 'Carbon credits'],
            'players': 'Clim8, Aspiration'
        },
        {
            'name': 'Carbon\nTracking',
            'x': 5.5, 'y': 6.5,
            'color': '#4A90E2',
            'examples': ['Spending footprint', 'Offset purchases', 'Eco rewards'],
            'players': 'Doconomy, Cogo'
        },
        {
            'name': 'Green\nLending',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'examples': ['Solar financing', 'EV loans', 'Green mortgages'],
            'players': 'Mosaic, GoodLeap'
        },
        {
            'name': 'Sustainable\nBanking',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'examples': ['Ethical deposits', 'Tree planting', 'No fossil fuel'],
            'players': 'Tomorrow, Aspiration'
        },
    ]

    for cat in categories:
        box = mpatches.FancyBboxPatch((cat['x']-1.5, cat['y']-1.5), 3, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(cat['x'], cat['y']+1.2, cat['name'], ha='center',
               fontsize=12, fontweight='bold', color=cat['color'])

        for i, ex in enumerate(cat['examples']):
            ax.text(cat['x'], cat['y']+0.4-i*0.4, f'* {ex}', ha='center', fontsize=10)

        ax.text(cat['x'], cat['y']-1.1, cat['players'], ha='center',
               fontsize=9, style='italic', color='#666666')

    # Market stats
    stats = """Green FinTech Growth:
    - ESG assets: USD 50T+ globally
    - Sustainable bond issuance: USD 1T+ (2024)
    - Carbon market: USD 100B+
    - Gen Z: 2x more likely to choose sustainable option"""

    ax.text(7, 2.5, stats, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Bloomberg NEF, MSCI ESG research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_sustainability.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
