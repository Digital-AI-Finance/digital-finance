"""
Institutional Crypto Adoption
Line chart showing institutional investment trends

Output: institutional_crypto_adoption.pdf
Module: module_02_blockchain
Lesson: 24 - Regulation & Future
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Institutional Crypto Adoption',
    'module': 'module_02_blockchain',
    'lesson': 24,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/institutional_crypto_adoption'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 14,
    'ytick.labelsize': 16,
    'legend.fontsize': 14,
})

def create_chart():
    """Create institutional adoption trend chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    x = np.arange(len(years))

    # Different institutional metrics
    hedge_funds = [10, 25, 47, 38, 45, 55]  # % with crypto exposure
    pension_funds = [1, 2, 5, 4, 8, 12]
    family_offices = [15, 30, 55, 40, 50, 62]

    ax.plot(x, hedge_funds, 'b-', linewidth=4, marker='o', markersize=12, label='Hedge Funds')
    ax.plot(x, pension_funds, 'g-', linewidth=4, marker='s', markersize=12, label='Pension Funds')
    ax.plot(x, family_offices, 'r-', linewidth=4, marker='^', markersize=12, label='Family Offices')

    # Key events
    ax.axvline(x=5, color='#F39C12', linestyle='--', linewidth=2, alpha=0.7)
    ax.annotate('BTC ETF\nApproved', xy=(5, 60), xytext=(4.5, 70),
               fontsize=12, arrowprops=dict(arrowstyle='->', color='#F39C12'),
               bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#F39C12'))

    ax.set_xlabel('Year', fontsize=20)
    ax.set_ylabel('% with Crypto Allocation', fontsize=20)
    ax.set_title('Institutional Crypto Adoption Trends', fontsize=26, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 80)

    fig.text(0.5, 0.02, 'Source: Fidelity Digital Assets Survey, PwC Crypto Hedge Fund Report (2024) [ILLUSTRATIVE]',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'institutional_crypto_adoption.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
