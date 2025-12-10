"""
Regulatory Reporting Requirements
Major regulatory reports timeline

Output: regulatory_reporting.pdf
Module: module_04_trad_finance
Lesson: 43 - RegTech Compliance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Regulatory Reporting',
    'module': 'module_04_trad_finance',
    'lesson': 43,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/regulatory_reporting'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Report frequency and complexity
    ax1 = axes[0]

    reports = ['Form 13F', 'Form PF', 'CAT Reports', 'CCAR/DFAST', 'MiFID II\nReports', 'EMIR Trade\nReports']
    frequency = ['Quarterly', 'Quarterly', 'Daily', 'Annual', 'Daily', 'T+1']
    complexity = [3, 4, 5, 5, 4, 3]  # 1-5 scale
    data_volume = [2, 3, 5, 4, 5, 4]  # 1-5 scale

    x = np.arange(len(reports))
    width = 0.35

    bars1 = ax1.bar(x - width/2, complexity, width, label='Complexity', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x + width/2, data_volume, width, label='Data Volume', color='#FF7F0E', alpha=0.8)

    ax1.set_ylabel('Score (1-5)', fontsize=11)
    ax1.set_title('Regulatory Report Complexity', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(reports, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 6)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add frequency labels
    for i, freq in enumerate(frequency):
        ax1.text(i, 5.5, freq, ha='center', fontsize=8, style='italic', color='#666666')

    # Reporting timeline
    ax2 = axes[1]

    timeline_reports = ['Trade\nReporting', 'Position\nReporting', 'Risk\nMetrics', 'Stress\nTests', 'Capital\nAdequacy']
    t_minus = [0, 1, 5, 30, 45]  # Days from period end
    deadline = [1, 5, 15, 60, 90]  # Days allowed

    # Create Gantt-like chart
    for i, (report, start, dur) in enumerate(zip(timeline_reports, t_minus, deadline)):
        color = '#44A044' if dur <= 15 else '#FF7F0E' if dur <= 45 else '#D62728'
        ax2.barh(i, dur, left=start, height=0.6, color=color, alpha=0.8, edgecolor='black')
        ax2.text(start + dur + 2, i, f'T+{dur}', va='center', fontsize=9, fontweight='bold')

    ax2.set_xlabel('Days from Period End', fontsize=11)
    ax2.set_title('Reporting Deadlines', fontsize=12, fontweight='bold')
    ax2.set_yticks(range(len(timeline_reports)))
    ax2.set_yticklabels(timeline_reports, fontsize=10)
    ax2.set_xlim(0, 120)
    ax2.xaxis.grid(True, alpha=0.3)

    # Legend for colors
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#44A044', label='Short deadline (<15d)'),
        Patch(facecolor='#FF7F0E', label='Medium (15-45d)'),
        Patch(facecolor='#D62728', label='Extended (>45d)')
    ]
    ax2.legend(handles=legend_elements, loc='lower right', fontsize=9)

    fig.suptitle('Regulatory Reporting Requirements', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'regulatory_reporting.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
