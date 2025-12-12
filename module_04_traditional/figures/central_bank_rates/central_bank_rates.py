"""
Central Bank Policy Rates
Shows key interest rates across major economies

Output: central_bank_rates.pdf
Module: module_04_traditional
Lesson: 37 - Financial Markets
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
MLRED = '#D62728'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Central banks and their current rates (Dec 2024)
    banks = ['Federal\nReserve', 'ECB', 'Bank of\nEngland', 'Bank of\nJapan', 'SNB', 'RBA']
    rates = [4.50, 3.25, 4.75, 0.25, 1.00, 4.35]

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, '#888888', MLRED]

    bars = ax.bar(banks, rates, color=colors, edgecolor='white', linewidth=2)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{rate}%', ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('Policy Rate (%)', fontsize=11)
    ax.set_title('Central Bank Policy Rates (December 2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 6)
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative rates]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'central_bank_rates.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
