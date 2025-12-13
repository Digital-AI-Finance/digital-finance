"""Merkle Tree Structure - Binary hash tree diagram"""
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

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'Merkle Tree: Efficient Transaction Summary', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Draw tree levels
# Level 0 - Root
root_x, root_y = 5.5, 4.8
root_box = FancyBboxPatch((root_x - 0.9, root_y - 0.3), 1.8, 0.6,
                           boxstyle="round,pad=0.05", facecolor=MLPURPLE, edgecolor='none')
ax.add_patch(root_box)
ax.text(root_x, root_y, 'Merkle Root', ha='center', va='center',
        fontsize=9, fontweight='bold', color='white')

# Level 1 - Hash AB, Hash CD
level1_y = 3.6
level1_positions = [(3, level1_y), (8, level1_y)]
level1_labels = ['Hash(AB)', 'Hash(CD)']

for (x, y), label in zip(level1_positions, level1_labels):
    box = FancyBboxPatch((x - 0.7, y - 0.25), 1.4, 0.5,
                          boxstyle="round,pad=0.03", facecolor=MLBLUE, edgecolor='none')
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, color='white')

# Level 2 - Hash A, B, C, D
level2_y = 2.4
level2_positions = [(1.5, level2_y), (4.5, level2_y), (6.5, level2_y), (9.5, level2_y)]
level2_labels = ['Hash(A)', 'Hash(B)', 'Hash(C)', 'Hash(D)']

for (x, y), label in zip(level2_positions, level2_labels):
    box = FancyBboxPatch((x - 0.6, y - 0.25), 1.2, 0.5,
                          boxstyle="round,pad=0.03", facecolor=MLORANGE, edgecolor='none')
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=8, color='white')

# Level 3 - Transactions
level3_y = 1.2
level3_positions = [(1.5, level3_y), (4.5, level3_y), (6.5, level3_y), (9.5, level3_y)]
level3_labels = ['Tx A', 'Tx B', 'Tx C', 'Tx D']

for (x, y), label in zip(level3_positions, level3_labels):
    box = FancyBboxPatch((x - 0.5, y - 0.25), 1.0, 0.5,
                          boxstyle="round,pad=0.03", facecolor=MLGREEN, edgecolor='none')
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Draw connecting lines
# Root to Level 1
ax.plot([root_x, 3], [root_y - 0.3, level1_y + 0.25], color='#666666', lw=1.5)
ax.plot([root_x, 8], [root_y - 0.3, level1_y + 0.25], color='#666666', lw=1.5)

# Level 1 to Level 2
ax.plot([3, 1.5], [level1_y - 0.25, level2_y + 0.25], color='#666666', lw=1.5)
ax.plot([3, 4.5], [level1_y - 0.25, level2_y + 0.25], color='#666666', lw=1.5)
ax.plot([8, 6.5], [level1_y - 0.25, level2_y + 0.25], color='#666666', lw=1.5)
ax.plot([8, 9.5], [level1_y - 0.25, level2_y + 0.25], color='#666666', lw=1.5)

# Level 2 to Level 3
for x in [1.5, 4.5, 6.5, 9.5]:
    ax.plot([x, x], [level2_y - 0.25, level3_y + 0.25], color='#666666', lw=1.5)

# Legend
ax.text(0.3, 0.5, 'Root stored in block header', fontsize=8, color=MLPURPLE, fontweight='bold')
ax.text(0.3, 0.2, 'Change any transaction = new Merkle Root', fontsize=8, color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'merkle_tree_structure.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
