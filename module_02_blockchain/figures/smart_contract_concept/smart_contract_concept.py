"""
Smart Contract Concept
Explains what smart contracts are

Output: smart_contract_concept.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Smart Contract Concept',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/smart_contract_concept'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(7, 10.3, 'Smart Contracts: Self-Executing Code', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 9.5, '"Code is law" - automated agreements that execute when conditions are met', fontsize=12, ha='center', color='#666')

    # Contract structure
    contract_box = mpatches.FancyBboxPatch((3, 5), 8, 4, boxstyle='round', facecolor='#3498DB', alpha=0.2, edgecolor='#3498DB', lw=3)
    ax.add_patch(contract_box)
    ax.text(7, 8.5, 'SMART CONTRACT', ha='center', fontsize=16, fontweight='bold', color='#2980B9')

    # Components
    components = [
        ('State Variables', 'Store data on chain', 4.5),
        ('Functions', 'Execute logic', 7),
        ('Events', 'Emit logs', 9.5),
    ]
    for name, desc, x in components:
        comp_box = mpatches.FancyBboxPatch((x-1.3, 6.5), 2.6, 1.5, boxstyle='round', facecolor='white', edgecolor='#3498DB', lw=1.5)
        ax.add_patch(comp_box)
        ax.text(x, 7.6, name, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 7.0, desc, ha='center', fontsize=9)

    # Input/Output
    ax.annotate('', xy=(3, 7), xytext=(1, 7), arrowprops=dict(arrowstyle='->', lw=2, color='#27AE60'))
    ax.text(0.5, 7.5, 'Trigger\n(Transaction)', fontsize=10, ha='center')

    ax.annotate('', xy=(13, 7), xytext=(11, 7), arrowprops=dict(arrowstyle='->', lw=2, color='#E74C3C'))
    ax.text(13.5, 7.5, 'Result\n(State change)', fontsize=10, ha='center')

    # Example
    example_box = mpatches.FancyBboxPatch((1, 1.5), 12, 3, boxstyle='round', facecolor='#F8F9FA', edgecolor='#CCC', lw=1)
    ax.add_patch(example_box)
    ax.text(7, 4.1, 'Example: Escrow Contract', ha='center', fontsize=14, fontweight='bold')

    steps = [
        ('1. Buyer deposits', 'funds locked'),
        ('2. Seller delivers', 'condition met'),
        ('3. Auto-release', 'funds transfer'),
    ]
    for i, (step, result) in enumerate(steps):
        x = 2.5 + i * 4
        ax.text(x, 3.2, step, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 2.6, result, ha='center', fontsize=10, color='#27AE60')
        if i < 2:
            ax.annotate('', xy=(x+1.8, 2.9), xytext=(x+1.2, 2.9), arrowprops=dict(arrowstyle='->', lw=1.5, color='#333'))

    # Properties
    ax.text(7, 1.0, 'Properties: Immutable | Transparent | Trustless | Deterministic', ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    fig.text(0.5, 0.02, 'Source: Szabo, "Smart Contracts" (1994), Ethereum Yellow Paper', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'smart_contract_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
