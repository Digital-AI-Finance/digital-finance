"""
Financial Market Structure - Capital flows diagram
Shows key market participants and flows

Output: market_structure.pdf
Module: module_04_traditional
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
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

    # Market size data (in trillions USD, 2024)
    markets = ['Equity\nMarkets', 'Bond\nMarkets', 'FX\nMarkets', 'Derivatives\n(Notional)', 'Crypto\nMarkets']
    sizes = [110, 130, 7.5, 700, 2.5]  # Daily volume for FX, notional for derivatives

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, '#999999']

    bars = ax.bar(markets, sizes, color=colors, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val in zip(bars, sizes):
        label = f'${val:.0f}T' if val >= 10 else f'${val:.1f}T'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
                label, ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax.set_ylabel('Market Size (USD Trillions)', fontsize=11)
    ax.set_title('Global Financial Markets Size (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    # Add annotations
    ax.annotate('Daily\nvolume', xy=(2, 7.5), xytext=(2, 50),
                fontsize=8, color='#666666', ha='center',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    ax.set_ylim(0, 800)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: BIS, World Federation of Exchanges [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
