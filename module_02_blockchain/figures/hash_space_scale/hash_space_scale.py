"""Hash Space Scale - 2^256 visualization"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

plt.rcParams.update({
    'font.size': 10, 'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
    'figure.dpi': 150, 'font.family': 'serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLRED = '#D62728'
MLGREEN = '#2CA02C'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'SHA-256 Hash Space: Incomprehensibly Large', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# The big number
ax.text(5.5, 4.5, '2^256', ha='center', fontsize=28, fontweight='bold',
        color=MLPURPLE, family='monospace')
ax.text(5.5, 3.9, '= 115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,936',
        ha='center', fontsize=7, color='#444444', family='monospace')

# Comparison boxes
comparisons = [
    ('Atoms in Universe', '~10^80', 'Hash space is 10^77 times larger!', MLBLUE),
    ('Grains of Sand on Earth', '~10^23', 'Hash space is 10^54 times larger!', MLORANGE),
    ('Seconds Since Big Bang', '~10^17', 'Hash space is 10^60 times larger!', MLGREEN),
]

box_width = 3.2
start_x = 0.6
y = 1.8

for i, (name, value, note, color) in enumerate(comparisons):
    x = start_x + i * (box_width + 0.3)

    # Box
    box = FancyBboxPatch((x, y), box_width, 1.6, boxstyle="round,pad=0.08",
                          facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(box)

    ax.text(x + box_width/2, y + 1.3, name, ha='center', va='center',
            fontsize=9, fontweight='bold', color=color)
    ax.text(x + box_width/2, y + 0.85, value, ha='center', va='center',
            fontsize=14, fontweight='bold', color='#333333', family='monospace')
    ax.text(x + box_width/2, y + 0.35, note, ha='center', va='center',
            fontsize=7, color='#666666')

# Bottom note
ax.text(5.5, 0.8, 'Probability of collision: Winning the lottery every day for a billion years',
        ha='center', fontsize=9, style='italic', color='#666666')
ax.text(5.5, 0.3, 'This massive space makes brute-force attacks computationally infeasible',
        ha='center', fontsize=9, color='#444444')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'hash_space_scale.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
