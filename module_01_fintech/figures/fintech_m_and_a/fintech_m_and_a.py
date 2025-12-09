"""
FinTech M&A
Shows major FinTech mergers and acquisitions

Output: fintech_m_and_a.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech M&A',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_m_and_a'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech M&A diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Major FinTech M&A Deals', fontsize=20, fontweight='bold', ha='center')

    # Major deals
    deals = [
        {'acquirer': 'Schwab', 'target': 'TD Ameritrade', 'value': 'USD 26B', 'year': '2020', 'y': 7.5},
        {'acquirer': 'Morgan Stanley', 'target': 'E*TRADE', 'value': 'USD 13B', 'year': '2020', 'y': 6.5},
        {'acquirer': 'Visa', 'target': 'Plaid', 'value': 'USD 5.3B*', 'year': '2020', 'y': 5.5},
        {'acquirer': 'SoFi', 'target': 'Galileo', 'value': 'USD 1.2B', 'year': '2020', 'y': 4.5},
        {'acquirer': 'PayPal', 'target': 'Honey', 'value': 'USD 4B', 'year': '2019', 'y': 3.5},
        {'acquirer': 'Mastercard', 'target': 'Finicity', 'value': 'USD 825M', 'year': '2020', 'y': 2.5},
    ]

    for deal in deals:
        # Acquirer box
        acq_box = mpatches.FancyBboxPatch((1, deal['y']-0.4), 3, 0.8,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#4A90E2', alpha=0.2,
                                          edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(acq_box)
        ax.text(2.5, deal['y'], deal['acquirer'], ha='center', va='center',
               fontsize=12, fontweight='bold')

        # Arrow
        ax.annotate('', xy=(5.8, deal['y']), xytext=(4.2, deal['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
        ax.text(5, deal['y']+0.25, 'acquires', ha='center', fontsize=9)

        # Target box
        tgt_box = mpatches.FancyBboxPatch((6, deal['y']-0.4), 3, 0.8,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#44A044', alpha=0.2,
                                          edgecolor='#44A044', lw=1.5)
        ax.add_patch(tgt_box)
        ax.text(7.5, deal['y'], deal['target'], ha='center', va='center',
               fontsize=12, fontweight='bold')

        # Value
        ax.text(10.5, deal['y'], deal['value'], ha='center', va='center',
               fontsize=12, fontweight='bold', color='#D62728')

        # Year
        ax.text(12.5, deal['y'], deal['year'], ha='center', va='center',
               fontsize=11, color='#666666')

    # Header row
    ax.text(2.5, 8.3, 'Acquirer', ha='center', fontsize=12, fontweight='bold', color='#4A90E2')
    ax.text(7.5, 8.3, 'Target', ha='center', fontsize=12, fontweight='bold', color='#44A044')
    ax.text(10.5, 8.3, 'Value', ha='center', fontsize=12, fontweight='bold', color='#D62728')
    ax.text(12.5, 8.3, 'Year', ha='center', fontsize=12, fontweight='bold')

    # Note about Visa/Plaid
    ax.text(7, 1.5, '*Visa/Plaid deal blocked by DOJ antitrust concerns',
           ha='center', fontsize=10, style='italic', color='#666666')

    # Trend note
    trend = "2023-24 Trend: Consolidation continues, focus on profitable targets, lower valuations"
    ax.text(7, 0.8, trend, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: PitchBook, company announcements',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_m_and_a.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
