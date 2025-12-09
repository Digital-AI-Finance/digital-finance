"""
Global Open Banking Map
Shows adoption of open banking regulations worldwide

Output: global_open_banking_map.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Global Open Banking Map',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/global_open_banking_map'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create global open banking adoption chart"""
    fig, ax = plt.subplots(figsize=(13, 8))

    # Data: regions and their open banking status
    regions = [
        ('UK', 'Mandatory', 2018, '#44A044', 'CMA Order'),
        ('EU', 'Mandatory', 2018, '#44A044', 'PSD2'),
        ('Australia', 'Mandatory', 2020, '#44A044', 'CDR'),
        ('Brazil', 'Mandatory', 2021, '#44A044', 'Open Finance'),
        ('Mexico', 'Mandatory', 2022, '#44A044', 'FinTech Law'),
        ('Saudi Arabia', 'Mandatory', 2022, '#44A044', 'SAMA'),
        ('India', 'Emerging', 2021, '#4A90E2', 'Account Aggregator'),
        ('Singapore', 'Market-led', 2020, '#FF7F0E', 'SGQR/PayNow'),
        ('Hong Kong', 'Market-led', 2019, '#FF7F0E', 'HKMA Framework'),
        ('Japan', 'Market-led', 2017, '#FF7F0E', 'Banking Act Rev'),
        ('US', 'Market-led', 2024, '#FF7F0E', 'CFPB Rule 1033'),
        ('Canada', 'In Progress', 2024, '#999999', 'Framework TBD'),
        ('South Korea', 'Market-led', 2019, '#FF7F0E', 'MyData'),
    ]

    # Sort by year
    regions_sorted = sorted(regions, key=lambda x: x[2])

    y_positions = np.arange(len(regions_sorted))
    colors = [r[3] for r in regions_sorted]
    years = [r[2] for r in regions_sorted]

    # Horizontal bar chart showing timeline
    bars = ax.barh(y_positions, [2025 - y for y in years], left=years,
                   color=colors, edgecolor='#333333', lw=0.5, height=0.7)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([r[0] for r in regions_sorted], fontsize=9)
    ax.set_xlim(2016, 2026)
    ax.set_xlabel('Year', fontsize=11)

    # Add framework labels
    for i, (region, status, year, color, framework) in enumerate(regions_sorted):
        ax.text(year + 0.1, i, f'{framework} ({status})', va='center',
               fontsize=7, color='white', fontweight='bold')

    ax.set_title('Global Open Banking Adoption Timeline',
                fontsize=14, fontweight='bold', pad=15)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#44A044', edgecolor='#333333', label='Mandatory'),
        mpatches.Patch(facecolor='#FF7F0E', edgecolor='#333333', label='Market-led'),
        mpatches.Patch(facecolor='#4A90E2', edgecolor='#333333', label='Emerging'),
        mpatches.Patch(facecolor='#999999', edgecolor='#333333', label='In Progress'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Key differences box
    differences = """Approach Differences:
    - Mandatory: Government-led with compliance deadlines
    - Market-led: Industry-driven with guidance
    - Scope varies: payments only vs full open finance"""

    ax.text(2016.5, 11, differences, fontsize=8, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: OECD, national regulatory announcements (as of 2024)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'global_open_banking_map.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
