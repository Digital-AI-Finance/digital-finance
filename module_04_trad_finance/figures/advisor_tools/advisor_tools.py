"""
Advisor Tools and Productivity
Technology for wealth advisors

Output: advisor_tools.pdf
Module: module_04_trad_finance
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Advisor Tools',
    'module': 'module_04_trad_finance',
    'lesson': 46,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/advisor_tools'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Time allocation: Before vs After Tech
    ax1 = axes[0]

    activities = ['Client\nMeetings', 'Investment\nResearch', 'Admin\nTasks', 'Compliance', 'Prospecting', 'Planning']
    before = [20, 15, 30, 20, 8, 7]
    after = [35, 20, 10, 10, 12, 13]

    x = np.arange(len(activities))
    width = 0.35

    bars1 = ax1.bar(x - width/2, before, width, label='Before Tech',
                    color='#D62728', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, after, width, label='With Tech Tools',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Time Allocation (%)', fontsize=11)
    ax1.set_title('Advisor Time Allocation', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(activities, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 40)
    ax1.yaxis.grid(True, alpha=0.3)

    # Highlight improvements
    value_add = ['Client\nMeetings', 'Investment\nResearch', 'Prospecting', 'Planning']
    for i, act in enumerate(activities):
        if act in value_add:
            ax1.annotate('', xy=(i + width/2, after[i]), xytext=(i + width/2, after[i] + 3),
                        arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    ax1.text(1.5, 37, 'Value-add activities increase', fontsize=9, style='italic', color='#44A044')

    # Productivity metrics
    ax2 = axes[1]

    metrics = ['Clients per\nAdvisor', 'AUM per\nAdvisor ($M)', 'Revenue per\nClient ($K)', 'Retention\nRate (%)', 'NPS\nScore']
    baseline = [80, 50, 4, 85, 35]
    with_tech = [120, 75, 5.5, 92, 55]

    x = np.arange(len(metrics))
    width = 0.35

    bars3 = ax2.bar(x - width/2, baseline, width, label='Industry Average',
                    color='#888888', alpha=0.6, edgecolor='black')
    bars4 = ax2.bar(x + width/2, with_tech, width, label='Tech-Enabled',
                    color='#4A90E2', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Metric Value', fontsize=11)
    ax2.set_title('Advisor Productivity Metrics', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(metrics, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add improvement percentages
    for i, (b, t) in enumerate(zip(baseline, with_tech)):
        improvement = ((t - b) / b) * 100
        ax2.text(i, max(b, t) + 3, f'+{improvement:.0f}%',
                ha='center', fontsize=9, fontweight='bold', color='#44A044')

    fig.suptitle('Advisor Tools & Productivity Impact', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'advisor_tools.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
