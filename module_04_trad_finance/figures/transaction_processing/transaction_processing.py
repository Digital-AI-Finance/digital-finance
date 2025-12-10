"""
Transaction Processing Flow
Bank transaction lifecycle

Output: transaction_processing.pdf
Module: module_04_trad_finance
Lesson: 38 - Core Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Transaction Processing',
    'module': 'module_04_trad_finance',
    'lesson': 38,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/transaction_processing'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    # Transaction flow steps
    steps = [
        (2, 4, 'Initiation', '#4A90E2', 'Channel Input\nValidation'),
        (5, 4, 'Authorization', '#44A044', 'Limits Check\nFraud Screen'),
        (8, 4, 'Processing', '#FF7F0E', 'Account Update\nLedger Entry'),
        (11, 4, 'Settlement', '#9B59B6', 'Net Position\nFinal Transfer'),
        (14, 4, 'Reporting', '#D62728', 'Confirmation\nAudit Trail'),
    ]

    for x, y, label, color, desc in steps:
        # Main circle
        circle = plt.Circle((x, y), 0.8, facecolor=color, edgecolor='black', linewidth=2, alpha=0.8)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color='white')

        # Description below
        ax.text(x, y - 1.5, desc, ha='center', va='top', fontsize=8)

        # Arrow to next
        if x < 14:
            ax.annotate('', xy=(x+1.3, y), xytext=(x+0.9, y),
                       arrowprops=dict(arrowstyle='->', color='black', lw=2))

    # Timeline
    ax.text(8, 6.5, 'Transaction Lifecycle: Milliseconds to Days', ha='center',
           fontsize=12, fontweight='bold')

    times = ['<1 sec', '1-5 sec', 'Real-time', 'T+0 to T+2', 'Immediate']
    for i, (x, _, _, _, _) in enumerate(steps):
        ax.text(x, 2.2, times[i], ha='center', fontsize=9, color='#666666')

    ax.set_title('Bank Transaction Processing Flow', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'transaction_processing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
