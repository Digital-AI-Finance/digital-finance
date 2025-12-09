"""
N26 European Expansion Map
Shows N26's growth across European markets

Output: n26_expansion.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'N26 European Expansion',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/n26_expansion'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create N26 expansion timeline and market presence chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Timeline of expansion
    years = [2013, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    milestones = [
        'Founded in Berlin',
        'German launch',
        'EU expansion (6 markets)',
        'UK launch',
        '2.5M customers',
        'US launch, $3.5B valuation',
        'UK exit (Brexit)',
        '7M customers',
        'Profitability path',
        '8M+ customers',
        'Focus on core EU markets'
    ]

    customers_millions = [0, 0.1, 0.5, 1.0, 2.5, 3.5, 5.0, 7.0, 7.5, 8.0, 8.5]

    ax1.plot(years, customers_millions, 'o-', color='#4A90E2', lw=2, markersize=8)
    ax1.fill_between(years, customers_millions, alpha=0.2, color='#4A90E2')

    # Milestone annotations (alternating above/below)
    for i, (year, milestone, cust) in enumerate(zip(years, milestones, customers_millions)):
        if i % 2 == 0:
            ax1.annotate(milestone, xy=(year, cust), xytext=(0, 15),
                        textcoords='offset points', ha='center', fontsize=7,
                        arrowprops=dict(arrowstyle='-', color='#999999', lw=0.5))
        else:
            ax1.annotate(milestone, xy=(year, cust), xytext=(0, -20),
                        textcoords='offset points', ha='center', fontsize=7,
                        arrowprops=dict(arrowstyle='-', color='#999999', lw=0.5))

    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Customers (Millions)', fontsize=11)
    ax1.set_title('N26 Growth Timeline', fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlim(2012, 2025)
    ax1.set_ylim(0, 10)
    ax1.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Right: Market presence by region
    ax2.axis('off')

    # European markets
    markets = [
        ('Germany', 'HQ', '#333333', 3.0),
        ('France', 'Core', '#4A90E2', 1.5),
        ('Spain', 'Core', '#4A90E2', 1.2),
        ('Italy', 'Core', '#4A90E2', 1.0),
        ('Austria', 'Core', '#4A90E2', 0.8),
        ('Netherlands', 'Growing', '#44A044', 0.5),
        ('Belgium', 'Growing', '#44A044', 0.4),
        ('Ireland', 'Growing', '#44A044', 0.3),
        ('Portugal', 'Growing', '#44A044', 0.3),
        ('Other EU', 'Various', '#999999', 0.5),
    ]

    # Sort by customer base
    markets_sorted = sorted(markets, key=lambda x: x[3], reverse=True)

    y_positions = np.arange(len(markets_sorted))
    bars = ax2.barh(y_positions, [m[3] for m in markets_sorted],
                    color=[m[2] for m in markets_sorted], edgecolor='#333333', lw=0.5)

    ax2.set_yticks(y_positions)
    ax2.set_yticklabels([m[0] for m in markets_sorted])
    ax2.set_xlabel('Estimated Customers (Millions)', fontsize=10)
    ax2.set_title('N26 Market Presence by Country', fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlim(0, 4)
    ax2.axis('on')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Value labels
    for i, (market, status, color, value) in enumerate(markets_sorted):
        ax2.text(value + 0.1, i, f'{value}M', va='center', fontsize=8)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#333333', edgecolor='#333333', label='Headquarters'),
        mpatches.Patch(facecolor='#4A90E2', edgecolor='#333333', label='Core Markets'),
        mpatches.Patch(facecolor='#44A044', edgecolor='#333333', label='Growth Markets'),
        mpatches.Patch(facecolor='#999999', edgecolor='#333333', label='Other'),
    ]
    ax2.legend(handles=legend_elements, loc='lower right', fontsize=8)

    # Main title
    fig.suptitle('N26: European Digital Banking Leader', fontsize=14, fontweight='bold', y=1.02)

    # Key facts box
    facts = """Key Facts:
    - German banking license (BaFin)
    - Mobile-first, no branches
    - Withdrew from UK (2020) & US (2022)
    - Focus on EU profitability"""

    fig.text(0.98, 0.02, facts, fontsize=7, ha='right', va='bottom',
            bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Synthetic label
    fig.text(0.02, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
            ha='left', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'n26_expansion.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
