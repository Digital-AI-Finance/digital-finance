"""
Cryptography Comparison
Compares symmetric vs asymmetric encryption

Output: crypto_comparison.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Cryptography Comparison',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/crypto_comparison'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create cryptography comparison diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Symmetric vs Asymmetric Cryptography', fontsize=20, fontweight='bold', ha='center')

    # Symmetric section
    sym_box = mpatches.FancyBboxPatch((0.5, 5.5), 6, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#3498DB', alpha=0.15,
                                       edgecolor='#3498DB', lw=2)
    ax.add_patch(sym_box)
    ax.text(3.5, 9, 'SYMMETRIC', ha='center', fontsize=16, fontweight='bold', color='#2980B9')
    ax.text(3.5, 8.4, 'Same key for encrypt & decrypt', ha='center', fontsize=12)

    # Key icon
    key_box = mpatches.FancyBboxPatch((2.5, 7), 2, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F39C12', alpha=0.8,
                                       edgecolor='#D68910', lw=2)
    ax.add_patch(key_box)
    ax.text(3.5, 7.5, 'KEY', ha='center', fontsize=14, fontweight='bold', color='white')

    # Arrows
    ax.annotate('', xy=(2, 6.5), xytext=(3, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.annotate('', xy=(5, 6.5), xytext=(4, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

    ax.text(1.5, 6.2, 'Alice', ha='center', fontsize=11)
    ax.text(5.5, 6.2, 'Bob', ha='center', fontsize=11)

    # Properties
    sym_props = ['Fast (AES: GB/s)', 'Key distribution problem', 'Examples: AES, ChaCha20']
    for i, prop in enumerate(sym_props):
        ax.text(3.5, 5.7 - i*0.4, prop, ha='center', fontsize=10)

    # Asymmetric section
    asym_box = mpatches.FancyBboxPatch((7.5, 5.5), 6, 4,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#27AE60', alpha=0.15,
                                        edgecolor='#27AE60', lw=2)
    ax.add_patch(asym_box)
    ax.text(10.5, 9, 'ASYMMETRIC', ha='center', fontsize=16, fontweight='bold', color='#1E8449')
    ax.text(10.5, 8.4, 'Public key + Private key pair', ha='center', fontsize=12)

    # Two keys
    pub_key = mpatches.FancyBboxPatch((8.5, 7), 1.8, 1,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#27AE60', alpha=0.8,
                                       edgecolor='#1E8449', lw=2)
    ax.add_patch(pub_key)
    ax.text(9.4, 7.5, 'PUBLIC', ha='center', fontsize=11, fontweight='bold', color='white')

    priv_key = mpatches.FancyBboxPatch((10.7, 7), 1.8, 1,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#E74C3C', alpha=0.8,
                                        edgecolor='#C0392B', lw=2)
    ax.add_patch(priv_key)
    ax.text(11.6, 7.5, 'PRIVATE', ha='center', fontsize=11, fontweight='bold', color='white')

    # Properties
    asym_props = ['Slower (RSA: KB/s)', 'Solves key distribution', 'Examples: RSA, ECDSA']
    for i, prop in enumerate(asym_props):
        ax.text(10.5, 5.7 - i*0.4, prop, ha='center', fontsize=10)

    # Comparison table
    table_box = mpatches.FancyBboxPatch((1, 0.5), 12, 4.5,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#F8F9FA', alpha=0.9,
                                         edgecolor='#CCC', lw=1)
    ax.add_patch(table_box)

    # Table headers
    ax.text(4, 4.5, 'Symmetric', ha='center', fontsize=12, fontweight='bold', color='#3498DB')
    ax.text(10, 4.5, 'Asymmetric', ha='center', fontsize=12, fontweight='bold', color='#27AE60')

    # Table rows
    rows = [
        ('Speed', 'Very Fast', 'Slow'),
        ('Key Length', '128-256 bits', '2048+ bits (RSA)'),
        ('Use Case', 'Bulk encryption', 'Key exchange, signatures'),
        ('In Blockchain', 'Encrypt data', 'Sign transactions'),
    ]

    for i, (category, sym, asym) in enumerate(rows):
        y = 3.8 - i * 0.8
        ax.text(1.5, y, category, fontsize=11, fontweight='bold')
        ax.text(4, y, sym, ha='center', fontsize=11)
        ax.text(10, y, asym, ha='center', fontsize=11)
        if i < len(rows) - 1:
            ax.plot([1.2, 12.8], [y - 0.35, y - 0.35], 'k-', alpha=0.2)

    # Source
    fig.text(0.5, 0.02, 'Source: NIST Cryptographic Standards, Applied Cryptography (Schneier)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'crypto_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
