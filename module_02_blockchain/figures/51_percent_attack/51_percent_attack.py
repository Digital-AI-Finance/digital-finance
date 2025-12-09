"""
51 Percent Attack
Illustrates how a 51% attack works and its implications

Output: 51_percent_attack.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': '51 Percent Attack',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/51_percent_attack'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create 51% attack diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, '51% Attack: Double Spending via Chain Reorg', fontsize=20, fontweight='bold', ha='center')

    # Honest chain
    ax.text(7, 9.2, 'Step 1: Attacker sends BTC to exchange (Block N)', fontsize=12, ha='center', style='italic')

    # Draw honest chain blocks
    honest_blocks = [(2, 8), (4.5, 8), (7, 8), (9.5, 8)]
    for i, (x, y) in enumerate(honest_blocks):
        color = '#27AE60' if i < 3 else '#3498DB'
        block = mpatches.FancyBboxPatch((x-0.8, y-0.5), 1.6, 1,
                                         boxstyle='round,pad=0.05',
                                         facecolor=color, alpha=0.8,
                                         edgecolor='black', lw=2)
        ax.add_patch(block)
        label = f'N-{3-i}' if i < 3 else 'N (Tx)'
        ax.text(x, y, label, ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Arrows between honest blocks
    for i in range(len(honest_blocks)-1):
        ax.annotate('', xy=(honest_blocks[i+1][0]-0.8, 8), xytext=(honest_blocks[i][0]+0.8, 8),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    ax.text(12, 8, 'Honest Chain', fontsize=12, fontweight='bold', color='#27AE60', va='center')

    # Secret attacker chain
    ax.text(7, 6.7, 'Step 2: Attacker secretly mines alternative chain (without Tx)', fontsize=12, ha='center', style='italic')

    attacker_blocks = [(2, 5.5), (4.5, 5.5), (7, 5.5), (9.5, 5.5), (12, 5.5)]
    for i, (x, y) in enumerate(attacker_blocks):
        block = mpatches.FancyBboxPatch((x-0.8, y-0.5), 1.6, 1,
                                         boxstyle='round,pad=0.05',
                                         facecolor='#E74C3C', alpha=0.8,
                                         edgecolor='black', lw=2)
        ax.add_patch(block)
        label = f"N'-{4-i}" if i < 4 else "N'+1"
        ax.text(x, y, label, ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Arrows between attacker blocks
    for i in range(len(attacker_blocks)-1):
        ax.annotate('', xy=(attacker_blocks[i+1][0]-0.8, 5.5), xytext=(attacker_blocks[i][0]+0.8, 5.5),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    ax.text(2, 4.7, 'Secret Attacker Chain (longer = wins)', fontsize=12, fontweight='bold', color='#E74C3C')

    # Step 3: Broadcast
    ax.text(7, 3.8, 'Step 3: Attacker broadcasts longer chain - network accepts it', fontsize=12, ha='center', style='italic')

    # Result box
    result_box = mpatches.FancyBboxPatch((1.5, 1.5), 11, 1.8,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#9B59B6', alpha=0.2,
                                          edgecolor='#9B59B6', lw=2)
    ax.add_patch(result_box)
    ax.text(7, 2.8, 'RESULT: Original transaction reversed!', ha='center', fontsize=14, fontweight='bold', color='#8E44AD')
    ax.text(7, 2.2, 'Attacker keeps both: BTC + goods/services from exchange', ha='center', fontsize=12)

    # Defense box
    defense_box = mpatches.FancyBboxPatch((3, 0.2), 8, 1,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#27AE60', alpha=0.2,
                                           edgecolor='#27AE60', lw=2)
    ax.add_patch(defense_box)
    ax.text(7, 0.8, 'Defense: Wait for 6+ confirmations before accepting large payments', ha='center', fontsize=12, fontweight='bold', color='#1E8449')

    # Cost note
    ax.text(7, 4.5, 'Cost to attack Bitcoin (2024): ~$1-2 million/hour in electricity + hardware',
           ha='center', fontsize=10, color='#666',
           bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#CCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Crypto51.app, Bitcoin Security Analysis (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / '51_percent_attack.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
