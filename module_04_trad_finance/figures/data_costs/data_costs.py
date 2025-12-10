"""
Data Costs Analysis
Financial data spending breakdown

Output: data_costs.pdf
Module: module_04_trad_finance
Lesson: 47 - Data Vendors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Data Costs',
    'module': 'module_04_trad_finance',
    'lesson': 47,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/data_costs'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Cost breakdown by category
    ax1 = axes[0]

    categories = ['Market Data\nFeeds', 'Terminal\nSubscriptions', 'Research &\nRatings', 'Reference\nData', 'Alternative\nData', 'Analytics\nTools']
    spend = [8.5, 6.2, 3.8, 2.5, 1.8, 2.2]  # Annual spend in $M for large firm
    growth = [5, 2, 4, 3, 25, 12]  # YoY growth %
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#E91E63']

    bars = ax1.bar(categories, spend, color=colors, alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Annual Spend ($M)', fontsize=11)
    ax1.set_title('Large Asset Manager: Data Costs', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 12)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add growth labels
    for bar, g in zip(bars, growth):
        height = bar.get_height()
        color = '#D62728' if g > 10 else '#FF7F0E' if g > 5 else '#44A044'
        ax1.text(bar.get_x() + bar.get_width()/2, height + 0.3,
                f'+{g}%', ha='center', fontsize=9, fontweight='bold', color=color)

    ax1.text(3, 11, 'YoY Growth Rate', fontsize=9, color='#666666', style='italic')

    # Cost trends over time
    ax2 = axes[1]

    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    traditional = [20, 21, 22, 23, 24, 25]
    alt_data = [0.5, 0.8, 1.2, 1.8, 2.8, 4.2]
    cloud = [1, 1.5, 2.5, 3.5, 5, 7]

    ax2.stackplot(years, traditional, alt_data, cloud,
                  labels=['Traditional Data', 'Alternative Data', 'Cloud/Processing'],
                  colors=['#4A90E2', '#D62728', '#44A044'], alpha=0.8)

    ax2.set_ylabel('Annual Spend ($M)', fontsize=11)
    ax2.set_title('Data Spend Evolution', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=9)
    ax2.set_ylim(0, 40)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add annotation
    total_2024 = traditional[-1] + alt_data[-1] + cloud[-1]
    ax2.text(5, 30, f'2024 Total:\n${total_2024:.1f}M', fontsize=10, fontweight='bold',
            ha='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    fig.suptitle('Financial Data Costs & Trends', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_costs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
