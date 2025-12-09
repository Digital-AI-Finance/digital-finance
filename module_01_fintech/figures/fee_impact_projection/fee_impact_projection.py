"""
Fee Impact Projection
Shows long-term impact of fees on portfolio growth

Output: fee_impact_projection.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Fee Impact Projection',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fee_impact_projection'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create fee impact projection chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Assumptions: $100K initial, 7% gross return, 30 years
    years = np.arange(0, 31)
    initial = 100000
    gross_return = 0.07

    # Different fee levels
    fees = {
        'No fees (theoretical)': 0.00,
        'Index funds (0.10%)': 0.001,
        'Robo-advisor (0.35%)': 0.0035,
        'Traditional advisor (1.0%)': 0.01,
        'High-cost funds (1.5%)': 0.015,
    }

    colors = ['#44A044', '#4A90E2', '#FF7F0E', '#6B5B95', '#D62728']

    for (label, fee), color in zip(fees.items(), colors):
        net_return = gross_return - fee
        values = initial * (1 + net_return) ** years
        ax.plot(years, values / 1000, label=label, color=color, lw=2.5)

    ax.set_xlabel('Years', fontsize=14)
    ax.set_ylabel('Portfolio Value ($K)', fontsize=14)
    ax.set_title('Long-Term Impact of Fees on $100K Investment', fontsize=20, fontweight='bold', pad=15)

    ax.legend(loc='upper left', fontsize=11)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 900)

    ax.yaxis.grid(True, alpha=0.3)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Final values annotation
    final_values = """30-Year Final Values:
    No fees: $761K
    Index: $744K
    Robo: $693K
    Traditional: $574K
    High-cost: $501K"""

    ax.text(0.98, 0.35, final_values, transform=ax.transAxes, fontsize=11,
           va='top', ha='right',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Assumptions note
    ax.text(0.5, 0.02, 'Assumptions: $100K initial | 7% gross return | No additional contributions',
           transform=ax.transAxes, fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fee_impact_projection.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
