"""
Staking Options
Compares different ways to stake cryptocurrency

Output: staking_options.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Staking Options',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/staking_options'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create staking options comparison chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Ethereum Staking Options Comparison', fontsize=20, fontweight='bold', ha='center')

    # Options
    options = [
        {
            'name': 'Solo Staking',
            'x': 2.5, 'color': '#27AE60',
            'min': '32 ETH',
            'control': 'Full',
            'rewards': '100%',
            'complexity': 'High',
            'risk': 'Slashing',
        },
        {
            'name': 'Staking Pool',
            'x': 6, 'color': '#3498DB',
            'min': '0.01 ETH',
            'control': 'None',
            'rewards': '90-95%',
            'complexity': 'Low',
            'risk': 'Pool risk',
        },
        {
            'name': 'Liquid Staking',
            'x': 9.5, 'color': '#F39C12',
            'min': 'Any amount',
            'control': 'Token',
            'rewards': '90-95%',
            'complexity': 'Low',
            'risk': 'Smart contract',
        },
        {
            'name': 'Exchange',
            'x': 12.5, 'color': '#9B59B6',
            'min': 'Any amount',
            'control': 'None',
            'rewards': '80-90%',
            'complexity': 'Very Low',
            'risk': 'Custodial',
        },
    ]

    # Draw option boxes
    for opt in options:
        # Header
        header_box = mpatches.FancyBboxPatch((opt['x']-1.5, 8), 3, 1.3,
                                              boxstyle='round,pad=0.1',
                                              facecolor=opt['color'], alpha=0.8,
                                              edgecolor='black', lw=2)
        ax.add_patch(header_box)
        ax.text(opt['x'], 8.8, opt['name'], ha='center', fontsize=12, fontweight='bold', color='white')

        # Details
        details_box = mpatches.FancyBboxPatch((opt['x']-1.5, 3), 3, 4.8,
                                               boxstyle='round,pad=0.1',
                                               facecolor=opt['color'], alpha=0.15,
                                               edgecolor=opt['color'], lw=1.5)
        ax.add_patch(details_box)

        # Attributes
        attrs = [
            ('Min:', opt['min']),
            ('Control:', opt['control']),
            ('Rewards:', opt['rewards']),
            ('Complexity:', opt['complexity']),
            ('Risk:', opt['risk']),
        ]

        for i, (label, value) in enumerate(attrs):
            y = 7.2 - i * 0.9
            ax.text(opt['x']-1.3, y, label, fontsize=10, fontweight='bold')
            ax.text(opt['x']+1.3, y, value, fontsize=10, ha='right')

    # Examples row
    examples = ['Run your own\nnode + validator', 'Rocket Pool,\nStakeWise', 'Lido (stETH),\nRocket Pool (rETH)', 'Coinbase,\nKraken']
    for i, (opt, ex) in enumerate(zip(options, examples)):
        ax.text(opt['x'], 2.5, 'Example:', fontsize=9, fontweight='bold', ha='center')
        ax.text(opt['x'], 1.8, ex, fontsize=9, ha='center', style='italic')

    # Recommendation
    rec_box = mpatches.FancyBboxPatch((1, 0.3), 12, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F8F9FA', alpha=0.9,
                                       edgecolor='#999', lw=1)
    ax.add_patch(rec_box)
    ax.text(7, 0.8, 'Recommendation: Balance control vs complexity based on your technical ability and amount',
           ha='center', fontsize=11, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Ethereum.org Staking Guide, DeFiLlama (Dec 2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'staking_options.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
