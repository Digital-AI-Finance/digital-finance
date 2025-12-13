"""SHA-256 Visualization - Hash function diagram"""
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

fig, ax = plt.subplots(figsize=(11, 5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')

# Title
ax.text(5.5, 4.7, 'SHA-256: Cryptographic Hash Function', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Input box
input_box = FancyBboxPatch((0.5, 1.5), 3, 2, boxstyle="round,pad=0.1",
                            facecolor='#E8E8F0', edgecolor=MLBLUE, linewidth=2)
ax.add_patch(input_box)
ax.text(2, 3.1, 'INPUT', ha='center', fontsize=10, fontweight='bold', color=MLBLUE)
ax.text(2, 2.5, 'Any data', ha='center', fontsize=9, color='#666666')
ax.text(2, 2.1, '(any size)', ha='center', fontsize=9, color='#666666')
ax.text(2, 1.7, '"Hello World"', ha='center', fontsize=8, family='monospace')

# Arrow
ax.annotate('', xy=(4.3, 2.5), xytext=(3.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=2))

# Hash function box
hash_box = FancyBboxPatch((4.3, 1.8), 2.4, 1.4, boxstyle="round,pad=0.1",
                           facecolor=MLPURPLE, edgecolor='none')
ax.add_patch(hash_box)
ax.text(5.5, 2.5, 'SHA-256', ha='center', fontsize=11, fontweight='bold', color='white')

# Arrow
ax.annotate('', xy=(7.5, 2.5), xytext=(6.7, 2.5),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=2))

# Output box
output_box = FancyBboxPatch((7.5, 1.5), 3, 2, boxstyle="round,pad=0.1",
                             facecolor='#F0E8E0', edgecolor=MLORANGE, linewidth=2)
ax.add_patch(output_box)
ax.text(9, 3.1, 'OUTPUT', ha='center', fontsize=10, fontweight='bold', color=MLORANGE)
ax.text(9, 2.5, '256-bit hash', ha='center', fontsize=9, color='#666666')
ax.text(9, 2.1, '(always 64 hex)', ha='center', fontsize=9, color='#666666')
ax.text(9, 1.7, 'a591a6d4...', ha='center', fontsize=8, family='monospace')

# Properties at bottom
props = [
    ('Deterministic', 'Same input = same output'),
    ('One-way', 'Cannot reverse'),
    ('Collision-resistant', 'Unique outputs'),
    ('Fast', '~1M hashes/sec'),
]

for i, (name, desc) in enumerate(props):
    x = 1.5 + i * 2.5
    ax.text(x, 0.8, name, ha='center', fontsize=9, fontweight='bold', color=MLPURPLE)
    ax.text(x, 0.4, desc, ha='center', fontsize=8, color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'sha256_visualization.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
