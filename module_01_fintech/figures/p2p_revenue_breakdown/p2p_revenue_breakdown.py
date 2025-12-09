"""
P2P Platform Revenue Breakdown
Shows revenue sources for P2P lending platforms

Output: p2p_revenue_breakdown.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'P2P Revenue Breakdown',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_revenue_breakdown'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P revenue breakdown pie chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # LendingClub revenue breakdown
    lc_labels = ['Origination\nFees', 'Servicing\nFees', 'Interest\nIncome', 'Other']
    lc_sizes = [45, 20, 30, 5]
    lc_colors = ['#4A90E2', '#44A044', '#FF7F0E', '#999999']

    wedges1, texts1, autotexts1 = ax1.pie(lc_sizes, labels=lc_labels, autopct='%1.0f%%',
                                           colors=lc_colors, startangle=90,
                                           wedgeprops=dict(edgecolor='#333333', lw=1.5))
    ax1.set_title('LendingClub (Post-Bank)', fontsize=14, fontweight='bold', pad=10)
    for autotext in autotexts1:
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    for text in texts1:
        text.set_fontsize(10)

    # Traditional P2P platform
    p2p_labels = ['Origination\nFees', 'Servicing\nFees', 'Late\nFees', 'Investor\nFees']
    p2p_sizes = [60, 25, 10, 5]
    p2p_colors = ['#4A90E2', '#44A044', '#D62728', '#6B5B95']

    wedges2, texts2, autotexts2 = ax2.pie(p2p_sizes, labels=p2p_labels, autopct='%1.0f%%',
                                           colors=p2p_colors, startangle=90,
                                           wedgeprops=dict(edgecolor='#333333', lw=1.5))
    ax2.set_title('Pure P2P Marketplace', fontsize=14, fontweight='bold', pad=10)
    for autotext in autotexts2:
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    for text in texts2:
        text.set_fontsize(10)

    fig.suptitle('P2P Platform Revenue Breakdown', fontsize=17, fontweight='bold', y=1.02)

    # Add note
    fig.text(0.5, 0.02, 'Note: Bank model includes interest income from balance sheet lending | Source: Company filings [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_revenue_breakdown.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
