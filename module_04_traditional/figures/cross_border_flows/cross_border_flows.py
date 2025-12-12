"""
Cross-Border Capital Flows
Shows major corridors for international payments

Output: cross_border_flows.pdf
Module: module_04_traditional
Lesson: 39 - Payment Rails
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

    corridors = ['US-UK', 'US-China', 'US-Mexico', 'UK-EU', 'China-HK', 'India-UAE', 'US-Canada']
    volumes = [180, 150, 120, 100, 95, 85, 80]  # Billions USD annually

    colors = [MLBLUE, MLORANGE, MLGREEN, MLBLUE, MLORANGE, MLLAVENDER, MLGREEN]

    bars = ax.barh(corridors, volumes, color=colors, edgecolor='white', linewidth=2)

    for bar, vol in zip(bars, volumes):
        ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2,
                f'${vol}B', va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Annual Cross-Border Flow (USD Billions)', fontsize=11)
    ax.set_title('Top Cross-Border Payment Corridors', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(0, 220)
    ax.invert_yaxis()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: World Bank Remittance data [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'cross_border_flows.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
