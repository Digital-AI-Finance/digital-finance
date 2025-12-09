"""
P2P Lending Market Growth
Shows global P2P lending market size and growth

Output: p2p_market_growth.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'P2P Lending Market Growth',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_market_growth'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P market growth chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Data
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    # Global P2P lending market size in $B (including China before collapse)
    market_size = [25, 64, 128, 180, 67, 83, 115, 150, 195, 230]

    # Plot
    bars = ax.bar(years, market_size, color='#4A90E2', edgecolor='#333333', lw=1.5)

    # Highlight China collapse impact
    for i, (year, size) in enumerate(zip(years, market_size)):
        if year == 2019:
            bars[i].set_color('#D62728')
            bars[i].set_alpha(0.7)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Global Market Size ($B)', fontsize=12)
    ax.set_title('P2P Lending Market Growth', fontsize=17, fontweight='bold', pad=15)

    ax.set_xticks(years)
    ax.set_xticklabels(years, fontsize=10)
    ax.set_ylim(0, 260)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, market_size):
        ax.annotate(f'${val}B',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=10)

    # Annotation for China collapse
    ax.annotate('China P2P\nCollapse\n(2018-2019)', xy=(2019, 67), xytext=(2016.5, 100),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#D62728'),
               bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Key stats
    stats = """Key Markets (2024):
    US: $80B+
    UK: $15B+
    China: $10B (down from $180B)
    Europe: $25B+
    Source: Statista, PwC"""

    ax.text(0.02, 0.98, stats, transform=ax.transAxes, fontsize=10, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_market_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
