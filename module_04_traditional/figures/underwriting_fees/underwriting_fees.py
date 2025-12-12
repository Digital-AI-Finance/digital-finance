"""
Investment Banking Fee Structure
Shows typical fees by deal type

Output: underwriting_fees.pdf
Module: module_04_traditional
Lesson: 44 - Capital Markets Tech
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

    # Fee types by transaction
    deal_types = ['IPO\n(Small)', 'IPO\n(Large)', 'Follow-on\nOffering', 'M&A\nAdvisory', 'Debt\nIssuance']
    fees = [7.0, 4.0, 3.5, 1.5, 0.5]  # Percentage

    colors = [MLBLUE, MLBLUE, MLORANGE, MLGREEN, MLLAVENDER]

    bars = ax.bar(deal_types, fees, color=colors, edgecolor='white', linewidth=2)

    for bar, fee in zip(bars, fees):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                f'{fee}%', ha='center', fontsize=11, fontweight='bold')

    ax.set_ylabel('Fee (% of Deal Value)', fontsize=11)
    ax.set_title('Investment Banking Fees by Transaction Type', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 9)

    # Add annotation about size dependency
    ax.annotate('Fees decrease with\ndeal size', xy=(0.5, 5.5), xytext=(2, 6.5),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                ha='center', color='#555555')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Dealogic, industry estimates [SYNTHETIC DATA]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'underwriting_fees.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
