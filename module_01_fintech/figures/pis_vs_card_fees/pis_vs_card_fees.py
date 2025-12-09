"""
PIS vs Card Payment Fees Comparison
Compares costs of payment initiation vs card payments

Output: pis_vs_card_fees.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'PIS vs Card Payment Fees',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/pis_vs_card_fees'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create PIS vs card fees comparison chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Fee comparison bar chart
    payment_types = ['Credit\nCard', 'Debit\nCard', 'Open Banking\n(PIS)', 'Direct\nDebit']

    # Fee components (percentage of transaction)
    interchange = [1.8, 0.2, 0, 0]
    scheme_fees = [0.3, 0.15, 0, 0]
    acquirer_margin = [0.4, 0.3, 0, 0]
    pis_fee = [0, 0, 0.3, 0.2]

    x = np.arange(len(payment_types))
    width = 0.6

    ax1.bar(x, interchange, width, label='Interchange', color='#D62728')
    ax1.bar(x, scheme_fees, width, bottom=interchange, label='Scheme fees', color='#FF7F0E')
    ax1.bar(x, acquirer_margin, width, bottom=np.array(interchange)+np.array(scheme_fees),
           label='Acquirer margin', color='#4A90E2')
    ax1.bar(x, pis_fee, width, bottom=np.array(interchange)+np.array(scheme_fees)+np.array(acquirer_margin),
           label='Provider fee', color='#44A044')

    ax1.set_ylabel('Total Fee (%)', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(payment_types, fontsize=9)
    ax1.set_ylim(0, 3)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_title('Payment Method Fee Comparison', fontsize=12, fontweight='bold', pad=10)

    # Add total labels
    totals = [2.5, 0.65, 0.3, 0.2]
    for i, total in enumerate(totals):
        ax1.text(i, total + 0.1, f'{total}%', ha='center', fontsize=9, fontweight='bold')

    ax1.yaxis.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Right: Savings analysis
    transaction_values = [50, 100, 200, 500, 1000]
    card_fees = [t * 0.025 for t in transaction_values]  # 2.5%
    pis_fees = [t * 0.003 for t in transaction_values]   # 0.3%
    savings = [c - p for c, p in zip(card_fees, pis_fees)]

    x2 = np.arange(len(transaction_values))
    width2 = 0.35

    ax2.bar(x2 - width2/2, card_fees, width2, label='Card (2.5%)', color='#D62728')
    ax2.bar(x2 + width2/2, pis_fees, width2, label='PIS (0.3%)', color='#44A044')

    # Add savings line
    ax2_twin = ax2.twinx()
    ax2_twin.plot(x2, savings, 'o-', color='#4A90E2', lw=2, markersize=8, label='Savings')
    ax2_twin.set_ylabel('Savings per Transaction', fontsize=10, color='#4A90E2')
    ax2_twin.tick_params(axis='y', labelcolor='#4A90E2')

    ax2.set_xlabel('Transaction Value', fontsize=10)
    ax2.set_ylabel('Fee Amount', fontsize=10)
    ax2.set_xticks(x2)
    ax2.set_xticklabels([f'${v}' for v in transaction_values], fontsize=9)
    ax2.set_title('Merchant Fee Savings with Open Banking', fontsize=12, fontweight='bold', pad=10)

    # Combined legend
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)

    ax2.yaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Main title
    fig.suptitle('Open Banking Payment Initiation: Cost Advantage',
                fontsize=14, fontweight='bold', y=1.02)

    # Source
    fig.text(0.5, 0.02, 'Source: Typical UK/EU merchant rates (2024). Actual rates vary by provider and volume.',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'pis_vs_card_fees.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
