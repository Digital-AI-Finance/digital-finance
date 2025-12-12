"""
Wealth Management Fee Comparison
Shows fees across different service types

Output: fee_comparison.pdf
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

    services = ['DIY\nBrokerage', 'Robo-\nAdvisor', 'Online\nAdvisor', 'Traditional\nAdvisor', 'Private\nBank']

    # Total annual fees as percentage of AUM
    fees_low = [0.0, 0.25, 0.50, 0.75, 1.0]
    fees_high = [0.05, 0.50, 0.80, 1.25, 2.0]

    x = np.arange(len(services))
    width = 0.4

    # Plot fee ranges
    for i, (low, high) in enumerate(zip(fees_low, fees_high)):
        ax.bar(i, high - low, width, bottom=low, color=MLBLUE, alpha=0.7)
        ax.plot([i-width/4, i+width/4], [low, low], color=MLBLUE, linewidth=2)
        ax.plot([i-width/4, i+width/4], [high, high], color=MLBLUE, linewidth=2)
        ax.text(i, high + 0.05, f'{low}-{high}%', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('Annual Fee (% of AUM)', fontsize=11)
    ax.set_title('Wealth Management Fees by Service Type', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(services)
    ax.set_ylim(0, 2.5)

    # Add minimum investment annotations
    minimums = ['$0', '$500', '$25K', '$250K', '$1M+']
    for i, mini in enumerate(minimums):
        ax.text(i, -0.15, f'Min: {mini}', ha='center', fontsize=8, color='#555555')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Industry surveys [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    output_path = Path(__file__).parent / 'fee_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
