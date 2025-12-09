"""
Embedded Finance Growth
Shows embedded finance market growth

Output: embedded_finance_growth.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Embedded Finance Growth',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/embedded_finance_growth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create embedded finance growth chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    # Embedded finance market size in USD B
    market = [54, 73, 92, 115, 145, 185, 240, 310, 400, 520]

    # Historical vs projected
    historical = market[:4]
    projected = market[3:]

    ax.fill_between(years[:4], historical, alpha=0.3, color='#4A90E2')
    ax.plot(years[:4], historical, 'o-', color='#4A90E2', lw=3, markersize=10, label='Historical')

    ax.fill_between(years[3:], projected, alpha=0.2, color='#44A044')
    ax.plot(years[3:], projected, 's--', color='#44A044', lw=3, markersize=10, label='Projected')

    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Market Size (USD B)', fontsize=14)
    ax.set_title('Embedded Finance Market Growth', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 600)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(fontsize=12, loc='upper left')

    # CAGR
    ax.text(0.98, 0.95, 'CAGR: 26%\n(2024-2030)',
           transform=ax.transAxes, fontsize=14, fontweight='bold',
           ha='right', va='top', color='#44A044',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#44A044'))

    # Definition
    ax.text(0.02, 0.02, 'Embedded Finance: Financial services integrated into\nnon-financial platforms (e-commerce, SaaS, apps)',
           transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Bain & Company, Lightyear Capital, embedded finance reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'embedded_finance_growth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
