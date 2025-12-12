"""
Capital Markets Trade Lifecycle
Shows the stages of a securities trade

Output: capital_markets_workflow.pdf
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Trade lifecycle stages with typical timings (in different units)
    stages = ['Order\nEntry', 'Execution', 'Clearing', 'Settlement', 'Custody']

    # Time ranges showing pre-T+1 vs T+1 settlement
    pre_t1_times = [0.1, 0.001, 1, 2, 0.5]  # Time in days (approximate)
    t1_times = [0.1, 0.001, 1, 1, 0.5]  # T+1 settlement

    x = np.arange(len(stages))
    width = 0.35

    bars1 = ax.bar(x - width/2, pre_t1_times, width, label='T+2 Settlement (pre-2024)',
                   color=MLORANGE, alpha=0.8)
    bars2 = ax.bar(x + width/2, t1_times, width, label='T+1 Settlement (2024+)',
                   color=MLBLUE, alpha=0.8)

    ax.set_ylabel('Time (Days)', fontsize=11)
    ax.set_title('Securities Trade Lifecycle Duration', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(stages)
    ax.legend(loc='upper right', framealpha=0.9)

    # Add annotations for key stages
    ax.annotate('Microseconds', xy=(1, 0.001), xytext=(1, 0.8),
                fontsize=8, ha='center', arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555')

    ax.annotate('Major change:\n2 days -> 1 day', xy=(3.3, 1.5), fontsize=9,
                ha='center', color=MLPURPLE, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax.set_ylim(0, 3)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative timings]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'capital_markets_workflow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
