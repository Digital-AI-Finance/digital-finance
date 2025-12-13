"""Blockchain Use Cases - Category breakdown"""
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
MLTEAL = '#17BECF'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'Blockchain Use Cases Beyond Cryptocurrency', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

categories = [
    ('Financial\nServices', ['Cross-border payments', 'Trade finance', 'Securities settlement'], MLBLUE),
    ('Supply\nChain', ['Product tracking', 'Provenance verification', 'Counterfeit prevention'], MLGREEN),
    ('Digital\nIdentity', ['Self-sovereign ID', 'KYC/AML', 'Credential verification'], MLORANGE),
    ('Healthcare', ['Medical records', 'Drug traceability', 'Clinical trials'], MLRED),
    ('Government', ['Voting systems', 'Land registry', 'Public records'], MLTEAL),
]

box_width = 2.0
box_height = 3.8
spacing = 0.15
start_x = 0.4

for i, (title, examples, color) in enumerate(categories):
    x = start_x + i * (box_width + spacing)
    y = 0.8

    # Main box
    box = FancyBboxPatch((x, y), box_width, box_height, boxstyle="round,pad=0.08",
                          facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch((x, y + box_height - 0.9), box_width, 0.9,
                             boxstyle="round,pad=0.05,rounding_size=0.15",
                             facecolor=color, edgecolor='none')
    ax.add_patch(header)
    ax.text(x + box_width/2, y + box_height - 0.45, title, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

    # Examples
    for j, example in enumerate(examples):
        ax.text(x + 0.15, y + box_height - 1.3 - j*0.7, f'- {example}',
                fontsize=8, color='#444444', va='top')

# Bottom note
ax.text(5.5, 0.2, 'Blockchain adds value where trust, transparency, and immutability are critical',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'blockchain_use_cases.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
