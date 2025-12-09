"""
DAI Peg History
Line chart showing DAI's price stability over time

Output: dai_peg_history.pdf
Module: module_02_blockchain
Lesson: 22 - Stablecoins
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'DAI Peg History',
    'module': 'module_02_blockchain',
    'lesson': 22,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/dai_peg_history'
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
    """Create DAI peg history line chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Synthetic data based on real DAI price behavior
    np.random.seed(42)
    days = 365 * 3  # 3 years
    x = np.arange(days)

    # Base price with small deviations
    price = 1.0 + np.random.normal(0, 0.005, days)

    # Add some stress events
    price[100:120] = 1.0 + np.random.normal(0.03, 0.01, 20)  # Black Thursday
    price[400:420] = 1.0 + np.random.normal(-0.02, 0.01, 20)  # Minor depeg
    price[700:730] = 1.0 + np.random.normal(0.015, 0.005, 30)  # USDC depeg contagion

    ax.plot(x, price, 'b-', linewidth=1.5, alpha=0.8)
    ax.axhline(y=1.0, color='#27AE60', linestyle='--', linewidth=2, label='$1.00 Target')
    ax.fill_between(x, 0.99, 1.01, alpha=0.1, color='green', label='1% band')

    # Mark events
    ax.annotate('Black Thursday\n(Mar 2020)', xy=(110, 1.03), xytext=(110, 1.06),
               fontsize=12, ha='center', arrowprops=dict(arrowstyle='->', color='#E74C3C'))
    ax.annotate('USDC Depeg\n(Mar 2023)', xy=(710, 1.015), xytext=(710, 1.04),
               fontsize=12, ha='center', arrowprops=dict(arrowstyle='->', color='#F39C12'))

    ax.set_xlabel('Days', fontsize=20)
    ax.set_ylabel('DAI Price (USD)', fontsize=20)
    ax.set_title('DAI Stablecoin Peg Stability (3-Year)', fontsize=28, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.95, 1.08)

    # Stats box
    ax.text(0.02, 0.98, f'Mean: ${price.mean():.4f}\nStd: ${price.std():.4f}',
           transform=ax.transAxes, fontsize=14, va='top',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    fig.text(0.5, 0.02, 'Source: CoinGecko, MakerDAO Dashboard [SYNTHETIC ILLUSTRATION]',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'dai_peg_history.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
