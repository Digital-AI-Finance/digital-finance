"""
Lemonade Economics
Shows Lemonade's financial performance and metrics

Output: lemonade_economics.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Lemonade Economics',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/lemonade_economics'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Lemonade economics chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Chart 1: Premium Growth
    ax1 = axes[0]
    years = ['2019', '2020', '2021', '2022', '2023', '2024E']
    premiums = [116, 213, 380, 525, 680, 850]  # $M in-force premium

    bars1 = ax1.bar(years, premiums, color='#FF69B4', edgecolor='#333333', lw=1.5)
    ax1.set_ylabel('In-Force Premium ($M)', fontsize=14)
    ax1.set_title('Lemonade Premium Growth', fontsize=17, fontweight='bold', pad=10)
    ax1.set_ylim(0, 1000)
    ax1.yaxis.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars1, premiums):
        ax1.annotate(f'${val}M',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

    # CAGR annotation
    ax1.text(0.95, 0.95, 'CAGR: ~48%', transform=ax1.transAxes, fontsize=12,
            fontweight='bold', ha='right', va='top', color='#FF69B4',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#FF69B4'))

    # Chart 2: Key Metrics
    ax2 = axes[1]
    metrics = ['Loss\nRatio', 'Gross\nMargin', 'Customer\nRetention', 'CAC\nPayback']
    values = [87, 25, 85, 24]  # %, %, %, months
    colors = ['#D62728', '#44A044', '#4A90E2', '#FF7F0E']

    bars2 = ax2.bar(metrics, values, color=colors, edgecolor='#333333', lw=1.5)
    ax2.set_ylabel('Value (% or months)', fontsize=14)
    ax2.set_title('Key Operating Metrics (2024)', fontsize=17, fontweight='bold', pad=10)
    ax2.set_ylim(0, 120)
    ax2.yaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Add value labels with units
    units = ['%', '%', '%', ' mo']
    for bar, val, unit in zip(bars2, values, units):
        ax2.annotate(f'{val}{unit}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Profitability note
    fig.text(0.5, 0.02, 'Source: Lemonade SEC filings, Q3 2024 earnings | Note: Not yet profitable, targeting 2025-2026',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'lemonade_economics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
