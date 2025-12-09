"""
Fee Comparison by Wealth Level
Compares fees across wealth management options

Output: fee_comparison_wealth.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Fee Comparison by Wealth',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fee_comparison_wealth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create fee comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    categories = ['DIY\nIndex Funds', 'Robo-\nAdvisor', 'Hybrid\nRobo', 'Independent\nRIA', 'Private\nWealth']

    # Fees (total annual cost %)
    fees = [0.10, 0.35, 0.55, 1.00, 1.50]

    # Minimum investment ($)
    minimums = ['$0', '$0-500', '$25K-100K', '$100K-500K', '$1M+']

    colors = ['#44A044', '#4A90E2', '#FF7F0E', '#6B5B95', '#D62728']

    bars = ax.bar(categories, fees, color=colors, edgecolor='#333333', lw=2, alpha=0.8)

    ax.set_ylabel('Total Annual Fee (%)', fontsize=14)
    ax.set_title('Fee Comparison: Investment Management Options', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 2.0)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add fee labels
    for bar, fee in zip(bars, fees):
        ax.annotate(f'{fee:.2f}%',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=13, fontweight='bold')

    # Add minimum labels below
    for i, (bar, min_inv) in enumerate(zip(bars, minimums)):
        ax.text(bar.get_x() + bar.get_width() / 2, -0.15, f'Min: {min_inv}',
               ha='center', fontsize=10, color='#666666')

    # Fee impact annotation
    impact = """Fee Impact Example ($100K, 30 years, 7% return):
    0.10%: $744K | 0.35%: $693K | 1.00%: $574K
    Difference: $170K in lifetime wealth"""

    ax.text(0.5, 0.98, impact, transform=ax.transAxes, fontsize=11,
           va='top', ha='center',
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    output_path = Path(__file__).parent / 'fee_comparison_wealth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
