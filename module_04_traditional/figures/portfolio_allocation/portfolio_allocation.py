"""
Portfolio Allocation by Risk Profile
Shows typical asset allocations

Output: portfolio_allocation.pdf
Module: module_04_traditional
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    profiles = ['Conservative', 'Moderate', 'Balanced', 'Growth', 'Aggressive']

    # Asset allocation percentages
    equities = [20, 35, 50, 70, 90]
    bonds = [50, 40, 30, 20, 5]
    alternatives = [10, 10, 10, 5, 3]
    cash = [20, 15, 10, 5, 2]

    x = np.arange(len(profiles))
    width = 0.6

    ax.bar(x, equities, width, label='Equities', color=MLBLUE)
    ax.bar(x, bonds, width, bottom=equities, label='Bonds', color=MLORANGE)
    ax.bar(x, alternatives, width, bottom=np.array(equities)+np.array(bonds),
           label='Alternatives', color=MLGREEN)
    ax.bar(x, cash, width,
           bottom=np.array(equities)+np.array(bonds)+np.array(alternatives),
           label='Cash', color=MLLAVENDER)

    ax.set_ylabel('Allocation (%)', fontsize=11)
    ax.set_title('Model Portfolio Allocations by Risk Profile', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(profiles)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 110)

    # Add expected return/risk annotations
    returns = ['4-5%', '5-6%', '6-7%', '7-8%', '8-10%']
    for i, ret in enumerate(returns):
        ax.text(i, 103, f'E[R]: {ret}', ha='center', fontsize=8, color='#555555')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical robo-advisor allocations]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'portfolio_allocation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
