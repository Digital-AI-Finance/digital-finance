"""Immutability Cascade - Chain reaction when tampering"""
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
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'Immutability: Why Tampering is Impractical', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Draw chain of blocks
block_width = 2.0
block_height = 1.8
y_top = 4.0
y_bottom = 1.5

# Top row - Original chain (valid)
ax.text(0.3, y_top + 0.6, 'Original Chain (Valid)', fontsize=10, fontweight='bold', color=MLGREEN)

for i, (label, hash_start) in enumerate([('Block N-2', '7a3f...'), ('Block N-1', 'b2c1...'), ('Block N', 'd4e5...')]):
    x = 0.5 + i * 3.5
    box = FancyBboxPatch((x, y_top - block_height/2), block_width, block_height,
                          boxstyle="round,pad=0.05", facecolor='#E8F5E8', edgecolor=MLGREEN, linewidth=2)
    ax.add_patch(box)
    ax.text(x + block_width/2, y_top + 0.5, label, ha='center', fontsize=9, fontweight='bold', color=MLGREEN)
    ax.text(x + block_width/2, y_top + 0.1, f'Hash: {hash_start}', ha='center', fontsize=7, family='monospace')
    ax.text(x + block_width/2, y_top - 0.2, f'Prev: ...', ha='center', fontsize=7, family='monospace', color='#666666')

    # Checkmark
    ax.text(x + block_width - 0.2, y_top + 0.6, 'OK', fontsize=8, color=MLGREEN, fontweight='bold')

    # Arrow to next block
    if i < 2:
        ax.annotate('', xy=(x + block_width + 1.3, y_top), xytext=(x + block_width + 0.2, y_top),
                    arrowprops=dict(arrowstyle='->', color='#666666', lw=1.5))

# Bottom row - Tampered chain (invalid)
ax.text(0.3, y_bottom + 0.6, 'After Tampering Block N-2', fontsize=10, fontweight='bold', color=MLRED)

statuses = [('CHANGED!', MLRED), ('INVALID!', MLRED), ('INVALID!', MLRED)]
for i, (label, hash_start) in enumerate([('Block N-2', 'XXXX...'), ('Block N-1', 'b2c1...'), ('Block N', 'd4e5...')]):
    x = 0.5 + i * 3.5
    color = MLRED if i == 0 else '#FFCCCC'
    edge = MLRED
    box = FancyBboxPatch((x, y_bottom - block_height/2), block_width, block_height,
                          boxstyle="round,pad=0.05", facecolor='#FFE8E8' if i > 0 else '#FFCCCC',
                          edgecolor=edge, linewidth=2)
    ax.add_patch(box)
    ax.text(x + block_width/2, y_bottom + 0.5, label, ha='center', fontsize=9, fontweight='bold', color=MLRED)

    if i == 0:
        ax.text(x + block_width/2, y_bottom + 0.1, f'Hash: {hash_start}', ha='center', fontsize=7,
                family='monospace', color=MLRED, fontweight='bold')
    else:
        ax.text(x + block_width/2, y_bottom + 0.1, f'Hash: {hash_start}', ha='center', fontsize=7, family='monospace')

    ax.text(x + block_width/2, y_bottom - 0.2, f'Prev: ...', ha='center', fontsize=7, family='monospace', color='#666666')

    # Status
    status, scolor = statuses[i]
    ax.text(x + block_width - 0.2, y_bottom + 0.6, status, fontsize=7, color=scolor, fontweight='bold')

    # Arrow to next block
    if i < 2:
        ax.annotate('', xy=(x + block_width + 1.3, y_bottom), xytext=(x + block_width + 0.2, y_bottom),
                    arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5))

# Cascade explanation
ax.annotate('', xy=(5.5, y_top - 1.2), xytext=(5.5, y_bottom + 1.0),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax.text(6.0, 2.75, 'Change one block\n= must re-hash ALL\nfollowing blocks', fontsize=8, color=MLRED)

# Bottom note
ax.text(5.5, 0.2, 'To alter history: must re-mine all subsequent blocks faster than the network adds new ones',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'immutability_cascade.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
