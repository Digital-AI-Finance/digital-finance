"""
Open Finance Scope Evolution
Shows evolution from open banking to open finance to open data

Output: open_finance_scope.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Finance Scope Evolution',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/open_finance_scope'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open finance scope evolution chart"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'From Open Banking to Open Data',
           fontsize=14, fontweight='bold', ha='center')

    # Three concentric stages
    # Open Banking (innermost)
    ob_rect = mpatches.FancyBboxPatch((3.5, 3.5), 6, 4, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.3, edgecolor='#4A90E2', lw=2)
    ax.add_patch(ob_rect)

    # Open Finance (middle)
    of_rect = mpatches.FancyBboxPatch((2, 2.2), 9, 5.6, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.2, edgecolor='#44A044', lw=2)
    ax.add_patch(of_rect)

    # Open Data (outermost)
    od_rect = mpatches.FancyBboxPatch((0.5, 0.8), 12, 7.5, boxstyle='round,pad=0.1',
                                       facecolor='#FF7F0E', alpha=0.1, edgecolor='#FF7F0E', lw=2)
    ax.add_patch(od_rect)

    # Labels for each layer
    ax.text(6.5, 7.2, 'OPEN BANKING', fontsize=12, fontweight='bold',
           ha='center', color='#4A90E2')
    ax.text(6.5, 6.6, 'Payment accounts | Transactions | Payments',
           fontsize=9, ha='center', color='#4A90E2')

    ax.text(2.3, 7.3, 'OPEN FINANCE', fontsize=11, fontweight='bold',
           ha='left', color='#44A044', rotation=90)

    ax.text(0.8, 8, 'OPEN DATA', fontsize=11, fontweight='bold',
           ha='left', color='#FF7F0E', rotation=90)

    # Contents within each layer
    # Open Banking core
    ob_items = ['Current accounts', 'Savings accounts', 'Transaction data', 'Payment initiation']
    for i, item in enumerate(ob_items):
        ax.text(6.5, 5.8 - i*0.5, f'* {item}', fontsize=8, ha='center', color='#333333')

    # Open Finance additions (sides)
    of_left = ['Mortgages', 'Loans', 'Insurance', 'Pensions']
    of_right = ['Investments', 'Credit cards', 'Consumer credit', 'SME finance']

    for i, item in enumerate(of_left):
        ax.text(2.5, 6.5 - i*0.6, f'* {item}', fontsize=8, ha='left', color='#333333')

    for i, item in enumerate(of_right):
        ax.text(10.5, 6.5 - i*0.6, f'* {item}', fontsize=8, ha='right', color='#333333')

    # Open Data additions (corners)
    od_items = [
        (1.2, 2.5, 'Utilities'),
        (1.2, 2, 'Telecoms'),
        (1.2, 1.5, 'Government'),
        (11.8, 2.5, 'Healthcare'),
        (11.8, 2, 'Education'),
        (11.8, 1.5, 'Smart data'),
    ]

    for x, y, item in od_items:
        ax.text(x, y, f'* {item}', fontsize=8, ha='left' if x < 6 else 'right', color='#333333')

    # Timeline at bottom
    ax.annotate('', xy=(11.5, 0.5), xytext=(1.5, 0.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    timeline = [
        (2, 0.2, '2018', 'PSD2'),
        (5, 0.2, '2024', 'Open Finance'),
        (8.5, 0.2, '2027+', 'Open Data'),
    ]

    for x, y, year, label in timeline:
        ax.plot(x, 0.5, 'o', color='#333333', markersize=8)
        ax.text(x, y, f'{year}\n{label}', fontsize=8, ha='center', fontweight='bold')

    # Jurisdictions pursuing open finance
    jurisdictions = """Jurisdictions Moving to Open Finance:
    - Brazil: Full open finance since 2022
    - Australia: CDR expanding sectors
    - UK: Open finance roadmap
    - EU: FIDA proposal (2023)"""

    ax.text(12.5, 4, jurisdictions, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Regulatory announcements, OECD frameworks',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'open_finance_scope.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
