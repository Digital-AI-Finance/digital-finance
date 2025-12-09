"""
RegTech Market Growth
Shows RegTech market size and growth projections

Output: regtech_market_growth.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Market Growth',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regtech_market_growth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create RegTech market growth chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    # Market size in $B
    market_size = [6.3, 7.8, 9.5, 11.8, 14.8, 17.9, 21.5, 25.8, 30.9, 37.1, 44.5]

    # Historical vs projected
    historical = market_size[:5]
    projected = market_size[4:]

    ax.fill_between(years[:5], historical, alpha=0.3, color='#4A90E2')
    ax.plot(years[:5], historical, 'o-', color='#4A90E2', lw=3, markersize=10, label='Historical')

    ax.fill_between(years[4:], projected, alpha=0.2, color='#44A044')
    ax.plot(years[4:], projected, 's--', color='#44A044', lw=3, markersize=10, label='Projected')

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Market Size ($B)', fontsize=14)
    ax.set_title('Global RegTech Market Size', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 50)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(fontsize=12, loc='upper left')

    # CAGR annotation
    ax.text(0.98, 0.95, 'CAGR: 18%\n(2024-2030)',
           transform=ax.transAxes, fontsize=14, fontweight='bold',
           ha='right', va='top', color='#44A044',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#44A044'))

    # Key drivers
    drivers = 'Key Drivers: Regulatory complexity, digital transformation,\nAI adoption, cost pressure, remote work'
    ax.text(0.02, 0.02, drivers, transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Grand View Research, MarketsandMarkets (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'regtech_market_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
