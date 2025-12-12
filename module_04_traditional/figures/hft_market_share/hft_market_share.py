"""
HFT Market Share by Asset Class
Shows high-frequency trading penetration

Output: hft_market_share.pdf
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
MLGREEN = '#2CA02C'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # HFT share of trading volume by asset class
    asset_classes = ['US Equities', 'EU Equities', 'FX Spot', 'US Treasuries', 'Futures', 'Options']
    hft_share = [50, 35, 25, 20, 60, 15]  # Percentage
    non_hft = [100 - x for x in hft_share]

    x = np.arange(len(asset_classes))
    width = 0.6

    ax.bar(x, hft_share, width, label='HFT', color=MLBLUE)
    ax.bar(x, non_hft, width, bottom=hft_share, label='Non-HFT', color=MLLAVENDER)

    # Add percentage labels
    for i, (hft, total) in enumerate(zip(hft_share, [100]*len(hft_share))):
        ax.text(i, hft/2, f'{hft}%', ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')

    ax.set_ylabel('Trading Volume Share (%)', fontsize=11)
    ax.set_title('High-Frequency Trading Market Share by Asset Class', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(asset_classes)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 110)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: SEC, ESMA estimates [SYNTHETIC DATA]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'hft_market_share.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

MLLAVENDER = '#ADADE0'

if __name__ == '__main__':
    create_chart()
