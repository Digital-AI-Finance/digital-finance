"""
Liquidity Metrics
Measuring market liquidity

Output: liquidity_metrics.pdf
Module: module_04_trad_finance
Lesson: 41 - Market Microstructure
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Liquidity Metrics',
    'module': 'module_04_trad_finance',
    'lesson': 41,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/liquidity_metrics'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))

    metrics = ['Bid-Ask\nSpread', 'Depth', 'Volume', 'Price\nImpact', 'Turnover', 'Resiliency']
    stocks = ['AAPL', 'MSFT', 'Small Cap A', 'Small Cap B']

    # Liquidity scores (higher = more liquid)
    scores = np.array([
        [95, 92, 95, 90, 88, 85],   # AAPL
        [93, 90, 93, 88, 85, 82],   # MSFT
        [45, 40, 35, 55, 30, 35],   # Small Cap A
        [35, 30, 25, 65, 20, 25]    # Small Cap B
    ])

    im = ax.imshow(scores, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

    ax.set_xticks(np.arange(len(metrics)))
    ax.set_yticks(np.arange(len(stocks)))
    ax.set_xticklabels(metrics, fontsize=10)
    ax.set_yticklabels(stocks, fontsize=10)

    for i in range(len(stocks)):
        for j in range(len(metrics)):
            text_color = 'white' if scores[i, j] < 40 or scores[i, j] > 70 else 'black'
            ax.text(j, i, f'{scores[i, j]}', ha='center', va='center',
                   color=text_color, fontsize=11, fontweight='bold')

    ax.set_title('Liquidity Metrics Comparison: Large vs. Small Cap', fontsize=14, fontweight='bold', pad=15)

    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('Liquidity Score (0-100)', fontsize=10)

    # Add metric descriptions
    ax.text(8, 0, 'Higher = Tighter spread', fontsize=8, va='center')
    ax.text(8, 1, 'Higher = More depth', fontsize=8, va='center')
    ax.text(8, 2, 'Higher = More volume', fontsize=8, va='center')
    ax.text(8, 3, 'Higher = Lower impact', fontsize=8, va='center')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'liquidity_metrics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
