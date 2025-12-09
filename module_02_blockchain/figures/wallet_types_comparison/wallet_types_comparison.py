"""
Wallet Types Comparison
Compares different cryptocurrency wallet types and their security tradeoffs

Output: wallet_types_comparison.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Wallet Types Comparison',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/wallet_types_comparison'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create wallet types comparison chart"""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Wallet types
    wallets = ['Hardware\nWallet', 'Paper\nWallet', 'Desktop\nWallet', 'Mobile\nWallet', 'Web\nWallet', 'Exchange\n(Custodial)']

    # Metrics (1-10 scale)
    security = [9, 8, 6, 5, 3, 2]
    convenience = [4, 2, 6, 8, 9, 10]
    cost = [2, 10, 9, 9, 10, 10]  # Free = 10

    x = np.arange(len(wallets))
    width = 0.25

    bars1 = ax.bar(x - width, security, width, label='Security', color='#27AE60', alpha=0.8)
    bars2 = ax.bar(x, convenience, width, label='Convenience', color='#3498DB', alpha=0.8)
    bars3 = ax.bar(x + width, cost, width, label='Cost (10=Free)', color='#F39C12', alpha=0.8)

    ax.set_ylabel('Score (1-10)', fontsize=14)
    ax.set_title('Cryptocurrency Wallet Comparison', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(wallets, fontsize=11)
    ax.legend(loc='upper right', fontsize=12)
    ax.set_ylim(0, 12)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                       xytext=(0, 3), textcoords='offset points', ha='center', fontsize=9)

    # Examples row
    examples = ['Ledger, Trezor', 'Generated\noffline', 'Electrum,\nExodus', 'Trust Wallet,\nBlue Wallet', 'MetaMask,\nMyEtherWallet', 'Coinbase,\nBinance']
    for i, ex in enumerate(examples):
        ax.text(i, -1.5, ex, ha='center', fontsize=9, color='#666', style='italic')

    # Key insight box
    ax.text(0.5, -0.22, 'Security vs Convenience Tradeoff: "Not your keys, not your coins"',
           transform=ax.transAxes, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    # Custody indicator
    ax.axvline(x=4.5, color='#E74C3C', linestyle='--', linewidth=2, alpha=0.5)
    ax.text(2, 11.5, 'Self-Custody (You control keys)', ha='center', fontsize=11, color='#27AE60', fontweight='bold')
    ax.text(5.2, 11.5, 'Third-Party', ha='left', fontsize=11, color='#E74C3C', fontweight='bold')

    # Source
    fig.text(0.5, 0.02, 'Source: Bitcoin.org Wallet Guide, Security Best Practices (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)

    output_path = Path(__file__).parent / 'wallet_types_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
