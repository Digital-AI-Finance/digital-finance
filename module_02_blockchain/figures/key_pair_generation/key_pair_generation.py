"""
Key Pair Generation
Shows how public-private key pairs are generated

Output: key_pair_generation.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Key Pair Generation',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/key_pair_generation'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create key pair generation diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Elliptic Curve Key Pair Generation', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 9.6, 'How Bitcoin creates public/private keys', fontsize=14, ha='center', color='#666')

    # Step 1: Random number
    step1 = mpatches.FancyBboxPatch((1, 7), 3.5, 2,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#9B59B6', alpha=0.3,
                                     edgecolor='#9B59B6', lw=2)
    ax.add_patch(step1)
    ax.text(2.75, 8.5, '1. Generate Random', ha='center', fontsize=12, fontweight='bold', color='#8E44AD')
    ax.text(2.75, 7.9, '256-bit number', ha='center', fontsize=11)
    ax.text(2.75, 7.4, '(CSPRNG)', ha='center', fontsize=10, style='italic')

    # Arrow
    ax.annotate('', xy=(5.5, 8), xytext=(4.5, 8),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Step 2: Private key
    step2 = mpatches.FancyBboxPatch((5.5, 7), 3, 2,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#E74C3C', alpha=0.3,
                                     edgecolor='#E74C3C', lw=2)
    ax.add_patch(step2)
    ax.text(7, 8.5, '2. Private Key (k)', ha='center', fontsize=12, fontweight='bold', color='#C0392B')
    ax.text(7, 7.9, '256 bits', ha='center', fontsize=11)
    ax.text(7, 7.4, 'KEEP SECRET!', ha='center', fontsize=10, fontweight='bold', color='#E74C3C')

    # Arrow
    ax.annotate('', xy=(9.5, 8), xytext=(8.5, 8),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Step 3: EC multiplication
    step3 = mpatches.FancyBboxPatch((9.5, 7), 4, 2,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#F39C12', alpha=0.3,
                                     edgecolor='#F39C12', lw=2)
    ax.add_patch(step3)
    ax.text(11.5, 8.5, '3. EC Point Multiply', ha='center', fontsize=12, fontweight='bold', color='#D68910')
    ax.text(11.5, 7.9, 'K = k * G', ha='center', fontsize=14, family='monospace')
    ax.text(11.5, 7.4, 'G = generator point', ha='center', fontsize=10, style='italic')

    # Arrow down
    ax.annotate('', xy=(11.5, 6), xytext=(11.5, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    # Step 4: Public key
    step4 = mpatches.FancyBboxPatch((9, 4), 5, 2,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#27AE60', alpha=0.3,
                                     edgecolor='#27AE60', lw=2)
    ax.add_patch(step4)
    ax.text(11.5, 5.5, '4. Public Key (K)', ha='center', fontsize=12, fontweight='bold', color='#1E8449')
    ax.text(11.5, 4.9, '(x, y) coordinates', ha='center', fontsize=11)
    ax.text(11.5, 4.4, 'Can share freely', ha='center', fontsize=10, style='italic')

    # Secp256k1 parameters
    params_box = mpatches.FancyBboxPatch((0.5, 2), 6, 3.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#3498DB', alpha=0.15,
                                          edgecolor='#3498DB', lw=2)
    ax.add_patch(params_box)
    ax.text(3.5, 5, 'secp256k1 Curve Parameters', ha='center', fontsize=12, fontweight='bold', color='#2980B9')
    params = [
        'p = 2^256 - 2^32 - 977 (prime)',
        'a = 0, b = 7',
        'y^2 = x^3 + 7 (mod p)',
        'Order n = ~2^256',
    ]
    for i, param in enumerate(params):
        ax.text(3.5, 4.3 - i*0.5, param, ha='center', fontsize=10, family='monospace')

    # Security note
    security_box = mpatches.FancyBboxPatch((7, 0.3), 6.5, 1.5,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#E74C3C', alpha=0.15,
                                            edgecolor='#E74C3C', lw=2)
    ax.add_patch(security_box)
    ax.text(10.25, 1.3, 'One-Way Function:', ha='center', fontsize=11, fontweight='bold', color='#C0392B')
    ax.text(10.25, 0.8, 'K = k*G is easy, but finding k from K is infeasible', ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, 'Source: SEC 2: Recommended Elliptic Curve Domain Parameters (Certicom)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'key_pair_generation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
