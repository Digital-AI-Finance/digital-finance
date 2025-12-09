"""
P2P Lending vs Traditional Banking
Compares P2P platforms with traditional bank lending

Output: p2p_vs_bank.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'P2P vs Traditional Banking',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/p2p_vs_bank'
}

# 20% larger fonts
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create P2P vs bank comparison diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.3, 'P2P Lending vs Traditional Banking', fontsize=17, fontweight='bold', ha='center')

    # Traditional Bank (left)
    bank_box = mpatches.FancyBboxPatch((0.5, 3.5), 5.5, 5, boxstyle='round,pad=0.1',
                                        facecolor='#4A90E2', alpha=0.2,
                                        edgecolor='#4A90E2', lw=2)
    ax.add_patch(bank_box)
    ax.text(3.25, 8, 'Traditional Bank', ha='center', fontsize=14, fontweight='bold', color='#4A90E2')

    bank_features = [
        ('Intermediary', 'Bank holds deposits, lends own capital'),
        ('Cost structure', 'Branches, staff, compliance overhead'),
        ('Interest spread', '3-6% spread between deposit/loan rates'),
        ('Approval time', 'Days to weeks'),
        ('Minimum loan', 'Often $5,000+'),
    ]
    for i, (feat, desc) in enumerate(bank_features):
        ax.text(0.8, 7.2-i*0.8, f'{feat}:', fontsize=10, fontweight='bold')
        ax.text(3.2, 7.2-i*0.8, desc, fontsize=10)

    # P2P Platform (right)
    p2p_box = mpatches.FancyBboxPatch((7, 3.5), 5.5, 5, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.2,
                                       edgecolor='#44A044', lw=2)
    ax.add_patch(p2p_box)
    ax.text(9.75, 8, 'P2P Platform', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    p2p_features = [
        ('Marketplace', 'Connects borrowers directly to investors'),
        ('Cost structure', 'Tech platform, lower overhead'),
        ('Interest spread', 'Platform takes 1-3% fee'),
        ('Approval time', 'Minutes to hours (automated)'),
        ('Minimum loan', '$1,000 or less'),
    ]
    for i, (feat, desc) in enumerate(p2p_features):
        ax.text(7.3, 7.2-i*0.8, f'{feat}:', fontsize=10, fontweight='bold')
        ax.text(9.5, 7.2-i*0.8, desc, fontsize=10)

    # Value proposition
    value = "P2P Value: Better rates for borrowers | Higher returns for investors | Faster decisions"
    ax.text(6.5, 2.8, value, ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Key metrics comparison
    metrics = """Typical Rates (2024):
    Bank personal loan: 10-24% APR
    P2P personal loan: 7-20% APR
    Bank savings: 4-5% APY
    P2P investor return: 5-10%
    Source: Bankrate, LendingClub"""

    ax.text(6.5, 1.5, metrics, ha='center', fontsize=10, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'p2p_vs_bank.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
