"""
DeFi TVL Growth
Line chart showing Total Value Locked over time

Output: defi_tvl_growth.pdf
Module: module_02_blockchain
Lesson: 21 - DeFi
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'DeFi TVL Growth',
    'module': 'module_02_blockchain',
    'lesson': 21,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/defi_tvl_growth'
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
    """Create DeFi TVL growth line chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Synthetic data based on real DeFi TVL trends
    dates = ['2019\nQ1', 'Q3', '2020\nQ1', 'Q3', '2021\nQ1', 'Q3', '2022\nQ1', 'Q3', '2023\nQ1', 'Q3', '2024\nQ1', 'Q3']
    tvl = [0.5, 0.8, 1, 12, 45, 180, 200, 55, 50, 45, 90, 110]  # Billions USD

    x = np.arange(len(dates))
    ax.plot(x, tvl, 'b-', linewidth=4, marker='o', markersize=12, color='#3498DB')
    ax.fill_between(x, tvl, alpha=0.2, color='#3498DB')

    # Key events
    ax.annotate('DeFi Summer', xy=(5, 180), xytext=(4, 220),
               fontsize=14, arrowprops=dict(arrowstyle='->', color='#27AE60', lw=2),
               bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    ax.annotate('UST/Luna\nCollapse', xy=(7, 55), xytext=(8, 120),
               fontsize=14, arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2),
               bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    ax.annotate('ATH: $180B', xy=(5, 180), xytext=(5, 180), fontsize=12)

    ax.set_xlabel('Time Period', fontsize=20)
    ax.set_ylabel('Total Value Locked ($ Billions)', fontsize=20)
    ax.set_title('DeFi Total Value Locked (2019-2024)', fontsize=28, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(dates, fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 250)

    fig.text(0.5, 0.02, 'Source: DeFiLlama (Dec 2024) [SYNTHETIC ILLUSTRATION]',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'defi_tvl_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
