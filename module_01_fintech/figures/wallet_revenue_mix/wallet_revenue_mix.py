"""
Mobile Wallet Revenue Mix Chart
Shows breakdown of revenue sources for digital wallets

Output: wallet_revenue_mix.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Mobile Wallet Revenue Mix',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wallet_revenue_mix'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create mobile wallet revenue mix chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Pie chart of revenue sources
    revenue_sources = ['Transaction Fees', 'Interchange', 'Interest on\nFloat',
                       'Merchant\nServices', 'Value-Added\nServices', 'Data\nMonetization']
    percentages = [35, 25, 15, 12, 8, 5]
    colors = ['#333333', '#4A90E2', '#44A044', '#FF7F0E', '#6B5B95', '#999999']
    explode = (0.05, 0, 0, 0, 0, 0)

    wedges, texts, autotexts = ax1.pie(
        percentages,
        explode=explode,
        labels=revenue_sources,
        autopct='%1.0f%%',
        colors=colors,
        startangle=90,
        pctdistance=0.75
    )

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
    for text in texts:
        text.set_fontsize(8)

    ax1.set_title('Revenue Mix by Source', fontsize=12, fontweight='bold', pad=10)

    # Right: Bar chart comparing wallet types
    wallet_types = ['Consumer\nWallet', 'Merchant\nWallet', 'P2P\nPlatform', 'Super\nApp']

    # Revenue composition for each type
    transaction_fees = [40, 25, 45, 30]
    interchange = [30, 35, 20, 25]
    float_income = [10, 15, 15, 10]
    other = [20, 25, 20, 35]

    x = np.arange(len(wallet_types))
    width = 0.6

    ax2.bar(x, transaction_fees, width, label='Transaction Fees', color='#333333')
    ax2.bar(x, interchange, width, bottom=transaction_fees, label='Interchange', color='#4A90E2')
    ax2.bar(x, float_income, width, bottom=np.array(transaction_fees)+np.array(interchange),
           label='Float Income', color='#44A044')
    ax2.bar(x, other, width, bottom=np.array(transaction_fees)+np.array(interchange)+np.array(float_income),
           label='Other Services', color='#FF7F0E')

    ax2.set_ylabel('Revenue Share (%)', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(wallet_types, fontsize=9)
    ax2.set_ylim(0, 105)
    ax2.legend(loc='upper right', fontsize=8, framealpha=0.9)
    ax2.set_title('Revenue Mix by Wallet Type', fontsize=12, fontweight='bold', pad=10)

    # Add grid
    ax2.yaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Main title
    fig.suptitle('Mobile Wallet Revenue Model Analysis', fontsize=14, fontweight='bold', y=1.02)

    # Synthetic label
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wallet_revenue_mix.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
