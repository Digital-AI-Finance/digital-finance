"""
Exchange Types Comparison
Different exchange structures

Output: exchange_types.pdf
Module: module_04_trad_finance
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Exchange Types',
    'module': 'module_04_trad_finance',
    'lesson': 37,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/exchange_types'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))

    exchange_types = ['Traditional\nExchange', 'ECN', 'Dark Pool', 'OTC', 'MTF/ATS']

    attributes = ['Transparency', 'Liquidity', 'Speed', 'Cost', 'Regulation', 'Anonymous']

    scores = np.array([
        [95, 85, 70, 60, 90, 10],   # Traditional Exchange
        [80, 70, 95, 75, 85, 30],   # ECN
        [20, 60, 85, 80, 70, 95],   # Dark Pool
        [40, 50, 60, 50, 60, 70],   # OTC
        [75, 65, 90, 80, 80, 40]    # MTF/ATS
    ])

    im = ax.imshow(scores, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

    ax.set_xticks(np.arange(len(attributes)))
    ax.set_yticks(np.arange(len(exchange_types)))
    ax.set_xticklabels(attributes, fontsize=10)
    ax.set_yticklabels(exchange_types, fontsize=10)

    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    # Add text annotations
    for i in range(len(exchange_types)):
        for j in range(len(attributes)):
            text_color = 'white' if scores[i, j] < 40 or scores[i, j] > 70 else 'black'
            ax.text(j, i, f'{scores[i, j]}', ha='center', va='center',
                   color=text_color, fontsize=10, fontweight='bold')

    ax.set_title('Exchange Types: Attribute Comparison', fontsize=14, fontweight='bold', pad=15)

    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('Score (0-100)', fontsize=10)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'exchange_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
