"""
Global Derivatives Market
Market size and composition

Output: derivatives_market.pdf
Module: module_04_trad_finance
Lesson: 45 - Derivatives
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Derivatives Market',
    'module': 'module_04_trad_finance',
    'lesson': 45,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/derivatives_market'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # OTC vs Exchange-Traded
    ax1 = axes[0]

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    otc = [544, 559, 582, 610, 632, 667, 715]  # Notional in trillions
    exchange = [75, 82, 95, 88, 85, 92, 98]

    x = np.arange(len(years))
    width = 0.35

    bars1 = ax1.bar(x - width/2, otc, width, label='OTC Derivatives', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x + width/2, exchange, width, label='Exchange-Traded', color='#44A044', alpha=0.8)

    ax1.set_ylabel('Notional Outstanding ($T)', fontsize=11)
    ax1.set_title('Global Derivatives Market Size', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years, fontsize=9)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_ylim(0, 800)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add total labels
    for i, (o, e) in enumerate(zip(otc, exchange)):
        ax1.text(i, o + 15, f'${o}T', ha='center', fontsize=8, color='#4A90E2')

    # OTC breakdown by product
    ax2 = axes[1]

    products = ['Interest\nRate', 'FX', 'Credit\n(CDS)', 'Equity', 'Commodity']
    notional = [500, 110, 8, 7, 3]  # In trillions
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728']

    wedges, texts, autotexts = ax2.pie(notional, labels=products, autopct='%1.1f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.02, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    for text in texts:
        text.set_fontsize(9)

    ax2.set_title('OTC Derivatives by Product Type', fontsize=12, fontweight='bold')

    # Add center text
    centre_circle = plt.Circle((0, 0), 0.4, fc='white')
    ax2.add_patch(centre_circle)
    ax2.text(0, 0.05, 'Total OTC:', ha='center', va='center', fontsize=9)
    ax2.text(0, -0.15, '$715T', ha='center', va='center', fontsize=11, fontweight='bold')

    fig.suptitle('Global Derivatives Markets (2024)', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'derivatives_market.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
