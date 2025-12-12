"""
Derivatives Margin Requirements
Shows initial margin by asset class

Output: margin_requirements.pdf
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    products = ['Interest Rate\nSwaps', 'FX\nForwards', 'Equity\nOptions', 'Commodity\nFutures', 'Credit\nDerivatives']
    margins = [2, 3, 15, 8, 5]  # Initial margin as % of notional

    colors = [MLBLUE, MLGREEN, MLORANGE, MLORANGE, MLBLUE]

    bars = ax.bar(products, margins, color=colors, edgecolor='white', linewidth=2)

    for bar, margin in zip(bars, margins):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{margin}%', ha='center', fontsize=11, fontweight='bold')

    ax.set_ylabel('Initial Margin (% of Notional)', fontsize=11)
    ax.set_title('Typical Initial Margin Requirements by Product', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 20)

    # Add explanation
    ax.text(0.5, 0.95, 'Higher margin = Higher perceived risk',
            transform=ax.transAxes, ha='center', va='top', fontsize=9,
            color='#555555', style='italic')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: CME, LCH [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'margin_requirements.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
