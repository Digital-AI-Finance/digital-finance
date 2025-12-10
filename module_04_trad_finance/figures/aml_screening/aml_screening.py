"""
AML Screening Process
Transaction monitoring and sanctions

Output: aml_screening.pdf
Module: module_04_trad_finance
Lesson: 43 - RegTech Compliance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'AML Screening',
    'module': 'module_04_trad_finance',
    'lesson': 43,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/aml_screening'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # AML Screening Funnel
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    # Funnel stages
    stages = [
        ('All Transactions', 9, '#4A90E2', '10M/day'),
        ('Rule-Based Alerts', 5, '#FF7F0E', '50K'),
        ('ML Prioritized', 2, '#9B59B6', '5K'),
        ('Analyst Review', 0.8, '#D62728', '500'),
        ('SARs Filed', 0.15, '#333333', '50'),
    ]

    y_positions = [8, 6.5, 5, 3.5, 2]

    for i, (label, width, color, count) in enumerate(stages):
        y = y_positions[i]
        rect = mpatches.FancyBboxPatch((5-width/2, y-0.4), width, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black')
        ax1.add_patch(rect)
        ax1.text(5, y, f'{label}\n({count})', ha='center', va='center',
                fontsize=9, fontweight='bold', color='white' if i < 4 else 'white')

        # Reduction arrow and percentage
        if i > 0:
            prev_count = stages[i-1][3]
            curr_count = count
            ax1.annotate('', xy=(5, y+0.4), xytext=(5, y_positions[i-1]-0.4),
                        arrowprops=dict(arrowstyle='->', color='#666666', lw=1.5))

    ax1.text(5, 9.2, 'AML Screening Funnel', ha='center', va='center',
            fontsize=12, fontweight='bold')
    ax1.text(5, 0.8, 'False Positive Rate: 95%+ at rule level\nML reduces by 90%',
            ha='center', va='center', fontsize=9, style='italic', color='#666666')

    # Alert types breakdown
    ax2 = axes[1]

    alert_types = ['Large Cash\nTransactions', 'Structuring', 'Rapid\nMovement', 'High-Risk\nCountry', 'PEP\nMatches', 'Sanctions\nHits']
    volumes = [15000, 12000, 8000, 7000, 5000, 3000]
    false_positive_rates = [96, 94, 92, 88, 75, 45]

    x = np.arange(len(alert_types))
    width = 0.6

    colors = ['#44A044' if fp < 80 else '#FF7F0E' if fp < 92 else '#D62728' for fp in false_positive_rates]
    bars = ax2.bar(x, volumes, width, color=colors, alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Monthly Alert Volume', fontsize=11)
    ax2.set_title('Alert Types & False Positive Rates', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(alert_types, fontsize=9)
    ax2.set_ylim(0, 20000)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add FP rate labels
    for bar, fp in zip(bars, false_positive_rates):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 400,
                f'{fp}% FP', ha='center', fontsize=9, fontweight='bold',
                color='#D62728' if fp > 90 else '#FF7F0E' if fp > 75 else '#44A044')

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#D62728', label='High FP (>90%)'),
        Patch(facecolor='#FF7F0E', label='Medium FP (75-90%)'),
        Patch(facecolor='#44A044', label='Low FP (<75%)')
    ]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=9)

    fig.suptitle('AML Transaction Monitoring', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'aml_screening.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
