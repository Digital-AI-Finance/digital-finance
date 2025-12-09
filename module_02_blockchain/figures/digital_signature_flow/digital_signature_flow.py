"""
Digital Signature Flow
Shows the process of creating and verifying digital signatures

Output: digital_signature_flow.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Digital Signature Flow',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/digital_signature_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create digital signature flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Digital Signature: Sign and Verify', fontsize=20, fontweight='bold', ha='center')

    # SIGNING SECTION
    ax.text(3.5, 9.3, 'SIGNING (Sender)', fontsize=16, fontweight='bold', color='#E74C3C', ha='center')

    # Message
    msg_box = mpatches.FancyBboxPatch((0.5, 7.5), 2.5, 1.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#3498DB', alpha=0.3,
                                       edgecolor='#3498DB', lw=2)
    ax.add_patch(msg_box)
    ax.text(1.75, 8.5, 'Message', ha='center', fontsize=12, fontweight='bold')
    ax.text(1.75, 7.9, '"Send 1 BTC"', ha='center', fontsize=10, family='monospace')

    # Arrow to hash
    ax.annotate('', xy=(3.5, 8.25), xytext=(3, 8.25),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Hash
    hash_box = mpatches.FancyBboxPatch((3.5, 7.5), 2, 1.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#F39C12', alpha=0.3,
                                        edgecolor='#F39C12', lw=2)
    ax.add_patch(hash_box)
    ax.text(4.5, 8.5, 'Hash', ha='center', fontsize=12, fontweight='bold')
    ax.text(4.5, 7.9, 'SHA-256', ha='center', fontsize=10)

    # Arrow to sign
    ax.annotate('', xy=(6, 8.25), xytext=(5.5, 8.25),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Sign with private key
    sign_box = mpatches.FancyBboxPatch((6, 7), 2, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#E74C3C', alpha=0.3,
                                        edgecolor='#E74C3C', lw=2)
    ax.add_patch(sign_box)
    ax.text(7, 9, 'Sign', ha='center', fontsize=12, fontweight='bold')
    ax.text(7, 8.4, 'ECDSA', ha='center', fontsize=10)
    ax.text(7, 7.8, '+', ha='center', fontsize=14)
    ax.text(7, 7.3, 'Private Key', ha='center', fontsize=10, color='#E74C3C', fontweight='bold')

    # VERIFICATION SECTION
    ax.text(10.5, 9.3, 'VERIFYING (Receiver)', fontsize=16, fontweight='bold', color='#27AE60', ha='center')

    # Received message + signature
    recv_box = mpatches.FancyBboxPatch((8.5, 7), 2.5, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#9B59B6', alpha=0.3,
                                        edgecolor='#9B59B6', lw=2)
    ax.add_patch(recv_box)
    ax.text(9.75, 9, 'Received', ha='center', fontsize=12, fontweight='bold')
    ax.text(9.75, 8.4, 'Message', ha='center', fontsize=10)
    ax.text(9.75, 7.9, '+', ha='center', fontsize=12)
    ax.text(9.75, 7.4, 'Signature (r,s)', ha='center', fontsize=10)

    # Verify with public key
    verify_box = mpatches.FancyBboxPatch((11.5, 7), 2, 2.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#27AE60', alpha=0.3,
                                          edgecolor='#27AE60', lw=2)
    ax.add_patch(verify_box)
    ax.text(12.5, 9, 'Verify', ha='center', fontsize=12, fontweight='bold')
    ax.text(12.5, 8.4, 'ECDSA', ha='center', fontsize=10)
    ax.text(12.5, 7.8, '+', ha='center', fontsize=14)
    ax.text(12.5, 7.3, 'Public Key', ha='center', fontsize=10, color='#27AE60', fontweight='bold')

    # Arrow between sections
    ax.annotate('', xy=(11.5, 8.25), xytext=(11, 8.25),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Properties box
    props_box = mpatches.FancyBboxPatch((0.5, 3.5), 13, 3,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#F8F9FA', alpha=0.9,
                                         edgecolor='#CCC', lw=1)
    ax.add_patch(props_box)
    ax.text(7, 6.1, 'Digital Signature Properties', ha='center', fontsize=14, fontweight='bold')

    properties = [
        ('Authentication', 'Only private key holder can create valid signature'),
        ('Integrity', 'Any change to message invalidates signature'),
        ('Non-repudiation', 'Signer cannot deny having signed'),
    ]

    for i, (prop, desc) in enumerate(properties):
        y = 5.3 - i * 0.7
        ax.text(1, y, prop + ':', fontsize=12, fontweight='bold', color='#2C3E50')
        ax.text(4, y, desc, fontsize=11)

    # Bitcoin use case
    btc_box = mpatches.FancyBboxPatch((2, 0.5), 10, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F39C12', alpha=0.15,
                                       edgecolor='#F39C12', lw=2)
    ax.add_patch(btc_box)
    ax.text(7, 2.5, 'In Bitcoin Transactions:', ha='center', fontsize=14, fontweight='bold', color='#D68910')
    ax.text(7, 1.8, 'Sender signs transaction with private key', ha='center', fontsize=11)
    ax.text(7, 1.2, 'Network verifies using sender\'s public key (from address)', ha='center', fontsize=11)
    ax.text(7, 0.7, 'Proves ownership of funds without revealing private key', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, 'Source: NIST FIPS 186-5 Digital Signature Standard (2023)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'digital_signature_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
