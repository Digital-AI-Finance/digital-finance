"""
Open Banking Use Cases
Shows practical applications of open banking services

Output: open_banking_use_cases.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking Use Cases',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/open_banking_use_cases'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open banking use cases chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Open Banking Use Cases', fontsize=14, fontweight='bold', ha='center')

    # Use case categories (2x3 grid)
    use_cases = [
        {
            'title': 'Account Aggregation',
            'x': 2.2, 'y': 7,
            'color': '#4A90E2',
            'description': 'View all bank accounts\nin one app',
            'examples': ['Personal finance apps', 'Wealth dashboards', 'Business accounting'],
            'benefit': 'Single view of finances'
        },
        {
            'title': 'Payment Initiation',
            'x': 6.5, 'y': 7,
            'color': '#44A044',
            'description': 'Pay directly from\nbank account',
            'examples': ['E-commerce checkout', 'Bill payments', 'P2P transfers'],
            'benefit': 'Lower merchant fees'
        },
        {
            'title': 'Credit Decisioning',
            'x': 10.8, 'y': 7,
            'color': '#FF7F0E',
            'description': 'Real-time income &\nspending verification',
            'examples': ['Mortgage affordability', 'Loan applications', 'BNPL checks'],
            'benefit': 'Faster approvals'
        },
        {
            'title': 'Identity Verification',
            'x': 2.2, 'y': 3,
            'color': '#6B5B95',
            'description': 'Confirm identity via\nbank account ownership',
            'examples': ['Account opening', 'Age verification', 'KYC checks'],
            'benefit': 'Reduced fraud'
        },
        {
            'title': 'Recurring Payments',
            'x': 6.5, 'y': 3,
            'color': '#D62728',
            'description': 'Variable recurring\npayments (VRP)',
            'examples': ['Subscriptions', 'Sweeping savings', 'Utility bills'],
            'benefit': 'Flexible direct debits'
        },
        {
            'title': 'Embedded Finance',
            'x': 10.8, 'y': 3,
            'color': '#333333',
            'description': 'Banking in non-bank\nplatforms',
            'examples': ['In-app payments', 'Marketplace lending', 'Insurance offers'],
            'benefit': 'Contextual services'
        },
    ]

    for uc in use_cases:
        x, y = uc['x'], uc['y']

        # Main box
        box = mpatches.FancyBboxPatch((x-1.8, y-1.3), 3.6, 2.6,
                                       boxstyle='round,pad=0.05',
                                       facecolor='white', edgecolor=uc['color'], lw=2)
        ax.add_patch(box)

        # Color header
        header = mpatches.FancyBboxPatch((x-1.75, y+0.9), 3.5, 0.35,
                                          boxstyle='round,pad=0.02',
                                          facecolor=uc['color'], edgecolor='none')
        ax.add_patch(header)

        # Title
        ax.text(x, y+1.05, uc['title'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        # Description
        ax.text(x, y+0.45, uc['description'], ha='center', va='center',
               fontsize=8, color='#666666')

        # Examples
        examples_text = ', '.join(uc['examples'])
        ax.text(x, y-0.15, examples_text, ha='center', va='center',
               fontsize=7, style='italic', wrap=True)

        # Benefit badge
        ax.text(x, y-0.85, uc['benefit'], ha='center', va='center',
               fontsize=7, fontweight='bold', color=uc['color'],
               bbox=dict(boxstyle='round', facecolor=uc['color'], alpha=0.15))

    # Adoption statistics
    stats = """UK Open Banking Adoption (2024):
    - 7.5M+ active users
    - 11M+ payments monthly
    - 60+ regulated providers
    Source: OBIE"""

    ax.text(0.3, 0.5, stats, fontsize=7, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'open_banking_use_cases.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
