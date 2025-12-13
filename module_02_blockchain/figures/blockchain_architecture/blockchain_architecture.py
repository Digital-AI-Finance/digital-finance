"""Blockchain Architecture - Visual showing block structure and chaining"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.size': 10, 'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
    'figure.dpi': 150, 'font.family': 'serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLLAVENDER = '#9999CC'
MLORANGE = '#FF7F0E'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Draw 3 blocks
block_width = 2.5
block_height = 4
y_pos = 1

for i, (x_pos, block_num) in enumerate([(0.5, 'N-1'), (4, 'N'), (7.5, 'N+1')]):
    # Main block rectangle
    block = FancyBboxPatch((x_pos, y_pos), block_width, block_height,
                           boxstyle="round,pad=0.05", facecolor=MLLAVENDER,
                           edgecolor=MLPURPLE, linewidth=2)
    ax.add_patch(block)

    # Block header
    header = FancyBboxPatch((x_pos + 0.1, y_pos + 2.8), block_width - 0.2, 1,
                            boxstyle="round,pad=0.02", facecolor=MLPURPLE,
                            edgecolor='none')
    ax.add_patch(header)
    ax.text(x_pos + block_width/2, y_pos + 3.3, f'Block {block_num}',
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Hash of previous block
    ax.text(x_pos + block_width/2, y_pos + 2.4, 'Prev Hash:', ha='center',
            fontsize=8, fontweight='bold', color=MLPURPLE)
    if i == 0:
        ax.text(x_pos + block_width/2, y_pos + 2.0, '0x7a3f...', ha='center',
                fontsize=8, family='monospace', color='#666666')
    else:
        ax.text(x_pos + block_width/2, y_pos + 2.0, '0x9b2c...', ha='center',
                fontsize=8, family='monospace', color=MLORANGE)

    # Transactions
    ax.text(x_pos + block_width/2, y_pos + 1.4, 'Transactions', ha='center',
            fontsize=8, fontweight='bold', color=MLPURPLE)
    ax.text(x_pos + block_width/2, y_pos + 1.0, 'Tx1, Tx2, Tx3...', ha='center',
            fontsize=8, color='#666666')

    # Merkle Root
    ax.text(x_pos + block_width/2, y_pos + 0.5, 'Merkle Root', ha='center',
            fontsize=8, color='#666666')

# Draw arrows connecting blocks
arrow_style = "Simple,tail_width=0.5,head_width=4,head_length=8"
for x_start in [3.0, 6.5]:
    arrow = FancyArrowPatch((x_start, y_pos + block_height/2),
                           (x_start + 1.0, y_pos + block_height/2),
                           arrowstyle=arrow_style, color=MLORANGE, linewidth=2)
    ax.add_patch(arrow)

# Title and labels
ax.text(5.5, 5.7, 'Blockchain: Linked Blocks via Cryptographic Hashes',
        ha='center', va='center', fontsize=12, fontweight='bold', color=MLPURPLE)

ax.text(5.5, 0.3, 'Each block contains a hash of the previous block, creating an immutable chain',
        ha='center', va='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'blockchain_architecture.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
