"""
IPO Process Timeline
Shows key milestones in going public

Output: ipo_timeline.pdf
Module: module_04_traditional
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # IPO timeline phases (weeks before/after pricing)
    phases = ['Planning\n& Selection', 'Due\nDiligence', 'SEC\nFiling', 'Road\nShow', 'Pricing', 'Trading']
    weeks = [-24, -16, -8, -2, 0, 1]
    durations = [8, 8, 6, 2, 0.5, 0]  # Duration of each phase

    colors = [MLLAVENDER, MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLGREEN]

    # Create horizontal bars showing duration
    for i, (phase, start, dur) in enumerate(zip(phases, weeks, durations)):
        if dur > 0:
            ax.barh(i, dur, left=start, height=0.6, color=colors[i],
                   edgecolor='white', linewidth=2)
        else:
            ax.scatter([start], [i], s=200, color=colors[i], zorder=5, marker='D')

    ax.set_yticks(range(len(phases)))
    ax.set_yticklabels(phases)
    ax.set_xlabel('Weeks (relative to pricing)', fontsize=11)
    ax.set_title('Typical IPO Process Timeline', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.axvline(x=0, color='gray', linestyle='--', linewidth=2, label='Pricing Day')
    ax.set_xlim(-28, 4)

    # Add annotations
    ax.annotate('S-1 Filed', xy=(-8, 2), xytext=(-12, 3.5),
                fontsize=8, arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('First\nTrade', xy=(1, 5), fontsize=8, ha='center')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical US IPO timeline]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ipo_timeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

MLLAVENDER = '#ADADE0'

if __name__ == '__main__':
    create_chart()
