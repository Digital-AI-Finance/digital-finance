"""
Risk Grade Performance
Shows loan performance by risk grade in P2P lending

Output: risk_grade_performance.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Risk Grade Performance',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/risk_grade_performance'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create risk grade performance chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Risk grades
    grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Data (LendingClub-style metrics)
    interest_rates = [7.5, 10.5, 14.0, 18.5, 23.0, 27.5, 30.0]
    default_rates = [2.5, 4.5, 8.0, 12.0, 18.0, 25.0, 32.0]
    net_returns = [5.0, 6.0, 6.0, 6.5, 5.0, 2.5, -2.0]

    x = np.arange(len(grades))
    width = 0.25

    bars1 = ax.bar(x - width, interest_rates, width, label='Interest Rate (%)', color='#4A90E2')
    bars2 = ax.bar(x, default_rates, width, label='Default Rate (%)', color='#D62728')
    bars3 = ax.bar(x + width, net_returns, width, label='Net Return (%)', color='#44A044')

    ax.set_xlabel('Risk Grade', fontsize=12)
    ax.set_ylabel('Percentage (%)', fontsize=12)
    ax.set_title('P2P Loan Performance by Risk Grade', fontsize=17, fontweight='bold', pad=15)

    ax.set_xticks(x)
    ax.set_xticklabels(grades, fontsize=11)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_ylim(-5, 35)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add zero line for net returns
    ax.axhline(y=0, color='#333333', linestyle='--', lw=1)

    # Annotations
    ax.annotate('Highest risk-adjusted\nreturns', xy=(2, 6), xytext=(4, 15),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#44A044'),
               bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    ax.annotate('Negative returns\nafter defaults', xy=(6, -2), xytext=(5, -4),
               fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: LendingClub historical data patterns [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_grade_performance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
