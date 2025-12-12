"""
Interest Rate and Yield Curve
Shows the typical yield curve shape and key rates

Output: interest_rate_yield.pdf
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Treasury yield curve maturities and rates (Dec 2024 approx)
    maturities = [1/12, 3/12, 6/12, 1, 2, 3, 5, 7, 10, 20, 30]
    maturity_labels = ['1M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y']

    # Normal yield curve (upward sloping)
    normal_rates = [4.4, 4.35, 4.25, 4.1, 4.0, 3.95, 4.0, 4.1, 4.2, 4.4, 4.35]

    # Inverted yield curve (2022-2023 style)
    inverted_rates = [5.5, 5.45, 5.35, 5.1, 4.7, 4.5, 4.3, 4.25, 4.2, 4.4, 4.35]

    ax.plot(range(len(maturities)), normal_rates, 'o-', color=MLBLUE,
            linewidth=2, markersize=8, label='Normal Yield Curve')
    ax.plot(range(len(maturities)), inverted_rates, 's--', color=MLORANGE,
            linewidth=2, markersize=8, label='Inverted Yield Curve')

    ax.set_xticks(range(len(maturities)))
    ax.set_xticklabels(maturity_labels)

    ax.set_xlabel('Maturity', fontsize=11)
    ax.set_ylabel('Yield (%)', fontsize=11)
    ax.set_title('US Treasury Yield Curve', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(3.5, 6)

    # Add recession warning annotation
    ax.annotate('Inverted curve:\nRecession signal', xy=(2, 4.7), xytext=(4, 5.5),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative rates]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'interest_rate_yield.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
