"""
Neobank Profitability Journey
Shows the path to profitability for major neobanks

Output: neobank_profitability.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank Profitability Journey',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/neobank_profitability'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank profitability journey chart"""
    fig, ax = plt.subplots(figsize=(13, 7))

    # Neobanks and their profitability journey
    # Based on public announcements and annual reports
    neobanks = {
        'Nubank': {
            'founded': 2013,
            'first_profit': 2023,
            'color': '#6B5B95',
            'status': 'Profitable',
            'y': 5
        },
        'Revolut': {
            'founded': 2015,
            'first_profit': 2023,
            'color': '#333333',
            'status': 'Profitable',
            'y': 4
        },
        'Monzo': {
            'founded': 2015,
            'first_profit': 2024,
            'color': '#FF7F0E',
            'status': 'Near-profit',
            'y': 3
        },
        'N26': {
            'founded': 2013,
            'first_profit': None,
            'color': '#4A90E2',
            'status': 'Path to profit',
            'y': 2
        },
        'Chime': {
            'founded': 2013,
            'first_profit': None,
            'color': '#44A044',
            'status': 'Path to profit',
            'y': 1
        }
    }

    # Timeline
    years = range(2013, 2026)
    ax.set_xlim(2012.5, 2025.5)
    ax.set_ylim(0, 6)

    # Draw timeline for each neobank
    for name, data in neobanks.items():
        y = data['y']
        color = data['color']

        # Founding marker
        ax.plot(data['founded'], y, 'o', color=color, markersize=12, zorder=3)
        ax.text(data['founded'], y+0.15, 'Founded', ha='center', va='bottom',
               fontsize=7, color='#666666')

        # Timeline line
        end_year = 2025
        ax.plot([data['founded'], end_year], [y, y], '-', color=color, lw=3, alpha=0.6)

        # Profitability marker
        if data['first_profit']:
            ax.plot(data['first_profit'], y, '*', color='#D62728', markersize=15, zorder=4)
            ax.text(data['first_profit'], y-0.2, 'First\nProfit', ha='center', va='top',
                   fontsize=7, color='#D62728', fontweight='bold')

        # Label
        ax.text(2012.7, y, f"{name}", ha='right', va='center',
               fontsize=10, fontweight='bold', color=color)

        # Status
        status_colors = {'Profitable': '#44A044', 'Near-profit': '#FF7F0E', 'Path to profit': '#999999'}
        ax.text(2025.3, y, data['status'], ha='left', va='center',
               fontsize=8, color=status_colors.get(data['status'], '#999999'))

    # Key metrics box
    metrics = """Years to Profitability:
    - Nubank: 10 years (2013-2023)
    - Revolut: 8 years (2015-2023)
    - Monzo: 9 years (2015-2024)
    - N26: 11+ years (ongoing)
    - Chime: 11+ years (ongoing)

    Key Success Factors:
    - Customer scale (>5M users)
    - Revenue diversification
    - CAC optimization
    - Interest rate environment"""

    ax.text(2019, 0.3, metrics, fontsize=8, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    ax.set_xlabel('Year', fontsize=11)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Title
    ax.set_title('Neobank Path to Profitability', fontsize=14, fontweight='bold', pad=15)

    # Legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#666666',
                   markersize=10, label='Founded'),
        plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='#D62728',
                   markersize=12, label='First Profit'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

    # Source
    fig.text(0.5, 0.02, 'Source: Company annual reports and public announcements (2023-2024)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'neobank_profitability.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
