"""
Global FinTech Hubs
Shows major FinTech hubs worldwide

Output: global_fintech_hubs.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Global FinTech Hubs',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/global_fintech_hubs'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create global FinTech hubs diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Global FinTech Hubs', fontsize=20, fontweight='bold', ha='center')

    # Hubs
    hubs = [
        {
            'name': 'San Francisco',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'companies': 'Stripe, Plaid, Chime',
            'focus': 'Payments, infrastructure'
        },
        {
            'name': 'New York',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'companies': 'Betterment, Brex',
            'focus': 'WealthTech, B2B'
        },
        {
            'name': 'London',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'companies': 'Revolut, Monzo, Wise',
            'focus': 'Neobanks, FX'
        },
        {
            'name': 'Singapore',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'companies': 'Grab, Sea',
            'focus': 'Super apps, SEA'
        },
        {
            'name': 'China',
            'x': 2.2, 'y': 2.5,
            'color': '#D62728',
            'companies': 'Ant Group, WeBank',
            'focus': 'Mobile payments, lending'
        },
        {
            'name': 'India',
            'x': 5.5, 'y': 2.5,
            'color': '#333333',
            'companies': 'Paytm, PhonePe, Razorpay',
            'focus': 'UPI, digital payments'
        },
        {
            'name': 'Brazil',
            'x': 8.5, 'y': 2.5,
            'color': '#17BECF',
            'companies': 'Nubank, PicPay',
            'focus': 'Neobanks, Pix'
        },
        {
            'name': 'Berlin',
            'x': 11.8, 'y': 2.5,
            'color': '#E377C2',
            'companies': 'N26, Raisin, Trade Republic',
            'focus': 'Neobanks, investing'
        },
    ]

    for hub in hubs:
        box = mpatches.FancyBboxPatch((hub['x']-1.5, hub['y']-1.2), 3, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=hub['color'], alpha=0.15,
                                       edgecolor=hub['color'], lw=2)
        ax.add_patch(box)
        ax.text(hub['x'], hub['y']+0.9, hub['name'], ha='center',
               fontsize=12, fontweight='bold', color=hub['color'])
        ax.text(hub['x'], hub['y']+0.2, hub['companies'], ha='center', fontsize=9, style='italic')
        ax.text(hub['x'], hub['y']-0.4, hub['focus'], ha='center', fontsize=10)

    # Global ranking note
    ranking = "2024 Hub Ranking: 1. US 2. UK 3. Singapore 4. Hong Kong 5. Australia"
    ax.text(7, 0.8, ranking, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Global FinTech Rankings, Findexable (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'global_fintech_hubs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
