"""
eIDAS Framework Overview
Shows the EU electronic identification and trust services framework

Output: eidas_framework.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'eIDAS Framework',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/eidas_framework'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create eIDAS framework overview chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'eIDAS: EU Electronic Identification & Trust Services',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'Regulation (EU) No 910/2014 + eIDAS 2.0 (2024)',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Two main pillars
    # Left: eID
    eid_box = mpatches.FancyBboxPatch((0.5, 3), 5.5, 5, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.2, edgecolor='#4A90E2', lw=2)
    ax.add_patch(eid_box)
    ax.text(3.25, 7.6, 'Electronic Identification (eID)', ha='center',
           fontsize=12, fontweight='bold', color='#4A90E2')

    eid_elements = [
        'National eID schemes notification',
        'Mutual recognition across EU',
        'Assurance levels (Low/Substantial/High)',
        'eID Node interoperability',
        'EU Digital Identity Wallet (eIDAS 2.0)'
    ]
    for i, elem in enumerate(eid_elements):
        ax.text(3.25, 6.8 - i*0.7, f'* {elem}', ha='center', fontsize=8)

    # Right: Trust Services
    trust_box = mpatches.FancyBboxPatch((7, 3), 5.5, 5, boxstyle='round,pad=0.1',
                                         facecolor='#44A044', alpha=0.2, edgecolor='#44A044', lw=2)
    ax.add_patch(trust_box)
    ax.text(9.75, 7.6, 'Trust Services', ha='center',
           fontsize=12, fontweight='bold', color='#44A044')

    trust_elements = [
        'Electronic signatures (QES)',
        'Electronic seals',
        'Time stamps',
        'Registered delivery',
        'Website authentication (QWAC)'
    ]
    for i, elem in enumerate(trust_elements):
        ax.text(9.75, 6.8 - i*0.7, f'* {elem}', ha='center', fontsize=8)

    # Key changes in eIDAS 2.0
    changes_box = mpatches.FancyBboxPatch((2, 0.5), 9, 2, boxstyle='round,pad=0.1',
                                           facecolor='#FF7F0E', alpha=0.2, edgecolor='#FF7F0E', lw=2)
    ax.add_patch(changes_box)
    ax.text(6.5, 2.2, 'eIDAS 2.0 Key Changes (2024)', ha='center',
           fontsize=11, fontweight='bold', color='#FF7F0E')
    ax.text(6.5, 1.5, 'EU Digital Identity Wallet | Verifiable credentials | Remote identity proofing | Private sector acceptance mandate',
           ha='center', fontsize=8)
    ax.text(6.5, 0.9, 'All EU citizens entitled to a digital wallet by 2026',
           ha='center', fontsize=8, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: EU Regulation 910/2014, eIDAS 2.0 (2024)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'eidas_framework.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
