"""
Self-Sovereign Identity (SSI) Architecture
Shows the decentralized identity model

Output: ssi_architecture.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Self-Sovereign Identity Architecture',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ssi_architecture'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create SSI architecture diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Self-Sovereign Identity (SSI) Architecture', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'User-Controlled Decentralized Identity', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Three main actors
    # Issuer
    issuer_box = mpatches.FancyBboxPatch((0.5, 5), 3, 3, boxstyle='round,pad=0.1',
                                          facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(issuer_box)
    ax.text(2, 7.5, 'ISSUER', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(2, 6.8, '(Government, University,\nEmployer, Bank)', ha='center', fontsize=8, color='white')
    ax.text(2, 5.5, 'Issues Verifiable\nCredentials', ha='center', fontsize=8, color='white')

    # Holder (center)
    holder_box = mpatches.FancyBboxPatch((5, 5), 3, 3, boxstyle='round,pad=0.1',
                                          facecolor='#44A044', edgecolor='#333333', lw=2)
    ax.add_patch(holder_box)
    ax.text(6.5, 7.5, 'HOLDER', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(6.5, 6.8, '(Individual User)', ha='center', fontsize=8, color='white')
    ax.text(6.5, 5.8, 'Stores credentials\nin Digital Wallet', ha='center', fontsize=8, color='white')
    ax.text(6.5, 5.3, 'Controls sharing', ha='center', fontsize=8, color='white')

    # Verifier
    verifier_box = mpatches.FancyBboxPatch((9.5, 5), 3, 3, boxstyle='round,pad=0.1',
                                            facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(verifier_box)
    ax.text(11, 7.5, 'VERIFIER', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(11, 6.8, '(Service Provider,\nMerchant, Employer)', ha='center', fontsize=8, color='white')
    ax.text(11, 5.5, 'Requests & Verifies\nCredentials', ha='center', fontsize=8, color='white')

    # Arrows and labels
    # Issuer -> Holder
    ax.annotate('', xy=(4.9, 6.5), xytext=(3.6, 6.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(4.25, 6.9, 'Issue\nCredential', ha='center', fontsize=7)

    # Holder -> Verifier
    ax.annotate('', xy=(9.4, 6.5), xytext=(8.1, 6.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(8.75, 6.9, 'Present\nProof', ha='center', fontsize=7)

    # Verifiable Data Registry (bottom)
    registry = mpatches.FancyBboxPatch((3, 1.5), 7, 2, boxstyle='round,pad=0.1',
                                        facecolor='#6B5B95', alpha=0.2,
                                        edgecolor='#6B5B95', lw=2)
    ax.add_patch(registry)
    ax.text(6.5, 3.1, 'Verifiable Data Registry', ha='center', fontsize=10, fontweight='bold', color='#6B5B95')
    ax.text(6.5, 2.5, '(Blockchain / Distributed Ledger)', ha='center', fontsize=9, color='#6B5B95')
    ax.text(6.5, 2, 'DIDs | Public Keys | Revocation Status | Schemas', ha='center', fontsize=8)

    # Connections to registry
    ax.annotate('', xy=(2, 4.9), xytext=(4, 3.6),
               arrowprops=dict(arrowstyle='<->', color='#6B5B95', lw=1.5, ls='--'))
    ax.annotate('', xy=(6.5, 4.9), xytext=(6.5, 3.6),
               arrowprops=dict(arrowstyle='<->', color='#6B5B95', lw=1.5, ls='--'))
    ax.annotate('', xy=(11, 4.9), xytext=(9, 3.6),
               arrowprops=dict(arrowstyle='<->', color='#6B5B95', lw=1.5, ls='--'))

    # Key principles
    principles = """SSI Principles:
    * User controls identity
    * Minimal disclosure
    * Decentralized (no central authority)
    * Interoperable credentials
    * Cryptographically verifiable"""

    ax.text(0.3, 4.3, principles, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Standards
    standards = """Standards:
    * W3C DIDs
    * W3C Verifiable Credentials
    * DIDComm messaging
    * EU eIDAS 2.0 / EUDI Wallet"""

    ax.text(12.7, 4.3, standards, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: W3C Decentralized Identifiers (DIDs), Verifiable Credentials Data Model',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ssi_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
