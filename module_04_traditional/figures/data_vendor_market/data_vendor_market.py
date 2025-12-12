"""
Financial Data Vendor Market Share
Shows major providers and their market positions

Output: data_vendor_market.pdf
Module: module_04_traditional
Lesson: 47 - Data Vendors
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

    # Market share of financial data providers (2024)
    providers = ['Bloomberg', 'Refinitiv\n(LSEG)', 'S&P Global', 'MSCI', 'FactSet', 'Moody\'s', 'ICE', 'Others']
    market_share = [33, 22, 12, 8, 5, 5, 4, 11]  # Percentage

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLRED, MLLAVENDER, '#888888', '#cccccc']

    # Horizontal bar chart
    bars = ax.barh(providers, market_share, color=colors, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val in zip(bars, market_share):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{val}%', va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Market Share (%)', fontsize=11)
    ax.set_title('Financial Data & Analytics Market Share (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(0, 45)
    ax.invert_yaxis()

    # Add market size annotation
    ax.text(0.98, 0.05, 'Total Market: ~$45B annually',
            transform=ax.transAxes, ha='right', va='bottom', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Burton-Taylor, Opimas Research [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_vendor_market.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
