"""
AMM Bonding Curve
Shows the constant product formula x*y=k

Output: amm_bonding_curve.pdf
Module: module_02_blockchain
Lesson: 21 - DeFi
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'AMM Bonding Curve',
    'module': 'module_02_blockchain',
    'lesson': 21,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/amm_bonding_curve'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create AMM bonding curve visualization"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Constant product curve: x * y = k
    k = 10000
    x = np.linspace(10, 200, 500)
    y = k / x

    ax.plot(x, y, 'b-', linewidth=4, label='x * y = k (constant product)')
    ax.fill_between(x, y, alpha=0.1, color='blue')

    # Mark a trade
    x1, y1 = 50, 200
    x2, y2 = 100, 100
    ax.plot([x1, x2], [y1, y2], 'r--', linewidth=2, alpha=0.7)
    ax.scatter([x1, x2], [y1, y2], s=200, c=['green', 'red'], zorder=5, edgecolors='black', linewidths=2)
    ax.annotate('Before swap', (x1, y1), textcoords='offset points', xytext=(-60, 20), fontsize=16)
    ax.annotate('After swap', (x2, y2), textcoords='offset points', xytext=(20, 20), fontsize=16)

    # Arrow showing trade
    ax.annotate('', xy=(x2-5, y2+5), xytext=(x1+5, y1-5),
               arrowprops=dict(arrowstyle='->', lw=3, color='#E74C3C'))
    ax.text(75, 170, 'SWAP', fontsize=18, fontweight='bold', color='#E74C3C', ha='center')

    ax.set_xlabel('Token A Reserve', fontsize=20)
    ax.set_ylabel('Token B Reserve', fontsize=20)
    ax.set_title('AMM Constant Product Formula', fontsize=28, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 220)
    ax.set_ylim(0, 250)

    # Formula box
    ax.text(150, 220, 'x * y = k\n(k stays constant)', fontsize=18, ha='center',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60', lw=2))

    fig.text(0.5, 0.02, 'Source: Uniswap Whitepaper (2018), Bancor Protocol',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'amm_bonding_curve.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
