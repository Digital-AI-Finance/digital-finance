"""
Emerging Market FinTech
Shows FinTech in emerging markets

Output: emerging_market_fintech.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Emerging Market FinTech',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/emerging_market_fintech'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create emerging market FinTech diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'FinTech in Emerging Markets', fontsize=20, fontweight='bold', ha='center')

    # Regions
    regions = [
        {
            'name': 'India',
            'x': 2.2, 'y': 6.5,
            'color': '#FF7F0E',
            'highlight': 'UPI: 10B+ monthly txns',
            'players': 'PhonePe, Paytm, Razorpay'
        },
        {
            'name': 'Brazil',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'highlight': 'Nubank: 100M+ customers',
            'players': 'Nubank, PicPay, Inter'
        },
        {
            'name': 'Indonesia',
            'x': 8.5, 'y': 6.5,
            'color': '#4A90E2',
            'highlight': 'Super apps dominant',
            'players': 'Gojek, Dana, OVO'
        },
        {
            'name': 'Africa',
            'x': 11.8, 'y': 6.5,
            'color': '#D62728',
            'highlight': 'M-Pesa model spreads',
            'players': 'Flutterwave, Chipper, Wave'
        },
        {
            'name': 'MENA',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'highlight': 'Saudi/UAE digital push',
            'players': 'Tabby, STC Pay, Tamara'
        },
        {
            'name': 'LATAM',
            'x': 9.25, 'y': 2.5,
            'color': '#17BECF',
            'highlight': 'Pix/SPEI rails',
            'players': 'Clip, Ualá, Kushki'
        },
    ]

    for region in regions:
        box = mpatches.FancyBboxPatch((region['x']-1.5, region['y']-1.2), 3, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=region['color'], alpha=0.15,
                                       edgecolor=region['color'], lw=2)
        ax.add_patch(box)
        ax.text(region['x'], region['y']+0.9, region['name'], ha='center',
               fontsize=13, fontweight='bold', color=region['color'])
        ax.text(region['x'], region['y']+0.2, region['highlight'], ha='center',
               fontsize=10, fontweight='bold')
        ax.text(region['x'], region['y']-0.4, region['players'], ha='center',
               fontsize=9, style='italic')

    # Key insight
    insight = "Opportunity: 1.4B unbanked | Mobile-first | Leapfrogging legacy infrastructure"
    ax.text(7, 0.8, insight, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: World Bank, Bain/Google EM fintech reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'emerging_market_fintech.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
