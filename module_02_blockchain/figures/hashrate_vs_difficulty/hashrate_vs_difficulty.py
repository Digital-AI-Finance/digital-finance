"""
Hashrate vs Difficulty
Shows the relationship between network hashrate and mining difficulty

Output: hashrate_vs_difficulty.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Hashrate vs Difficulty',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/hashrate_vs_difficulty'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create hashrate vs difficulty chart"""
    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Generate synthetic data (based on real Bitcoin trends 2019-2024)
    years = np.array([2019, 2020, 2021, 2022, 2023, 2024])
    # Hashrate in EH/s (exahashes per second)
    hashrate = np.array([50, 120, 180, 250, 400, 650])
    # Difficulty in trillions
    difficulty = np.array([7, 20, 25, 35, 55, 95])

    color1 = '#3498DB'
    ax1.set_xlabel('Year', fontsize=14)
    ax1.set_ylabel('Network Hashrate (EH/s)', color=color1, fontsize=14)
    line1 = ax1.plot(years, hashrate, color=color1, marker='o', linewidth=3, markersize=10, label='Hashrate')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.fill_between(years, hashrate, alpha=0.2, color=color1)

    ax2 = ax1.twinx()
    color2 = '#E74C3C'
    ax2.set_ylabel('Mining Difficulty (Trillions)', color=color2, fontsize=14)
    line2 = ax2.plot(years, difficulty, color=color2, marker='s', linewidth=3, markersize=10, linestyle='--', label='Difficulty')
    ax2.tick_params(axis='y', labelcolor=color2)

    # Title
    ax1.set_title('Bitcoin Hashrate and Difficulty Correlation (2019-2024)', fontsize=20, fontweight='bold', pad=20)

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=12)

    # Correlation note
    ax1.text(0.98, 0.05, 'Correlation: ~0.99\nDifficulty adjusts to maintain\n10-minute block time as\nhashrate changes',
            transform=ax1.transAxes, fontsize=11, ha='right', va='bottom',
            bbox=dict(boxstyle='round', facecolor='#F0F0F0', edgecolor='#999'))

    # Key events
    ax1.annotate('China Mining Ban', xy=(2021.5, 180), xytext=(2021, 120),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='#666'),
                bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#F39C12'))

    ax1.annotate('ETF Approval', xy=(2024, 650), xytext=(2023.5, 550),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='#666'),
                bbox=dict(boxstyle='round', facecolor='#D4EDDA', edgecolor='#27AE60'))

    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(2018.8, 2024.2)

    # Source
    fig.text(0.5, 0.02, 'Source: Blockchain.com, CoinMetrics (Dec 2024) [SYNTHETIC DATA FOR ILLUSTRATION]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'hashrate_vs_difficulty.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
