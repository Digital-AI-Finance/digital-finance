"""
Financial Data Vendor Landscape
Major players and market share

Output: data_vendor_landscape.pdf
Module: module_04_trad_finance
Lesson: 47 - Data Vendors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Data Vendor Landscape',
    'module': 'module_04_trad_finance',
    'lesson': 47,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/data_vendor_landscape'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Market share by vendor
    ax1 = axes[0]

    vendors = ['Bloomberg', 'Refinitiv\n(LSEG)', 'S&P Global', 'MSCI', 'Moody\'s', 'FactSet', 'Others']
    market_share = [33, 22, 12, 8, 7, 5, 13]
    colors = ['#FF7F0E', '#4A90E2', '#44A044', '#9B59B6', '#D62728', '#E91E63', '#888888']

    wedges, texts, autotexts = ax1.pie(market_share, labels=vendors, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.03, 0.02, 0, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    for text in texts:
        text.set_fontsize(9)

    ax1.set_title('Market Data Vendor Market Share', fontsize=12, fontweight='bold')

    # Add center annotation
    centre_circle = plt.Circle((0, 0), 0.35, fc='white')
    ax1.add_patch(centre_circle)
    ax1.text(0, 0, 'Total:\n$45B', ha='center', va='center', fontsize=10, fontweight='bold')

    # Revenue by segment
    ax2 = axes[1]

    segments = ['Terminal\nServices', 'Data\nFeeds', 'Analytics\n& Indices', 'Research\n& Ratings', 'Reference\nData']
    revenue = [18, 12, 8, 5, 2]
    growth = [3, 8, 12, 5, 6]  # YoY growth %
    colors2 = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728']

    x = np.arange(len(segments))
    bars = ax2.bar(x, revenue, color=colors2, alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Annual Revenue ($B)', fontsize=11)
    ax2.set_title('Market by Data Segment', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(segments, fontsize=9)
    ax2.set_ylim(0, 25)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add growth labels
    for bar, g, r in zip(bars, growth, revenue):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                f'${r}B\n+{g}% YoY', ha='center', fontsize=9, fontweight='bold')

    # Highlight fastest growing
    ax2.annotate('Fastest\ngrowing', xy=(2, 8), xytext=(3.5, 15),
                fontsize=9, color='#FF7F0E',
                arrowprops=dict(arrowstyle='->', color='#FF7F0E'))

    fig.suptitle('Financial Data Vendor Market', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_vendor_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
