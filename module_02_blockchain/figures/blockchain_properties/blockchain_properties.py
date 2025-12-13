"""Blockchain Properties - 5 key properties infographic"""
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
MLGREEN = '#2CA02C'
MLRED = '#D62728'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'Five Key Properties of Blockchain', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLPURPLE)

properties = [
    ('Decentralization', 'No single authority', MLBLUE, 'D'),
    ('Transparency', 'All transactions visible', MLGREEN, 'T'),
    ('Immutability', 'Cannot alter history', MLORANGE, 'I'),
    ('Security', 'Cryptographically secured', MLRED, 'S'),
    ('Pseudonymity', 'Addresses, not names', MLPURPLE, 'P'),
]

# Draw 5 boxes in a row
box_width = 1.8
box_height = 3.5
spacing = 0.3
start_x = 0.5

for i, (name, desc, color, letter) in enumerate(properties):
    x = start_x + i * (box_width + spacing)
    y = 1

    # Main box
    box = FancyBboxPatch((x, y), box_width, box_height, boxstyle="round,pad=0.1",
                          facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(box)

    # Icon circle at top
    circle = Circle((x + box_width/2, y + box_height - 0.5), 0.35,
                    facecolor=color, edgecolor='white', linewidth=2)
    ax.add_patch(circle)
    ax.text(x + box_width/2, y + box_height - 0.5, letter, ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')

    # Property name
    ax.text(x + box_width/2, y + box_height - 1.2, name, ha='center', va='center',
            fontsize=9, fontweight='bold', color=color, wrap=True)

    # Description
    ax.text(x + box_width/2, y + 0.8, desc, ha='center', va='center',
            fontsize=8, color='#666666', wrap=True)

# Bottom note
ax.text(5.5, 0.3, 'These properties combine to create a trustless, tamper-proof system',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'blockchain_properties.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
