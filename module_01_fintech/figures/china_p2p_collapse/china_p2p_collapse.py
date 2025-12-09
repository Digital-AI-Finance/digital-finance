"""
China P2P Collapse
Shows the rise and fall of China's P2P lending industry

Output: china_p2p_collapse.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'China P2P Collapse',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/china_p2p_collapse'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create China P2P collapse chart"""
    fig, ax1 = plt.subplots(figsize=(12, 7))

    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

    # Number of active platforms
    platforms = [200, 800, 1575, 3500, 5800, 5500, 3000, 900, 50, 0]

    # Outstanding loan balance (in $B)
    balance = [5, 20, 50, 100, 180, 250, 200, 100, 20, 0]

    color1 = '#4A90E2'
    color2 = '#D62728'

    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Active Platforms', fontsize=12, color=color1)
    ax1.bar(years, platforms, color=color1, alpha=0.7, width=0.6)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 6500)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Outstanding Balance ($B)', fontsize=12, color=color2)
    ax2.plot(years, balance, 'o-', color=color2, lw=3, markersize=8)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 300)

    ax1.set_title('China P2P Industry: Rise and Collapse', fontsize=17, fontweight='bold', pad=15)

    # Key events
    events = [
        (2015, 4500, 'Ezubao Ponzi\n($7.6B fraud)'),
        (2016, 6000, 'Peak:\n6,000+ platforms'),
        (2018, 3800, 'Regulatory\ncrackdown'),
        (2020, 1200, 'Industry\nbanned'),
    ]

    for year, y, text in events:
        ax1.annotate(text, xy=(year, platforms[years.index(year)] + 200), fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700', alpha=0.9))

    # Lessons box
    lessons = """Lessons Learned:
    - Lack of licensing led to fraud
    - Guarantee promises unsustainable
    - Shadow banking risks
    - ~$115B in investor losses"""

    ax1.text(2011.5, 6000, lessons, fontsize=10, va='top',
            bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: PBOC, CBRC, WDZJ.com industry data',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'china_p2p_collapse.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
