"""
Global Derivatives Market Size
Shows notional outstanding by product type

Output: derivatives_notional.pdf
Module: module_04_traditional
Lesson: 45 - Derivatives Technology
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

    # Derivatives notional outstanding (USD trillions, 2024)
    categories = ['Interest Rate\nSwaps', 'FX\nForwards', 'Credit\nDerivatives', 'Equity\nDerivatives', 'Commodity\nDerivatives']
    notional = [450, 120, 8, 7, 3]  # Trillions USD

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLLAVENDER]

    bars = ax.bar(categories, notional, color=colors, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val in zip(bars, notional):
        label = f'${val}T' if val >= 10 else f'${val}T'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                label, ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax.set_ylabel('Notional Outstanding (USD Trillions)', fontsize=11)
    ax.set_title('Global OTC Derivatives Market (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 550)

    # Add total annotation
    total = sum(notional)
    ax.text(0.98, 0.95, f'Total: ${total}T notional',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: BIS OTC Derivatives Statistics [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'derivatives_notional.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
