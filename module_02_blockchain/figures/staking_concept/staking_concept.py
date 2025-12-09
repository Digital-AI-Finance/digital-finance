"""
Staking Concept
Illustrates how Proof of Stake consensus works

Output: staking_concept.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Staking Concept',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/staking_concept'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create staking concept diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Proof of Stake: Staking as Consensus', fontsize=20, fontweight='bold', ha='center')

    # PoW vs PoS comparison
    ax.text(3.5, 9.2, 'Proof of Work', fontsize=14, fontweight='bold', color='#E74C3C', ha='center')
    ax.text(10.5, 9.2, 'Proof of Stake', fontsize=14, fontweight='bold', color='#27AE60', ha='center')

    # PoW box
    pow_box = mpatches.FancyBboxPatch((0.5, 6.5), 6, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#E74C3C', alpha=0.15,
                                       edgecolor='#E74C3C', lw=2)
    ax.add_patch(pow_box)
    ax.text(3.5, 8.5, 'Resource: Computing Power', ha='center', fontsize=12)
    ax.text(3.5, 7.9, 'Selection: Most work done', ha='center', fontsize=12)
    ax.text(3.5, 7.3, 'Security: Energy expenditure', ha='center', fontsize=12)
    ax.text(3.5, 6.7, 'Cost: $1M+/hour electricity', ha='center', fontsize=11, color='#E74C3C')

    # PoS box
    pos_box = mpatches.FancyBboxPatch((7.5, 6.5), 6, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#27AE60', alpha=0.15,
                                       edgecolor='#27AE60', lw=2)
    ax.add_patch(pos_box)
    ax.text(10.5, 8.5, 'Resource: Staked Tokens', ha='center', fontsize=12)
    ax.text(10.5, 7.9, 'Selection: Stake-weighted random', ha='center', fontsize=12)
    ax.text(10.5, 7.3, 'Security: Economic collateral', ha='center', fontsize=12)
    ax.text(10.5, 6.7, 'Cost: 99.95% less energy', ha='center', fontsize=11, color='#27AE60')

    # Staking process
    process_box = mpatches.FancyBboxPatch((1, 3), 12, 3,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#3498DB', alpha=0.15,
                                           edgecolor='#3498DB', lw=2)
    ax.add_patch(process_box)
    ax.text(7, 5.7, 'Staking Process', ha='center', fontsize=14, fontweight='bold', color='#2980B9')

    # Steps
    steps = [
        ('1. Deposit', 'Lock tokens\nas collateral'),
        ('2. Validate', 'Propose/attest\nblocks'),
        ('3. Rewards', 'Earn ~4-5%\nAPY'),
        ('4. Penalties', 'Slashing for\nmisbehavior'),
    ]

    for i, (title, desc) in enumerate(steps):
        x = 2 + i * 3.2
        step_box = mpatches.FancyBboxPatch((x-1, 3.4), 2, 1.8,
                                            boxstyle='round,pad=0.1',
                                            facecolor='white', alpha=0.9,
                                            edgecolor='#3498DB', lw=1.5)
        ax.add_patch(step_box)
        ax.text(x, 4.8, title, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 4.0, desc, ha='center', fontsize=10)

    # Key insight
    insight_box = mpatches.FancyBboxPatch((2, 0.5), 10, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#F39C12', alpha=0.2,
                                           edgecolor='#F39C12', lw=2)
    ax.add_patch(insight_box)
    ax.text(7, 2.0, 'Key Insight: "Skin in the Game"', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7, 1.4, 'Validators risk their own capital - cheating = losing staked tokens', ha='center', fontsize=12)
    ax.text(7, 0.8, 'Ethereum requires 32 ETH (~$60K) minimum stake', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum.org, Proof-of-Stake Documentation (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'staking_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
