"""
Bank Balance Sheet Structure
Shows typical assets and liabilities of a commercial bank

Output: bank_balance_sheet.pdf
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
MLGREEN = '#2CA02C'
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # Assets side
    assets = ['Loans', 'Securities', 'Cash/Reserves', 'Other']
    asset_values = [60, 25, 10, 5]  # percentages
    asset_colors = [MLBLUE, MLORANGE, MLGREEN, MLLAVENDER]

    ax1.barh(assets, asset_values, color=asset_colors, edgecolor='white', linewidth=2)
    ax1.set_xlabel('Percentage of Total Assets', fontsize=10)
    ax1.set_title('Assets', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax1.set_xlim(0, 70)

    for i, (a, v) in enumerate(zip(assets, asset_values)):
        ax1.text(v + 1, i, f'{v}%', va='center', fontsize=10, fontweight='bold')

    # Liabilities side
    liabilities = ['Customer\nDeposits', 'Wholesale\nFunding', 'Equity', 'Other\nLiabilities']
    liability_values = [70, 15, 10, 5]  # percentages
    liability_colors = [MLBLUE, MLORANGE, MLGREEN, MLLAVENDER]

    ax2.barh(liabilities, liability_values, color=liability_colors, edgecolor='white', linewidth=2)
    ax2.set_xlabel('Percentage of Total Liabilities', fontsize=10)
    ax2.set_title('Liabilities & Equity', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax2.set_xlim(0, 80)

    for i, (l, v) in enumerate(zip(liabilities, liability_values)):
        ax2.text(v + 1, i, f'{v}%', va='center', fontsize=10, fontweight='bold')

    # Remove spines
    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    fig.suptitle('Commercial Bank Balance Sheet Structure', fontsize=14,
                 fontweight='bold', color=MLPURPLE, y=1.02)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical bank structure]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'bank_balance_sheet.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
