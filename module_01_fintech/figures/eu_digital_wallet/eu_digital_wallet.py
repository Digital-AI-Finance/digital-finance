"""
EU Digital Identity Wallet (EUDI)
Shows the upcoming EU-wide digital identity wallet

Output: eu_digital_wallet.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'EU Digital Identity Wallet',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/eu_digital_wallet'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create EU Digital Wallet diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'EU Digital Identity Wallet (EUDI)', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'eIDAS 2.0 - Available to all EU citizens by 2026', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Central wallet icon
    wallet = mpatches.FancyBboxPatch((4.5, 5), 4, 2.5, boxstyle='round,pad=0.2',
                                      facecolor='#4A90E2', edgecolor='#333333', lw=3)
    ax.add_patch(wallet)
    ax.text(6.5, 6.5, 'EUDI Wallet', ha='center', fontsize=14, fontweight='bold', color='white')
    ax.text(6.5, 5.8, 'Smartphone App', ha='center', fontsize=10, color='white')
    ax.text(6.5, 5.3, '(Government-issued)', ha='center', fontsize=8, color='white')

    # Credentials that can be stored
    credentials = [
        ('National ID', 0.5, 7),
        ('Driving License', 0.5, 6),
        ('Health Records', 0.5, 5),
        ('Diplomas', 0.5, 4),
        ('Bank Accounts', 12.5, 7),
        ('Travel Docs', 12.5, 6),
        ('Professional\nCertificates', 12.5, 5),
        ('Age Verification', 12.5, 4),
    ]

    for cred, x, y in credentials:
        ha = 'left' if x < 6 else 'right'
        color = '#44A044' if x < 6 else '#FF7F0E'
        ax.text(x, y, f'* {cred}', ha=ha, fontsize=9, color=color, fontweight='bold')
        # Arrow to wallet
        if x < 6:
            ax.annotate('', xy=(4.4, 6.25), xytext=(2.5, y),
                       arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.5))
        else:
            ax.annotate('', xy=(8.6, 6.25), xytext=(10.5, y),
                       arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.5))

    ax.text(2, 8, 'Verifiable Credentials', ha='center', fontsize=10, fontweight='bold', color='#44A044')
    ax.text(11, 8, 'Use Cases', ha='center', fontsize=10, fontweight='bold', color='#FF7F0E')

    # Key features
    features = mpatches.FancyBboxPatch((0.5, 1), 5.5, 2.8, boxstyle='round,pad=0.1',
                                        facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(features)
    ax.text(3.25, 3.5, 'Key Features', ha='center', fontsize=10, fontweight='bold')

    feature_list = [
        'Cross-border recognition in all EU states',
        'User-controlled selective disclosure',
        'Offline verification capability',
        'High assurance level (eIDAS)',
        'Free for citizens',
    ]
    for i, feat in enumerate(feature_list):
        ax.text(0.8, 3-i*0.4, f'* {feat}', fontsize=7)

    # Acceptance requirements
    accept = mpatches.FancyBboxPatch((7, 1), 5.5, 2.8, boxstyle='round,pad=0.1',
                                      facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(accept)
    ax.text(9.75, 3.5, 'Mandatory Acceptance', ha='center', fontsize=10, fontweight='bold')

    accept_list = [
        'Public services (all)',
        'Banking & financial services',
        'Telecom operators',
        'Healthcare providers',
        'Large online platforms (250+ employees)',
    ]
    for i, item in enumerate(accept_list):
        ax.text(7.3, 3-i*0.4, f'* {item}', fontsize=7)

    # Timeline
    ax.text(6.5, 0.4, 'Timeline: Regulation adopted 2024 | Wallets available 2026 | Full rollout 2027',
           ha='center', fontsize=8, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: European Commission, eIDAS 2.0 Regulation (EU) 2024/1183',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'eu_digital_wallet.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
