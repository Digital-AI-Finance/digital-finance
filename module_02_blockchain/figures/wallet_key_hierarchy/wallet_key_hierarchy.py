"""
Wallet Key Hierarchy
Shows BIP-32 HD wallet key derivation structure

Output: wallet_key_hierarchy.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Wallet Key Hierarchy',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/wallet_key_hierarchy'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create HD wallet key hierarchy diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'BIP-32/44: Hierarchical Deterministic Wallet', fontsize=20, fontweight='bold', ha='center')

    # Master seed
    master = mpatches.FancyBboxPatch((5.5, 8.5), 3, 1.2,
                                      boxstyle='round,pad=0.1',
                                      facecolor='#9B59B6', alpha=0.8,
                                      edgecolor='#8E44AD', lw=2)
    ax.add_patch(master)
    ax.text(7, 9.3, 'Master Seed', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(7, 8.8, '(from mnemonic)', ha='center', fontsize=10, color='white')

    # Derivation path explanation
    ax.text(7, 7.8, "m / purpose' / coin' / account' / change / index", ha='center', fontsize=12, family='monospace',
           bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#999'))

    # Level boxes
    levels = [
        ('Purpose', "44'", 'BIP-44 standard', 2),
        ('Coin', "0'", 'Bitcoin', 5),
        ('Account', "0'", 'First account', 8),
        ('Change', '0', 'Receiving', 11),
    ]

    y = 6.5
    for name, value, desc, x in levels:
        box = mpatches.FancyBboxPatch((x-1, y), 2, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#3498DB', alpha=0.3,
                                       edgecolor='#3498DB', lw=1.5)
        ax.add_patch(box)
        ax.text(x, y+0.8, name, ha='center', fontsize=10, fontweight='bold')
        ax.text(x, y+0.3, value, ha='center', fontsize=11, family='monospace')

    # Arrows between levels
    ax.plot([3, 4], [7.1, 7.1], 'k-', lw=1.5)
    ax.plot([6, 7], [7.1, 7.1], 'k-', lw=1.5)
    ax.plot([9, 10], [7.1, 7.1], 'k-', lw=1.5)

    # Address generation
    addresses_box = mpatches.FancyBboxPatch((1, 3), 12, 3,
                                             boxstyle='round,pad=0.1',
                                             facecolor='#27AE60', alpha=0.15,
                                             edgecolor='#27AE60', lw=2)
    ax.add_patch(addresses_box)
    ax.text(7, 5.6, 'Generated Addresses (index 0, 1, 2...)', ha='center', fontsize=14, fontweight='bold', color='#1E8449')

    # Example addresses
    addresses = [
        ("m/44'/0'/0'/0/0", 'bc1qxy2k...'),
        ("m/44'/0'/0'/0/1", 'bc1qar0s...'),
        ("m/44'/0'/0'/0/2", 'bc1q9h6m...'),
    ]

    for i, (path, addr) in enumerate(addresses):
        x = 2.5 + i * 4
        ax.text(x, 4.8, path, ha='center', fontsize=9, family='monospace')
        ax.text(x, 4.2, addr, ha='center', fontsize=10, family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#27AE60'))
        ax.text(x, 3.6, f'Address {i}', ha='center', fontsize=10)

    # Benefits
    benefits_box = mpatches.FancyBboxPatch((1, 0.5), 12, 2,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#F8F9FA', alpha=0.9,
                                            edgecolor='#CCC', lw=1)
    ax.add_patch(benefits_box)
    ax.text(7, 2.1, 'HD Wallet Benefits:', ha='center', fontsize=12, fontweight='bold')
    benefits = ['Single backup (seed)', 'Infinite addresses', 'Privacy (new addr per tx)', 'Multi-coin support']
    for i, benefit in enumerate(benefits):
        ax.text(2 + i*3.3, 1.3, f'* {benefit}', fontsize=10)

    # Source
    fig.text(0.5, 0.02, 'Source: BIP-32, BIP-44 (Bitcoin Improvement Proposals)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wallet_key_hierarchy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
