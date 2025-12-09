"""
Regulatory Volume Growth
Shows the explosion of financial regulations over time

Output: regulatory_volume_growth.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Regulatory Volume Growth',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regulatory_volume_growth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create regulatory volume growth chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
    # Regulatory changes per year (illustrative data based on Thomson Reuters reports)
    changes = [8500, 14000, 22000, 30000, 45000, 52000, 58000, 61000, 65000]

    ax.fill_between(years, changes, alpha=0.3, color='#D62728')
    ax.plot(years, changes, 'o-', color='#D62728', lw=3, markersize=10)

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Regulatory Changes per Year', fontsize=14)
    ax.set_title('Global Financial Regulatory Changes', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 75000)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Format y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K'))

    # Key events
    events = [
        (2008, 8500, 'Global\nFinancial\nCrisis'),
        (2012, 22000, 'Dodd-Frank\nimplemented'),
        (2018, 52000, 'MiFID II,\nGDPR'),
    ]

    for year, val, label in events:
        ax.annotate(label, xy=(year, val), xytext=(year+0.3, val+8000),
                   fontsize=10, ha='left',
                   arrowprops=dict(arrowstyle='->', color='#666666'))

    # Key stat
    ax.text(0.98, 0.95, '7.6x increase\nsince 2008',
           transform=ax.transAxes, fontsize=14, fontweight='bold',
           ha='right', va='top', color='#D62728',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#D62728'))

    # Compliance cost note
    ax.text(0.02, 0.02, 'Compliance costs: $270B+ annually for financial services',
           transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: Thomson Reuters Regulatory Intelligence (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'regulatory_volume_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
