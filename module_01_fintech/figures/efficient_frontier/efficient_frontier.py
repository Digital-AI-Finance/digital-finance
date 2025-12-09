"""
Efficient Frontier
Shows Modern Portfolio Theory efficient frontier

Output: efficient_frontier.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Efficient Frontier',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/efficient_frontier'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create efficient frontier chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Generate efficient frontier curve
    risk = np.linspace(5, 25, 100)
    # Expected return = sqrt function (diminishing returns for risk)
    returns = 2 + 2.5 * np.sqrt(risk - 4)

    # Plot efficient frontier
    ax.plot(risk, returns, 'b-', lw=3, label='Efficient Frontier', color='#4A90E2')
    ax.fill_between(risk, returns, 2, alpha=0.1, color='#4A90E2')

    # Plot sample portfolios on the frontier
    portfolios = [
        (6, 4.5, 'Conservative'),
        (10, 7.5, 'Moderate'),
        (15, 9.3, 'Balanced'),
        (20, 10.5, 'Growth'),
        (24, 11.2, 'Aggressive'),
    ]

    for r, ret, name in portfolios:
        ax.scatter(r, ret, s=150, c='#44A044', edgecolor='#333333', lw=2, zorder=5)
        ax.annotate(name, (r, ret), xytext=(5, 8), textcoords='offset points',
                   fontsize=11, fontweight='bold')

    # Inefficient portfolios (below frontier)
    inefficient = [
        (12, 5, 'Sub-optimal'),
        (18, 7, 'Inefficient'),
    ]
    for r, ret, name in inefficient:
        ax.scatter(r, ret, s=100, c='#D62728', marker='x', lw=3, zorder=5)
        ax.annotate(name, (r, ret), xytext=(5, -12), textcoords='offset points',
                   fontsize=10, color='#D62728')

    ax.set_xlabel('Risk (Standard Deviation %)', fontsize=14)
    ax.set_ylabel('Expected Return (%)', fontsize=14)
    ax.set_title('Efficient Frontier: Optimal Risk-Return Portfolios', fontsize=20, fontweight='bold', pad=15)

    ax.set_xlim(4, 26)
    ax.set_ylim(2, 13)
    ax.grid(True, alpha=0.3)

    # MPT explanation
    explanation = """Modern Portfolio Theory (Markowitz 1952):
    - Diversification reduces risk
    - Efficient frontier = best return for given risk
    - Robos optimize along this curve"""

    ax.text(0.98, 0.02, explanation, transform=ax.transAxes, fontsize=11,
           va='bottom', ha='right',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'efficient_frontier.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
