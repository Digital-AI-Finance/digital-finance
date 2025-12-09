"""
Bitcoin vs Ethereum
Compares the two largest blockchain platforms

Output: bitcoin_vs_ethereum.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Bitcoin vs Ethereum',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/bitcoin_vs_ethereum'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(7, 10.3, 'Bitcoin vs Ethereum: Key Differences', fontsize=20, fontweight='bold', ha='center')

    # Headers
    ax.text(4.5, 9.3, 'Bitcoin', fontsize=18, fontweight='bold', ha='center', color='#F39C12')
    ax.text(10.5, 9.3, 'Ethereum', fontsize=18, fontweight='bold', ha='center', color='#3498DB')

    # Comparison rows
    comparisons = [
        ('Purpose', 'Digital gold / Store of value', 'World computer / DApps platform'),
        ('Consensus', 'Proof of Work', 'Proof of Stake (since 2022)'),
        ('Block Time', '~10 minutes', '~12 seconds'),
        ('Language', 'Bitcoin Script (limited)', 'Solidity (Turing-complete)'),
        ('Supply', '21M cap (deflationary)', 'No cap (minimal inflation)'),
        ('Smart Contracts', 'Basic (multi-sig, timelocks)', 'Full programmability'),
        ('Use Cases', 'Payments, savings', 'DeFi, NFTs, DAOs, gaming'),
        ('Market Cap', '~$800B (Dec 2024)', '~$350B (Dec 2024)'),
    ]

    for i, (category, btc, eth) in enumerate(comparisons):
        y = 8.3 - i * 0.95

        # Category
        ax.text(0.5, y, category, fontsize=11, fontweight='bold')

        # Bitcoin value
        btc_box = mpatches.FancyBboxPatch((2, y-0.35), 4.5, 0.7, boxstyle='round', facecolor='#F39C12', alpha=0.15, edgecolor='#F39C12', lw=1)
        ax.add_patch(btc_box)
        ax.text(4.25, y, btc, fontsize=10, ha='center')

        # Ethereum value
        eth_box = mpatches.FancyBboxPatch((7.5, y-0.35), 5.5, 0.7, boxstyle='round', facecolor='#3498DB', alpha=0.15, edgecolor='#3498DB', lw=1)
        ax.add_patch(eth_box)
        ax.text(10.25, y, eth, fontsize=10, ha='center')

    # Bottom insight
    insight_box = mpatches.FancyBboxPatch((1, 0.3), 12, 1, boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60', lw=2)
    ax.add_patch(insight_box)
    ax.text(7, 0.8, 'Key Insight: Bitcoin = digital gold, Ethereum = programmable money', ha='center', fontsize=12, fontweight='bold', color='#1E8449')

    fig.text(0.5, 0.02, 'Source: CoinMarketCap, Blockchain.com, Ethereum.org (Dec 2024)', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'bitcoin_vs_ethereum.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
