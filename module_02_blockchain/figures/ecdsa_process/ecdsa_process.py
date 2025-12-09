"""
ECDSA Process
Shows the ECDSA signing and verification algorithm steps

Output: ecdsa_process.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'ECDSA Process',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/ecdsa_process'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create ECDSA process diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'ECDSA: Elliptic Curve Digital Signature Algorithm', fontsize=20, fontweight='bold', ha='center')

    # Left column: Signing
    ax.text(3.5, 9.3, 'SIGNING', fontsize=16, fontweight='bold', color='#E74C3C', ha='center')

    signing_steps = [
        ('1. Hash message', 'z = SHA256(message)'),
        ('2. Random k', 'k = random [1, n-1]'),
        ('3. Calculate R', 'R = k*G, r = R.x mod n'),
        ('4. Calculate s', 's = k^-1(z + r*d) mod n'),
        ('5. Signature', 'sig = (r, s)'),
    ]

    for i, (step, formula) in enumerate(signing_steps):
        y = 8.3 - i * 1.4
        box = mpatches.FancyBboxPatch((0.5, y-0.5), 6, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#E74C3C', alpha=0.15,
                                       edgecolor='#E74C3C', lw=1.5)
        ax.add_patch(box)
        ax.text(1, y+0.2, step, fontsize=11, fontweight='bold')
        ax.text(3.5, y-0.2, formula, fontsize=10, family='monospace', ha='center')

    # Right column: Verification
    ax.text(10.5, 9.3, 'VERIFICATION', fontsize=16, fontweight='bold', color='#27AE60', ha='center')

    verify_steps = [
        ('1. Hash message', 'z = SHA256(message)'),
        ('2. Calculate u1', 'u1 = z * s^-1 mod n'),
        ('3. Calculate u2', 'u2 = r * s^-1 mod n'),
        ('4. Calculate P', 'P = u1*G + u2*Q'),
        ('5. Check', 'Valid if P.x mod n = r'),
    ]

    for i, (step, formula) in enumerate(verify_steps):
        y = 8.3 - i * 1.4
        box = mpatches.FancyBboxPatch((7.5, y-0.5), 6, 1.2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#27AE60', alpha=0.15,
                                       edgecolor='#27AE60', lw=1.5)
        ax.add_patch(box)
        ax.text(8, y+0.2, step, fontsize=11, fontweight='bold')
        ax.text(10.5, y-0.2, formula, fontsize=10, family='monospace', ha='center')

    # Legend
    legend_box = mpatches.FancyBboxPatch((1, 0.5), 12, 1.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#F8F9FA', alpha=0.9,
                                          edgecolor='#CCC', lw=1)
    ax.add_patch(legend_box)
    ax.text(7, 1.6, 'Variables: G=generator, n=curve order, d=private key, Q=public key, k=nonce',
           ha='center', fontsize=11)
    ax.text(7, 1.0, 'Bitcoin uses secp256k1 curve with 256-bit keys and SHA-256 hashing',
           ha='center', fontsize=11, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: SEC 1: Elliptic Curve Cryptography, ANSI X9.62',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ecdsa_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
