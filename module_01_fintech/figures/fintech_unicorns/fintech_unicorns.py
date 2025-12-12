"""
Top FinTech Companies by Valuation (2024)
Shows major fintech companies by valuation with verified data

Output: fintech_unicorns.pdf
Module: module_01_fintech
Lesson: 1 - Introduction to FinTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# DATA VERIFICATION SECTION
# =============================================================================
# Sources:
# 1. CB Insights Unicorn Tracker
#    URL: https://www.cbinsights.com/research-unicorn-companies
#    Accessed: December 11, 2024
#
# 2. Statista - Most valuable fintech unicorns Q4 2024
#    URL: https://www.statista.com/statistics/1238898/most-valuable-fintech-unicorns-worldwide/
#    Accessed: December 11, 2024
#
# 3. Failory - Full List of 235 FinTech Unicorn Startups
#    URL: https://www.failory.com/startups/fintech-unicorns
#    Accessed: December 11, 2024
#
# Data verification (late 2024 valuations):
# - Ant Group: $78-80B (post-restructuring, down from $150B+ pre-IPO)
#   Source: Multiple reports post-2021 regulatory crackdown
# - Stripe: $70B (2024 valuation, up from $50B low in 2023)
#   Source: CB Insights, Founders Forum
# - Nubank: $60B (public company market cap, NYSE: NU)
#   Source: Public market data
# - Revolut: $45B (2024 funding round valuation)
#   Source: CB Insights, company announcements
# - Adyen: $40B (public company market cap, AMS: ADYEN)
#   Source: Public market data
# - Chime: $25B (2021 valuation, no new funding)
#   Source: CB Insights
# - Klarna: $14.6B (2024 funding, down from $46B peak)
#   Source: Company announcements
# - Plaid: $13.4B (2021 Series D valuation)
#   Source: CB Insights
# - N26: $9B (2021 valuation)
#   Source: CB Insights
# - Wise: $8B (public company market cap, LSE: WISE)
#   Source: Public market data
#
# Note: Private company valuations from last funding round; may not reflect current
# market value. Public companies marked with * show market cap.
# =============================================================================

CHART_METADATA = {
    'title': 'Top FinTech Companies by Valuation',
    'source': 'CB Insights, Statista, Company filings (Dec 2024)',
    'url': 'https://www.cbinsights.com/research-unicorn-companies',
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
    """Create FinTech unicorns chart with verified 2024 data"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Companies and valuations (verified from multiple sources)
    companies = ['Ant Group', 'Stripe', 'Nubank*', 'Revolut', 'Adyen*',
                'Chime', 'Klarna', 'Plaid', 'N26', 'Wise*']
    valuations = [78, 70, 60, 45, 40, 25, 14.6, 13.4, 9, 8]  # USD Billion
    # * = Public company (market cap as of Dec 2024)

    regions = ['Asia', 'USA', 'LatAm', 'UK', 'Europe',
               'USA', 'Europe', 'USA', 'Europe', 'UK']

    # Color by region
    color_map = {'Asia': MLRED, 'USA': MLBLUE, 'UK': MLPURPLE,
                 'Europe': MLGREEN, 'LatAm': MLORANGE}
    colors = [color_map[r] for r in regions]

    bars = ax.barh(companies, valuations, color=colors, edgecolor='#333333', lw=1)

    ax.set_xlabel('Valuation (USD Billion)', fontsize=10)
    ax.set_title('Top FinTech Companies by Valuation (2024)', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlim(0, 90)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    ax.invert_yaxis()  # Highest at top

    # Add value labels
    for bar, val in zip(bars, valuations):
        ax.annotate(f'${val}B',
                   xy=(bar.get_width(), bar.get_y() + bar.get_height()/2),
                   xytext=(3, 0), textcoords="offset points",
                   ha='left', va='center', fontsize=8, fontweight='bold')

    # Legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, facecolor=MLBLUE, edgecolor='#333333', label='USA'),
        plt.Rectangle((0,0),1,1, facecolor=MLPURPLE, edgecolor='#333333', label='UK'),
        plt.Rectangle((0,0),1,1, facecolor=MLGREEN, edgecolor='#333333', label='Europe'),
        plt.Rectangle((0,0),1,1, facecolor=MLRED, edgecolor='#333333', label='Asia'),
        plt.Rectangle((0,0),1,1, facecolor=MLORANGE, edgecolor='#333333', label='LatAm'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8, framealpha=0.9)

    # Note about valuations
    ax.text(0.98, 0.15, '* = Public company (market cap)\nPrivate valuations from last funding',
           transform=ax.transAxes, fontsize=7, va='bottom', ha='right',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.9))

    # REQUIRED: Source citation
    fig.text(0.98, 0.02, f"Source: {CHART_METADATA['source']}",
             fontsize=7, ha='right', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_unicorns.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
