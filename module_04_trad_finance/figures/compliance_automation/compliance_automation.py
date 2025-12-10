"""
Compliance Automation Benefits
Manual vs automated comparison

Output: compliance_automation.pdf
Module: module_04_trad_finance
Lesson: 43 - RegTech Compliance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Compliance Automation',
    'module': 'module_04_trad_finance',
    'lesson': 43,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/compliance_automation'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Manual vs Automated comparison
    ax1 = axes[0]

    categories = ['Data\nCollection', 'Validation', 'Report\nGeneration', 'Review\n& Filing', 'Exception\nHandling']
    manual_hours = [40, 25, 30, 20, 35]
    automated_hours = [2, 3, 1, 5, 8]

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax1.bar(x - width/2, manual_hours, width, label='Manual Process',
                    color='#D62728', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, automated_hours, width, label='Automated (RegTech)',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Hours per Reporting Cycle', fontsize=11)
    ax1.set_title('Time Savings: Manual vs. Automated Compliance', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 50)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add reduction percentages
    for i, (m, a) in enumerate(zip(manual_hours, automated_hours)):
        reduction = ((m - a) / m) * 100
        ax1.text(i, max(m, a) + 2, f'-{reduction:.0f}%', ha='center',
                fontsize=9, fontweight='bold', color='#44A044')

    # Cost comparison
    ax2 = axes[1]

    cost_categories = ['Personnel', 'Technology', 'Penalties\n(avoided)', 'Total TCO']
    manual_costs = [500, 100, 200, 800]
    automated_costs = [150, 250, 20, 420]

    x = np.arange(len(cost_categories))

    bars3 = ax2.bar(x - width/2, manual_costs, width, label='Manual Process',
                    color='#D62728', alpha=0.8, edgecolor='black')
    bars4 = ax2.bar(x + width/2, automated_costs, width, label='RegTech Solution',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Annual Cost ($K)', fontsize=11)
    ax2.set_title('Cost Comparison: Manual vs. RegTech', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(cost_categories, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 1000)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add cost labels
    for bars in [bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, height + 15,
                    f'${height}K', ha='center', fontsize=9)

    # ROI annotation
    ax2.annotate('47% Cost\nReduction', xy=(3, 420), xytext=(2.3, 700),
                fontsize=11, fontweight='bold', color='#44A044',
                arrowprops=dict(arrowstyle='->', color='#44A044'))

    fig.suptitle('RegTech Automation: Time & Cost Benefits', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'compliance_automation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
