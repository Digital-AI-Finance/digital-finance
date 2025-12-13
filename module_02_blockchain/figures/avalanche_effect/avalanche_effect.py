"""Avalanche Effect - Tiny input change, massive output change"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import hashlib

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
ax.text(5.5, 5.7, 'Avalanche Effect: One Bit Change = Completely Different Hash',
        ha='center', fontsize=12, fontweight='bold', color=MLPURPLE)

# Generate actual hashes
inputs = ['Hello', 'hello', 'Hello!', 'Hellp']
hashes = [hashlib.sha256(s.encode()).hexdigest() for s in inputs]

# Display comparisons
y_positions = [4.2, 3.0, 1.8, 0.6]

for i, (inp, h, y) in enumerate(zip(inputs, hashes, y_positions)):
    # Input box
    input_box = FancyBboxPatch((0.5, y), 2, 0.8, boxstyle="round,pad=0.05",
                                facecolor='#E8E8F0', edgecolor=MLBLUE, linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, y + 0.4, f'"{inp}"', ha='center', va='center',
            fontsize=11, family='monospace', color=MLBLUE, fontweight='bold')

    # Arrow
    ax.annotate('', xy=(3.3, y + 0.4), xytext=(2.5, y + 0.4),
                arrowprops=dict(arrowstyle='->', color='#999999', lw=1.5))

    # Hash output
    hash_box = FancyBboxPatch((3.3, y), 7, 0.8, boxstyle="round,pad=0.05",
                               facecolor='#F5F5F5', edgecolor=MLORANGE, linewidth=1)
    ax.add_patch(hash_box)
    ax.text(6.8, y + 0.4, h[:32] + '...', ha='center', va='center',
            fontsize=8, family='monospace', color='#444444')

# Highlight the difference
ax.annotate('', xy=(1.5, 3.8), xytext=(1.5, 3.5),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax.text(2.8, 3.65, 'One character\ndifference!', fontsize=8, color=MLRED,
        fontweight='bold', ha='left')

# Bottom note
ax.text(5.5, 0.1, 'Even the smallest change produces a completely unpredictable new hash',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'avalanche_effect.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
