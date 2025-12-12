"""
Corporate Bond Rating Distribution
Shows distribution of bond ratings

Output: credit_rating_distribution.pdf
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

    ratings = ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC\nand below']
    percentages = [2, 8, 22, 35, 18, 12, 3]

    # Investment grade vs high yield coloring
    colors = [MLGREEN, MLGREEN, MLBLUE, MLBLUE, MLORANGE, MLORANGE, MLRED]

    bars = ax.bar(ratings, percentages, color=colors, edgecolor='white', linewidth=2)

    for bar, pct in zip(bars, percentages):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{pct}%', ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('Percentage of Market', fontsize=11)
    ax.set_title('US Corporate Bond Market by Credit Rating', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 42)

    # Add investment grade line
    ax.axvline(x=3.5, color='gray', linestyle='--', linewidth=2)
    ax.text(1.5, 38, 'Investment Grade\n(67%)', ha='center', fontsize=9, color=MLBLUE)
    ax.text(5, 38, 'High Yield\n(33%)', ha='center', fontsize=9, color=MLORANGE)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: SIFMA, S&P [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'credit_rating_distribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
