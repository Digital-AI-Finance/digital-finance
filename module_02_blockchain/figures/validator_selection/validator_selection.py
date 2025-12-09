"""
Validator Selection
Shows how validators are selected in Proof of Stake

Output: validator_selection.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Validator Selection',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/validator_selection'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create validator selection diagram"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

    # Left: Stake-weighted selection
    stakes = [100, 50, 30, 20]
    labels = ['Validator A\n(100 ETH)', 'Validator B\n(50 ETH)', 'Validator C\n(30 ETH)', 'Validator D\n(20 ETH)']
    colors = ['#3498DB', '#27AE60', '#F39C12', '#E74C3C']

    wedges, texts, autotexts = ax1.pie(stakes, labels=labels, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0])
    ax1.set_title('Selection Probability\n(Proportional to Stake)', fontsize=14, fontweight='bold')

    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    # Right: Selection process
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Ethereum PoS Selection', fontsize=14, fontweight='bold')

    # Validator pool
    pool_box = mpatches.FancyBboxPatch((0.5, 7), 9, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#3498DB', alpha=0.2,
                                        edgecolor='#3498DB', lw=2)
    ax2.add_patch(pool_box)
    ax2.text(5, 9, 'Active Validator Pool', ha='center', fontsize=12, fontweight='bold')
    ax2.text(5, 8.3, '~1,000,000 validators (Dec 2024)', ha='center', fontsize=11)
    ax2.text(5, 7.5, '32 ETH minimum each', ha='center', fontsize=10)

    # RANDAO arrow
    ax2.annotate('', xy=(5, 6.5), xytext=(5, 7),
                arrowprops=dict(arrowstyle='->', lw=2, color='#9B59B6'))
    ax2.text(5, 6.7, 'RANDAO', ha='center', fontsize=11, fontweight='bold', color='#9B59B6',
            bbox=dict(boxstyle='round', facecolor='#E8E0F0', edgecolor='#9B59B6'))

    # Selected validators
    roles = [
        ('Block Proposer', '1 per slot', '#E74C3C'),
        ('Attesters', '~128 per slot', '#27AE60'),
        ('Sync Committee', '512 every 27h', '#F39C12'),
    ]

    for i, (role, count, color) in enumerate(roles):
        y = 5 - i * 1.8
        role_box = mpatches.FancyBboxPatch((1, y), 8, 1.5,
                                            boxstyle='round,pad=0.1',
                                            facecolor=color, alpha=0.2,
                                            edgecolor=color, lw=1.5)
        ax2.add_patch(role_box)
        ax2.text(5, y+1.0, role, ha='center', fontsize=11, fontweight='bold')
        ax2.text(5, y+0.4, count, ha='center', fontsize=10)

    # Key properties
    ax2.text(5, 0.3, 'Randomness prevents prediction attacks',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#999'))

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum Beacon Chain Specification, beaconcha.in (Dec 2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'validator_selection.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
