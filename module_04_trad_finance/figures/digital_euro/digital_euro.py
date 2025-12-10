"""
Digital Euro Project
ECB's CBDC initiative

Output: digital_euro.pdf
Module: module_04_trad_finance
Lesson: 48 - CBDC
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Digital Euro',
    'module': 'module_04_trad_finance',
    'lesson': 48,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/digital_euro'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Timeline
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    phases = [
        ('Investigation\nPhase', '2021-2023', 2, 8, '#FFD700', 'Completed'),
        ('Preparation\nPhase', '2023-2025', 2, 6, '#4A90E2', 'Current'),
        ('Legislative\nProcess', '2024-2025', 2, 4, '#FF7F0E', 'In Progress'),
        ('Realization\n(if approved)', '2025-2027', 2, 2, '#44A044', 'Planned'),
    ]

    for name, period, x, y, color, status in phases:
        rect = mpatches.FancyBboxPatch((x-1.5, y-0.6), 7, 1.2,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.6, edgecolor='black', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold')
        ax1.text(5.5, y, period, ha='center', va='center', fontsize=10)
        ax1.text(8, y, status, ha='center', va='center', fontsize=9,
                style='italic', color='#666666')

    # Arrows
    for i in range(3):
        ax1.annotate('', xy=(2, phases[i+1][3] + 0.6), xytext=(2, phases[i][3] - 0.6),
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    ax1.text(5, 9.3, 'Digital Euro Timeline', ha='center', fontsize=12, fontweight='bold')

    # Key design features
    ax2 = axes[1]

    features = ['Holding\nLimit', 'Offline\nPayments', 'Privacy\nLevel', 'Interest\nRate', 'Pan-Euro\nAccess', 'Programmability']
    planned = [85, 90, 70, 20, 95, 40]
    importance = [80, 85, 95, 30, 90, 60]

    x = np.arange(len(features))
    width = 0.35

    bars1 = ax2.bar(x - width/2, planned, width, label='Planned Implementation',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax2.bar(x + width/2, importance, width, label='Public Interest',
                    color='#FF7F0E', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Score (%)', fontsize=11)
    ax2.set_title('Digital Euro: Features & Priorities', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(features, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    # Key stats annotation
    ax2.text(3, 102, 'Proposed: 3000 EUR holding limit | Privacy: "cash-like" for small tx',
            fontsize=9, style='italic', color='#666666', ha='center')

    fig.suptitle('Digital Euro (ECB Project)', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'digital_euro.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
