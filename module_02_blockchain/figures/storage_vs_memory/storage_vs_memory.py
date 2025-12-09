"""
Storage vs Memory
Explains Ethereum's data locations

Output: storage_vs_memory.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Storage vs Memory',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/storage_vs_memory'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Ethereum Data Locations', fontsize=20, fontweight='bold', ha='center')

    # Storage
    storage_box = mpatches.FancyBboxPatch((0.5, 4.5), 4, 4.5, boxstyle='round', facecolor='#E74C3C', alpha=0.2, edgecolor='#E74C3C', lw=3)
    ax.add_patch(storage_box)
    ax.text(2.5, 8.5, 'Storage', ha='center', fontsize=16, fontweight='bold', color='#C0392B')

    storage_props = ['Persistent (on-chain)', 'Expensive to write', '~20,000 gas per slot', 'State variables', 'Key-value store']
    for i, prop in enumerate(storage_props):
        ax.text(2.5, 7.7 - i*0.6, prop, ha='center', fontsize=11)

    # Memory
    memory_box = mpatches.FancyBboxPatch((5, 4.5), 4, 4.5, boxstyle='round', facecolor='#3498DB', alpha=0.2, edgecolor='#3498DB', lw=3)
    ax.add_patch(memory_box)
    ax.text(7, 8.5, 'Memory', ha='center', fontsize=16, fontweight='bold', color='#2980B9')

    memory_props = ['Temporary (per call)', 'Cheaper than storage', '~3 gas per word', 'Function variables', 'Linear byte array']
    for i, prop in enumerate(memory_props):
        ax.text(7, 7.7 - i*0.6, prop, ha='center', fontsize=11)

    # Calldata
    calldata_box = mpatches.FancyBboxPatch((9.5, 4.5), 4, 4.5, boxstyle='round', facecolor='#27AE60', alpha=0.2, edgecolor='#27AE60', lw=3)
    ax.add_patch(calldata_box)
    ax.text(11.5, 8.5, 'Calldata', ha='center', fontsize=16, fontweight='bold', color='#1E8449')

    calldata_props = ['Read-only input', 'Cheapest option', '~3 gas per byte', 'Function arguments', 'Immutable']
    for i, prop in enumerate(calldata_props):
        ax.text(11.5, 7.7 - i*0.6, prop, ha='center', fontsize=11)

    # Cost comparison
    cost_box = mpatches.FancyBboxPatch((1, 0.5), 12, 3.5, boxstyle='round', facecolor='#F8F9FA', edgecolor='#CCC', lw=1)
    ax.add_patch(cost_box)
    ax.text(7, 3.6, 'Gas Cost Comparison (approximate)', ha='center', fontsize=14, fontweight='bold')

    costs = [
        ('Storage write (new)', '~20,000 gas', '#E74C3C'),
        ('Storage write (update)', '~5,000 gas', '#E74C3C'),
        ('Memory expansion', '~3 gas/word', '#3498DB'),
        ('Calldata read', '~3 gas/byte', '#27AE60'),
    ]
    for i, (op, cost, color) in enumerate(costs):
        x = 2 + (i % 2) * 5.5
        y = 2.8 if i < 2 else 1.5
        ax.text(x, y, f'{op}: ', fontsize=11)
        ax.text(x+3, y, cost, fontsize=11, fontweight='bold', color=color)

    # Best practice
    ax.text(7, 0.8, 'Best Practice: Use calldata for read-only, memory for temp, storage only when needed',
           ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    fig.text(0.5, 0.02, 'Source: Solidity Documentation, EVM Gas Costs', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'storage_vs_memory.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
