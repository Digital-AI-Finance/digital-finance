"""
ETF Industry Growth
Shows AUM growth in exchange-traded funds

Output: etf_growth.pdf
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

def create_chart():
    fig, ax1 = plt.subplots(figsize=(10, 6))

    years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]

    # Global ETF AUM in trillions
    aum = [1.3, 1.8, 2.7, 3.4, 4.7, 7.7, 9.5, 12.5]
    # Number of ETFs
    num_etfs = [2500, 3300, 4500, 5500, 6200, 7600, 9200, 10500]

    color1 = MLBLUE
    ax1.bar(years, aum, color=color1, alpha=0.7, width=1.5)
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Global ETF AUM (USD Trillions)', fontsize=11, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 15)

    # Add AUM labels
    for year, val in zip(years, aum):
        ax1.text(year, val + 0.3, f'${val}T', ha='center', fontsize=8, fontweight='bold', color=color1)

    ax2 = ax1.twinx()
    color2 = MLORANGE
    ax2.plot(years, num_etfs, 'o-', color=color2, linewidth=2, markersize=8)
    ax2.set_ylabel('Number of ETFs', fontsize=11, color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 12000)

    ax1.set_title('Global ETF Industry Growth', fontsize=14,
                  fontweight='bold', color=MLPURPLE, pad=10)

    # Add CAGR
    cagr = ((aum[-1]/aum[0])**(1/len(years)) - 1) * 100
    ax1.text(0.02, 0.95, f'AUM CAGR: {cagr:.0f}%',
             transform=ax1.transAxes, ha='left', va='top', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: ETFGI, BlackRock [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'etf_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
