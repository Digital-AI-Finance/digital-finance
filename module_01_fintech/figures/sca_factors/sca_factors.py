"""
Strong Customer Authentication (SCA) Factors
Shows the three categories of authentication factors under PSD2

Output: sca_factors.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Strong Customer Authentication Factors',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/sca_factors'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create SCA factors diagram"""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Three factor categories
    factors = [
        {
            'name': 'KNOWLEDGE',
            'subtitle': 'Something you know',
            'x': 2,
            'color': '#4A90E2',
            'icon': 'brain',
            'examples': ['PIN', 'Password', 'Security questions', 'Pattern']
        },
        {
            'name': 'POSSESSION',
            'subtitle': 'Something you have',
            'x': 6,
            'color': '#44A044',
            'icon': 'phone',
            'examples': ['Mobile phone', 'Hardware token', 'Smart card', 'Registered device']
        },
        {
            'name': 'INHERENCE',
            'subtitle': 'Something you are',
            'x': 10,
            'color': '#FF7F0E',
            'icon': 'fingerprint',
            'examples': ['Fingerprint', 'Face recognition', 'Voice', 'Behavioral biometrics']
        }
    ]

    for factor in factors:
        x = factor['x']

        # Main circle
        circle = mpatches.Circle((x, 5.5), 1.5, facecolor=factor['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)

        # Factor name
        ax.text(x, 5.8, factor['name'], ha='center', va='center',
               fontsize=12, fontweight='bold', color='white')
        ax.text(x, 5.2, factor['subtitle'], ha='center', va='center',
               fontsize=8, color='white')

        # Examples box below
        examples_text = '\n'.join([f'* {ex}' for ex in factor['examples']])
        ax.text(x, 2.8, examples_text, ha='center', va='top', fontsize=8,
               bbox=dict(boxstyle='round', facecolor='white', edgecolor=factor['color'], lw=1.5))

    # SCA requirement
    ax.text(6, 8.5, 'Strong Customer Authentication (SCA)',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6, 8, 'Requires 2 of 3 factors from different categories',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Plus signs between circles
    ax.text(4, 5.5, '+', fontsize=24, ha='center', va='center', fontweight='bold', color='#333333')
    ax.text(8, 5.5, '+', fontsize=24, ha='center', va='center', fontweight='bold', color='#333333')

    # Valid combinations
    combinations = """Valid 2FA Combinations:
    - Password + SMS OTP (Knowledge + Possession)
    - PIN + Fingerprint (Knowledge + Inherence)
    - Device token + Face ID (Possession + Inherence)

    Invalid (same category):
    - Password + PIN (both Knowledge)"""

    ax.text(6, 0.8, combinations, fontsize=8, ha='center', va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Exemptions note
    exemptions = """SCA Exemptions:
    - Low-value (<30 EUR)
    - Recurring payments
    - Trusted beneficiaries
    - Corporate payments"""

    ax.text(11.5, 8, exemptions, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: PSD2 RTS on Strong Customer Authentication (EU 2018/389)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'sca_factors.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
