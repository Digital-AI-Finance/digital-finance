"""
ACH Payment Flow
Automated Clearing House process

Output: ach_flow.pdf
Module: module_04_trad_finance
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'ACH Flow',
    'module': 'module_04_trad_finance',
    'lesson': 39,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/ach_flow'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    # Flow participants
    participants = [
        (2, 6, 'Originator', '#4A90E2', 'Initiates\npayment'),
        (5, 6, 'ODFI', '#44A044', 'Originating\nBank'),
        (8, 6, 'ACH\nOperator', '#FF7F0E', 'Fed/EPN'),
        (11, 6, 'RDFI', '#44A044', 'Receiving\nBank'),
        (14, 6, 'Receiver', '#4A90E2', 'Gets\npayment'),
    ]

    for x, y, label, color, desc in participants:
        rect = mpatches.FancyBboxPatch((x-1.2, y-0.8), 2.4, 1.6,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.1, label, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')
        ax.text(x, y - 0.4, desc, ha='center', va='center', fontsize=8, color='white')

        if x < 14:
            ax.annotate('', xy=(x+1.8, y), xytext=(x+1.3, y),
                       arrowprops=dict(arrowstyle='->', color='black', lw=2))

    # Timeline
    ax.text(8, 3, 'Settlement Timeline', fontsize=12, fontweight='bold', ha='center')

    timeline = [
        (3, 'T+0', 'File\nSubmission'),
        (6, 'T+0', 'Batch\nProcessing'),
        (9, 'T+1', 'Settlement'),
        (12, 'T+1/T+2', 'Funds\nAvailable'),
    ]

    for x, day, event in timeline:
        ax.plot(x, 2, 'ko', markersize=10)
        ax.text(x, 2.4, day, ha='center', fontsize=9, fontweight='bold', color='#D62728')
        ax.text(x, 1.5, event, ha='center', fontsize=8)

    ax.plot([3, 12], [2, 2], 'k-', linewidth=2)

    # Same Day ACH note
    ax.text(8, 0.8, 'Same Day ACH: Settlement within same business day (additional fee)',
           ha='center', fontsize=9, style='italic', color='#666666')

    ax.set_title('ACH Payment Flow: Originator to Receiver', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'ach_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
