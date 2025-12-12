"""
Stock Exchange Market Capitalization
Shows largest exchanges by listed company value

Output: exchange_market_cap.pdf
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    exchanges = ['NYSE', 'NASDAQ', 'Shanghai', 'Euronext', 'Tokyo', 'Shenzhen', 'Hong Kong', 'LSE']
    market_cap = [28, 25, 7, 7, 6, 5, 4.5, 3.5]  # Trillions USD

    colors = [MLBLUE if x > 10 else MLORANGE for x in market_cap]

    bars = ax.barh(exchanges, market_cap, color=colors, edgecolor='white', linewidth=2)

    for bar, val in zip(bars, market_cap):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'${val}T', va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Market Capitalization (USD Trillions)', fontsize=11)
    ax.set_title('Largest Stock Exchanges by Market Cap (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xlim(0, 35)
    ax.invert_yaxis()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: World Federation of Exchanges [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'exchange_market_cap.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
