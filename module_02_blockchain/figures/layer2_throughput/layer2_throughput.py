"""
Layer 2 Throughput Comparison
Bar chart comparing L2 scaling solutions TPS

Output: layer2_throughput.pdf
Module: module_02_blockchain
Lesson: 24 - Regulation & Future
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Layer 2 Throughput Comparison',
    'module': 'module_02_blockchain',
    'lesson': 24,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/layer2_throughput'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 14,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create L2 throughput comparison chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    solutions = ['Ethereum\nL1', 'Arbitrum', 'Optimism', 'Base', 'zkSync', 'Polygon\nzkEVM', 'StarkNet']
    tps = [15, 40000, 2000, 2000, 10000, 2000, 5000]  # Theoretical max TPS
    tvl = [50, 12, 7, 6, 1.5, 0.5, 0.3]  # TVL in billions
    colors = ['#95A5A6', '#3498DB', '#E74C3C', '#3498DB', '#9B59B6', '#9B59B6', '#9B59B6']

    x = np.arange(len(solutions))
    width = 0.6

    bars = ax.bar(x, tps, width, color=colors, alpha=0.85, edgecolor='black', linewidth=2)

    ax.set_yscale('log')
    ax.set_ylabel('Transactions per Second (TPS)', fontsize=20)
    ax.set_title('Layer 2 Scaling Solutions: Throughput', fontsize=26, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(solutions, fontsize=14)
    ax.set_ylim(10, 100000)

    # Add TPS labels
    for bar, t in zip(bars, tps):
        label = f'{t/1000:.0f}K' if t >= 1000 else str(t)
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.3,
               label, ha='center', fontsize=14, fontweight='bold')

    # Add TVL as secondary info
    for i, (bar, t) in enumerate(zip(bars, tvl)):
        ax.text(bar.get_x() + bar.get_width()/2, 20,
               f'TVL: ${t}B', ha='center', fontsize=11, color='white', fontweight='bold')

    # Legend for rollup types
    ax.text(0.98, 0.95, 'Optimistic Rollups: Blue\nZK Rollups: Purple',
           transform=ax.transAxes, fontsize=12, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    ax.grid(axis='y', alpha=0.3, which='both')

    fig.text(0.5, 0.02, 'Source: L2Beat.com, Rollup Documentation (Dec 2024)',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'layer2_throughput.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
