"""
Multi-Factor Authentication (MFA) Factors
Shows the three categories of authentication factors

Output: mfa_factors.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'MFA Authentication Factors',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/mfa_factors'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create MFA factors diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Multi-Factor Authentication (MFA)', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'Three Categories of Authentication Factors', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Three factor categories
    factors = [
        {
            'name': 'Something You\nKNOW',
            'x': 2.2,
            'color': '#4A90E2',
            'examples': ['Password', 'PIN', 'Security questions', 'Pattern lock'],
            'pros': 'Easy to implement',
            'cons': 'Can be guessed/stolen',
        },
        {
            'name': 'Something You\nHAVE',
            'x': 6.5,
            'color': '#44A044',
            'examples': ['Mobile phone (SMS/OTP)', 'Hardware token', 'Smart card', 'Security key (FIDO2)'],
            'pros': 'Physical possession',
            'cons': 'Can be lost/stolen',
        },
        {
            'name': 'Something You\nARE',
            'x': 10.8,
            'color': '#FF7F0E',
            'examples': ['Fingerprint', 'Face recognition', 'Voice', 'Iris scan'],
            'pros': 'Unique to individual',
            'cons': 'Privacy concerns',
        },
    ]

    for factor in factors:
        # Main circle
        circle = mpatches.Circle((factor['x'], 6.5), 1.5, facecolor=factor['color'],
                                  edgecolor='#333333', lw=2, alpha=0.9)
        ax.add_patch(circle)
        ax.text(factor['x'], 6.5, factor['name'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        # Examples box
        examples_box = mpatches.FancyBboxPatch((factor['x']-1.5, 2.5), 3, 2.5,
                                                boxstyle='round,pad=0.1',
                                                facecolor='white', edgecolor=factor['color'], lw=1.5)
        ax.add_patch(examples_box)
        ax.text(factor['x'], 4.7, 'Examples:', ha='center', fontsize=8, fontweight='bold')
        for i, example in enumerate(factor['examples']):
            ax.text(factor['x'], 4.2-i*0.4, f'* {example}', ha='center', fontsize=7)

        # Pros/cons
        ax.text(factor['x'], 2.2, f'+: {factor["pros"]}', ha='center', fontsize=7, color='#44A044')
        ax.text(factor['x'], 1.8, f'-: {factor["cons"]}', ha='center', fontsize=7, color='#D62728')

    # Connecting line for 2FA/MFA
    ax.annotate('', xy=(4.5, 6.5), xytext=(4, 6.5),
               arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5))
    ax.annotate('', xy=(9, 6.5), xytext=(8.5, 6.5),
               arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5))

    # 2FA label
    ax.text(6.5, 8.3, '2FA = Any 2 different factors | MFA = 2 or more factors',
           ha='center', fontsize=9, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8E8E8', edgecolor='#666666'))

    # Security levels
    security = """Security Strength:
    1 factor: Basic
    2 factors: Strong
    3 factors: Very Strong

    Regulatory:
    PSD2 SCA requires 2+ factors"""

    ax.text(0.3, 2.5, security, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: NIST SP 800-63B Digital Identity Guidelines',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mfa_factors.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
