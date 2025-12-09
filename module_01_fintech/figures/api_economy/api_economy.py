"""
API Economy
Shows the financial services API economy

Output: api_economy.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'API Economy',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/api_economy'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create API economy diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The Financial Services API Economy', fontsize=20, fontweight='bold', ha='center')

    # API categories
    categories = [
        {
            'name': 'Account\nData',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'providers': 'Plaid, Yodlee, MX',
            'use': 'Aggregation, verification'
        },
        {
            'name': 'Payments',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'providers': 'Stripe, Adyen, Dwolla',
            'use': 'ACH, cards, instant'
        },
        {
            'name': 'Lending',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'providers': 'Blend, Upstart API',
            'use': 'Origination, decisioning'
        },
        {
            'name': 'Identity',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'providers': 'Persona, Socure',
            'use': 'KYC, fraud prevention'
        },
        {
            'name': 'Card\nIssuing',
            'x': 4.75, 'y': 2.5,
            'color': '#D62728',
            'providers': 'Marqeta, Galileo',
            'use': 'Virtual/physical cards'
        },
        {
            'name': 'Banking\nCore',
            'x': 9.25, 'y': 2.5,
            'color': '#333333',
            'providers': 'Unit, Synapse, Bond',
            'use': 'Accounts, ledger'
        },
    ]

    for cat in categories:
        box = mpatches.FancyBboxPatch((cat['x']-1.5, cat['y']-1.2), 3, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(cat['x'], cat['y']+0.9, cat['name'], ha='center',
               fontsize=12, fontweight='bold', color=cat['color'])
        ax.text(cat['x'], cat['y']+0.1, cat['providers'], ha='center', fontsize=10, style='italic')
        ax.text(cat['x'], cat['y']-0.5, cat['use'], ha='center', fontsize=10)

    # API-first benefits
    benefits = "API Economy: Build financial products in weeks not years | USD 50B+ API fintech market by 2027"
    ax.text(7, 0.8, benefits, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: RapidAPI, Plaid, industry reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'api_economy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
