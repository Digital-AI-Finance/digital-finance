"""
Bid-Ask Spread Evolution
Shows how spreads have compressed over time with electronic trading

Output: bid_ask_spread.pdf
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]

    # Average bid-ask spread in basis points for large-cap stocks
    spreads_large_cap = [50, 35, 15, 8, 3, 1.5, 0.8, 0.5]
    spreads_small_cap = [200, 150, 80, 50, 30, 20, 15, 10]

    ax.semilogy(years, spreads_large_cap, 'o-', color=MLBLUE, linewidth=2,
                markersize=8, label='Large-Cap Stocks')
    ax.semilogy(years, spreads_small_cap, 's--', color=MLORANGE, linewidth=2,
                markersize=8, label='Small-Cap Stocks')

    # Add key event annotations
    events = [
        (2001, 'Decimalization'),
        (2007, 'Reg NMS'),
        (2010, 'Flash Crash')
    ]

    for year, event in events:
        ax.axvline(x=year, color='gray', linestyle=':', alpha=0.5)
        ax.text(year, 200, event, rotation=90, va='bottom', ha='right',
                fontsize=8, color='#666666')

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Average Spread (basis points, log scale)', fontsize=11)
    ax.set_title('Bid-Ask Spread Compression Over Time', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1988, 2026)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative trend]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'bid_ask_spread.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
