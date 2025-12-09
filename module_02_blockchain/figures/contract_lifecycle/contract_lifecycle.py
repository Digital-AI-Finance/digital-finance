"""
Contract Lifecycle
Shows the lifecycle of a smart contract

Output: contract_lifecycle.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Contract Lifecycle',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/contract_lifecycle'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Smart Contract Lifecycle', fontsize=20, fontweight='bold', ha='center')

    # Stages
    stages = [
        ('1. Write', 'Solidity code\n.sol file', '#9B59B6', 1.5),
        ('2. Compile', 'Bytecode +\nABI', '#3498DB', 4.5),
        ('3. Deploy', 'Send to\nnetwork', '#F39C12', 7.5),
        ('4. Interact', 'Call\nfunctions', '#27AE60', 10.5),
    ]

    for name, desc, color, x in stages:
        # Circle
        circle = plt.Circle((x, 6), 1.2, facecolor=color, alpha=0.3, edgecolor=color, lw=3)
        ax.add_patch(circle)
        ax.text(x, 6.4, name, ha='center', fontsize=12, fontweight='bold')
        ax.text(x, 5.5, desc, ha='center', fontsize=10)

        # Arrow to next
        if x < 10:
            ax.annotate('', xy=(x+1.8, 6), xytext=(x+1.3, 6), arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Details boxes
    # Compile output
    compile_box = mpatches.FancyBboxPatch((0.5, 2), 4, 2.5, boxstyle='round', facecolor='#3498DB', alpha=0.15, edgecolor='#3498DB', lw=1.5)
    ax.add_patch(compile_box)
    ax.text(2.5, 4.1, 'Compilation Output', ha='center', fontsize=12, fontweight='bold', color='#2980B9')
    ax.text(2.5, 3.4, 'Bytecode: EVM instructions', ha='center', fontsize=10)
    ax.text(2.5, 2.8, 'ABI: Interface definition', ha='center', fontsize=10)
    ax.text(2.5, 2.2, 'Source Map: Debug info', ha='center', fontsize=10)

    # Deployment
    deploy_box = mpatches.FancyBboxPatch((5, 2), 4, 2.5, boxstyle='round', facecolor='#F39C12', alpha=0.15, edgecolor='#F39C12', lw=1.5)
    ax.add_patch(deploy_box)
    ax.text(7, 4.1, 'Deployment', ha='center', fontsize=12, fontweight='bold', color='#D68910')
    ax.text(7, 3.4, 'Creates contract address', ha='center', fontsize=10)
    ax.text(7, 2.8, 'Runs constructor once', ha='center', fontsize=10)
    ax.text(7, 2.2, 'Costs gas (bytecode size)', ha='center', fontsize=10)

    # Interaction
    interact_box = mpatches.FancyBboxPatch((9.5, 2), 4, 2.5, boxstyle='round', facecolor='#27AE60', alpha=0.15, edgecolor='#27AE60', lw=1.5)
    ax.add_patch(interact_box)
    ax.text(11.5, 4.1, 'Interaction', ha='center', fontsize=12, fontweight='bold', color='#1E8449')
    ax.text(11.5, 3.4, 'Read: Free (view/pure)', ha='center', fontsize=10)
    ax.text(11.5, 2.8, 'Write: Costs gas', ha='center', fontsize=10)
    ax.text(11.5, 2.2, 'Events: Emit logs', ha='center', fontsize=10)

    # Immutability note
    ax.text(7, 0.8, 'Note: Once deployed, contract code cannot be changed (immutable)', ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    fig.text(0.5, 0.02, 'Source: Solidity Documentation, ethereum.org/developers', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'contract_lifecycle.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
