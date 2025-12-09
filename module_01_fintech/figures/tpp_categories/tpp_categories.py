"""
Third Party Provider Categories
Shows the different types of TPPs under PSD2 regulation

Output: tpp_categories.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Third Party Provider Categories',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/tpp_categories'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create TPP categories chart"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Third Party Provider (TPP) Categories',
           fontsize=14, fontweight='bold', ha='center')

    # Three main TPP types
    tpp_types = [
        {
            'name': 'AISP',
            'full': 'Account Information\nService Provider',
            'x': 2.2,
            'color': '#4A90E2',
            'access': 'Read-only',
            'services': ['Account aggregation', 'Personal finance mgmt',
                        'Credit scoring', 'Accounting integration'],
            'examples': 'Plaid, TrueLayer, Tink'
        },
        {
            'name': 'PISP',
            'full': 'Payment Initiation\nService Provider',
            'x': 6.5,
            'color': '#44A044',
            'access': 'Write (payments)',
            'services': ['Payment initiation', 'E-commerce checkout',
                        'Bill payments', 'Account transfers'],
            'examples': 'Trustly, GoCardless, Volt'
        },
        {
            'name': 'CBPII',
            'full': 'Card-Based Payment\nInstrument Issuer',
            'x': 10.8,
            'color': '#FF7F0E',
            'access': 'Balance confirmation',
            'services': ['Virtual cards', 'Card issuance',
                        'Balance verification', 'Funds availability'],
            'examples': 'Curve, Revolut (card issuing)'
        }
    ]

    for tpp in tpp_types:
        x = tpp['x']

        # Header circle
        circle = mpatches.Circle((x, 7.5), 0.8, facecolor=tpp['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)
        ax.text(x, 7.5, tpp['name'], ha='center', va='center', fontsize=12,
               fontweight='bold', color='white')

        # Full name
        ax.text(x, 6.3, tpp['full'], ha='center', va='center', fontsize=9,
               color='#666666')

        # Access type badge
        badge = mpatches.FancyBboxPatch((x-0.8, 5.5), 1.6, 0.5, boxstyle='round,pad=0.02',
                                         facecolor=tpp['color'], alpha=0.3, edgecolor=tpp['color'])
        ax.add_patch(badge)
        ax.text(x, 5.75, tpp['access'], ha='center', va='center', fontsize=8,
               fontweight='bold', color=tpp['color'])

        # Services box
        services_text = '\n'.join([f'* {s}' for s in tpp['services']])
        ax.text(x, 4.8, services_text, ha='center', va='top', fontsize=8,
               bbox=dict(boxstyle='round', facecolor='#F9F9F9', edgecolor='#CCCCCC'))

        # Examples
        ax.text(x, 1.8, f"Examples:\n{tpp['examples']}", ha='center', va='top',
               fontsize=7, style='italic', color='#666666')

    # Registration requirements box
    requirements = """TPP Registration Requirements:
    - Authorized by national competent authority
    - Listed in EBA registers
    - Must have professional indemnity insurance
    - eIDAS certificates for API access"""

    ax.text(6.5, 0.5, requirements, fontsize=8, ha='center', va='bottom',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Combination note
    ax.text(6.5, 8.7, 'Note: A single provider can register for multiple TPP categories',
           fontsize=8, ha='center', style='italic', color='#666666')

    # Source
    fig.text(0.5, 0.02, 'Source: PSD2 (EU 2015/2366), EBA Register',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'tpp_categories.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
