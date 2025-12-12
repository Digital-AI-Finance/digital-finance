"""
Settlement System Comparison
Shows T+n settlement cycles by market

Output: settlement_systems.pdf
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

    markets = ['US Equities\n(post-May 2024)', 'EU Equities', 'US Treasuries', 'FX Spot', 'Crypto\n(on-chain)']
    settlement = [1, 2, 1, 2, 0]  # T+n days

    colors = [MLGREEN if x <= 1 else MLORANGE for x in settlement]

    bars = ax.bar(markets, settlement, color=colors, edgecolor='white', linewidth=2)

    for bar, days in zip(bars, settlement):
        label = 'T+0' if days == 0 else f'T+{days}'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                label, ha='center', fontsize=11, fontweight='bold')

    ax.set_ylabel('Settlement Cycle (Days after Trade)', fontsize=11)
    ax.set_title('Settlement Cycles by Market', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 3)

    # Add trend annotation
    ax.annotate('Industry moving\ntoward T+1/T+0', xy=(2.5, 1.5),
                fontsize=9, ha='center', color='#555555',
                bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[ILLUSTRATIVE - As of late 2024]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'settlement_systems.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
