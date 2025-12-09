"""
Slashing Conditions
Shows the penalties for validator misbehavior

Output: slashing_conditions.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Slashing Conditions',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/slashing_conditions'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create slashing conditions diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Slashing: Penalties for Validator Misbehavior', fontsize=20, fontweight='bold', ha='center')

    # Slashable offenses
    offenses_box = mpatches.FancyBboxPatch((0.5, 6), 13, 3.5,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#E74C3C', alpha=0.15,
                                            edgecolor='#E74C3C', lw=2)
    ax.add_patch(offenses_box)
    ax.text(7, 9, 'Slashable Offenses', ha='center', fontsize=16, fontweight='bold', color='#C0392B')

    offenses = [
        ('Double Voting', 'Proposing 2 blocks\nfor same slot', '1/32 stake\n(~1 ETH)', 2.5),
        ('Surround Vote', 'Attestation that\nsurrounds another', '1/32 stake\n(~1 ETH)', 7),
        ('Correlation', 'Many slashed\ntogether', 'Up to 100%\nof stake', 11.5),
    ]

    for name, desc, penalty, x in offenses:
        off_box = mpatches.FancyBboxPatch((x-2, 6.3), 4, 2.3,
                                           boxstyle='round,pad=0.1',
                                           facecolor='white', alpha=0.9,
                                           edgecolor='#E74C3C', lw=1.5)
        ax.add_patch(off_box)
        ax.text(x, 8.2, name, ha='center', fontsize=12, fontweight='bold', color='#E74C3C')
        ax.text(x, 7.5, desc, ha='center', fontsize=10)
        ax.text(x, 6.7, f'Penalty: {penalty}', ha='center', fontsize=9, color='#C0392B')

    # Non-slashable penalties
    minor_box = mpatches.FancyBboxPatch((0.5, 2.5), 13, 3,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#F39C12', alpha=0.15,
                                         edgecolor='#F39C12', lw=2)
    ax.add_patch(minor_box)
    ax.text(7, 5.1, 'Non-Slashing Penalties (Inactivity)', ha='center', fontsize=16, fontweight='bold', color='#D68910')

    minor_penalties = [
        ('Missed Attestation', 'Same as reward\nwould have been', 3.5),
        ('Offline', 'Gradual balance\ndecay', 7),
        ('Inactivity Leak', 'During non-finality\n(quadratic decay)', 10.5),
    ]

    for name, desc, x in minor_penalties:
        pen_box = mpatches.FancyBboxPatch((x-1.8, 2.8), 3.6, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='white', alpha=0.9,
                                           edgecolor='#F39C12', lw=1.5)
        ax.add_patch(pen_box)
        ax.text(x, 4.4, name, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 3.5, desc, ha='center', fontsize=10)

    # Key insight
    insight_box = mpatches.FancyBboxPatch((2, 0.5), 10, 1.5,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#27AE60', alpha=0.2,
                                           edgecolor='#27AE60', lw=2)
    ax.add_patch(insight_box)
    ax.text(7, 1.5, 'Design Goal: Make attacks more expensive than potential gain', ha='center', fontsize=12, fontweight='bold', color='#1E8449')
    ax.text(7, 0.9, 'Correlation penalty discourages coordinated attacks', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum Consensus Specifications, eth2book.info',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'slashing_conditions.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
