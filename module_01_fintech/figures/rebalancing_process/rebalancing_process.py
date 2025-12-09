"""
Portfolio Rebalancing Process
Shows how robo-advisors automatically rebalance portfolios

Output: rebalancing_process.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Rebalancing Process',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/rebalancing_process'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create rebalancing process diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Automatic Portfolio Rebalancing', fontsize=20, fontweight='bold', ha='center')

    # Example scenario
    # Before (drifted) - left
    before_box = mpatches.FancyBboxPatch((0.5, 4), 4, 4.5, boxstyle='round,pad=0.1',
                                          facecolor='#D62728', alpha=0.15,
                                          edgecolor='#D62728', lw=2)
    ax.add_patch(before_box)
    ax.text(2.5, 8, 'Before: Drifted', ha='center', fontsize=14, fontweight='bold', color='#D62728')

    before_alloc = [
        ('Stocks', '75%', '(target: 60%)'),
        ('Bonds', '20%', '(target: 35%)'),
        ('Other', '5%', '(target: 5%)'),
    ]
    for i, (asset, pct, target) in enumerate(before_alloc):
        ax.text(1, 7.2-i*0.9, f'{asset}: {pct}', fontsize=12, fontweight='bold')
        ax.text(3, 7.2-i*0.9, target, fontsize=11, color='#666666')

    ax.text(2.5, 4.5, 'Stocks up 25%\nBonds flat', ha='center', fontsize=11,
           style='italic', color='#D62728')

    # Arrow
    ax.annotate('', xy=(5.5, 6), xytext=(4.7, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=3))
    ax.text(5.1, 6.5, 'Rebalance', fontsize=12, fontweight='bold', ha='center')

    # Rebalancing action (center)
    action_box = mpatches.FancyBboxPatch((5.5, 4), 3.5, 4.5, boxstyle='round,pad=0.1',
                                          facecolor='#FF7F0E', alpha=0.15,
                                          edgecolor='#FF7F0E', lw=2)
    ax.add_patch(action_box)
    ax.text(7.25, 8, 'Actions', ha='center', fontsize=14, fontweight='bold', color='#FF7F0E')

    actions = [
        'Sell: 15% stocks',
        'Buy: 15% bonds',
        'Tax-loss harvest',
        '(if applicable)',
    ]
    for i, action in enumerate(actions):
        ax.text(7.25, 7.2-i*0.8, action, ha='center', fontsize=12)

    # Arrow
    ax.annotate('', xy=(10, 6), xytext=(9.2, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=3))

    # After (rebalanced) - right
    after_box = mpatches.FancyBboxPatch((10, 4), 3.5, 4.5, boxstyle='round,pad=0.1',
                                         facecolor='#44A044', alpha=0.15,
                                         edgecolor='#44A044', lw=2)
    ax.add_patch(after_box)
    ax.text(11.75, 8, 'After: On Target', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    after_alloc = [
        ('Stocks', '60%'),
        ('Bonds', '35%'),
        ('Other', '5%'),
    ]
    for i, (asset, pct) in enumerate(after_alloc):
        ax.text(11.75, 7.2-i*0.8, f'{asset}: {pct}', ha='center', fontsize=12, fontweight='bold')

    # Rebalancing triggers
    triggers = """Rebalancing Triggers:
    - Drift threshold (e.g., 5% deviation)
    - Calendar-based (quarterly/annual)
    - Cash flow events (deposits)
    - Tax-loss harvesting opportunities"""

    ax.text(7, 2.5, triggers, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL EXAMPLE]', fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'rebalancing_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
