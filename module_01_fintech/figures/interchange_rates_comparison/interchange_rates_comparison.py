"""
Interchange Fee Rates: EU vs USA Comparison
Shows regulated vs unregulated interchange fee caps

Output: interchange_rates_comparison.pdf
Module: module_01_fintech
Lesson: 2 - Digital Payments Fundamentals
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# DATA VERIFICATION SECTION
# =============================================================================
# Sources:
# 1. European Commission - Interchange Fee Regulation (IFR) 2015/751
#    URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751
#    Article 3: Consumer debit cap 0.2%
#    Article 4: Consumer credit cap 0.3%
#    Accessed: December 11, 2024
#
# 2. Federal Reserve Board - Regulation II (Durbin Amendment)
#    URL: https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm
#    Debit cap: $0.21 + 0.05% (for banks >$10B assets)
#    Note: Credit cards unregulated in US
#    Accessed: December 11, 2024
#
# 3. Visa and Mastercard published interchange fee schedules (2024)
#    Visa USA: https://usa.visa.com/support/merchant/library/visa-merchant-business-news-digest.html
#    Mastercard USA: https://www.mastercard.us/en-us/business/overview/support/merchant-interchange-rates.html
#    Accessed: December 11, 2024
#
# Data verification:
# - EU Consumer Debit: 0.2% cap (IFR Article 3)
# - EU Consumer Credit: 0.3% cap (IFR Article 4)
# - EU Commercial Cards: Exempt from caps (~1.5-2.5%)
# - US Debit (regulated): ~0.24% effective (Durbin applies to >$10B banks)
# - US Debit (exempt): ~0.7-1.0% (small banks exempt from Durbin)
# - US Credit: Unregulated, ~1.5-2.5% (rewards cards up to 3%)
# - US Premium Credit: Up to 3.5% for high-rewards cards
# =============================================================================

CHART_METADATA = {
    'title': 'Interchange Fee Rates Comparison',
    'source': 'EU IFR 2015/751, Fed Regulation II (2024)',
    'url': 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R0751',
    'module': 'module_01_fintech',
    'lesson': 2,
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
    """Create interchange rates comparison chart with verified regulatory data"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Card types
    card_types = ['Consumer\nDebit', 'Consumer\nCredit', 'Commercial\nCards', 'Premium\nRewards']

    # Interchange rates (percentage of transaction)
    # EU rates (regulated by IFR 2015/751)
    eu_rates = [0.2, 0.3, 2.0, 2.0]  # Commercial/Premium exempt from caps

    # US rates (market-driven, credit unregulated)
    us_rates = [0.8, 2.0, 2.5, 3.2]  # Average effective rates

    x = np.arange(len(card_types))
    width = 0.35

    # Create bars
    bars_eu = ax.bar(x - width/2, eu_rates, width, label='European Union',
                     color=MLBLUE, edgecolor='#333333', lw=1)
    bars_us = ax.bar(x + width/2, us_rates, width, label='United States',
                     color=MLORANGE, edgecolor='#333333', lw=1)

    # Add value labels
    for bar, val in zip(bars_eu, eu_rates):
        ax.annotate(f'{val}%',
                   xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                   xytext=(0, 3), textcoords="offset points",
                   ha='center', va='bottom', fontsize=8, fontweight='bold', color=MLBLUE)

    for bar, val in zip(bars_us, us_rates):
        ax.annotate(f'{val}%',
                   xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                   xytext=(0, 3), textcoords="offset points",
                   ha='center', va='bottom', fontsize=8, fontweight='bold', color=MLORANGE)

    ax.set_ylabel('Interchange Rate (%)', fontsize=10)
    ax.set_title('Interchange Fee Rates: EU vs USA', fontsize=12, fontweight='bold', pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(card_types, fontsize=9)
    ax.set_ylim(0, 4)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    ax.legend(loc='upper left', fontsize=9)

    # Add regulatory annotation
    ax.annotate('EU IFR 2015/751\nCaps: 0.2% debit, 0.3% credit',
                xy=(0, 0.3), xytext=(0.5, 1.5),
                fontsize=8, color=MLBLUE,
                arrowprops=dict(arrowstyle='->', color=MLBLUE, lw=1),
                bbox=dict(boxstyle='round', facecolor='#E8F4F8', edgecolor=MLBLUE, alpha=0.8))

    ax.annotate('US: Credit cards\nunregulated',
                xy=(1.35, 2.0), xytext=(1.8, 3.2),
                fontsize=8, color=MLORANGE,
                arrowprops=dict(arrowstyle='->', color=MLORANGE, lw=1),
                bbox=dict(boxstyle='round', facecolor='#FFF4E8', edgecolor=MLORANGE, alpha=0.8))

    # REQUIRED: Source citation
    fig.text(0.98, 0.02, f"Source: {CHART_METADATA['source']}",
             fontsize=7, ha='right', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'interchange_rates_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
