"""
Copy Trading Flow
Shows how copy trading works

Output: copy_trading_flow.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Copy Trading Flow',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/copy_trading_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create copy trading flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Copy Trading: How It Works', fontsize=20, fontweight='bold', ha='center')

    # Expert trader
    expert_box = mpatches.FancyBboxPatch((1, 5), 3, 2.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#4A90E2', alpha=0.2,
                                          edgecolor='#4A90E2', lw=2)
    ax.add_patch(expert_box)
    ax.text(2.5, 7, 'Expert Trader', ha='center', fontsize=14, fontweight='bold', color='#4A90E2')
    ax.text(2.5, 6.4, 'Track record: +35%/yr', ha='center', fontsize=11)
    ax.text(2.5, 5.9, 'Risk score: 4/10', ha='center', fontsize=11)
    ax.text(2.5, 5.4, 'Copiers: 5,000+', ha='center', fontsize=11)

    # Action
    ax.annotate('', xy=(5.5, 6.25), xytext=(4.2, 6.25),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(4.85, 6.8, 'Buys AAPL', ha='center', fontsize=12, fontweight='bold')

    # Platform
    platform_box = mpatches.FancyBboxPatch((5.5, 5), 3, 2.5,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#FF7F0E', alpha=0.2,
                                            edgecolor='#FF7F0E', lw=2)
    ax.add_patch(platform_box)
    ax.text(7, 7, 'Platform', ha='center', fontsize=14, fontweight='bold', color='#FF7F0E')
    ax.text(7, 6.4, 'Detects trade', ha='center', fontsize=11)
    ax.text(7, 5.9, 'Calculates allocations', ha='center', fontsize=11)
    ax.text(7, 5.4, 'Executes copies', ha='center', fontsize=11)

    # Arrow to copiers
    ax.annotate('', xy=(9.8, 6.25), xytext=(8.7, 6.25),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(9.25, 6.8, 'Auto-replicates', ha='center', fontsize=12, fontweight='bold')

    # Copier accounts
    copier_box = mpatches.FancyBboxPatch((10, 4.5), 3, 3.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#44A044', alpha=0.2,
                                          edgecolor='#44A044', lw=2)
    ax.add_patch(copier_box)
    ax.text(11.5, 7.5, 'Copier Accounts', ha='center', fontsize=14, fontweight='bold', color='#44A044')
    ax.text(11.5, 6.8, 'User A (USD 1,000):', ha='center', fontsize=10)
    ax.text(11.5, 6.4, 'Buys USD 50 AAPL', ha='center', fontsize=10, style='italic')
    ax.text(11.5, 5.8, 'User B (USD 10,000):', ha='center', fontsize=10)
    ax.text(11.5, 5.4, 'Buys USD 500 AAPL', ha='center', fontsize=10, style='italic')
    ax.text(11.5, 4.9, '(Proportional allocation)', ha='center', fontsize=9)

    # Key considerations
    considerations = """Key Considerations:
    - Past performance not guaranteed
    - Expert incentives (fees from copiers)
    - Liquidity impact on large copy pools
    - Stop-loss and risk settings"""

    ax.text(4, 2.5, considerations, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Scale
    scale = "Copy Trading Scale: USD 2T+ assets copied globally (2024)"
    ax.text(10, 2.5, scale, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[ILLUSTRATIVE WORKFLOW]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'copy_trading_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
