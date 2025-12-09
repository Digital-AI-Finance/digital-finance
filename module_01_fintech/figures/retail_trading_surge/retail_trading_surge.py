"""
Retail Trading Surge
Shows the post-2020 retail trading explosion

Output: retail_trading_surge.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Retail Trading Surge',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/retail_trading_surge'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create retail trading surge chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    # Retail share of equity trading volume (%)
    retail_share = [10, 12, 20, 25, 23, 22, 24]

    colors = ['#4A90E2'] * 2 + ['#D62728'] * 2 + ['#FF7F0E'] * 3

    bars = ax.bar(years, retail_share, color=colors, edgecolor='#333333', lw=1.5)

    ax.set_ylabel('Retail Share of US Equity Volume (%)', fontsize=14)
    ax.set_title('Rise of Retail Trading', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 35)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, retail_share):
        ax.annotate(f'{val}%',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Key events
    ax.annotate('COVID\nStimulus', xy=(2, 20), xytext=(2, 28),
               fontsize=11, ha='center',
               arrowprops=dict(arrowstyle='->', color='#D62728'))
    ax.annotate('Meme\nStocks', xy=(3, 25), xytext=(3, 32),
               fontsize=11, ha='center',
               arrowprops=dict(arrowstyle='->', color='#D62728'))

    # Key drivers
    drivers = """Drivers:
    - Commission-free trading
    - Mobile-first platforms
    - Fractional shares
    - Social media (Reddit, Twitter)
    - Stimulus checks + lockdowns"""

    ax.text(0.02, 0.98, drivers, transform=ax.transAxes, fontsize=11,
           va='top', bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: SEC, Bloomberg market structure data (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'retail_trading_surge.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
