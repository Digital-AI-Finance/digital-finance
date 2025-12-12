"""
Central Clearing Counterparty (CCP) Volumes
Shows growth in centrally cleared derivatives

Output: clearing_process.pdf
Module: module_04_traditional
Lesson: 44 - Capital Markets Tech
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

    years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]

    # Percentage of OTC derivatives centrally cleared
    irs_cleared = [20, 35, 55, 65, 75, 80, 82, 85]  # Interest rate swaps
    cds_cleared = [10, 20, 35, 50, 60, 65, 70, 75]  # Credit default swaps

    ax.plot(years, irs_cleared, 'o-', color=MLBLUE, linewidth=2,
            markersize=8, label='Interest Rate Swaps')
    ax.plot(years, cds_cleared, 's--', color=MLORANGE, linewidth=2,
            markersize=8, label='Credit Default Swaps')

    # Add Dodd-Frank marker
    ax.axvline(x=2012, color='gray', linestyle=':', linewidth=2, alpha=0.7)
    ax.text(2012.2, 20, 'Dodd-Frank\nClearing Mandate', fontsize=8, color='#555555')

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Centrally Cleared (%)', fontsize=11)
    ax.set_title('OTC Derivatives Central Clearing Adoption', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='lower right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)
    ax.set_xlim(2009, 2025)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: ISDA, BIS [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'clearing_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
