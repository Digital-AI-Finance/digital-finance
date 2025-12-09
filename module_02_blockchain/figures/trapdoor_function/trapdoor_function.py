"""
Trapdoor Function
Illustrates one-way trapdoor functions used in cryptography

Output: trapdoor_function.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Trapdoor Function',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/trapdoor_function'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create trapdoor function diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Trapdoor Functions: The Foundation of Public Key Crypto', fontsize=20, fontweight='bold', ha='center')

    # Forward direction (easy)
    ax.text(7, 8.3, 'Forward Direction: EASY', fontsize=14, ha='center', color='#27AE60', fontweight='bold')

    input_box = mpatches.FancyBboxPatch((1, 6.5), 3, 1.5,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#3498DB', alpha=0.3,
                                         edgecolor='#3498DB', lw=2)
    ax.add_patch(input_box)
    ax.text(2.5, 7.5, 'Input x', ha='center', fontsize=14, fontweight='bold')
    ax.text(2.5, 6.9, '(Private Key)', ha='center', fontsize=11, color='#666')

    func_box = mpatches.FancyBboxPatch((5.5, 6.5), 3, 1.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#27AE60', alpha=0.3,
                                        edgecolor='#27AE60', lw=2)
    ax.add_patch(func_box)
    ax.text(7, 7.5, 'f(x)', ha='center', fontsize=14, fontweight='bold')
    ax.text(7, 6.9, 'Trapdoor Function', ha='center', fontsize=11, color='#666')

    output_box = mpatches.FancyBboxPatch((10, 6.5), 3, 1.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#F39C12', alpha=0.3,
                                          edgecolor='#F39C12', lw=2)
    ax.add_patch(output_box)
    ax.text(11.5, 7.5, 'Output y', ha='center', fontsize=14, fontweight='bold')
    ax.text(11.5, 6.9, '(Public Key)', ha='center', fontsize=11, color='#666')

    # Forward arrows
    ax.annotate('', xy=(5.5, 7.25), xytext=(4, 7.25),
               arrowprops=dict(arrowstyle='->', lw=3, color='#27AE60'))
    ax.annotate('', xy=(10, 7.25), xytext=(8.5, 7.25),
               arrowprops=dict(arrowstyle='->', lw=3, color='#27AE60'))

    # Reverse direction (hard without trapdoor)
    ax.text(7, 5.5, 'Reverse Direction: HARD (without secret trapdoor)', fontsize=14, ha='center', color='#E74C3C', fontweight='bold')

    # Reverse arrow with X
    ax.annotate('', xy=(4, 4.5), xytext=(10, 4.5),
               arrowprops=dict(arrowstyle='->', lw=3, color='#E74C3C', linestyle='dashed'))
    ax.text(7, 4.8, 'X', fontsize=24, ha='center', color='#E74C3C', fontweight='bold')

    # Examples
    examples_box = mpatches.FancyBboxPatch((1, 1), 12, 3,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#F8F9FA', alpha=0.9,
                                            edgecolor='#CCC', lw=1)
    ax.add_patch(examples_box)
    ax.text(7, 3.6, 'Common Trapdoor Functions in Cryptography', ha='center', fontsize=14, fontweight='bold')

    examples = [
        ('Multiplication', 'Easy: 17 x 23 = 391', 'Hard: Factor 391 = ?'),
        ('ECC', 'Easy: K = k * G', 'Hard: Find k from K'),
        ('Discrete Log', 'Easy: g^x mod p', 'Hard: Find x from g^x'),
    ]

    for i, (name, easy, hard) in enumerate(examples):
        x = 2 + i * 4
        ax.text(x, 2.9, name, ha='center', fontsize=12, fontweight='bold', color='#2C3E50')
        ax.text(x, 2.4, easy, ha='center', fontsize=10, color='#27AE60')
        ax.text(x, 1.9, hard, ha='center', fontsize=10, color='#E74C3C')

    # Trapdoor secret
    ax.text(7, 1.2, 'Trapdoor = Secret info (private key) that makes reverse computation easy',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    # Source
    fig.text(0.5, 0.02, 'Source: Diffie & Hellman, "New Directions in Cryptography" (1976)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'trapdoor_function.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
