"""
Finality Comparison
Compares finality mechanisms in different blockchains

Output: finality_comparison.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Finality Comparison',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/finality_comparison'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create finality comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    blockchains = ['Bitcoin\n(PoW)', 'Ethereum\n(PoS)', 'Solana\n(PoH)', 'Avalanche\n(Snow)', 'Cosmos\n(Tendermint)']
    finality_time = [60, 12.8, 0.4, 1, 6]  # minutes
    finality_type = ['Probabilistic', 'Economic', 'Optimistic', 'Probabilistic', 'Absolute']
    colors = ['#F39C12', '#3498DB', '#9B59B6', '#E74C3C', '#27AE60']

    bars = ax.bar(blockchains, finality_time, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    ax.set_ylabel('Time to Finality (minutes)', fontsize=14)
    ax.set_title('Blockchain Finality Comparison', fontsize=18, fontweight='bold', pad=20)

    # Add value labels
    for bar, time, ftype in zip(bars, finality_time, finality_type):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
               f'{time} min', ha='center', fontsize=12, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, height/2,
               ftype, ha='center', fontsize=9, color='white', fontweight='bold', rotation=90 if height > 10 else 0)

    ax.set_ylim(0, 75)
    ax.grid(axis='y', alpha=0.3)

    # Note about Bitcoin
    ax.annotate('6 confirmations\nstandard', xy=(0, 60), xytext=(0.8, 70),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#666'))

    # Finality types explanation
    ax.text(0.5, -0.15, 'Probabilistic: Reversible but increasingly unlikely | Economic: Costly to reverse | Absolute: Mathematically final',
           transform=ax.transAxes, ha='center', fontsize=10, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Blockchain protocol documentation, Messari Research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'finality_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
