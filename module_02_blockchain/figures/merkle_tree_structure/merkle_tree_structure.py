"""
Merkle Tree Structure
Visualizes how Merkle trees organize transaction hashes in blockchain

Output: merkle_tree_structure.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Merkle Tree Structure',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/merkle_tree_structure'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Merkle tree structure diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Merkle Tree: Efficient Transaction Verification', fontsize=20, fontweight='bold', ha='center')

    # Root level
    root_box = mpatches.FancyBboxPatch((5.5, 8), 3, 1.2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#E74C3C', alpha=0.8,
                                        edgecolor='#C0392B', lw=2)
    ax.add_patch(root_box)
    ax.text(7, 8.8, 'Merkle Root', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(7, 8.3, 'Hash(H12 + H34)', ha='center', fontsize=10, color='white')

    # Level 2
    for i, (x, label, hash_label) in enumerate([(3.5, 'H12', 'Hash(H1+H2)'), (10.5, 'H34', 'Hash(H3+H4)')]):
        box = mpatches.FancyBboxPatch((x-1.2, 5.5), 2.4, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F39C12', alpha=0.8,
                                       edgecolor='#D68910', lw=2)
        ax.add_patch(box)
        ax.text(x, 6.3, label, ha='center', fontsize=12, fontweight='bold', color='white')
        ax.text(x, 5.8, hash_label, ha='center', fontsize=9, color='white')

    # Level 3 (leaf hashes)
    positions = [(1.5, 'H1', 'Hash(Tx1)'), (5.5, 'H2', 'Hash(Tx2)'),
                 (8.5, 'H3', 'Hash(Tx3)'), (12.5, 'H4', 'Hash(Tx4)')]
    for x, label, hash_label in positions:
        box = mpatches.FancyBboxPatch((x-1, 3), 2, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#3498DB', alpha=0.8,
                                       edgecolor='#2980B9', lw=2)
        ax.add_patch(box)
        ax.text(x, 3.8, label, ha='center', fontsize=11, fontweight='bold', color='white')
        ax.text(x, 3.3, hash_label, ha='center', fontsize=9, color='white')

    # Transactions (bottom)
    tx_positions = [(1.5, 'Tx1'), (5.5, 'Tx2'), (8.5, 'Tx3'), (12.5, 'Tx4')]
    for x, label in tx_positions:
        box = mpatches.FancyBboxPatch((x-0.8, 0.8), 1.6, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#27AE60', alpha=0.8,
                                       edgecolor='#1E8449', lw=2)
        ax.add_patch(box)
        ax.text(x, 1.3, label, ha='center', fontsize=11, fontweight='bold', color='white')

    # Connecting lines
    # Root to level 2
    ax.plot([7, 3.5], [8, 6.7], 'k-', lw=1.5)
    ax.plot([7, 10.5], [8, 6.7], 'k-', lw=1.5)

    # Level 2 to level 3
    ax.plot([3.5, 1.5], [5.5, 4.2], 'k-', lw=1.5)
    ax.plot([3.5, 5.5], [5.5, 4.2], 'k-', lw=1.5)
    ax.plot([10.5, 8.5], [5.5, 4.2], 'k-', lw=1.5)
    ax.plot([10.5, 12.5], [5.5, 4.2], 'k-', lw=1.5)

    # Level 3 to transactions
    for x in [1.5, 5.5, 8.5, 12.5]:
        ax.plot([x, x], [3, 1.8], 'k-', lw=1.5)

    # Key benefits box
    benefits = [
        'Verify any Tx with O(log n) hashes',
        'Detect tampering instantly',
        'Used in SPV (light) wallets',
    ]
    ax.text(7, 0.4, '  |  '.join(benefits), ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60', lw=1.5))

    # Source
    fig.text(0.5, 0.02, 'Source: Nakamoto, Bitcoin Whitepaper (2008), Section 7',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'merkle_tree_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
