"""
Ethereum PoS Architecture
Shows the structure of Ethereum's Proof of Stake system

Output: ethereum_pos_architecture.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Ethereum PoS Architecture',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/ethereum_pos_architecture'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Ethereum PoS architecture diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Ethereum Proof of Stake Architecture', fontsize=20, fontweight='bold', ha='center')

    # Consensus layer (Beacon Chain)
    beacon_box = mpatches.FancyBboxPatch((0.5, 6.5), 13, 3,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#9B59B6', alpha=0.2,
                                          edgecolor='#9B59B6', lw=2)
    ax.add_patch(beacon_box)
    ax.text(7, 9, 'Consensus Layer (Beacon Chain)', ha='center', fontsize=16, fontweight='bold', color='#8E44AD')

    # Components
    beacon_components = [
        ('Validators', '~1M active', 2.5),
        ('Slots', '12 sec each', 5.5),
        ('Epochs', '32 slots', 8.5),
        ('Finality', '2 epochs', 11.5),
    ]

    for name, desc, x in beacon_components:
        comp_box = mpatches.FancyBboxPatch((x-1.2, 7), 2.4, 1.7,
                                            boxstyle='round,pad=0.1',
                                            facecolor='white', alpha=0.9,
                                            edgecolor='#9B59B6', lw=1.5)
        ax.add_patch(comp_box)
        ax.text(x, 8.2, name, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 7.5, desc, ha='center', fontsize=10)

    # Execution layer
    exec_box = mpatches.FancyBboxPatch((0.5, 3), 13, 3,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#3498DB', alpha=0.2,
                                        edgecolor='#3498DB', lw=2)
    ax.add_patch(exec_box)
    ax.text(7, 5.5, 'Execution Layer (EVM)', ha='center', fontsize=16, fontweight='bold', color='#2980B9')

    exec_components = [
        ('Transactions', 'User actions', 2.5),
        ('Smart Contracts', 'DApps logic', 5.5),
        ('State', 'Account balances', 8.5),
        ('Gas', 'Fee market', 11.5),
    ]

    for name, desc, x in exec_components:
        comp_box = mpatches.FancyBboxPatch((x-1.2, 3.5), 2.4, 1.7,
                                            boxstyle='round,pad=0.1',
                                            facecolor='white', alpha=0.9,
                                            edgecolor='#3498DB', lw=1.5)
        ax.add_patch(comp_box)
        ax.text(x, 4.7, name, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 4.0, desc, ha='center', fontsize=10)

    # Connection arrow
    ax.annotate('', xy=(7, 6.5), xytext=(7, 6),
               arrowprops=dict(arrowstyle='<->', lw=2, color='#333'))
    ax.text(7.5, 6.25, 'Engine API', fontsize=10, va='center')

    # Timeline
    timeline_box = mpatches.FancyBboxPatch((1, 0.5), 12, 2,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#F8F9FA', alpha=0.9,
                                            edgecolor='#CCC', lw=1)
    ax.add_patch(timeline_box)
    ax.text(7, 2.1, 'Block Production Timeline', ha='center', fontsize=12, fontweight='bold')

    timeline = [
        ('Slot start', '0s'),
        ('Attestations', '4s'),
        ('Block propagate', '8s'),
        ('Next slot', '12s'),
    ]

    for i, (event, time) in enumerate(timeline):
        x = 2 + i * 3.3
        ax.text(x, 1.5, event, ha='center', fontsize=10, fontweight='bold')
        ax.text(x, 1.0, time, ha='center', fontsize=11, color='#27AE60')

    # Arrow connecting timeline
    ax.annotate('', xy=(12, 1.25), xytext=(2, 1.25),
               arrowprops=dict(arrowstyle='->', lw=1.5, color='#27AE60'))

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum.org, The Merge Documentation (Sep 2022)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ethereum_pos_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
