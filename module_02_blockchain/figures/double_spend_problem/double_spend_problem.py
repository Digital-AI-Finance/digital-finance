"""Double Spend Problem - Visual showing the attack scenario"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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
MLORANGE = '#FF7F0E'

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.axis('off')

# Title
ax.text(5.5, 5.7, 'The Double-Spending Problem', ha='center', va='center',
        fontsize=13, fontweight='bold', color=MLPURPLE)

# Alice (sender)
alice_box = FancyBboxPatch((0.5, 2), 1.5, 2, boxstyle="round,pad=0.1",
                            facecolor='#E8E8F0', edgecolor=MLPURPLE, linewidth=2)
ax.add_patch(alice_box)
ax.text(1.25, 3.5, 'Alice', ha='center', va='center', fontsize=10, fontweight='bold', color=MLPURPLE)
ax.text(1.25, 2.8, 'Balance:', ha='center', fontsize=8)
ax.text(1.25, 2.4, '10 BTC', ha='center', fontsize=10, fontweight='bold', color=MLORANGE)

# Bob (merchant 1)
bob_box = FancyBboxPatch((8, 4), 2, 1.5, boxstyle="round,pad=0.1",
                          facecolor='#E8F0E8', edgecolor=MLGREEN, linewidth=2)
ax.add_patch(bob_box)
ax.text(9, 5, 'Bob (Merchant)', ha='center', va='center', fontsize=9, fontweight='bold', color=MLGREEN)
ax.text(9, 4.4, 'Receives 10 BTC', ha='center', fontsize=8)

# Charlie (merchant 2)
charlie_box = FancyBboxPatch((8, 0.5), 2, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#F0E8E8', edgecolor=MLRED, linewidth=2)
ax.add_patch(charlie_box)
ax.text(9, 1.5, 'Charlie (Merchant)', ha='center', va='center', fontsize=9, fontweight='bold', color=MLRED)
ax.text(9, 0.9, 'Receives 10 BTC', ha='center', fontsize=8)

# Arrows showing double spend
arrow_style = "Simple,tail_width=0.3,head_width=3,head_length=6"

# Arrow to Bob
ax.annotate('', xy=(8, 4.75), xytext=(2, 3.5),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.text(5, 4.5, 'Tx1: Send 10 BTC', fontsize=9, color=MLGREEN)

# Arrow to Charlie
ax.annotate('', xy=(8, 1.25), xytext=(2, 2.5),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=2))
ax.text(5, 1.5, 'Tx2: Send 10 BTC', fontsize=9, color=MLRED)

# Problem box
problem_box = FancyBboxPatch((3.5, 2.3), 3.5, 1.4, boxstyle="round,pad=0.1",
                              facecolor='#FFF0E0', edgecolor=MLORANGE, linewidth=2)
ax.add_patch(problem_box)
ax.text(5.25, 3.3, 'PROBLEM', ha='center', va='center', fontsize=10,
        fontweight='bold', color=MLORANGE)
ax.text(5.25, 2.8, 'Same coins spent twice!', ha='center', va='center',
        fontsize=9, color='#666666')
ax.text(5.25, 2.5, 'Which transaction is valid?', ha='center', va='center',
        fontsize=9, style='italic', color='#666666')

# Bottom note
ax.text(5.5, 0.1, 'Blockchain solves this by establishing a single, agreed-upon transaction order',
        ha='center', fontsize=9, style='italic', color='#666666')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'double_spend_problem.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
