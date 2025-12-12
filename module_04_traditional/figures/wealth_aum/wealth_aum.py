"""
Global Wealth Management AUM
Shows assets under management by segment

Output: wealth_aum.pdf
Module: module_04_traditional
Lesson: 46 - Wealth Management
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

    years = [2019, 2020, 2021, 2022, 2023, 2024]

    # AUM in trillions USD by segment
    uhnw = [35, 38, 45, 42, 48, 52]  # Ultra-high net worth (>$30M)
    hnw = [55, 60, 72, 68, 76, 84]   # High net worth ($1-30M)
    affluent = [45, 50, 60, 56, 64, 70]  # Affluent ($100K-$1M)
    mass = [25, 28, 32, 30, 34, 38]  # Mass affluent

    x = np.arange(len(years))
    width = 0.2

    ax.bar(x - 1.5*width, uhnw, width, label='UHNW (>$30M)', color=MLPURPLE)
    ax.bar(x - 0.5*width, hnw, width, label='HNW ($1-30M)', color=MLBLUE)
    ax.bar(x + 0.5*width, affluent, width, label='Affluent ($100K-1M)', color=MLORANGE)
    ax.bar(x + 1.5*width, mass, width, label='Mass Affluent', color=MLLAVENDER)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Assets Under Management (USD Trillions)', fontsize=11)
    ax.set_title('Global Wealth Management Assets by Segment', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.set_ylim(0, 100)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: BCG Global Wealth Report [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealth_aum.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
