"""
Banking as a Service (BaaS) Partnership Model
Shows how BaaS enables neobanks through partner banks

Output: baas_partnership.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'BaaS Partnership Model',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/baas_partnership'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create BaaS partnership model diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Three layers
    # Top: FinTech/Neobank (customer-facing)
    fintech_box = mpatches.FancyBboxPatch((1, 7), 11, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(fintech_box)
    ax.text(6.5, 8.3, 'FinTech / Neobank Layer', fontsize=12, fontweight='bold',
           ha='center', color='white')
    ax.text(6.5, 7.7, 'Customer App | Brand | UX | Marketing | Support',
           fontsize=9, ha='center', color='white')
    ax.text(2, 7.3, 'Examples: Chime, Current, Dave, Mercury', fontsize=8,
           ha='left', style='italic', color='white')

    # Middle: BaaS Platform
    baas_box = mpatches.FancyBboxPatch((1, 4.2), 11, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(baas_box)
    ax.text(6.5, 5.5, 'BaaS Platform Layer', fontsize=12, fontweight='bold',
           ha='center', color='white')
    ax.text(6.5, 4.9, 'APIs | Ledger | Compliance Tools | Card Issuance | KYC',
           fontsize=9, ha='center', color='white')
    ax.text(2, 4.5, 'Examples: Synapse, Unit, Treasury Prime, Galileo', fontsize=8,
           ha='left', style='italic', color='white')

    # Bottom: Sponsor Bank
    bank_box = mpatches.FancyBboxPatch((1, 1.4), 11, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#333333', edgecolor='#333333', lw=2)
    ax.add_patch(bank_box)
    ax.text(6.5, 2.7, 'Sponsor Bank Layer', fontsize=12, fontweight='bold',
           ha='center', color='white')
    ax.text(6.5, 2.1, 'Banking License | FDIC Insurance | Fed Access | Regulatory Compliance',
           fontsize=9, ha='center', color='white')
    ax.text(2, 1.7, 'Examples: Evolve, Bancorp, Cross River, Stride', fontsize=8,
           ha='left', style='italic', color='white')

    # Connection arrows
    # FinTech to BaaS
    ax.annotate('', xy=(5, 6.2), xytext=(5, 7),
               arrowprops=dict(arrowstyle='<->', color='#44A044', lw=2))
    ax.text(5.3, 6.6, 'APIs', fontsize=8, color='#44A044')

    # BaaS to Bank
    ax.annotate('', xy=(5, 3.4), xytext=(5, 4.2),
               arrowprops=dict(arrowstyle='<->', color='#44A044', lw=2))
    ax.text(5.3, 3.8, 'Banking\nRails', fontsize=8, color='#44A044')

    # Right side: what each layer provides
    provides = [
        (12.5, 8, 'Provides:\n- Customer acquisition\n- Product experience\n- Brand trust'),
        (12.5, 5.2, 'Provides:\n- Tech infrastructure\n- API abstraction\n- Compliance tooling'),
        (12.5, 2.4, 'Provides:\n- Charter/License\n- Deposit insurance\n- Regulatory cover'),
    ]

    for x, y, text in provides:
        ax.text(x, y, text, fontsize=7, ha='right', va='center',
               bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.8))

    # Revenue flow
    ax.text(0.5, 5.2, 'Revenue\nFlow', fontsize=9, ha='center', fontweight='bold', color='#D62728')
    ax.annotate('', xy=(0.5, 4.5), xytext=(0.5, 8.5),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2))

    # Title
    ax.text(6.5, 9.7, 'Banking as a Service (BaaS) Stack', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9.3, 'How neobanks launch without banking licenses', fontsize=10,
           ha='center', style='italic', color='#666666')

    # Economics note
    econ = """Economics:
    - FinTech keeps 60-80% of interchange
    - BaaS takes 10-20%
    - Sponsor bank takes 10-20%"""
    ax.text(0.5, 1.5, econ, fontsize=7, ha='left', va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: Industry structure based on public disclosures',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'baas_partnership.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
