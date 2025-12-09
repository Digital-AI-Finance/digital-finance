"""
Hash Function Properties
Visualizes the key properties of cryptographic hash functions

Output: hash_function_properties.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Hash Function Properties',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/hash_function_properties'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create hash function properties diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Cryptographic Hash Function Properties', fontsize=20, fontweight='bold', ha='center')

    # Central hash function box
    center_box = mpatches.FancyBboxPatch((5, 5), 4, 2,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#2E86AB', alpha=0.9,
                                          edgecolor='#1a5276', lw=3)
    ax.add_patch(center_box)
    ax.text(7, 6.2, 'Hash Function', ha='center', fontsize=16, fontweight='bold', color='white')
    ax.text(7, 5.5, 'H(x) = y', ha='center', fontsize=14, color='white', family='monospace')

    # Input arrow
    ax.annotate('', xy=(5, 6), xytext=(2, 6),
                arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.text(1.5, 6.5, 'Input\n(any size)', ha='center', fontsize=12)

    # Output arrow
    ax.annotate('', xy=(12, 6), xytext=(9, 6),
                arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.text(12.5, 6.5, 'Output\n(fixed size)', ha='center', fontsize=12)

    # Properties
    properties = [
        {
            'name': 'Deterministic',
            'desc': 'Same input always\nproduces same output',
            'x': 2.5, 'y': 3.5, 'color': '#27AE60'
        },
        {
            'name': 'One-Way',
            'desc': 'Cannot reverse:\nH(x) -> x impossible',
            'x': 5.5, 'y': 3.5, 'color': '#E74C3C'
        },
        {
            'name': 'Collision Resistant',
            'desc': 'Hard to find x1, x2\nwhere H(x1) = H(x2)',
            'x': 8.5, 'y': 3.5, 'color': '#9B59B6'
        },
        {
            'name': 'Avalanche Effect',
            'desc': 'Small input change =\ncompletely different output',
            'x': 11.5, 'y': 3.5, 'color': '#F39C12'
        },
    ]

    for prop in properties:
        box = mpatches.FancyBboxPatch((prop['x']-1.3, prop['y']-1.3), 2.6, 2.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=prop['color'], alpha=0.15,
                                       edgecolor=prop['color'], lw=2)
        ax.add_patch(box)
        ax.text(prop['x'], prop['y']+0.7, prop['name'], ha='center',
               fontsize=12, fontweight='bold', color=prop['color'])
        ax.text(prop['x'], prop['y']-0.3, prop['desc'], ha='center', fontsize=10)

    # Example box
    example_box = mpatches.FancyBboxPatch((1, 0.3), 12, 1.5,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#ECF0F1', alpha=0.8,
                                           edgecolor='#BDC3C7', lw=1.5)
    ax.add_patch(example_box)
    ax.text(7, 1.5, 'SHA-256 Example:', ha='center', fontsize=12, fontweight='bold')
    ax.text(7, 0.9, '"Hello" -> 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969',
           ha='center', fontsize=9, family='monospace')

    # Source
    fig.text(0.5, 0.02, 'Source: NIST FIPS 180-4 (Secure Hash Standard)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'hash_function_properties.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
