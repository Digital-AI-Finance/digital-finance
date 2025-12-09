"""
M-Pesa Ecosystem Diagram
Shows the components and participants in the M-Pesa mobile money ecosystem

Output: mpesa_ecosystem.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'M-Pesa Mobile Money Ecosystem',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/mpesa_ecosystem'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create M-Pesa ecosystem diagram"""
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Center - M-Pesa
    center = mpatches.Circle((5.5, 4), 1.2, facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(center)
    ax.text(5.5, 4, 'M-PESA\nPlatform', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    # Surrounding nodes
    nodes = [
        (2, 6.5, 'Mobile\nUsers', '#44A044'),
        (9, 6.5, 'Agent\nNetwork', '#FF7F0E'),
        (1.5, 4, 'Banks', '#6B5B95'),
        (9.5, 4, 'Merchants', '#D62728'),
        (2, 1.5, 'Utilities &\nBills', '#17BECF'),
        (9, 1.5, 'Government\nServices', '#999999'),
        (5.5, 7.2, 'Safaricom\n(MNO)', '#333333'),
        (5.5, 0.8, 'Central\nBank', '#333333'),
    ]

    for x, y, label, color in nodes:
        circle = mpatches.Circle((x, y), 0.9, facecolor=color,
                                  edgecolor='#333333', lw=1.5, alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
               fontweight='bold', color='white')

    # Draw connections
    for x, y, _, _ in nodes:
        ax.plot([5.5, x], [4, y], 'k-', lw=1, alpha=0.3, zorder=0)

    # Statistics box
    stats = """Key Statistics (2023):
    - 50+ million users in Kenya
    - 600,000+ agent locations
    - $300B+ annual transactions
    - Available in 7 countries"""

    ax.text(5.5, -0.5, stats, fontsize=8, ha='center', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Services offered
    services_left = ['Person-to-Person\nTransfers', 'Bill Payments',
                     'Savings (M-Shwari)', 'Loans (Fuliza)']
    services_right = ['International\nRemittances', 'Business\nPayments',
                      'Salary\nDisbursements', 'Mobile\nBanking']

    for i, svc in enumerate(services_left):
        ax.text(0.3, 6.5 - i*1.3, f'• {svc}', fontsize=7, va='top')

    for i, svc in enumerate(services_right):
        ax.text(10.7, 6.5 - i*1.3, f'• {svc}', fontsize=7, va='top', ha='right')

    # Title
    ax.text(5.5, 8.3, 'M-Pesa Mobile Money Ecosystem',
           fontsize=14, fontweight='bold', ha='center')

    # Synthetic label
    ax.text(10.8, -0.8, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mpesa_ecosystem.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
