"""
FIX Protocol Overview
Financial Information eXchange

Output: fix_protocol.pdf
Module: module_04_trad_finance
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FIX Protocol',
    'module': 'module_04_trad_finance',
    'lesson': 40,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/fix_protocol'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # FIX Message Flow
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # Participants
    buy_side = mpatches.FancyBboxPatch((0.5, 3), 2, 4,
                                        boxstyle="round,pad=0.1",
                                        facecolor='#4A90E2', alpha=0.8,
                                        edgecolor='black', linewidth=2)
    ax1.add_patch(buy_side)
    ax1.text(1.5, 5, 'Buy-Side\n(Asset Mgr)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    sell_side = mpatches.FancyBboxPatch((7.5, 3), 2, 4,
                                         boxstyle="round,pad=0.1",
                                         facecolor='#44A044', alpha=0.8,
                                         edgecolor='black', linewidth=2)
    ax1.add_patch(sell_side)
    ax1.text(8.5, 5, 'Sell-Side\n(Broker)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Message arrows
    messages = [
        (2.7, 6.5, 7.3, 6.5, 'New Order Single (D)'),
        (7.3, 5.5, 2.7, 5.5, 'Execution Report (8)'),
        (2.7, 4.5, 7.3, 4.5, 'Order Cancel Request (F)'),
        (7.3, 3.5, 2.7, 3.5, 'Order Cancel Ack (8)'),
    ]

    for x1, y1, x2, y2, label in messages:
        ax1.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        ax1.text((x1+x2)/2, y1+0.2, label, ha='center', fontsize=8, fontweight='bold')

    ax1.set_title('FIX Message Flow', fontsize=12, fontweight='bold')
    ax1.axis('off')

    # FIX Message Types
    ax2 = axes[1]

    msg_types = ['Execution\nReport', 'New Order', 'Market Data', 'Order\nCancel',
                'Trade\nCapture', 'Quote', 'Others']
    volume = [35, 25, 20, 8, 5, 4, 3]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#17BECF', '#888888']

    bars = ax2.bar(msg_types, volume, color=colors, alpha=0.8, edgecolor='black')

    for bar, vol in zip(bars, volume):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{vol}%', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlabel('FIX Message Type', fontsize=11)
    ax2.set_ylabel('Volume Share (%)', fontsize=11)
    ax2.set_title('FIX Message Type Distribution', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 45)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('FIX Protocol: Electronic Trading Standard', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'fix_protocol.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
