"""
Ethereum Account Types
Shows EOA vs Contract accounts

Output: account_types.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Ethereum Account Types',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/account_types'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Ethereum Account Types', fontsize=20, fontweight='bold', ha='center')

    # EOA
    eoa_box = mpatches.FancyBboxPatch((0.5, 4), 6, 5, boxstyle='round', facecolor='#3498DB', alpha=0.2, edgecolor='#3498DB', lw=3)
    ax.add_patch(eoa_box)
    ax.text(3.5, 8.5, 'Externally Owned Account', ha='center', fontsize=14, fontweight='bold', color='#2980B9')
    ax.text(3.5, 8, '(EOA)', ha='center', fontsize=12, color='#2980B9')

    eoa_props = [
        'Controlled by private key',
        'Can initiate transactions',
        'No code associated',
        'Example: MetaMask wallet',
    ]
    for i, prop in enumerate(eoa_props):
        ax.text(3.5, 7.2 - i*0.7, f'* {prop}', ha='center', fontsize=11)

    # Contract Account
    ca_box = mpatches.FancyBboxPatch((7.5, 4), 6, 5, boxstyle='round', facecolor='#27AE60', alpha=0.2, edgecolor='#27AE60', lw=3)
    ax.add_patch(ca_box)
    ax.text(10.5, 8.5, 'Contract Account', ha='center', fontsize=14, fontweight='bold', color='#1E8449')
    ax.text(10.5, 8, '(Smart Contract)', ha='center', fontsize=12, color='#1E8449')

    ca_props = [
        'Controlled by code',
        'Cannot initiate (only respond)',
        'Has associated bytecode',
        'Example: Uniswap, Aave',
    ]
    for i, prop in enumerate(ca_props):
        ax.text(10.5, 7.2 - i*0.7, f'* {prop}', ha='center', fontsize=11)

    # Both have
    both_box = mpatches.FancyBboxPatch((3, 0.5), 8, 3, boxstyle='round', facecolor='#F39C12', alpha=0.15, edgecolor='#F39C12', lw=2)
    ax.add_patch(both_box)
    ax.text(7, 3.1, 'Both Account Types Have:', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7, 2.4, 'Address (20 bytes) | Balance (ETH) | Nonce (transaction count)', ha='center', fontsize=11)
    ax.text(7, 1.7, 'Storage Root | Code Hash (empty for EOA)', ha='center', fontsize=11)

    # Interaction arrow
    ax.annotate('', xy=(7.5, 6), xytext=(6.5, 6), arrowprops=dict(arrowstyle='<->', lw=2, color='#333'))
    ax.text(7, 6.5, 'Interact', fontsize=10, ha='center')

    fig.text(0.5, 0.02, 'Source: Ethereum Yellow Paper, ethereum.org/developers', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'account_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
