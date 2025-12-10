"""
Clearing and Settlement Process
Trade lifecycle to settlement

Output: clearing_settlement.pdf
Module: module_04_trad_finance
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Clearing and Settlement',
    'module': 'module_04_trad_finance',
    'lesson': 44,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/clearing_settlement'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Trade lifecycle
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    stages = [
        ('Trade\nExecution', 1.5, 8, '#4A90E2', 'T'),
        ('Trade\nCapture', 1.5, 6.2, '#44A044', 'T'),
        ('Confirmation\n& Matching', 1.5, 4.4, '#FF7F0E', 'T+0'),
        ('Clearing\n(CCP)', 1.5, 2.6, '#9B59B6', 'T+0 to T+1'),
        ('Settlement', 1.5, 0.8, '#D62728', 'T+2'),
    ]

    for i, (name, x, y, color, time) in enumerate(stages):
        # Main box
        rect = mpatches.FancyBboxPatch((x-1.2, y-0.5), 2.4, 1,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

        # Time label
        ax1.text(3.5, y, time, ha='left', va='center', fontsize=10,
                fontweight='bold', color=color)

        # Arrow to next
        if i < len(stages) - 1:
            ax1.annotate('', xy=(1.5, stages[i+1][2]+0.5), xytext=(1.5, y-0.5),
                        arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Right side: key participants
    participants = [
        ('Exchanges\nATS/MTF', 6, 8, '#4A90E2'),
        ('Brokers', 6, 6.2, '#44A044'),
        ('Affirm\nServices', 6, 4.4, '#FF7F0E'),
        ('CCP\n(DTCC/LCH)', 6, 2.6, '#9B59B6'),
        ('CSD\n(Depository)', 6, 0.8, '#D62728'),
    ]

    for name, x, y, color in participants:
        rect = mpatches.FancyBboxPatch((x-1, y-0.5), 2, 1,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.3, edgecolor=color, linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x, y, name, ha='center', va='center', fontsize=9, fontweight='bold')

    # Connect stages to participants
    for i in range(5):
        ax1.plot([2.7, 5], [stages[i][2], participants[i][2]], '--', color='#888888', lw=1)

    ax1.text(4, 9.3, 'Trade Lifecycle', ha='center', fontsize=12, fontweight='bold')

    # Settlement cycles comparison
    ax2 = axes[1]

    regions = ['US Equities\n(2024)', 'EU Equities', 'US Treasuries', 'FX Spot', 'Derivatives', 'Crypto\n(Exchange)']
    cycles = [1, 2, 1, 2, 0, 0]  # T+ days
    target = [1, 1, 1, 1, 0, 0]  # Future target

    x = np.arange(len(regions))
    width = 0.35

    bars1 = ax2.bar(x - width/2, cycles, width, label='Current',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax2.bar(x + width/2, target, width, label='Target/Future',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Settlement Cycle (T+n days)', fontsize=11)
    ax2.set_title('Settlement Cycles by Asset Class', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(regions, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 3)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add labels
    for bar in bars1:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 0.1,
                f'T+{int(height)}', ha='center', fontsize=9, fontweight='bold')

    ax2.text(4.5, 2.5, 'US moved to T+1\nin May 2024', fontsize=9, style='italic',
            color='#666666', ha='center')

    fig.suptitle('Clearing and Settlement Infrastructure', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'clearing_settlement.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
