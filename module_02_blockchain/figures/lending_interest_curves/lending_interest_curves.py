"""
Lending Interest Rate Curves
Shows how DeFi lending rates change with utilization

Output: lending_interest_curves.pdf
Module: module_02_blockchain
Lesson: 21 - DeFi
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Lending Interest Rate Curves',
    'module': 'module_02_blockchain',
    'lesson': 21,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/lending_interest_curves'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create lending interest rate curves"""
    fig, ax = plt.subplots(figsize=(12, 8))

    utilization = np.linspace(0, 100, 200)

    # Kinked interest rate model (like Aave/Compound)
    optimal_util = 80
    base_rate = 2
    slope1 = 4  # Before kink
    slope2 = 75  # After kink (steep)

    borrow_rate = np.where(
        utilization <= optimal_util,
        base_rate + (utilization / optimal_util) * slope1,
        base_rate + slope1 + ((utilization - optimal_util) / (100 - optimal_util)) * slope2
    )

    supply_rate = borrow_rate * (utilization / 100) * 0.85  # 85% to suppliers

    ax.plot(utilization, borrow_rate, 'r-', linewidth=4, label='Borrow Rate')
    ax.plot(utilization, supply_rate, 'g-', linewidth=4, label='Supply Rate')

    # Mark optimal utilization
    ax.axvline(x=80, color='#F39C12', linestyle='--', linewidth=2, label='Optimal (80%)')
    ax.fill_betweenx([0, 100], 0, 80, alpha=0.05, color='green')
    ax.fill_betweenx([0, 100], 80, 100, alpha=0.1, color='red')

    ax.set_xlabel('Utilization Rate (%)', fontsize=20)
    ax.set_ylabel('Interest Rate (% APY)', fontsize=20)
    ax.set_title('DeFi Lending Interest Rate Model', fontsize=28, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Annotations
    ax.annotate('Low rates\nencourage\nborrowing', xy=(40, 15), fontsize=14, ha='center', color='#27AE60')
    ax.annotate('High rates\ndiscourage\nborrowing', xy=(90, 60), fontsize=14, ha='center', color='#E74C3C')

    fig.text(0.5, 0.02, 'Source: Aave Protocol Documentation, Compound Finance',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'lending_interest_curves.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
