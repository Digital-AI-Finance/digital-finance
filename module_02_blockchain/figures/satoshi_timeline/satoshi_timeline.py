"""Satoshi Timeline - Pre-Bitcoin attempts and Bitcoin milestones"""
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

fig, ax = plt.subplots(figsize=(11, 5))
ax.set_xlim(1988, 2015)
ax.set_ylim(-1, 3)
ax.axis('off')

# Title
ax.text(2001.5, 2.8, 'The Road to Bitcoin: Digital Cash Attempts', ha='center',
        fontsize=12, fontweight='bold', color=MLPURPLE)

# Timeline line
ax.plot([1990, 2014], [1, 1], color='#CCCCCC', linewidth=3, zorder=1)

# Events
events = [
    (1990, 'DigiCash', 'David Chaum', MLBLUE, 'below', 'Centralized, failed 1998'),
    (1997, 'Hashcash', 'Adam Back', MLBLUE, 'above', 'Proof-of-work concept'),
    (1998, 'b-money', 'Wei Dai', MLBLUE, 'below', 'Theoretical proposal'),
    (2005, 'Bit Gold', 'Nick Szabo', MLBLUE, 'above', 'Never implemented'),
    (2008, 'Bitcoin\nWhitepaper', 'Satoshi', MLORANGE, 'below', 'Oct 31, 2008'),
    (2009, 'Genesis\nBlock', 'Satoshi', MLGREEN, 'above', 'Jan 3, 2009'),
    (2010, 'First\nTransaction', '10K BTC', MLGREEN, 'below', 'Pizza purchase'),
]

for year, name, author, color, pos, note in events:
    # Circle marker
    circle = Circle((year, 1), 0.15, facecolor=color, edgecolor='white',
                    linewidth=2, zorder=3)
    ax.add_patch(circle)

    # Vertical line
    if pos == 'above':
        ax.plot([year, year], [1.15, 1.8], color=color, linewidth=1.5, zorder=2)
        y_text = 2.0
        va = 'bottom'
    else:
        ax.plot([year, year], [0.85, 0.2], color=color, linewidth=1.5, zorder=2)
        y_text = 0.0
        va = 'top'

    # Event name
    ax.text(year, y_text, name, ha='center', va=va, fontsize=9,
            fontweight='bold', color=color)

    # Note
    if pos == 'above':
        ax.text(year, y_text + 0.4, note, ha='center', va='bottom',
                fontsize=7, color='#666666', style='italic')
    else:
        ax.text(year, y_text - 0.4, note, ha='center', va='top',
                fontsize=7, color='#666666', style='italic')

# Year markers
for year in [1990, 1995, 2000, 2005, 2010]:
    ax.text(year, 0.7, str(year), ha='center', fontsize=8, color='#999999')

# Legend
ax.text(1992, -0.7, 'Pre-Bitcoin attempts', fontsize=8, color=MLBLUE)
ax.plot([1990, 1991], [-0.65, -0.65], color=MLBLUE, linewidth=3)
ax.text(2000, -0.7, 'Bitcoin milestones', fontsize=8, color=MLGREEN)
ax.plot([1998, 1999], [-0.65, -0.65], color=MLGREEN, linewidth=3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'satoshi_timeline.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
