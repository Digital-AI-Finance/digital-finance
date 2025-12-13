"""Block Structure Detailed - 80-byte header anatomy"""
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

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'Bitcoin Block Structure: 80-Byte Header', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Main block container
block = FancyBboxPatch((0.5, 0.5), 10, 4.8, boxstyle="round,pad=0.1",
                        facecolor='#F5F5F5', edgecolor=MLPURPLE, linewidth=2)
ax.add_patch(block)

# Header section
header = FancyBboxPatch((0.7, 3.0), 9.6, 2.0, boxstyle="round,pad=0.05",
                         facecolor=MLPURPLE, edgecolor='none')
ax.add_patch(header)
ax.text(5.5, 4.7, 'BLOCK HEADER (80 bytes)', ha='center', va='center',
        fontsize=11, fontweight='bold', color='white')

# Header fields
fields = [
    ('Version', '4 bytes', 'Protocol version'),
    ('Prev Block Hash', '32 bytes', 'Link to parent'),
    ('Merkle Root', '32 bytes', 'Transaction summary'),
    ('Timestamp', '4 bytes', 'Block creation time'),
    ('Difficulty', '4 bytes', 'Mining target'),
    ('Nonce', '4 bytes', 'Mining solution'),
]

field_width = 1.5
start_x = 0.9
y_field = 3.4

for i, (name, size, desc) in enumerate(fields):
    x = start_x + i * field_width

    # Field box
    box = FancyBboxPatch((x, y_field), field_width - 0.1, 1.3,
                          boxstyle="round,pad=0.02", facecolor='white',
                          edgecolor=MLBLUE, linewidth=1)
    ax.add_patch(box)

    ax.text(x + (field_width-0.1)/2, y_field + 1.0, name, ha='center', va='center',
            fontsize=7, fontweight='bold', color=MLPURPLE)
    ax.text(x + (field_width-0.1)/2, y_field + 0.65, size, ha='center', va='center',
            fontsize=8, color=MLORANGE, fontweight='bold')
    ax.text(x + (field_width-0.1)/2, y_field + 0.3, desc, ha='center', va='center',
            fontsize=6, color='#666666')

# Body section
body = FancyBboxPatch((0.7, 0.7), 9.6, 2.0, boxstyle="round,pad=0.05",
                       facecolor='#E8F0E8', edgecolor=MLGREEN, linewidth=2)
ax.add_patch(body)
ax.text(5.5, 2.4, 'BLOCK BODY (Variable size)', ha='center', va='center',
        fontsize=11, fontweight='bold', color=MLGREEN)

# Transaction boxes
for i in range(5):
    x = 1.5 + i * 1.7
    tx_box = FancyBboxPatch((x, 1.0), 1.3, 0.8, boxstyle="round,pad=0.02",
                             facecolor='white', edgecolor=MLGREEN, linewidth=1)
    ax.add_patch(tx_box)
    ax.text(x + 0.65, 1.4, f'Tx {i+1}', ha='center', va='center',
            fontsize=9, color=MLGREEN)

ax.text(9.5, 1.4, '...', ha='center', va='center', fontsize=14, color=MLGREEN)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'block_structure_detailed.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
