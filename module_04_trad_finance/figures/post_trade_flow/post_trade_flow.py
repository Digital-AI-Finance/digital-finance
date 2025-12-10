"""
Post-Trade Processing Flow
Trade to settlement workflow

Output: post_trade_flow.pdf
Module: module_04_trad_finance
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Post-Trade Flow',
    'module': 'module_04_trad_finance',
    'lesson': 44,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/post_trade_flow'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Main flow (horizontal)
    flow_steps = [
        ('Trade\nExecution', 1.5, 6, '#4A90E2'),
        ('Trade\nEnrichment', 4, 6, '#44A044'),
        ('Matching\n& Confirm', 6.5, 6, '#FF7F0E'),
        ('Netting', 9, 6, '#9B59B6'),
        ('Instruction\nGeneration', 11.5, 6, '#D62728'),
    ]

    for name, x, y, color in flow_steps:
        rect = mpatches.FancyBboxPatch((x-1.1, y-0.5), 2.2, 1,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

    # Arrows
    for i in range(len(flow_steps)-1):
        ax.annotate('', xy=(flow_steps[i+1][1]-1.1, flow_steps[i+1][2]),
                   xytext=(flow_steps[i][1]+1.1, flow_steps[i][2]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))

    # Second row
    flow_steps2 = [
        ('Settlement\n(CSD)', 11.5, 3.5, '#D62728'),
        ('Position\nUpdate', 9, 3.5, '#9B59B6'),
        ('Recon-\nciliation', 6.5, 3.5, '#FF7F0E'),
        ('Reporting', 4, 3.5, '#44A044'),
    ]

    for name, x, y, color in flow_steps2:
        rect = mpatches.FancyBboxPatch((x-1.1, y-0.5), 2.2, 1,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.6, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='black')

    # Connect first and second row
    ax.annotate('', xy=(11.5, 4), xytext=(11.5, 5.5),
               arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))

    # Arrows in second row
    for i in range(len(flow_steps2)-1):
        ax.annotate('', xy=(flow_steps2[i+1][1]+1.1, flow_steps2[i+1][2]),
                   xytext=(flow_steps2[i][1]-1.1, flow_steps2[i][2]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))

    # Exception handling box
    except_box = mpatches.FancyBboxPatch((0.5, 1), 5, 1.5,
                                          boxstyle="round,pad=0.05",
                                          facecolor='#FFE4E1', edgecolor='#D62728', linewidth=2)
    ax.add_patch(except_box)
    ax.text(3, 2.3, 'Exception Management', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#D62728')
    ax.text(3, 1.7, 'Fails | Breaks | Disputes | Amendments',
            ha='center', va='center', fontsize=9, color='#666666')
    ax.text(3, 1.2, 'STP Rate Target: 98%+', ha='center', va='center',
            fontsize=9, style='italic', color='#888888')

    # Dashed line from matching to exceptions
    ax.plot([6.5, 3], [5.5, 2.5], '--', color='#D62728', lw=1.5)

    # Data sources box
    data_box = mpatches.FancyBboxPatch((8.5, 1), 5, 1.5,
                                        boxstyle="round,pad=0.05",
                                        facecolor='#E6F3FF', edgecolor='#4A90E2', linewidth=2)
    ax.add_patch(data_box)
    ax.text(11, 2.3, 'Reference Data', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#4A90E2')
    ax.text(11, 1.7, 'SSI | LEI | ISIN | Market Rules',
            ha='center', va='center', fontsize=9, color='#666666')

    # Title
    ax.text(7, 7.5, 'Post-Trade Processing Workflow', ha='center', va='center',
            fontsize=14, fontweight='bold')

    # Timeline
    ax.text(1.5, 4.8, 'T+0', ha='center', fontsize=9, fontweight='bold', color='#4A90E2')
    ax.text(6.5, 4.8, 'T+0/T+1', ha='center', fontsize=9, fontweight='bold', color='#FF7F0E')
    ax.text(11.5, 4.8, 'T+1/T+2', ha='center', fontsize=9, fontweight='bold', color='#D62728')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'post_trade_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
