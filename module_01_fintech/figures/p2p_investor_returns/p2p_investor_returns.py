"""
P2P Investor Returns
Shows historical returns for P2P lending investors

Output: p2p_investor_returns.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'P2P Investor Returns',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_investor_returns'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P investor returns chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

    # Returns by diversification level
    well_diversified = [8.5, 7.8, 6.5, 5.8, 5.2, 4.8, 3.5, 4.5, 5.0, 5.5]
    moderate = [9.5, 8.0, 5.5, 4.5, 4.0, 3.5, 1.5, 3.5, 4.0, 4.5]
    concentrated = [12.0, 8.5, 3.0, 2.0, 1.0, -1.0, -3.0, 1.5, 2.0, 3.0]

    ax.plot(years, well_diversified, 'o-', label='Well Diversified (500+ loans)',
            color='#44A044', lw=2, markersize=8)
    ax.plot(years, moderate, 's-', label='Moderate (100-500 loans)',
            color='#FF7F0E', lw=2, markersize=8)
    ax.plot(years, concentrated, '^-', label='Concentrated (<100 loans)',
            color='#D62728', lw=2, markersize=8)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Net Annual Return (%)', fontsize=12)
    ax.set_title('P2P Investor Returns by Diversification', fontsize=17, fontweight='bold', pad=15)

    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(-5, 15)

    ax.yaxis.grid(True, alpha=0.3)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Zero line
    ax.axhline(y=0, color='#333333', linestyle='--', lw=1)

    # S&P 500 comparison
    ax.fill_between([2014, 2023], [5, 5], [10, 10], alpha=0.1, color='#4A90E2',
                    label='_nolegend_')
    ax.text(2018.5, 7.5, 'S&P 500 avg: 7-10%', fontsize=10, color='#4A90E2',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Key insight
    insight = """Key Insight: Diversification across 500+ loans
    significantly reduces variance in returns"""
    ax.text(2014, -3.5, insight, fontsize=10,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: LendingClub investor statistics [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_investor_returns.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
