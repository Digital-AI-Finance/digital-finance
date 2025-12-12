"""
Trading Latency Evolution
Shows dramatic decrease in trade execution time over decades

Output: trading_latency.pdf
Module: module_04_traditional
Lesson: 40 - Electronic Trading
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]
    latency_ms = [300000, 60000, 5000, 500, 50, 5, 0.5, 0.05]  # milliseconds

    ax.semilogy(years, latency_ms, 'o-', color=MLBLUE, linewidth=2, markersize=8)

    # Add era labels
    ax.axvspan(1990, 1998, alpha=0.1, color=MLORANGE, label='Floor Trading Era')
    ax.axvspan(1998, 2007, alpha=0.1, color=MLBLUE, label='Electronic Era')
    ax.axvspan(2007, 2024, alpha=0.1, color=MLPURPLE, label='HFT Era')

    # Add specific latency labels
    for year, lat in zip(years, latency_ms):
        if lat >= 1000:
            label = f'{lat/1000:.0f}s'
        elif lat >= 1:
            label = f'{lat:.0f}ms'
        else:
            label = f'{lat*1000:.0f}μs'
        ax.annotate(label, (year, lat), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=8)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Execution Latency (milliseconds, log scale)', fontsize=11)
    ax.set_title('Evolution of Trade Execution Latency', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(1988, 2026)
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(loc='upper right')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative trend]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'trading_latency.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
