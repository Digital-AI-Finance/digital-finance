"""Blockchain vs Database - Comparison table visualization"""
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
ax.text(5.5, 5.7, 'When to Use Blockchain vs Traditional Database', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Table data
headers = ['Aspect', 'Traditional DB', 'Blockchain']
rows = [
    ('Control', 'Centralized', 'Distributed'),
    ('Trust', 'Trust the admin', 'Trustless'),
    ('Performance', '1000s TPS', '10-1000 TPS'),
    ('Data modification', 'CRUD operations', 'Append-only'),
    ('Transparency', 'Private by default', 'Public by default'),
    ('Cost', 'Lower', 'Higher'),
]

# Draw table
col_widths = [2.5, 3.5, 3.5]
row_height = 0.65
start_x = 0.8
start_y = 4.5

# Header row
x = start_x
for i, (header, width) in enumerate(zip(headers, col_widths)):
    box = FancyBboxPatch((x, start_y), width, row_height,
                          boxstyle="square,pad=0", facecolor=MLPURPLE, edgecolor='white')
    ax.add_patch(box)
    ax.text(x + width/2, start_y + row_height/2, header, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    x += width

# Data rows
for row_idx, (aspect, traditional, blockchain) in enumerate(rows):
    y = start_y - (row_idx + 1) * row_height
    x = start_x

    # Alternating row colors
    bg_color = '#F5F5F5' if row_idx % 2 == 0 else 'white'

    # Aspect column
    box = FancyBboxPatch((x, y), col_widths[0], row_height,
                          boxstyle="square,pad=0", facecolor=bg_color, edgecolor='#CCCCCC')
    ax.add_patch(box)
    ax.text(x + col_widths[0]/2, y + row_height/2, aspect, ha='center', va='center',
            fontsize=9, fontweight='bold', color='#444444')
    x += col_widths[0]

    # Traditional DB column
    box = FancyBboxPatch((x, y), col_widths[1], row_height,
                          boxstyle="square,pad=0", facecolor=bg_color, edgecolor='#CCCCCC')
    ax.add_patch(box)
    ax.text(x + col_widths[1]/2, y + row_height/2, traditional, ha='center', va='center',
            fontsize=9, color=MLBLUE)
    x += col_widths[1]

    # Blockchain column
    box = FancyBboxPatch((x, y), col_widths[2], row_height,
                          boxstyle="square,pad=0", facecolor=bg_color, edgecolor='#CCCCCC')
    ax.add_patch(box)
    ax.text(x + col_widths[2]/2, y + row_height/2, blockchain, ha='center', va='center',
            fontsize=9, color=MLORANGE)

# Bottom verdict boxes
y_verdict = 0.3

# Use Database box
db_box = FancyBboxPatch((1, y_verdict), 4, 0.8, boxstyle="round,pad=0.05",
                         facecolor='#E8F0FF', edgecolor=MLBLUE, linewidth=2)
ax.add_patch(db_box)
ax.text(3, y_verdict + 0.55, 'Use Traditional Database when:', ha='center',
        fontsize=9, fontweight='bold', color=MLBLUE)
ax.text(3, y_verdict + 0.2, 'Single org, high performance, privacy needed',
        ha='center', fontsize=8, color='#666666')

# Use Blockchain box
bc_box = FancyBboxPatch((6, y_verdict), 4, 0.8, boxstyle="round,pad=0.05",
                         facecolor='#FFF0E8', edgecolor=MLORANGE, linewidth=2)
ax.add_patch(bc_box)
ax.text(8, y_verdict + 0.55, 'Use Blockchain when:', ha='center',
        fontsize=9, fontweight='bold', color=MLORANGE)
ax.text(8, y_verdict + 0.2, 'Multiple parties, trust issues, auditability',
        ha='center', fontsize=8, color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'blockchain_vs_database.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
