"""Merkle Proof - Light client verification path"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
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
ax.text(5.5, 5.7, 'Merkle Proof: Verify Transaction with Minimal Data', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Highlight the verification path for Tx C
# Level 0 - Root (highlighted)
root_x, root_y = 5.5, 4.6
root_box = FancyBboxPatch((root_x - 0.9, root_y - 0.3), 1.8, 0.6,
                           boxstyle="round,pad=0.05", facecolor=MLPURPLE, edgecolor=MLRED, linewidth=3)
ax.add_patch(root_box)
ax.text(root_x, root_y, 'Merkle Root', ha='center', va='center',
        fontsize=9, fontweight='bold', color='white')

# Level 1
level1_y = 3.5
# Hash AB - provided in proof (highlighted)
box_ab = FancyBboxPatch((2.3, level1_y - 0.25), 1.4, 0.5,
                         boxstyle="round,pad=0.03", facecolor='#FFE0E0', edgecolor=MLRED, linewidth=2)
ax.add_patch(box_ab)
ax.text(3, level1_y, 'Hash(AB)', ha='center', va='center', fontsize=8, color=MLRED, fontweight='bold')

# Hash CD - computed
box_cd = FancyBboxPatch((7.3, level1_y - 0.25), 1.4, 0.5,
                         boxstyle="round,pad=0.03", facecolor=MLBLUE, edgecolor=MLRED, linewidth=2)
ax.add_patch(box_cd)
ax.text(8, level1_y, 'Hash(CD)', ha='center', va='center', fontsize=8, color='white')

# Level 2
level2_y = 2.4
# Hash C - computed
box_c = FancyBboxPatch((5.9, level2_y - 0.25), 1.2, 0.5,
                        boxstyle="round,pad=0.03", facecolor=MLORANGE, edgecolor=MLRED, linewidth=2)
ax.add_patch(box_c)
ax.text(6.5, level2_y, 'Hash(C)', ha='center', va='center', fontsize=8, color='white')

# Hash D - provided in proof (highlighted)
box_d = FancyBboxPatch((8.9, level2_y - 0.25), 1.2, 0.5,
                        boxstyle="round,pad=0.03", facecolor='#FFE0E0', edgecolor=MLRED, linewidth=2)
ax.add_patch(box_d)
ax.text(9.5, level2_y, 'Hash(D)', ha='center', va='center', fontsize=8, color=MLRED, fontweight='bold')

# Level 3 - Tx C (the one being verified)
level3_y = 1.3
box_tx = FancyBboxPatch((5.9, level3_y - 0.25), 1.2, 0.5,
                         boxstyle="round,pad=0.03", facecolor=MLGREEN, edgecolor=MLRED, linewidth=3)
ax.add_patch(box_tx)
ax.text(6.5, level3_y, 'Tx C', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Draw verification path lines
ax.plot([root_x, 8], [root_y - 0.3, level1_y + 0.25], color=MLRED, lw=2)
ax.plot([root_x, 3], [root_y - 0.3, level1_y + 0.25], color=MLRED, lw=2, linestyle='--')
ax.plot([8, 6.5], [level1_y - 0.25, level2_y + 0.25], color=MLRED, lw=2)
ax.plot([8, 9.5], [level1_y - 0.25, level2_y + 0.25], color=MLRED, lw=2, linestyle='--')
ax.plot([6.5, 6.5], [level2_y - 0.25, level3_y + 0.25], color=MLRED, lw=2)

# Legend box
legend_box = FancyBboxPatch((0.3, 0.4), 3.8, 1.4, boxstyle="round,pad=0.1",
                             facecolor='#F8F8F8', edgecolor='#CCCCCC', linewidth=1)
ax.add_patch(legend_box)
ax.text(0.5, 1.5, 'To verify Tx C:', fontsize=9, fontweight='bold', color='#333333')
ax.text(0.5, 1.1, '1. Have: Tx C (the transaction)', fontsize=8, color='#444444')
ax.text(0.5, 0.8, '2. Need: Hash(D), Hash(AB) [proof]', fontsize=8, color=MLRED)
ax.text(0.5, 0.5, '3. Compute path to Root', fontsize=8, color='#444444')

# Efficiency note
ax.text(5.5, 0.2, 'Proof size: O(log n) - verify 1 of 1000 txs with only 10 hashes!',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'merkle_proof.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
