"""
Mining Pool Distribution
Shows the distribution of Bitcoin hashrate among major mining pools

Output: mining_pool_distribution.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Mining Pool Distribution',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/mining_pool_distribution'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create mining pool distribution pie chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

    # Current distribution (2024 data)
    pools = ['Foundry USA', 'AntPool', 'F2Pool', 'ViaBTC', 'Binance Pool', 'MARA Pool', 'Others']
    shares = [27, 18, 14, 11, 8, 5, 17]
    colors = ['#3498DB', '#E74C3C', '#F39C12', '#27AE60', '#9B59B6', '#1ABC9C', '#95A5A6']

    # Pie chart
    wedges, texts, autotexts = ax1.pie(shares, labels=pools, autopct='%1.1f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0, 0])
    ax1.set_title('Bitcoin Mining Pool Distribution (Dec 2024)', fontsize=16, fontweight='bold')

    for autotext in autotexts:
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    for text in texts:
        text.set_fontsize(11)

    # Concentration metrics bar chart
    metrics = ['Top 2 Pools', 'Top 5 Pools', 'Top 10 Pools']
    concentration = [45, 78, 95]
    bars = ax2.barh(metrics, concentration, color=['#E74C3C', '#F39C12', '#27AE60'], alpha=0.8, edgecolor='black')
    ax2.set_xlim(0, 100)
    ax2.set_xlabel('% of Total Hashrate', fontsize=14)
    ax2.set_title('Mining Pool Concentration', fontsize=16, fontweight='bold')

    # Add percentage labels
    for bar, pct in zip(bars, concentration):
        ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'{pct}%',
                va='center', fontsize=14, fontweight='bold')

    # 51% attack line
    ax2.axvline(x=51, color='#E74C3C', linestyle='--', linewidth=2)
    ax2.text(52, 2.2, '51% Attack\nThreshold', fontsize=10, color='#E74C3C')

    # Add warning box
    ax2.text(0.5, -0.15, 'Centralization Risk: Top 2 pools control 45% of hashrate',
            transform=ax2.transAxes, fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    ax2.grid(axis='x', alpha=0.3)

    # Source
    fig.text(0.5, 0.02, 'Source: BTC.com Pool Stats (December 2024) [SYNTHETIC ILLUSTRATION]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mining_pool_distribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
