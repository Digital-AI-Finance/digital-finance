"""
Global Trading Hours
Shows when major markets are open

Output: trading_hours.pdf
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    markets = ['Tokyo', 'Hong Kong', 'Singapore', 'London', 'Frankfurt', 'New York']

    # Trading hours in UTC (0-24)
    opens_utc = [0, 1.5, 1, 8, 8, 14.5]
    closes_utc = [6, 8, 9, 16.5, 16.5, 21]

    colors = [MLPURPLE, MLORANGE, MLGREEN, MLBLUE, MLBLUE, MLBLUE]

    for i, (market, open_t, close_t) in enumerate(zip(markets, opens_utc, closes_utc)):
        ax.barh(i, close_t - open_t, left=open_t, height=0.6, color=colors[i],
               edgecolor='white', linewidth=2, alpha=0.8)
        ax.text(open_t + (close_t - open_t)/2, i, market, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

    ax.set_xlabel('Time (UTC)', fontsize=11)
    ax.set_title('Major Stock Exchange Trading Hours', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(0, 24)
    ax.set_xticks(range(0, 25, 3))
    ax.set_xticklabels([f'{h:02d}:00' for h in range(0, 25, 3)])
    ax.set_yticks([])

    # Add region labels
    ax.text(3, 2.8, 'Asia-Pacific', fontsize=10, ha='center', color='#555555')
    ax.text(12, 4.8, 'Europe', fontsize=10, ha='center', color='#555555')
    ax.text(18, 5.8, 'Americas', fontsize=10, ha='center', color='#555555')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    fig.text(0.98, 0.02, '[ILLUSTRATIVE - Actual hours vary]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'trading_hours.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
