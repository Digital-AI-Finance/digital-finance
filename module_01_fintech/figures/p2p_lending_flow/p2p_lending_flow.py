"""
P2P Lending Flow
Shows how money flows from investors to borrowers via P2P platform

Output: p2p_lending_flow.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P Lending Flow',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_lending_flow'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P lending flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Lending Flow', fontsize=17, fontweight='bold', ha='center')

    # Borrowers (left)
    borrower_box = mpatches.FancyBboxPatch((0.5, 4), 3, 3, boxstyle='round,pad=0.1',
                                            facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(borrower_box)
    ax.text(2, 6.2, 'BORROWERS', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(2, 5.5, 'Apply for loans', ha='center', fontsize=10, color='white')
    ax.text(2, 4.8, 'Get funded', ha='center', fontsize=10, color='white')
    ax.text(2, 4.3, 'Repay principal', ha='center', fontsize=10, color='white')
    ax.text(2, 3.8, '+ interest', ha='center', fontsize=10, color='white')

    # Platform (center)
    platform_box = mpatches.FancyBboxPatch((5, 3), 3, 5, boxstyle='round,pad=0.1',
                                            facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(platform_box)
    ax.text(6.5, 7.3, 'P2P', ha='center', fontsize=14, fontweight='bold', color='white')
    ax.text(6.5, 6.6, 'PLATFORM', ha='center', fontsize=14, fontweight='bold', color='white')
    ax.text(6.5, 5.5, 'Credit scoring', ha='center', fontsize=10, color='white')
    ax.text(6.5, 4.9, 'Risk grading', ha='center', fontsize=10, color='white')
    ax.text(6.5, 4.3, 'Loan matching', ha='center', fontsize=10, color='white')
    ax.text(6.5, 3.7, 'Servicing', ha='center', fontsize=10, color='white')

    # Investors (right)
    investor_box = mpatches.FancyBboxPatch((9.5, 4), 3, 3, boxstyle='round,pad=0.1',
                                            facecolor='#44A044', edgecolor='#333333', lw=2)
    ax.add_patch(investor_box)
    ax.text(11, 6.2, 'INVESTORS', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(11, 5.5, 'Provide capital', ha='center', fontsize=10, color='white')
    ax.text(11, 4.8, 'Select loans', ha='center', fontsize=10, color='white')
    ax.text(11, 4.3, 'Receive returns', ha='center', fontsize=10, color='white')

    # Arrows with labels
    # Borrower -> Platform
    ax.annotate('', xy=(4.9, 5.5), xytext=(3.6, 5.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(4.25, 5.9, 'Loan', fontsize=10, ha='center')
    ax.text(4.25, 5.1, 'Application', fontsize=10, ha='center')

    # Platform -> Borrower
    ax.annotate('', xy=(3.6, 4.5), xytext=(4.9, 4.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(4.25, 4.1, 'Funds', fontsize=10, ha='center', color='#44A044')

    # Investor -> Platform
    ax.annotate('', xy=(8.1, 5.5), xytext=(9.4, 5.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(8.75, 5.9, 'Capital', fontsize=10, ha='center', color='#44A044')

    # Platform -> Investor
    ax.annotate('', xy=(9.4, 4.5), xytext=(8.1, 4.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(8.75, 4.1, 'Returns', fontsize=10, ha='center')

    # Platform fee note
    ax.text(6.5, 2.2, 'Platform Fee: 1-5% of loan amount (origination) + servicing fees',
           ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F0FE', edgecolor='#4A90E2'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL FLOW DIAGRAM]',
            fontsize=9, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_lending_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
