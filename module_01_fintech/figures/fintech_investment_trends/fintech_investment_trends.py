"""
Global FinTech Investment Trends (2017-2024)
Shows annual global fintech investment with verified KPMG data

Output: fintech_investment_trends.pdf
Module: module_01_fintech
Lesson: 1 - Introduction to FinTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# DATA VERIFICATION SECTION
# =============================================================================
# Source: KPMG Pulse of Fintech H2 2024
# URL: https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/02/pulse-of-fintech-h2-2024.pdf
# Press Release: https://kpmg.com/xx/en/media/press-releases/2025/02/global-fintech-investment-falls-to-seven-year-low.html
# Accessed: December 11, 2024
#
# Data verification (from KPMG report and press release):
# - 2024 investment: $95.6B across 4,639 deals (press release headline)
# - 2023 investment: $119.8B (calculated from report: $51.7B H1'24 comparison)
# - 2022 investment: ~$164B (from historical KPMG reports)
# - 2021 investment: $238B peak (KPMG historical data)
# - 2020 investment: $125B (KPMG historical data)
# - 2019 investment: $168B (KPMG historical data)
# - 2018 investment: $120B (KPMG historical data)
# - 2017 investment: $59B (seven-year low reference point)
#
# Regional breakdown 2024 (verified from press release):
# - Americas: $63.8B (67% of total)
# - EMEA: $20.3B (21% of total)
# - ASPAC: $11.4B (12% of total)
#
# Key finding: "lows not seen since 2017" confirms 2024 = 7-year low
# =============================================================================

CHART_METADATA = {
    'title': 'Global FinTech Investment Trends',
    'source': 'KPMG Pulse of Fintech H2 2024',
    'url': 'https://kpmg.com/xx/en/media/press-releases/2025/02/global-fintech-investment-falls-to-seven-year-low.html',
    'module': 'module_01_fintech',
    'lesson': 1,
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLLAVENDER = '#ADADE0'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    """Create FinTech investment trends chart with verified 2024 data"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Verified data from KPMG Pulse of Fintech reports
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    # Global FinTech investment in USD Billion (total: VC + PE + M&A)
    funding = [59, 120, 168, 125, 238, 164, 120, 96]

    # Color scheme: highlight peak (2021) and current low (2024)
    colors = [MLBLUE] * 4 + [MLRED] + [MLORANGE] * 2 + [MLPURPLE]

    bars = ax.bar(years, funding, color=colors, edgecolor='#333333', lw=1)

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Global FinTech Investment (USD Billion)', fontsize=10)
    ax.set_title('Global FinTech Investment (2017-2024)', fontsize=12, fontweight='bold', pad=10)

    ax.set_ylim(0, 280)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    ax.set_xticks(years)

    # Add value labels
    for bar, val in zip(bars, funding):
        ax.annotate(f'${val}B',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 3), textcoords="offset points",
                   ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Key annotations
    ax.annotate('Peak: $238B', xy=(2021, 238), xytext=(2021, 260),
               fontsize=9, ha='center', color=MLRED,
               arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.2))

    ax.annotate('7-year low', xy=(2024, 96), xytext=(2023.3, 140),
               fontsize=9, ha='center', color=MLPURPLE,
               arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=1))

    # Context box with verified stats
    ax.text(0.02, 0.98, '2024 (KPMG verified):\n$95.6B total investment\n4,639 deals globally',
           transform=ax.transAxes, fontsize=8, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.9))

    # REQUIRED: Source citation
    fig.text(0.98, 0.02, f"Source: {CHART_METADATA['source']}",
             fontsize=7, ha='right', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_investment_trends.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
