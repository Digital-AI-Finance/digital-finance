"""
FinTech vs Traditional Banking Comparison
Shows key metrics comparison

Output: fintech_traditional_comparison.pdf
Module: module_04_traditional
Lesson: 38 - Core Banking
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    metrics = ['Account\nOpening', 'Cost per\nTransaction', 'Loan\nApproval', 'Customer\nAcquisition', 'IT\nSpending']

    # Values (normalized where lower is better, except IT spending)
    traditional = [5, 3, 7, 300, 10]  # Days, $, Days, $, % of revenue
    fintech = [0.5, 0.5, 1, 50, 25]

    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax.bar(x - width/2, traditional, width, label='Traditional Bank', color=MLBLUE)
    bars2 = ax.bar(x + width/2, fintech, width, label='FinTech/Neobank', color=MLORANGE)

    ax.set_ylabel('Value (Various Units)', fontsize=11)
    ax.set_title('Traditional Banks vs FinTech: Key Metrics', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend(loc='upper right', framealpha=0.9)

    # Add unit labels
    units = ['days', '$', 'days', '$', '% rev']
    for i, (t, f, u) in enumerate(zip(traditional, fintech, units)):
        ax.text(i - width/2, t + max(traditional)*0.02, f'{t} {u}', ha='center', fontsize=7, color=MLBLUE)
        ax.text(i + width/2, f + max(traditional)*0.02, f'{f} {u}', ha='center', fontsize=7, color=MLORANGE)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Industry estimates]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_traditional_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
