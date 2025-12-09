"""
Block Header Anatomy
Shows the structure of a blockchain block header

Output: block_header_anatomy.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Block Header Anatomy',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/block_header_anatomy'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create block header anatomy diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Bitcoin Block Header Structure (80 bytes)', fontsize=20, fontweight='bold', ha='center')

    # Main block header box
    header_box = mpatches.FancyBboxPatch((1, 2), 12, 7.5,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#F8F9FA', alpha=0.9,
                                          edgecolor='#2C3E50', lw=3)
    ax.add_patch(header_box)
    ax.text(7, 9, 'BLOCK HEADER', ha='center', fontsize=16, fontweight='bold', color='#2C3E50')

    # Header fields
    fields = [
        {'name': 'Version', 'size': '4 bytes', 'desc': 'Block version number', 'y': 8, 'color': '#3498DB'},
        {'name': 'Previous Block Hash', 'size': '32 bytes', 'desc': 'Hash of previous block header', 'y': 7, 'color': '#E74C3C'},
        {'name': 'Merkle Root', 'size': '32 bytes', 'desc': 'Root hash of all transactions', 'y': 6, 'color': '#F39C12'},
        {'name': 'Timestamp', 'size': '4 bytes', 'desc': 'Block creation time (Unix)', 'y': 5, 'color': '#27AE60'},
        {'name': 'Difficulty Target', 'size': '4 bytes', 'desc': 'nBits - compact difficulty', 'y': 4, 'color': '#9B59B6'},
        {'name': 'Nonce', 'size': '4 bytes', 'desc': 'Counter for PoW mining', 'y': 3, 'color': '#1ABC9C'},
    ]

    for field in fields:
        # Field box
        box = mpatches.FancyBboxPatch((1.5, field['y']-0.4), 11, 0.8,
                                       boxstyle='round,pad=0.05',
                                       facecolor=field['color'], alpha=0.2,
                                       edgecolor=field['color'], lw=1.5)
        ax.add_patch(box)
        ax.text(2, field['y'], field['name'], fontsize=12, fontweight='bold', va='center')
        ax.text(7, field['y'], field['size'], fontsize=11, va='center', ha='center',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor=field['color']))
        ax.text(11.5, field['y'], field['desc'], fontsize=10, va='center', ha='right', style='italic')

    # Chain link visualization
    ax.text(7, 1.5, 'Each block links to previous via hash - creating an immutable chain',
           ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60', lw=1.5))

    # Block chain mini visualization
    for i, x in enumerate([2, 7, 12]):
        mini_box = mpatches.FancyBboxPatch((x-0.8, 0.4), 1.6, 0.6,
                                            boxstyle='round,pad=0.05',
                                            facecolor='#2C3E50' if i == 1 else '#95A5A6',
                                            edgecolor='#2C3E50', lw=1)
        ax.add_patch(mini_box)
        if i < 2:
            ax.annotate('', xy=(x+0.8, 0.7), xytext=(x+2.2, 0.7),
                       arrowprops=dict(arrowstyle='<-', lw=1.5, color='#2C3E50'))

    # Source
    fig.text(0.5, 0.02, 'Source: Bitcoin Developer Documentation, bitcoin.org (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'block_header_anatomy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
