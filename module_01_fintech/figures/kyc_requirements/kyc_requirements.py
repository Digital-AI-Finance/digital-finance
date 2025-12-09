"""
KYC Requirements Framework
Shows Know Your Customer regulatory requirements

Output: kyc_requirements.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'KYC Requirements Framework',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/kyc_requirements'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create KYC requirements framework chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Know Your Customer (KYC) Framework', fontsize=14, fontweight='bold', ha='center')

    # Three pillars of KYC
    pillars = [
        {
            'name': 'Customer\nIdentification',
            'abbr': 'CIP',
            'x': 2.5,
            'color': '#4A90E2',
            'elements': ['Name verification', 'Address verification',
                        'Date of birth', 'Government ID', 'Tax ID (SSN/TIN)']
        },
        {
            'name': 'Customer\nDue Diligence',
            'abbr': 'CDD',
            'x': 6.5,
            'color': '#44A044',
            'elements': ['Risk assessment', 'Source of funds',
                        'Nature of business', 'Expected activity', 'Beneficial ownership']
        },
        {
            'name': 'Enhanced\nDue Diligence',
            'abbr': 'EDD',
            'x': 10.5,
            'color': '#FF7F0E',
            'elements': ['PEP screening', 'Sanctions check',
                        'Adverse media', 'Detailed source of wealth', 'Senior approval']
        }
    ]

    for pillar in pillars:
        # Header box
        header = mpatches.FancyBboxPatch((pillar['x']-1.5, 7), 3, 1.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor=pillar['color'], edgecolor='#333333', lw=2)
        ax.add_patch(header)
        ax.text(pillar['x'], 8, pillar['name'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')
        ax.text(pillar['x'], 7.3, f"({pillar['abbr']})", ha='center', fontsize=9, color='white')

        # Elements box
        elements_box = mpatches.FancyBboxPatch((pillar['x']-1.5, 2.5), 3, 4,
                                                boxstyle='round,pad=0.1',
                                                facecolor='white', edgecolor=pillar['color'], lw=2)
        ax.add_patch(elements_box)

        # Elements list
        for i, element in enumerate(pillar['elements']):
            ax.text(pillar['x'], 6 - i*0.6, f'* {element}', ha='center', fontsize=8)

    # Risk tiers arrow
    ax.annotate('', xy=(11.5, 1.8), xytext=(1.5, 1.8),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(6.5, 1.4, 'Increasing Risk Level / Scrutiny', ha='center', fontsize=9,
           fontweight='bold')

    # Risk level labels
    ax.text(2.5, 2.1, 'Low Risk', ha='center', fontsize=8, color='#4A90E2')
    ax.text(6.5, 2.1, 'Standard', ha='center', fontsize=8, color='#44A044')
    ax.text(10.5, 2.1, 'High Risk', ha='center', fontsize=8, color='#FF7F0E')

    # Regulatory drivers
    regulations = """Key Regulations:
    - AML Directives (EU 4/5/6)
    - Bank Secrecy Act (US)
    - FATF Recommendations
    - OFAC Sanctions"""

    ax.text(0.3, 0.8, regulations, fontsize=7, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Penalties
    penalties = """Non-Compliance Penalties:
    - Fines: up to $1B+
    - License revocation
    - Criminal prosecution
    - Reputational damage"""

    ax.text(12.7, 0.8, penalties, fontsize=7, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: FATF Guidelines, AML regulatory frameworks',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'kyc_requirements.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
