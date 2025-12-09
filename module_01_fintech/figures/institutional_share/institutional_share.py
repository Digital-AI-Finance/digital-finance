"""
Institutional vs Retail Investor Share
Shows the shift from retail to institutional investors in P2P

Output: institutional_share.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Institutional vs Retail Share',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/institutional_share'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create institutional share stacked area chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

    # Percentage breakdown (institutional vs retail)
    institutional = [5, 10, 20, 35, 50, 60, 70, 75, 80, 85, 88, 90]
    retail = [95, 90, 80, 65, 50, 40, 30, 25, 20, 15, 12, 10]

    ax.stackplot(years, retail, institutional,
                 labels=['Retail Investors', 'Institutional Investors'],
                 colors=['#4A90E2', '#44A044'], alpha=0.8)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Share of Funding (%)', fontsize=12)
    ax.set_title('P2P Platform Funding: Institutional vs Retail', fontsize=17, fontweight='bold', pad=15)

    ax.legend(loc='upper left', fontsize=10)
    ax.set_xlim(2012, 2023)
    ax.set_ylim(0, 100)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Key milestone annotations
    ax.annotate('IPO\neffect', xy=(2014.5, 50), fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.annotate('Post-2016\nregulation', xy=(2017, 50), fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Impact note
    impact = """Impact: Higher institutional share means:
    - Lower returns for retail (competition)
    - More stable funding
    - Less marketplace, more balance sheet"""
    ax.text(2012.5, 8, impact, fontsize=10, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: LendingClub/Prosper SEC filings, industry reports [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'institutional_share.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
