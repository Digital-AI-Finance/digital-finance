"""Centralized vs Decentralized Networks - Side-by-side comparison"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.size': 10, 'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
    'figure.dpi': 150, 'font.family': 'serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLRED = '#D62728'
MLGREEN = '#2CA02C'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

# Centralized Network (Left)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.axis('off')
ax1.set_title('Centralized Network', fontsize=12, fontweight='bold', color=MLRED, pad=10)

# Central node
central = Circle((0, 0), 0.3, facecolor=MLRED, edgecolor='darkred', linewidth=2)
ax1.add_patch(central)
ax1.text(0, 0, 'Central\nServer', ha='center', va='center', fontsize=7, color='white', fontweight='bold')

# Peripheral nodes
angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
for angle in angles:
    x, y = 1.3 * np.cos(angle), 1.3 * np.sin(angle)
    node = Circle((x, y), 0.15, facecolor='#CCCCCC', edgecolor='#666666', linewidth=1)
    ax1.add_patch(node)
    # Connection to center
    ax1.plot([0, x*0.8], [0, y*0.8], color='#999999', linewidth=1, linestyle='-')

ax1.text(0, -1.8, 'Single Point of Failure', ha='center', fontsize=9, color=MLRED, style='italic')

# Decentralized Network (Right)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.axis('off')
ax2.set_title('Decentralized Network', fontsize=12, fontweight='bold', color=MLGREEN, pad=10)

# Create mesh of nodes
np.random.seed(42)
n_nodes = 12
positions = []
for i in range(n_nodes):
    angle = 2 * np.pi * i / n_nodes + np.random.uniform(-0.2, 0.2)
    radius = 1.0 + np.random.uniform(-0.3, 0.3)
    x, y = radius * np.cos(angle), radius * np.sin(angle)
    positions.append((x, y))
    node = Circle((x, y), 0.15, facecolor=MLGREEN, edgecolor='darkgreen', linewidth=1, alpha=0.8)
    ax2.add_patch(node)

# Connect nearby nodes (mesh)
for i, (x1, y1) in enumerate(positions):
    for j, (x2, y2) in enumerate(positions):
        if i < j:
            dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            if dist < 1.2:
                ax2.plot([x1, x2], [y1, y2], color=MLGREEN, linewidth=0.8, alpha=0.5)

ax2.text(0, -1.8, 'No Single Point of Failure', ha='center', fontsize=9, color=MLGREEN, style='italic')

# Add comparison box at bottom
fig.text(0.5, 0.02, 'Blockchain uses decentralized architecture for resilience and censorship resistance',
         ha='center', fontsize=10, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'centralized_vs_decentralized.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
