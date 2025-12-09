"""
Liquid Staking Flow
Shows how liquid staking protocols work

Output: liquid_staking_flow.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Liquid Staking Flow',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/liquid_staking_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create liquid staking flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Liquid Staking: Have Your Cake and Eat It Too', fontsize=20, fontweight='bold', ha='center')

    # User
    user_box = mpatches.FancyBboxPatch((0.5, 6), 2.5, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#3498DB', alpha=0.3,
                                        edgecolor='#3498DB', lw=2)
    ax.add_patch(user_box)
    ax.text(1.75, 7.3, 'User', ha='center', fontsize=14, fontweight='bold')
    ax.text(1.75, 6.6, 'Has ETH', ha='center', fontsize=11)

    # Arrow: Deposit
    ax.annotate('', xy=(4, 7), xytext=(3, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.text(3.5, 7.5, 'Deposit\nETH', ha='center', fontsize=10)

    # Protocol
    protocol_box = mpatches.FancyBboxPatch((4, 5.5), 3, 3,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#F39C12', alpha=0.3,
                                            edgecolor='#F39C12', lw=2)
    ax.add_patch(protocol_box)
    ax.text(5.5, 8, 'Liquid Staking', ha='center', fontsize=12, fontweight='bold')
    ax.text(5.5, 7.4, 'Protocol', ha='center', fontsize=12, fontweight='bold')
    ax.text(5.5, 6.6, '(Lido, Rocket Pool)', ha='center', fontsize=10, style='italic')
    ax.text(5.5, 5.9, 'Issues derivative', ha='center', fontsize=10)

    # Arrow: Receive stETH
    ax.annotate('', xy=(3, 5), xytext=(4, 5.5),
               arrowprops=dict(arrowstyle='->', lw=2, color='#27AE60'))
    ax.text(3.5, 4.8, 'Receive\nstETH/rETH', ha='center', fontsize=10, color='#27AE60')

    # Arrow: Stake
    ax.annotate('', xy=(8, 7), xytext=(7, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.text(7.5, 7.5, 'Stake on\nBeacon Chain', ha='center', fontsize=10)

    # Validators
    validators_box = mpatches.FancyBboxPatch((8, 5.5), 3, 3,
                                              boxstyle='round,pad=0.1',
                                              facecolor='#27AE60', alpha=0.3,
                                              edgecolor='#27AE60', lw=2)
    ax.add_patch(validators_box)
    ax.text(9.5, 8, 'Validators', ha='center', fontsize=14, fontweight='bold')
    ax.text(9.5, 7.3, 'Run by protocol', ha='center', fontsize=11)
    ax.text(9.5, 6.6, 'Earn rewards', ha='center', fontsize=11)
    ax.text(9.5, 5.9, '~4-5% APY', ha='center', fontsize=11, color='#27AE60')

    # Arrow: Rewards back
    ax.annotate('', xy=(7, 6), xytext=(8, 6),
               arrowprops=dict(arrowstyle='->', lw=2, color='#27AE60', linestyle='dashed'))

    # User uses liquid token
    defi_box = mpatches.FancyBboxPatch((0.5, 2), 6, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#9B59B6', alpha=0.2,
                                        edgecolor='#9B59B6', lw=2)
    ax.add_patch(defi_box)
    ax.text(3.5, 4, 'Meanwhile: Use stETH/rETH in DeFi', ha='center', fontsize=12, fontweight='bold', color='#8E44AD')

    uses = ['Collateral for loans', 'Liquidity provision', 'Yield farming']
    for i, use in enumerate(uses):
        ax.text(1.5 + i*2.2, 3.2, f'* {use}', fontsize=10)
    ax.text(3.5, 2.4, 'Double yield: Staking + DeFi returns', ha='center', fontsize=11, fontweight='bold')

    # Market leaders
    leaders_box = mpatches.FancyBboxPatch((7.5, 2), 6, 2.5,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#F8F9FA', alpha=0.9,
                                           edgecolor='#CCC', lw=1)
    ax.add_patch(leaders_box)
    ax.text(10.5, 4, 'Market Leaders (Dec 2024)', ha='center', fontsize=12, fontweight='bold')

    leaders = [
        ('Lido (stETH)', '29% of staked ETH'),
        ('Rocket Pool (rETH)', '3% of staked ETH'),
        ('Coinbase (cbETH)', '2% of staked ETH'),
    ]
    for i, (name, share) in enumerate(leaders):
        ax.text(8.5, 3.3 - i*0.5, name, fontsize=10, fontweight='bold')
        ax.text(12, 3.3 - i*0.5, share, fontsize=10, ha='right')

    # Risk warning
    ax.text(7, 0.8, 'Risks: Smart contract bugs, centralization concerns, peg stability',
           ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    # Source
    fig.text(0.5, 0.02, 'Source: DeFiLlama, Lido Finance, Rated.network (Dec 2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'liquid_staking_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
