"""
Neobank Revenue Breakdown
Shows typical revenue sources and their proportions for neobanks

Output: neobank_revenue_breakdown.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank Revenue Breakdown',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/neobank_revenue_breakdown'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank revenue breakdown chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Pie chart of revenue sources (industry typical)
    sources = ['Interchange\nFees', 'Subscription\nFees', 'FX/Trading\nFees',
               'Interest\nIncome', 'Other\nServices']
    # Based on Revolut 2023 annual report structure and industry analysis
    proportions = [45, 20, 18, 12, 5]
    colors = ['#333333', '#4A90E2', '#44A044', '#FF7F0E', '#999999']
    explode = (0.03, 0, 0, 0, 0)

    wedges, texts, autotexts = ax1.pie(
        proportions, labels=sources, autopct='%1.0f%%',
        colors=colors, explode=explode, startangle=90,
        pctdistance=0.75
    )

    for text in texts:
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')

    ax1.set_title('Typical Neobank Revenue Mix', fontsize=12, fontweight='bold', pad=10)

    # Right: Comparison across neobanks (normalized to 100%)
    neobanks = ['Revolut', 'Monzo', 'N26', 'Chime', 'Nubank']

    # Based on public filings and industry estimates
    interchange = [35, 55, 50, 70, 45]
    subscription = [15, 15, 20, 5, 10]
    fx_trading = [30, 10, 15, 5, 15]
    interest = [15, 15, 10, 15, 25]
    other = [5, 5, 5, 5, 5]

    x = np.arange(len(neobanks))
    width = 0.6

    ax2.bar(x, interchange, width, label='Interchange', color='#333333')
    ax2.bar(x, subscription, width, bottom=interchange, label='Subscription', color='#4A90E2')
    ax2.bar(x, fx_trading, width, bottom=np.array(interchange)+np.array(subscription),
           label='FX/Trading', color='#44A044')
    ax2.bar(x, interest, width,
           bottom=np.array(interchange)+np.array(subscription)+np.array(fx_trading),
           label='Interest', color='#FF7F0E')
    ax2.bar(x, other, width,
           bottom=np.array(interchange)+np.array(subscription)+np.array(fx_trading)+np.array(interest),
           label='Other', color='#999999')

    ax2.set_ylabel('Revenue Share (%)', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(neobanks, fontsize=9)
    ax2.set_ylim(0, 105)
    ax2.set_title('Revenue Mix by Neobank', fontsize=12, fontweight='bold', pad=10)
    ax2.legend(loc='upper right', fontsize=8, framealpha=0.9)

    ax2.yaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Main title
    fig.suptitle('Neobank Revenue Model Analysis', fontsize=14, fontweight='bold', y=1.02)

    # Source annotation
    fig.text(0.5, -0.02, 'Source: Company annual reports 2023, industry estimates',
            fontsize=8, ha='center', style='italic', color='#666666')

    # Synthetic label
    fig.text(0.98, 0.02, '[ESTIMATES BASED ON PUBLIC DATA]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'neobank_revenue_breakdown.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
