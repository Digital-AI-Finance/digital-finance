"""
Betterment Growth Timeline
Shows Betterment's growth and key milestones

Output: betterment_growth.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Betterment Growth',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/betterment_growth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Betterment growth chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
    aum = [0, 1, 3, 6, 14, 22, 34, 40]  # AUM in $B

    ax.fill_between(years, aum, alpha=0.3, color='#44A044')
    ax.plot(years, aum, 'o-', color='#44A044', lw=3, markersize=10)

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Assets Under Management ($B)', fontsize=14)
    ax.set_title('Betterment: Pioneer Robo-Advisor Growth', fontsize=20, fontweight='bold', pad=15)

    ax.set_xlim(2009, 2025)
    ax.set_ylim(0, 45)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Milestones
    milestones = [
        (2010, 0.5, 'Launch\n(TechCrunch Disrupt)'),
        (2014, 5, 'Retirement\naccounts added'),
        (2017, 11, 'Premium tier\nlaunched'),
        (2021, 29, 'Checking &\ncash accounts'),
    ]

    for year, y, text in milestones:
        ax.annotate(text, xy=(year, y), xytext=(year, y+8),
                   fontsize=11, ha='center',
                   arrowprops=dict(arrowstyle='->', color='#333333'),
                   bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Key stats
    stats = """Key Metrics (2024):
    - 800,000+ customers
    - $40B+ AUM
    - 0.25% annual fee (basic)
    Source: Betterment"""

    ax.text(2024, 10, stats, fontsize=11, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'betterment_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
