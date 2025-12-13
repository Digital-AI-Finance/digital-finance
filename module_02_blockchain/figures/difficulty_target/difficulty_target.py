"""Difficulty Target - Leading zeros visualization"""
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
ax.text(5.5, 5.7, 'Mining Difficulty: Finding a Hash Below Target', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Target explanation
ax.text(0.5, 5.0, 'Target:', fontsize=10, fontweight='bold', color=MLPURPLE)
ax.text(2.0, 5.0, '0000000000000000000abc123...', fontsize=10, family='monospace', color=MLPURPLE)
ax.text(0.5, 4.55, '(Hash must be below this value = must start with many zeros)', fontsize=8, color='#666666')

# Examples of hash attempts
examples = [
    ('Nonce: 1', '8f3a2b1c9e7d...', 'Too high', MLRED),
    ('Nonce: 12345', '4a7b3c2d1e9f...', 'Too high', MLRED),
    ('Nonce: 987654', '1c2d3e4f5a6b...', 'Too high', MLRED),
    ('Nonce: 2,847,293', '00003f2e1d4c...', 'Getting closer!', MLORANGE),
    ('Nonce: 18,432,847', '0000000000000...', 'VALID!', MLGREEN),
]

y_start = 3.8
for i, (nonce, hash_val, status, color) in enumerate(examples):
    y = y_start - i * 0.6

    # Nonce
    ax.text(0.5, y, nonce, fontsize=9, family='monospace', color='#444444')

    # Arrow
    ax.annotate('', xy=(3.2, y), xytext=(2.8, y),
                arrowprops=dict(arrowstyle='->', color='#999999', lw=1))

    # Hash
    ax.text(3.4, y, f'Hash: {hash_val}', fontsize=9, family='monospace', color='#333333')

    # Status
    ax.text(7.5, y, status, fontsize=9, fontweight='bold', color=color)

    # Check/X mark
    if color == MLGREEN:
        ax.text(9.0, y, '[Y]', fontsize=10, color=MLGREEN, fontweight='bold')
    else:
        ax.text(9.0, y, '[X]', fontsize=10, color=color)

# Difficulty adjustment note
note_box = FancyBboxPatch((0.5, 0.3), 10, 0.9, boxstyle="round,pad=0.1",
                           facecolor='#F0F0FF', edgecolor=MLPURPLE, linewidth=1)
ax.add_patch(note_box)
ax.text(5.5, 0.95, 'Difficulty Adjustment', ha='center', fontsize=9, fontweight='bold', color=MLPURPLE)
ax.text(5.5, 0.55, 'Bitcoin adjusts target every 2016 blocks (~2 weeks) to maintain 10-minute average block time',
        ha='center', fontsize=8, color='#444444')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'difficulty_target.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
