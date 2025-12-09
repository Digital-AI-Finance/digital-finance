"""
PSD2 Architecture Diagram
Shows the regulatory framework and participant types under PSD2

Output: psd2_architecture.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'PSD2 Architecture',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/psd2_architecture'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create PSD2 architecture diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.7, 'PSD2 Regulatory Architecture',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9.2, 'Payment Services Directive 2 (EU 2015/2366)',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Account Servicing Payment Service Providers (ASPSPs) - Banks
    aspsp_box = mpatches.FancyBboxPatch((0.5, 5.5), 3.5, 3,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#333333', edgecolor='none')
    ax.add_patch(aspsp_box)
    ax.text(2.25, 8, 'ASPSP', ha='center', va='center', fontsize=12,
           fontweight='bold', color='white')
    ax.text(2.25, 7.4, 'Account Servicing\nPayment Service Provider',
           ha='center', va='center', fontsize=8, color='white')
    ax.text(2.25, 6.3, 'Traditional Banks\nHold customer accounts\nMust provide API access',
           ha='center', va='center', fontsize=8, color='#CCCCCC')

    # Third Party Providers (TPPs)
    # AISP
    aisp_box = mpatches.FancyBboxPatch((5, 6.5), 3.5, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#4A90E2', edgecolor='none')
    ax.add_patch(aisp_box)
    ax.text(6.75, 8, 'AISP', ha='center', va='center', fontsize=12,
           fontweight='bold', color='white')
    ax.text(6.75, 7.4, 'Account Information\nService Provider',
           ha='center', va='center', fontsize=8, color='white')
    ax.text(6.75, 6.85, 'Read-only access', ha='center', fontsize=7, color='#CCE5FF')

    # PISP
    pisp_box = mpatches.FancyBboxPatch((9, 6.5), 3.5, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#44A044', edgecolor='none')
    ax.add_patch(pisp_box)
    ax.text(10.75, 8, 'PISP', ha='center', va='center', fontsize=12,
           fontweight='bold', color='white')
    ax.text(10.75, 7.4, 'Payment Initiation\nService Provider',
           ha='center', va='center', fontsize=8, color='white')
    ax.text(10.75, 6.85, 'Initiate payments', ha='center', fontsize=7, color='#CCE5CC')

    # CBPII
    cbpii_box = mpatches.FancyBboxPatch((7, 4), 3.5, 2,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#FF7F0E', edgecolor='none')
    ax.add_patch(cbpii_box)
    ax.text(8.75, 5.5, 'CBPII', ha='center', va='center', fontsize=12,
           fontweight='bold', color='white')
    ax.text(8.75, 4.9, 'Card-Based Payment\nInstrument Issuer',
           ha='center', va='center', fontsize=8, color='white')
    ax.text(8.75, 4.35, 'Confirm funds', ha='center', fontsize=7, color='#FFE5CC')

    # Customer
    customer_circle = mpatches.Circle((2.25, 2.5), 0.8, facecolor='#6B5B95',
                                       edgecolor='#333333', lw=2)
    ax.add_patch(customer_circle)
    ax.text(2.25, 2.5, 'Customer', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # Arrows
    # Customer to ASPSP
    ax.annotate('', xy=(2.25, 5.5), xytext=(2.25, 3.3),
               arrowprops=dict(arrowstyle='<->', color='#333333', lw=2))
    ax.text(1.5, 4.4, 'Has\nAccount', fontsize=7, color='#666666')

    # ASPSP to AISPs (API)
    ax.annotate('', xy=(5, 7.5), xytext=(4, 7.5),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))
    ax.text(4.5, 7.9, 'AIS API', fontsize=7, color='#4A90E2')

    # ASPSP to PISPs (API)
    ax.annotate('', xy=(9, 7), xytext=(4, 6.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2,
                              connectionstyle='arc3,rad=-0.2'))
    ax.text(6.5, 5.8, 'PIS API', fontsize=7, color='#44A044')

    # Customer consent flow
    ax.annotate('', xy=(6.75, 6.5), xytext=(3, 2.5),
               arrowprops=dict(arrowstyle='->', color='#999999', lw=1.5,
                              connectionstyle='arc3,rad=-0.3', linestyle='--'))
    ax.text(5, 3.8, 'Consent', fontsize=7, color='#999999', rotation=30)

    # Key requirements box
    requirements = """Key PSD2 Requirements:
    1. Strong Customer Authentication (SCA)
    2. Secure communication (eIDAS certificates)
    3. APIs must be free and non-discriminatory
    4. Dedicated interface fallback
    5. Customer explicit consent required"""

    ax.text(0.5, 0.5, requirements, fontsize=8, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Timeline
    ax.text(8, 1.5, 'Timeline:\n2018: PSD2 effective\n2019: SCA deadline (delayed)\n2020-21: SCA enforcement',
           fontsize=7, va='bottom', bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: EU Directive 2015/2366 (PSD2)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'psd2_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
