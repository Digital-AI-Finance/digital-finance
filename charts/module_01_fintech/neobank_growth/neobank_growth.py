"""
Neobank User Growth Timeline
Visualizes the growth of major neobanks over time
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Neobank User Growth Timeline',
    'url': 'https://github.com/Digital-AI-Finance/BSc-DigitalFinance/tree/main/charts/module_01_fintech/neobank_growth'
}

def create_neobank_growth_chart():
    """Create timeline chart of neobank user growth"""

    # Data (approximate user counts in millions)
    years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

    # User data for major neobanks (in millions)
    neobanks = {
        'Revolut': [0.1, 0.5, 2, 4, 8, 13, 16, 20, 30, 40],
        'N26': [0.1, 0.5, 1, 2.5, 5, 7, 8, 8, 8, 8.5],
        'Chime': [0, 0.1, 0.5, 2, 5, 8, 12, 13, 14, 15],
        'Nubank': [0.5, 2, 5, 8, 15, 30, 48, 70, 85, 95],
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    # Line styles (grayscale-friendly)
    styles = [
        {'color': '0.2', 'linestyle': '-', 'linewidth': 2, 'marker': 'o'},
        {'color': '0.4', 'linestyle': '--', 'linewidth': 2, 'marker': 's'},
        {'color': '0.55', 'linestyle': '-.', 'linewidth': 2, 'marker': '^'},
        {'color': '0.7', 'linestyle': ':', 'linewidth': 2.5, 'marker': 'd'},
    ]

    # Plot each neobank
    for idx, (bank, users) in enumerate(neobanks.items()):
        style = styles[idx]
        ax.plot(years, users, label=bank,
                color=style['color'], linestyle=style['linestyle'],
                linewidth=style['linewidth'], marker=style['marker'],
                markersize=5, markerfacecolor='white',
                markeredgewidth=1.5, markeredgecolor=style['color'])

    # Formatting
    ax.set_xlabel('Year', fontsize=8, fontweight='bold')
    ax.set_ylabel('Users (Millions)', fontsize=8, fontweight='bold')
    ax.set_title('Neobank User Growth (2015-2024)', fontsize=10, fontweight='bold', pad=15)

    # Grid
    ax.grid(True, axis='y', linestyle=':', alpha=0.4, color='0.5')
    ax.set_axisbelow(True)

    # Legend
    ax.legend(loc='upper left', fontsize=7, framealpha=0.95,
              edgecolor='0.5', fancybox=False)

    # Set y-axis to start at 0
    ax.set_ylim(0, max([max(users) for users in neobanks.values()]) * 1.1)
    ax.set_xlim(years[0], years[-1])

    # Tick formatting
    ax.tick_params(axis='both', labelsize=8)
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45)

    # Add milestone annotations
    ax.annotate('COVID-19\nPandemic', xy=(2020, 30), xytext=(2020, 65),
                ha='center', fontsize=6, color='0.3',
                arrowprops=dict(arrowstyle='->', color='0.4', linewidth=0.8))

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'neobank_growth.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_neobank_growth_chart()
