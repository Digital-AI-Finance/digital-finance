"""
Events Architecture
Shows how Ethereum events and logs work

Output: events_architecture.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Events Architecture',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/events_architecture'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Ethereum Events & Logs', fontsize=20, fontweight='bold', ha='center')

    # Contract emitting event
    contract_box = mpatches.FancyBboxPatch((0.5, 5.5), 4, 3.5, boxstyle='round', facecolor='#3498DB', alpha=0.2, edgecolor='#3498DB', lw=2)
    ax.add_patch(contract_box)
    ax.text(2.5, 8.5, 'Smart Contract', ha='center', fontsize=14, fontweight='bold', color='#2980B9')
    ax.text(2.5, 7.7, 'emit Transfer(', ha='center', fontsize=10, family='monospace')
    ax.text(2.5, 7.2, '  from, to, amount', ha='center', fontsize=10, family='monospace')
    ax.text(2.5, 6.7, ');', ha='center', fontsize=10, family='monospace')

    # Arrow
    ax.annotate('', xy=(5.5, 7), xytext=(4.5, 7), arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Log structure
    log_box = mpatches.FancyBboxPatch((5.5, 5.5), 4, 3.5, boxstyle='round', facecolor='#F39C12', alpha=0.2, edgecolor='#F39C12', lw=2)
    ax.add_patch(log_box)
    ax.text(7.5, 8.5, 'Log Entry', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7.5, 7.7, 'topics[0]: Event sig hash', ha='center', fontsize=10)
    ax.text(7.5, 7.2, 'topics[1-3]: Indexed params', ha='center', fontsize=10)
    ax.text(7.5, 6.7, 'data: Non-indexed params', ha='center', fontsize=10)
    ax.text(7.5, 6.0, '(Stored in tx receipt)', ha='center', fontsize=9, style='italic')

    # Arrow
    ax.annotate('', xy=(10.5, 7), xytext=(9.5, 7), arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # External listeners
    listeners_box = mpatches.FancyBboxPatch((10.5, 5.5), 3, 3.5, boxstyle='round', facecolor='#27AE60', alpha=0.2, edgecolor='#27AE60', lw=2)
    ax.add_patch(listeners_box)
    ax.text(12, 8.5, 'Listeners', ha='center', fontsize=14, fontweight='bold', color='#1E8449')
    ax.text(12, 7.7, 'DApps', ha='center', fontsize=11)
    ax.text(12, 7.2, 'Indexers', ha='center', fontsize=11)
    ax.text(12, 6.7, 'Analytics', ha='center', fontsize=11)
    ax.text(12, 6.0, '(The Graph)', ha='center', fontsize=9, style='italic')

    # Benefits
    benefits_box = mpatches.FancyBboxPatch((0.5, 2), 13, 3, boxstyle='round', facecolor='#F8F9FA', edgecolor='#CCC', lw=1)
    ax.add_patch(benefits_box)
    ax.text(7, 4.6, 'Why Use Events?', ha='center', fontsize=14, fontweight='bold')

    benefits = [
        ('Cheap storage', '~375 gas/byte vs 20K/slot'),
        ('Searchable', 'Indexed topics for filtering'),
        ('Off-chain access', 'DApps can subscribe'),
        ('Audit trail', 'Permanent record of activity'),
    ]
    for i, (name, desc) in enumerate(benefits):
        x = 1.5 + (i % 2) * 6
        y = 3.8 if i < 2 else 2.8
        ax.text(x, y, f'{name}:', fontsize=11, fontweight='bold')
        ax.text(x+2.5, y, desc, fontsize=10)

    # Example
    ax.text(7, 0.8, 'Common Events: Transfer, Approval, Swap, Mint, Burn', ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    fig.text(0.5, 0.02, 'Source: Solidity Events Documentation, ethereum.org', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'events_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
