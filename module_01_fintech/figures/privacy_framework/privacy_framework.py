"""
Identity Privacy Framework
Shows privacy considerations in digital identity

Output: privacy_framework.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Identity Privacy Framework',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/privacy_framework'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create privacy framework diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Digital Identity Privacy Framework', fontsize=14, fontweight='bold', ha='center')

    # Privacy principles (top row)
    principles = [
        {'name': 'Data\nMinimization', 'x': 2, 'color': '#4A90E2',
         'desc': 'Collect only\nwhat is needed'},
        {'name': 'Purpose\nLimitation', 'x': 4.5, 'color': '#44A044',
         'desc': 'Use only for\nstated purpose'},
        {'name': 'Consent\nManagement', 'x': 7, 'color': '#FF7F0E',
         'desc': 'User controls\ndata sharing'},
        {'name': 'Retention\nLimits', 'x': 9.5, 'color': '#6B5B95',
         'desc': 'Delete when\nno longer needed'},
        {'name': 'Security\nSafeguards', 'x': 12, 'color': '#D62728',
         'desc': 'Protect\nstored data'},
    ]

    for p in principles:
        circle = mpatches.Circle((p['x'], 7.5), 0.8, facecolor=p['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)
        ax.text(p['x'], 7.5, p['name'], ha='center', va='center',
               fontsize=7, fontweight='bold', color='white')
        ax.text(p['x'], 6.3, p['desc'], ha='center', fontsize=6)

    ax.text(7, 8.7, 'GDPR Privacy Principles', ha='center', fontsize=11, fontweight='bold')

    # Privacy Enhancing Technologies
    pet_box = mpatches.FancyBboxPatch((0.5, 2.5), 5.5, 3, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=2)
    ax.add_patch(pet_box)
    ax.text(3.25, 5.1, 'Privacy Enhancing Technologies (PETs)', ha='center',
           fontsize=10, fontweight='bold', color='#4A90E2')

    pets = [
        'Zero-Knowledge Proofs: Prove attributes without revealing data',
        'Selective Disclosure: Share only required attributes',
        'Pseudonymization: Replace identifiers with pseudonyms',
        'Encryption: End-to-end protection of data',
        'Secure Enclaves: Process data in isolated environments',
    ]
    for i, pet in enumerate(pets):
        ax.text(0.8, 4.5-i*0.4, f'* {pet}', fontsize=7)

    # Regulatory landscape
    reg_box = mpatches.FancyBboxPatch((7, 2.5), 5.5, 3, boxstyle='round,pad=0.1',
                                       facecolor='#FF7F0E', alpha=0.15,
                                       edgecolor='#FF7F0E', lw=2)
    ax.add_patch(reg_box)
    ax.text(9.75, 5.1, 'Regulatory Landscape', ha='center',
           fontsize=10, fontweight='bold', color='#FF7F0E')

    regulations = [
        ('GDPR (EU)', 'Comprehensive data protection'),
        ('BIPA (US-IL)', 'Biometric data consent'),
        ('CCPA (US-CA)', 'Consumer privacy rights'),
        ('PIPL (China)', 'Personal information protection'),
        ('LGPD (Brazil)', 'Data protection law'),
    ]
    for i, (reg, desc) in enumerate(regulations):
        ax.text(7.3, 4.5-i*0.4, f'* {reg}:', fontsize=7, fontweight='bold')
        ax.text(9, 4.5-i*0.4, desc, fontsize=7)

    # User rights
    rights = """User Rights (GDPR):
    * Right to access
    * Right to rectification
    * Right to erasure
    * Right to portability
    * Right to object"""

    ax.text(0.3, 1.8, rights, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Fines
    fines = """GDPR Penalties:
    Up to 20M EUR or
    4% global revenue
    (whichever higher)"""

    ax.text(12.7, 1.8, fines, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: GDPR (EU 2016/679), NIST Privacy Framework',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'privacy_framework.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
