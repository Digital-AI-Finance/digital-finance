"""
Dark Pool Trading Volume
Shows growth of off-exchange trading

Output: dark_pools.pdf
Module: module_04_traditional
Lesson: 41 - Market Microstructure
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

    years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]

    # US equity market share breakdown
    exchanges = [75, 70, 65, 62, 58, 55, 52, 50]
    dark_pools = [10, 13, 16, 18, 20, 22, 24, 25]
    internalizers = [15, 17, 19, 20, 22, 23, 24, 25]

    ax.stackplot(years, exchanges, dark_pools, internalizers,
                 labels=['Lit Exchanges', 'Dark Pools', 'Internalizers'],
                 colors=[MLBLUE, MLORANGE, MLLAVENDER], alpha=0.85)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Market Share (%)', fontsize=11)
    ax.set_title('US Equity Trading Venue Market Share', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xlim(2010, 2024)
    ax.set_ylim(0, 100)

    # Add annotation
    ax.annotate('Off-exchange\ntrading ~50%', xy=(2024, 50), xytext=(2019, 30),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555', ha='center')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: SEC Rule 606 Reports [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'dark_pools.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
