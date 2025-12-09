"""
eIDAS Assurance Levels
Shows the three levels of assurance in eIDAS framework

Output: eidas_assurance_levels.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'eIDAS Assurance Levels',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/eidas_assurance_levels'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create eIDAS assurance levels diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'eIDAS Assurance Levels', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'EU Electronic Identification Trust Framework', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Three levels as stacked boxes (pyramid style)
    levels = [
        {
            'name': 'HIGH',
            'y': 7,
            'width': 10,
            'color': '#44A044',
            'requirements': ['In-person or remote with NFC + liveness', 'Government-issued eID',
                           'Biometric verification', 'Photo match to authoritative source'],
            'use_cases': 'Banking, healthcare, legal documents, government services'
        },
        {
            'name': 'SUBSTANTIAL',
            'y': 4.5,
            'width': 10,
            'color': '#FF7F0E',
            'requirements': ['Remote identity proofing', 'Document + selfie verification',
                           'Database checks', 'Liveness detection'],
            'use_cases': 'Account opening, age verification, KYC'
        },
        {
            'name': 'LOW',
            'y': 2,
            'width': 10,
            'color': '#4A90E2',
            'requirements': ['Self-asserted identity', 'Email/phone verification',
                           'Basic attribute validation', 'Social login acceptable'],
            'use_cases': 'Newsletter signup, basic access, non-sensitive services'
        },
    ]

    for level in levels:
        # Main box
        x_start = (13 - level['width']) / 2
        box = mpatches.FancyBboxPatch((x_start, level['y']-0.8), level['width'], 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=level['color'], alpha=0.2,
                                       edgecolor=level['color'], lw=2)
        ax.add_patch(box)

        # Level name
        ax.text(x_start + 0.3, level['y']+0.8, level['name'], fontsize=12, fontweight='bold',
               color=level['color'], va='center')

        # Requirements (left side)
        for i, req in enumerate(level['requirements']):
            ax.text(x_start + 2.5, level['y']+0.5-i*0.35, f'* {req}', fontsize=7, va='center')

        # Use cases (right side)
        ax.text(x_start + level['width'] - 0.3, level['y'], level['use_cases'],
               fontsize=7, ha='right', va='center', style='italic',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#CCCCCC', alpha=0.8))

    # Arrow showing increasing assurance
    ax.annotate('', xy=(12, 8), xytext=(12, 1.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(12.3, 4.5, 'Increasing\nAssurance', fontsize=8, fontweight='bold',
           rotation=90, va='center', ha='left')

    # Column headers
    ax.text(3.5, 8.5, 'Requirements', fontsize=9, fontweight='bold', ha='center')
    ax.text(10, 8.5, 'Use Cases', fontsize=9, fontweight='bold', ha='center')

    # Key insight
    insight = "Higher assurance = More rigorous proofing = Greater trust in identity claim"
    ax.text(6.5, 0.5, insight, ha='center', fontsize=9, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: EU Regulation 910/2014, Implementing Regulation 2015/1502',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'eidas_assurance_levels.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
