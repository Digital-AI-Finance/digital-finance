"""
Mnemonic Generation
Shows how BIP-39 seed phrases are generated

Output: mnemonic_generation.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Mnemonic Generation',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/mnemonic_generation'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create mnemonic generation diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'BIP-39: Mnemonic Seed Phrase Generation', fontsize=20, fontweight='bold', ha='center')

    # Step 1: Entropy
    step1 = mpatches.FancyBboxPatch((0.5, 8), 3, 1.8,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#9B59B6', alpha=0.3,
                                     edgecolor='#9B59B6', lw=2)
    ax.add_patch(step1)
    ax.text(2, 9.4, '1. Generate Entropy', ha='center', fontsize=12, fontweight='bold')
    ax.text(2, 8.8, '128-256 bits random', ha='center', fontsize=10)
    ax.text(2, 8.3, '(CSPRNG)', ha='center', fontsize=9, style='italic')

    # Arrow
    ax.annotate('', xy=(4, 8.9), xytext=(3.5, 8.9),
               arrowprops=dict(arrowstyle='->', lw=2))

    # Step 2: Checksum
    step2 = mpatches.FancyBboxPatch((4, 8), 3, 1.8,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#3498DB', alpha=0.3,
                                     edgecolor='#3498DB', lw=2)
    ax.add_patch(step2)
    ax.text(5.5, 9.4, '2. Add Checksum', ha='center', fontsize=12, fontweight='bold')
    ax.text(5.5, 8.8, 'SHA256 first bits', ha='center', fontsize=10)
    ax.text(5.5, 8.3, '(4-8 bits)', ha='center', fontsize=9, style='italic')

    # Arrow
    ax.annotate('', xy=(7.5, 8.9), xytext=(7, 8.9),
               arrowprops=dict(arrowstyle='->', lw=2))

    # Step 3: Split
    step3 = mpatches.FancyBboxPatch((7.5, 8), 3, 1.8,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#F39C12', alpha=0.3,
                                     edgecolor='#F39C12', lw=2)
    ax.add_patch(step3)
    ax.text(9, 9.4, '3. Split into 11-bit', ha='center', fontsize=12, fontweight='bold')
    ax.text(9, 8.8, 'Groups (indices)', ha='center', fontsize=10)
    ax.text(9, 8.3, '12-24 groups', ha='center', fontsize=9, style='italic')

    # Arrow
    ax.annotate('', xy=(11, 8.9), xytext=(10.5, 8.9),
               arrowprops=dict(arrowstyle='->', lw=2))

    # Step 4: Words
    step4 = mpatches.FancyBboxPatch((11, 8), 2.5, 1.8,
                                     boxstyle='round,pad=0.1',
                                     facecolor='#27AE60', alpha=0.3,
                                     edgecolor='#27AE60', lw=2)
    ax.add_patch(step4)
    ax.text(12.25, 9.4, '4. Map to Words', ha='center', fontsize=12, fontweight='bold')
    ax.text(12.25, 8.8, '2048-word list', ha='center', fontsize=10)
    ax.text(12.25, 8.3, 'BIP-39 wordlist', ha='center', fontsize=9, style='italic')

    # Example seed phrase
    example_box = mpatches.FancyBboxPatch((1, 5.5), 12, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#E8F4EA', alpha=0.9,
                                           edgecolor='#27AE60', lw=2)
    ax.add_patch(example_box)
    ax.text(7, 7, 'Example 12-word Seed Phrase (128 bits):', ha='center', fontsize=12, fontweight='bold')
    ax.text(7, 6.3, 'witch collapse practice feed shame open despair creek road again ice least',
           ha='center', fontsize=11, family='monospace')
    ax.text(7, 5.7, '[EXAMPLE ONLY - Never use example seed phrases!]', ha='center', fontsize=9, color='#E74C3C')

    # Word count options
    options_box = mpatches.FancyBboxPatch((1, 3), 12, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#F8F9FA', alpha=0.9,
                                           edgecolor='#CCC', lw=1)
    ax.add_patch(options_box)
    ax.text(7, 4.6, 'Seed Phrase Options', ha='center', fontsize=12, fontweight='bold')

    options = [('12 words', '128 bits', '~2^128 combinations'),
               ('18 words', '192 bits', '~2^192 combinations'),
               ('24 words', '256 bits', '~2^256 combinations')]

    for i, (words, bits, strength) in enumerate(options):
        x = 2.5 + i * 4
        ax.text(x, 4.0, words, ha='center', fontsize=11, fontweight='bold')
        ax.text(x, 3.5, bits, ha='center', fontsize=10)
        ax.text(x, 3.2, strength, ha='center', fontsize=9, color='#666')

    # Security warning
    warning_box = mpatches.FancyBboxPatch((2, 0.5), 10, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#FFE6E6', alpha=0.9,
                                           edgecolor='#E74C3C', lw=2)
    ax.add_patch(warning_box)
    ax.text(7, 2.0, 'SECURITY: Seed phrase = Master key to all funds', ha='center', fontsize=12, fontweight='bold', color='#E74C3C')
    ax.text(7, 1.4, 'Store offline, never share, never enter online', ha='center', fontsize=11)
    ax.text(7, 0.9, 'Anyone with your seed phrase controls your crypto', ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, 'Source: BIP-39 (Bitcoin Improvement Proposal), github.com/bitcoin/bips',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mnemonic_generation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
