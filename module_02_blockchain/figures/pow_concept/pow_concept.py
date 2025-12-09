"""
Proof of Work Concept
Illustrates how PoW mining works to secure blockchain

Output: pow_concept.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Proof of Work Concept',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/pow_concept'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create proof of work concept diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Proof of Work: The Mining Process', fontsize=20, fontweight='bold', ha='center')

    # Step 1: Block data
    step1_box = mpatches.FancyBboxPatch((0.5, 7), 4, 2.5,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#3498DB', alpha=0.2,
                                         edgecolor='#3498DB', lw=2)
    ax.add_patch(step1_box)
    ax.text(2.5, 9, '1. Block Data', ha='center', fontsize=14, fontweight='bold', color='#2980B9')
    ax.text(2.5, 8.3, 'Transactions', ha='center', fontsize=11)
    ax.text(2.5, 7.8, 'Previous Hash', ha='center', fontsize=11)
    ax.text(2.5, 7.3, 'Timestamp', ha='center', fontsize=11)

    # Arrow
    ax.annotate('', xy=(5.5, 8.25), xytext=(4.5, 8.25),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Step 2: Add nonce
    step2_box = mpatches.FancyBboxPatch((5.5, 7), 3, 2.5,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#F39C12', alpha=0.2,
                                         edgecolor='#F39C12', lw=2)
    ax.add_patch(step2_box)
    ax.text(7, 9, '2. Add Nonce', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7, 8.3, 'Nonce = 0, 1, 2...', ha='center', fontsize=11)
    ax.text(7, 7.6, 'Try millions of', ha='center', fontsize=10)
    ax.text(7, 7.2, 'values per second', ha='center', fontsize=10)

    # Arrow
    ax.annotate('', xy=(9.5, 8.25), xytext=(8.5, 8.25),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Step 3: Hash
    step3_box = mpatches.FancyBboxPatch((9.5, 7), 4, 2.5,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#9B59B6', alpha=0.2,
                                         edgecolor='#9B59B6', lw=2)
    ax.add_patch(step3_box)
    ax.text(11.5, 9, '3. Calculate Hash', ha='center', fontsize=14, fontweight='bold', color='#8E44AD')
    ax.text(11.5, 8.2, 'SHA-256(data + nonce)', ha='center', fontsize=11)
    ax.text(11.5, 7.5, 'Compare to target', ha='center', fontsize=11)

    # Target explanation
    target_box = mpatches.FancyBboxPatch((1, 4), 12, 2.3,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#E74C3C', alpha=0.15,
                                          edgecolor='#E74C3C', lw=2)
    ax.add_patch(target_box)
    ax.text(7, 5.8, 'The Puzzle: Find hash with enough leading zeros', ha='center', fontsize=14, fontweight='bold', color='#C0392B')
    ax.text(7, 5.1, 'Target:  0000000000000000000abc...  (more zeros = harder)', ha='center', fontsize=11, family='monospace')
    ax.text(7, 4.4, 'Winner: First miner to find valid hash broadcasts block & earns reward', ha='center', fontsize=12)

    # Key properties
    props = [
        ('Hard to find', 'Avg 10 min per block'),
        ('Easy to verify', 'One hash check'),
        ('Adjustable', 'Difficulty retargets'),
    ]
    for i, (name, desc) in enumerate(props):
        x = 2 + i * 4.5
        prop_box = mpatches.FancyBboxPatch((x-1.5, 1), 3, 2,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#27AE60', alpha=0.2,
                                            edgecolor='#27AE60', lw=1.5)
        ax.add_patch(prop_box)
        ax.text(x, 2.5, name, ha='center', fontsize=12, fontweight='bold', color='#1E8449')
        ax.text(x, 1.8, desc, ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, 'Source: Nakamoto, Bitcoin Whitepaper (2008), Section 4',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'pow_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
