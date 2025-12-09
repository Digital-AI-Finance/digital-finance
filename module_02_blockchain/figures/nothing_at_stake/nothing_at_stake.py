"""
Nothing at Stake Problem
Illustrates the nothing-at-stake attack in PoS

Output: nothing_at_stake.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Nothing at Stake Problem',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/nothing_at_stake'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Nothing-at-Stake Problem in PoS', fontsize=20, fontweight='bold', ha='center')

    # Problem explanation
    ax.text(7, 8.5, 'Unlike PoW, validating on multiple forks costs nothing in PoS', fontsize=12, ha='center', color='#666')

    # Fork diagram
    # Main chain
    for i, x in enumerate([2, 4, 6]):
        box = mpatches.FancyBboxPatch((x-0.5, 6), 1, 0.8, boxstyle='round', facecolor='#3498DB', alpha=0.8, edgecolor='black', lw=1.5)
        ax.add_patch(box)
        ax.text(x, 6.4, f'B{i+1}', ha='center', color='white', fontweight='bold')

    # Fork A
    for i, x in enumerate([8, 10]):
        box = mpatches.FancyBboxPatch((x-0.5, 7.2), 1, 0.8, boxstyle='round', facecolor='#27AE60', alpha=0.8, edgecolor='black', lw=1.5)
        ax.add_patch(box)
        ax.text(x, 7.6, f'A{i+1}', ha='center', color='white', fontweight='bold')
    ax.text(12, 7.6, 'Fork A', fontsize=11, fontweight='bold', color='#27AE60')

    # Fork B
    for i, x in enumerate([8, 10]):
        box = mpatches.FancyBboxPatch((x-0.5, 4.8), 1, 0.8, boxstyle='round', facecolor='#E74C3C', alpha=0.8, edgecolor='black', lw=1.5)
        ax.add_patch(box)
        ax.text(x, 5.2, f'B{i+1}', ha='center', color='white', fontweight='bold')
    ax.text(12, 5.2, 'Fork B', fontsize=11, fontweight='bold', color='#E74C3C')

    # Arrows
    ax.plot([6.5, 7.5], [6.4, 7.6], 'k-', lw=1.5)
    ax.plot([6.5, 7.5], [6.4, 5.2], 'k-', lw=1.5)
    ax.plot([8.5, 9.5], [7.6, 7.6], 'k-', lw=1.5)
    ax.plot([8.5, 9.5], [5.2, 5.2], 'k-', lw=1.5)

    # Validator behavior
    val_box = mpatches.FancyBboxPatch((1, 2.5), 12, 2.5, boxstyle='round', facecolor='#F39C12', alpha=0.15, edgecolor='#F39C12', lw=2)
    ax.add_patch(val_box)
    ax.text(7, 4.5, 'Rational Validator Behavior', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7, 3.8, 'PoW: Must choose one fork (mining power is scarce)', ha='center', fontsize=11)
    ax.text(7, 3.2, 'PoS: Can validate ALL forks simultaneously (no extra cost)', ha='center', fontsize=11)
    ax.text(7, 2.6, 'Result: Validators have no incentive to converge on single chain', ha='center', fontsize=11, color='#E74C3C')

    # Solution
    sol_box = mpatches.FancyBboxPatch((2, 0.3), 10, 1.8, boxstyle='round', facecolor='#27AE60', alpha=0.2, edgecolor='#27AE60', lw=2)
    ax.add_patch(sol_box)
    ax.text(7, 1.7, 'Solution: Slashing penalties for double-voting', ha='center', fontsize=12, fontweight='bold', color='#1E8449')
    ax.text(7, 1.0, 'Validators lose stake if caught validating multiple forks', ha='center', fontsize=11)

    fig.text(0.5, 0.02, 'Source: Buterin, "A Proof of Stake Design Philosophy" (2016)', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'nothing_at_stake.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
