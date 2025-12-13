"""Blockchain Trilemma - Triangle diagram showing trade-offs"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, Circle
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

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.8, 1.5)
ax.axis('off')

# Triangle vertices
top = (0, 1.2)
left = (-1, -0.5)
right = (1, -0.5)

# Draw triangle
triangle = Polygon([top, left, right], facecolor='#E8E8F0', edgecolor=MLPURPLE,
                   linewidth=3, alpha=0.5)
ax.add_patch(triangle)

# Vertex labels with icons
ax.text(top[0], top[1] + 0.15, 'DECENTRALIZATION', ha='center', va='bottom',
        fontsize=11, fontweight='bold', color=MLPURPLE)
ax.text(left[0] - 0.1, left[1] - 0.1, 'SECURITY', ha='center', va='top',
        fontsize=11, fontweight='bold', color=MLPURPLE)
ax.text(right[0] + 0.1, right[1] - 0.1, 'SCALABILITY', ha='center', va='top',
        fontsize=11, fontweight='bold', color=MLPURPLE)

# Add blockchain positions
blockchains = [
    ('Bitcoin', -0.15, 0.5, MLORANGE, 'High security,\nhigh decentralization,\nlow scalability'),
    ('Ethereum', 0.15, 0.3, MLBLUE, 'Balanced approach\nafter PoS transition'),
    ('Solana', 0.5, -0.1, MLGREEN, 'High scalability,\nlower decentralization'),
]

for name, x, y, color, desc in blockchains:
    circle = Circle((x, y), 0.08, facecolor=color, edgecolor='white', linewidth=2, zorder=5)
    ax.add_patch(circle)
    ax.text(x, y, name[0], ha='center', va='center', fontsize=8,
            fontweight='bold', color='white', zorder=6)

# Legend
legend_y = -0.6
for i, (name, _, _, color, _) in enumerate(blockchains):
    x_pos = -0.8 + i * 0.8
    circle = Circle((x_pos, legend_y), 0.05, facecolor=color, edgecolor='white', linewidth=1)
    ax.add_patch(circle)
    ax.text(x_pos + 0.1, legend_y, name, ha='left', va='center', fontsize=9)

# Title
ax.text(0, 1.45, 'The Blockchain Trilemma', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLPURPLE)

# Subtitle
ax.text(0, -0.75, '"Pick any two" - No blockchain optimizes all three simultaneously',
        ha='center', va='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'blockchain_trilemma.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
