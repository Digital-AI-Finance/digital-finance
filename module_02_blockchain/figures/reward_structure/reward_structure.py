"""
Reward Structure
Shows staking rewards in Proof of Stake systems

Output: reward_structure.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Reward Structure',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/reward_structure'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create staking reward structure chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Left: APY vs Total Staked
    total_staked = np.array([1, 5, 10, 20, 30, 40, 50])  # Million ETH
    base_apy = 18 / np.sqrt(total_staked)  # Simplified formula

    ax1.plot(total_staked, base_apy, 'b-', linewidth=3, marker='o', markersize=8)
    ax1.fill_between(total_staked, base_apy, alpha=0.2)

    ax1.set_xlabel('Total ETH Staked (Million)', fontsize=14)
    ax1.set_ylabel('Base APY (%)', fontsize=14)
    ax1.set_title('Staking APY vs Total Staked', fontsize=16, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Current marker
    current_staked = 34  # Approximately Dec 2024
    current_apy = 18 / np.sqrt(current_staked)
    ax1.axvline(x=current_staked, color='#E74C3C', linestyle='--', linewidth=2)
    ax1.annotate(f'Current\n({current_staked}M ETH)\n~{current_apy:.1f}% APY',
                xy=(current_staked, current_apy), xytext=(40, 6),
                fontsize=11, ha='center',
                arrowprops=dict(arrowstyle='->', color='#E74C3C'),
                bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    ax1.set_xlim(0, 55)
    ax1.set_ylim(0, 20)

    # Right: Reward breakdown
    categories = ['Block\nRewards', 'Attestation\nRewards', 'Sync\nCommittee', 'Tips\n(MEV)']
    percentages = [25, 55, 5, 15]
    colors = ['#3498DB', '#27AE60', '#F39C12', '#9B59B6']

    bars = ax2.bar(categories, percentages, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Share of Total Rewards (%)', fontsize=14)
    ax2.set_title('Ethereum Staking Reward Breakdown', fontsize=16, fontweight='bold')
    ax2.set_ylim(0, 70)

    # Add value labels
    for bar, pct in zip(bars, percentages):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{pct}%', ha='center', fontsize=14, fontweight='bold')

    ax2.grid(axis='y', alpha=0.3)

    # Add note about MEV
    ax2.text(0.5, -0.12, 'Note: MEV (Maximal Extractable Value) varies significantly by block',
            transform=ax2.transAxes, ha='center', fontsize=10, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum.org Staking Rewards Calculator, beaconcha.in (Dec 2024) [ILLUSTRATIVE]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'reward_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
