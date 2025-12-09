"""
Base Fee Adjustment (EIP-1559)
Shows how Ethereum's base fee adjusts dynamically

Output: base_fee_adjustment.pdf
Module: module_02_blockchain
Lesson: 19 - Ethereum Smart Contracts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Base Fee Adjustment',
    'module': 'module_02_blockchain',
    'lesson': 19,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/base_fee_adjustment'
}

plt.rcParams.update({'font.size': 14, 'axes.labelsize': 14})

def create_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Left: Base fee adjustment mechanism
    blocks = np.arange(1, 11)
    # Simulate base fee changes based on block fullness
    fullness = [40, 60, 80, 90, 70, 50, 30, 45, 55, 50]  # % of target
    base_fee = [20]
    for f in fullness[:-1]:
        change = (f - 50) / 50 * 0.125  # Max 12.5% change
        base_fee.append(base_fee[-1] * (1 + change))

    ax1.bar(blocks, fullness, color='#3498DB', alpha=0.6, label='Block Fullness (%)')
    ax1.axhline(y=50, color='#E74C3C', linestyle='--', linewidth=2, label='Target (50%)')
    ax1.set_xlabel('Block Number', fontsize=14)
    ax1.set_ylabel('Block Fullness (%)', fontsize=14)
    ax1.set_title('Block Utilization', fontsize=16, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 100)
    ax1.grid(axis='y', alpha=0.3)

    ax1_twin = ax1.twinx()
    ax1_twin.plot(blocks, base_fee, 'g-', linewidth=3, marker='o', label='Base Fee (gwei)')
    ax1_twin.set_ylabel('Base Fee (gwei)', color='#27AE60', fontsize=14)
    ax1_twin.tick_params(axis='y', labelcolor='#27AE60')

    # Right: Fee structure
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('EIP-1559 Fee Structure', fontsize=16, fontweight='bold')

    # Components
    components = [
        ('Base Fee', 'Algorithmically set\nBurned (deflationary)', '#E74C3C', 7.5),
        ('Priority Fee', 'User-set tip\nGoes to validator', '#27AE60', 5),
        ('Max Fee', 'Maximum willing\nto pay per gas', '#3498DB', 2.5),
    ]

    for name, desc, color, y in components:
        box = plt.Rectangle((1, y-1), 8, 2, facecolor=color, alpha=0.2, edgecolor=color, lw=2)
        ax2.add_patch(box)
        ax2.text(5, y+0.3, name, ha='center', fontsize=14, fontweight='bold', color=color)
        ax2.text(5, y-0.5, desc, ha='center', fontsize=10)

    # Formula
    ax2.text(5, 0.5, 'Total Fee = (Base Fee + Priority Fee) x Gas Used', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#999'))

    fig.text(0.5, 0.02, 'Source: EIP-1559, Ethereum Improvement Proposal (Aug 2021)', fontsize=10, ha='center', style='italic', color='#666666')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'base_fee_adjustment.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
