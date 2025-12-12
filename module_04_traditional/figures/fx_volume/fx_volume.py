"""
FX Market Daily Volume by Currency Pair
Shows most traded currency pairs

Output: fx_volume.pdf
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Daily FX turnover by currency pair (April 2022, billions USD)
    pairs = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'USD/CNY', 'USD/CAD', 'USD/CHF', 'AUD/USD', 'Other']
    volumes = [1700, 1014, 714, 495, 410, 390, 380, 2400]  # Billions USD daily

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, '#888888', MLLAVENDER, '#666666', '#cccccc']

    bars = ax.barh(pairs, volumes, color=colors, edgecolor='white', linewidth=2)

    for bar, val in zip(bars, volumes):
        ax.text(bar.get_width() + 30, bar.get_y() + bar.get_height()/2,
                f'${val}B', va='center', fontsize=9, fontweight='bold')

    ax.set_xlabel('Daily Turnover (USD Billions)', fontsize=11)
    ax.set_title('FX Market Daily Volume by Currency Pair', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(0, 3000)
    ax.invert_yaxis()

    total = sum(volumes)
    ax.text(0.98, 0.05, f'Total Daily: ${total/1000:.1f}T',
            transform=ax.transAxes, ha='right', va='bottom', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: BIS Triennial Survey 2022 [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fx_volume.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
