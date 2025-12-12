"""
Global Payment Volumes by Type
Shows transaction volumes for different payment methods

Output: payment_volumes.pdf
Module: module_04_traditional
Lesson: 39 - Payment Rails
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2019, 2020, 2021, 2022, 2023, 2024]

    # Payment volumes in trillions of transactions
    card_payments = [480, 465, 520, 580, 640, 700]
    digital_wallets = [120, 180, 260, 340, 420, 500]
    bank_transfers = [180, 195, 210, 225, 240, 255]
    cash = [200, 150, 140, 135, 130, 125]

    ax.stackplot(years, card_payments, digital_wallets, bank_transfers, cash,
                 labels=['Card Payments', 'Digital Wallets', 'Bank Transfers', 'Cash'],
                 colors=[MLBLUE, MLORANGE, MLGREEN, MLLAVENDER], alpha=0.85)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Transactions (Billions)', fontsize=11)
    ax.set_title('Global Non-Cash Payment Volumes by Type', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9)
    ax.set_xlim(2019, 2024)
    ax.set_ylim(0, 1800)

    # Add growth annotation
    ax.annotate('Digital wallets\n+300% since 2019', xy=(2024, 1200), xytext=(2021.5, 1400),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555', ha='center')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: McKinsey Global Payments Report [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'payment_volumes.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
