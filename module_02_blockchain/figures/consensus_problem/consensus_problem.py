"""
Consensus Problem
Illustrates the Byzantine Generals Problem and distributed consensus

Output: consensus_problem.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Consensus Problem',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/consensus_problem'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create consensus problem diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Byzantine Generals Problem', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 9.6, 'How do distributed nodes agree without trusting each other?', fontsize=14, ha='center', color='#666')

    # Draw generals in a circle
    center_x, center_y = 7, 5.5
    radius = 3
    n_generals = 5
    angles = np.linspace(90, 90 - 360, n_generals + 1)[:-1] * np.pi / 180

    generals = []
    for i, angle in enumerate(angles):
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        generals.append((x, y))

        # Determine if traitor (1 out of 5)
        is_traitor = (i == 2)
        color = '#E74C3C' if is_traitor else '#27AE60'
        label = 'Traitor' if is_traitor else f'General {i+1}'

        circle = plt.Circle((x, y), 0.6, facecolor=color, alpha=0.3, edgecolor=color, lw=2)
        ax.add_patch(circle)
        ax.text(x, y, f'G{i+1}', ha='center', va='center', fontsize=12, fontweight='bold')
        if is_traitor:
            ax.text(x, y-0.9, '(Traitor)', ha='center', fontsize=10, color='#E74C3C')

    # Draw message lines between generals
    for i in range(n_generals):
        for j in range(i+1, n_generals):
            x1, y1 = generals[i]
            x2, y2 = generals[j]
            ax.plot([x1, x2], [y1, y2], 'k-', alpha=0.2, lw=1)

    # Central decision
    decision_circle = plt.Circle((center_x, center_y), 1.2, facecolor='#3498DB', alpha=0.3, edgecolor='#3498DB', lw=2)
    ax.add_patch(decision_circle)
    ax.text(center_x, center_y+0.3, 'Attack', ha='center', fontsize=12, fontweight='bold')
    ax.text(center_x, center_y-0.3, 'or Retreat?', ha='center', fontsize=12, fontweight='bold')

    # Requirements box
    req_box = mpatches.FancyBboxPatch((0.5, 0.5), 6, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F39C12', alpha=0.15,
                                       edgecolor='#F39C12', lw=2)
    ax.add_patch(req_box)
    ax.text(3.5, 2.7, 'Byzantine Fault Tolerance (BFT)', ha='center', fontsize=12, fontweight='bold', color='#D68910')
    ax.text(3.5, 2.1, 'Must tolerate f faulty nodes', ha='center', fontsize=11)
    ax.text(3.5, 1.6, 'Requires n >= 3f + 1 nodes', ha='center', fontsize=11)
    ax.text(3.5, 1.1, '(Can tolerate up to 33% malicious)', ha='center', fontsize=10, style='italic')

    # Blockchain solution box
    sol_box = mpatches.FancyBboxPatch((7.5, 0.5), 6, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#27AE60', alpha=0.15,
                                       edgecolor='#27AE60', lw=2)
    ax.add_patch(sol_box)
    ax.text(10.5, 2.7, 'Blockchain Solution', ha='center', fontsize=12, fontweight='bold', color='#1E8449')
    ax.text(10.5, 2.1, 'PoW: 51% honest hashpower', ha='center', fontsize=11)
    ax.text(10.5, 1.6, 'PoS: 2/3 honest stake', ha='center', fontsize=11)
    ax.text(10.5, 1.1, 'Economic incentives align behavior', ha='center', fontsize=10, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Lamport et al., "The Byzantine Generals Problem" (1982)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'consensus_problem.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
