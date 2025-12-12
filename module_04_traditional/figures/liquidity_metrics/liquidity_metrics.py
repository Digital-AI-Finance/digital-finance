"""
Market Liquidity Metrics Comparison
Shows liquidity across different markets

Output: liquidity_metrics.pdf
Module: module_04_traditional
Lesson: 41 - Market Microstructure
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

    markets = ['S&P 500\nStocks', 'Small Cap\nStocks', 'Corporate\nBonds', 'Municipal\nBonds', 'Emerging\nMarkets']

    # Metrics (normalized to large cap US = 100)
    bid_ask = [1, 15, 25, 50, 20]  # Relative spread
    depth = [100, 30, 20, 10, 25]  # Market depth
    turnover = [250, 100, 50, 30, 80]  # Annual turnover %

    x = np.arange(len(markets))
    width = 0.25

    ax.bar(x - width, bid_ask, width, label='Bid-Ask Spread (rel)', color=MLBLUE)
    ax.bar(x, depth, width, label='Market Depth (rel)', color=MLORANGE)
    ax.bar(x + width, turnover, width, label='Turnover (%)', color=MLGREEN)

    ax.set_ylabel('Relative Value / Percentage', fontsize=11)
    ax.set_title('Market Liquidity Comparison', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(markets)
    ax.legend(loc='upper right', framealpha=0.9)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Relative comparison]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'liquidity_metrics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
