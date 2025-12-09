"""
Difficulty Adjustment
Shows how Bitcoin adjusts mining difficulty every 2016 blocks

Output: difficulty_adjustment.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Difficulty Adjustment',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/difficulty_adjustment'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create difficulty adjustment diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Title
    ax.set_title('Bitcoin Difficulty Adjustment Mechanism', fontsize=20, fontweight='bold', pad=20)

    # Data for visualization
    epochs = ['Epoch 1', 'Epoch 2', 'Epoch 3', 'Epoch 4', 'Epoch 5']
    actual_time = [12, 14, 10, 8, 14]  # days to mine 2016 blocks
    target_time = [14, 14, 14, 14, 14]  # target is always 14 days

    x = np.arange(len(epochs))
    width = 0.35

    bars1 = ax.bar(x - width/2, actual_time, width, label='Actual Time', color='#3498DB', alpha=0.8)
    bars2 = ax.bar(x + width/2, target_time, width, label='Target (14 days)', color='#E74C3C', alpha=0.8)

    ax.set_xlabel('Mining Epoch (2016 blocks each)', fontsize=14)
    ax.set_ylabel('Days to Mine Epoch', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(epochs, fontsize=12)
    ax.legend(fontsize=12)
    ax.set_ylim(0, 18)

    # Add adjustment annotations
    adjustments = ['+16.7%', '-14.3%', '+40%', '-42.9%']
    adj_colors = ['#E74C3C', '#27AE60', '#E74C3C', '#27AE60']
    for i, (adj, color) in enumerate(zip(adjustments, adj_colors)):
        ax.annotate(f'Difficulty\n{adj}', xy=(i + 0.5, 16), fontsize=10, ha='center',
                   bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height}d', xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords='offset points', ha='center', fontsize=11)

    # Formula box
    formula_text = 'New Difficulty = Old Difficulty x (Target Time / Actual Time)\nAdjusts every 2016 blocks (~2 weeks) to maintain 10-minute block target'
    ax.text(0.5, -0.18, formula_text, transform=ax.transAxes, ha='center', fontsize=12,
           bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#999'))

    # Source
    fig.text(0.5, 0.02, 'Source: Bitcoin Core Implementation, BIP-42 (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()

    output_path = Path(__file__).parent / 'difficulty_adjustment.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
