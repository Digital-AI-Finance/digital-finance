"""
Gas Mechanism
Explains Ethereum's gas system for transaction fees

Output: gas_mechanism.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Gas Mechanism',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/gas_mechanism'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    ax.text(7, 10.3, 'Ethereum Gas: Fuel for the World Computer', fontsize=20, fontweight='bold', ha='center')

    # Formula
    formula_box = mpatches.FancyBboxPatch((2, 8), 10, 1.5, boxstyle='round', facecolor='#3498DB', alpha=0.2, edgecolor='#3498DB', lw=2)
    ax.add_patch(formula_box)
    ax.text(7, 9, 'Transaction Fee = Gas Used x Gas Price', ha='center', fontsize=16, fontweight='bold', color='#2980B9')
    ax.text(7, 8.3, '(in ETH)            (units)       (gwei/gas)', ha='center', fontsize=11, color='#666')

    # Gas costs table
    costs_box = mpatches.FancyBboxPatch((0.5, 4), 6.5, 3.5, boxstyle='round', facecolor='#F39C12', alpha=0.15, edgecolor='#F39C12', lw=2)
    ax.add_patch(costs_box)
    ax.text(3.75, 7.1, 'Common Gas Costs', ha='center', fontsize=14, fontweight='bold', color='#D68910')

    operations = [
        ('Simple transfer', '21,000 gas'),
        ('ERC-20 transfer', '~65,000 gas'),
        ('Uniswap swap', '~150,000 gas'),
        ('NFT mint', '~100,000 gas'),
        ('Deploy contract', '~500,000+ gas'),
    ]
    for i, (op, cost) in enumerate(operations):
        ax.text(1.5, 6.4 - i*0.5, op, fontsize=10)
        ax.text(6, 6.4 - i*0.5, cost, fontsize=10, ha='right', fontweight='bold')

    # Why gas
    why_box = mpatches.FancyBboxPatch((7.5, 4), 6, 3.5, boxstyle='round', facecolor='#27AE60', alpha=0.15, edgecolor='#27AE60', lw=2)
    ax.add_patch(why_box)
    ax.text(10.5, 7.1, 'Why Gas Exists', ha='center', fontsize=14, fontweight='bold', color='#1E8449')

    reasons = [
        'Prevents infinite loops',
        'Compensates validators',
        'Allocates scarce resources',
        'Spam protection',
    ]
    for i, reason in enumerate(reasons):
        ax.text(10.5, 6.4 - i*0.5, f'* {reason}', ha='center', fontsize=11)

    # Gas limit vs gas used
    limit_box = mpatches.FancyBboxPatch((1, 0.5), 12, 3, boxstyle='round', facecolor='#F8F9FA', edgecolor='#CCC', lw=1)
    ax.add_patch(limit_box)
    ax.text(7, 3.1, 'Gas Limit vs Gas Used', ha='center', fontsize=14, fontweight='bold')
    ax.text(7, 2.4, 'Gas Limit: Maximum you\'re willing to spend (set by user)', ha='center', fontsize=11)
    ax.text(7, 1.7, 'Gas Used: Actual computation consumed (unused gas refunded)', ha='center', fontsize=11)
    ax.text(7, 1.0, 'If Gas Used > Gas Limit: Transaction fails, gas still consumed', ha='center', fontsize=11, color='#E74C3C')

    fig.text(0.5, 0.02, 'Source: Ethereum Yellow Paper, etherscan.io/gastracker', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'gas_mechanism.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
