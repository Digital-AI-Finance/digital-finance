"""
Asset Allocation Profiles
Shows typical robo-advisor asset allocation by risk profile

Output: asset_allocation_profiles.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Asset Allocation Profiles',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/asset_allocation_profiles'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create asset allocation profiles chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    profiles = ['Conservative', 'Moderate-\nConservative', 'Moderate', 'Moderate-\nAggressive', 'Aggressive']

    # Asset classes (in %)
    us_stocks = [15, 30, 45, 60, 70]
    intl_stocks = [5, 10, 15, 20, 20]
    bonds = [60, 45, 30, 15, 5]
    real_estate = [5, 5, 5, 3, 3]
    commodities = [5, 5, 3, 2, 2]
    cash = [10, 5, 2, 0, 0]

    x = np.arange(len(profiles))
    width = 0.6

    # Stacked bar chart
    ax.bar(x, us_stocks, width, label='US Stocks', color='#4A90E2')
    ax.bar(x, intl_stocks, width, bottom=us_stocks, label='Intl Stocks', color='#44A044')
    ax.bar(x, bonds, width, bottom=np.array(us_stocks)+np.array(intl_stocks), label='Bonds', color='#FF7F0E')
    ax.bar(x, real_estate, width, bottom=np.array(us_stocks)+np.array(intl_stocks)+np.array(bonds),
           label='Real Estate', color='#6B5B95')
    ax.bar(x, commodities, width,
           bottom=np.array(us_stocks)+np.array(intl_stocks)+np.array(bonds)+np.array(real_estate),
           label='Commodities', color='#D62728')
    ax.bar(x, cash, width,
           bottom=np.array(us_stocks)+np.array(intl_stocks)+np.array(bonds)+np.array(real_estate)+np.array(commodities),
           label='Cash', color='#999999')

    ax.set_ylabel('Allocation (%)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(profiles, fontsize=12)
    ax.set_ylim(0, 105)
    ax.legend(loc='upper right', fontsize=11, ncol=2)
    ax.set_title('Robo-Advisor Asset Allocation by Risk Profile', fontsize=20, fontweight='bold', pad=15)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add total equity labels
    for i, (us, intl) in enumerate(zip(us_stocks, intl_stocks)):
        total_equity = us + intl
        ax.annotate(f'{total_equity}% equity', xy=(i, total_equity/2),
                   ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Source
    fig.text(0.5, 0.02, 'Source: Typical robo-advisor allocation models [ILLUSTRATIVE]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'asset_allocation_profiles.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
