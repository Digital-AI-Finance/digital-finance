"""
FinTech Investment Trends
Shows global FinTech funding over time

Output: fintech_investment_trends.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Investment Trends',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_investment_trends'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech investment trends chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    # Global FinTech funding in USD B
    funding = [22, 25, 35, 55, 52, 45, 132, 85, 52, 58]

    colors = ['#4A90E2'] * 5 + ['#44A044'] + ['#D62728'] + ['#FF7F0E'] * 3

    bars = ax.bar(years, funding, color=colors, edgecolor='#333333', lw=1.5)

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Global FinTech Funding (USD B)', fontsize=14)
    ax.set_title('Global FinTech Investment Trends', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 160)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, funding):
        ax.annotate(f'{val}B',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Key events
    ax.annotate('2021 Peak', xy=(2021, 132), xytext=(2021, 145),
               fontsize=11, ha='center', color='#D62728',
               arrowprops=dict(arrowstyle='->', color='#D62728'))

    ax.annotate('Rate hike\ncorrection', xy=(2022, 85), xytext=(2023.5, 110),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#666666'))

    # Deal count annotation
    ax.text(0.02, 0.98, 'Deal Count (2024): ~4,500 deals\nDown from 6,000+ in 2021',
           transform=ax.transAxes, fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: CB Insights, PitchBook, KPMG Pulse of FinTech (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'fintech_investment_trends.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
