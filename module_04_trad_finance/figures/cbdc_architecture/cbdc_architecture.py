"""
CBDC Architecture Options
Technical design choices

Output: cbdc_architecture.pdf
Module: module_04_trad_finance
Lesson: 48 - CBDC
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'CBDC Architecture',
    'module': 'module_04_trad_finance',
    'lesson': 48,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/cbdc_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Two-tier architecture diagram
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    # Central Bank
    cb_box = mpatches.FancyBboxPatch((3.5, 8), 3, 1.2,
                                      boxstyle="round,pad=0.05",
                                      facecolor='#D62728', alpha=0.8, edgecolor='black', linewidth=2)
    ax1.add_patch(cb_box)
    ax1.text(5, 8.6, 'Central Bank', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Intermediaries
    intermediaries = [('Bank A', 1.5), ('Bank B', 5), ('Bank C', 8.5)]
    for name, x in intermediaries:
        rect = mpatches.FancyBboxPatch((x-1, 5), 2, 1,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#4A90E2', alpha=0.8, edgecolor='black')
        ax1.add_patch(rect)
        ax1.text(x, 5.5, name, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

    # End users
    for i, x in enumerate([0.5, 2.5, 4, 6, 7.5, 9.5]):
        rect = mpatches.FancyBboxPatch((x-0.5, 2), 1, 0.8,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#44A044', alpha=0.8, edgecolor='black')
        ax1.add_patch(rect)
        ax1.text(x, 2.4, 'User', ha='center', va='center', fontsize=8, color='white')

    # Connections
    for x in [1.5, 5, 8.5]:
        ax1.annotate('', xy=(x, 6), xytext=(5, 8),
                    arrowprops=dict(arrowstyle='<->', color='#333333', lw=2))

    ax1.plot([1.5, 1.5], [5, 3], 'k-', lw=1.5)
    ax1.plot([0.5, 2.5], [3, 3], 'k-', lw=1.5)
    ax1.plot([0.5, 0.5], [3, 2.8], 'k-', lw=1.5)
    ax1.plot([2.5, 2.5], [3, 2.8], 'k-', lw=1.5)

    ax1.plot([5, 5], [5, 3], 'k-', lw=1.5)
    ax1.plot([4, 6], [3, 3], 'k-', lw=1.5)
    ax1.plot([4, 4], [3, 2.8], 'k-', lw=1.5)
    ax1.plot([6, 6], [3, 2.8], 'k-', lw=1.5)

    ax1.plot([8.5, 8.5], [5, 3], 'k-', lw=1.5)
    ax1.plot([7.5, 9.5], [3, 3], 'k-', lw=1.5)
    ax1.plot([7.5, 7.5], [3, 2.8], 'k-', lw=1.5)
    ax1.plot([9.5, 9.5], [3, 2.8], 'k-', lw=1.5)

    # Labels
    ax1.text(5, 9.5, 'Two-Tier CBDC Architecture', ha='center',
            fontsize=12, fontweight='bold')
    ax1.text(0.3, 8.5, 'Tier 1:\nCentral Bank', ha='left', fontsize=9, color='#D62728')
    ax1.text(0.3, 5.3, 'Tier 2:\nIntermediaries', ha='left', fontsize=9, color='#4A90E2')
    ax1.text(0.3, 2.3, 'End Users', ha='left', fontsize=9, color='#44A044')

    ax1.text(5, 0.8, 'Most common model: CB issues, banks distribute',
            ha='center', fontsize=9, style='italic', color='#666666')

    # Design choice comparison
    ax2 = axes[1]

    choices = ['Account-\nbased', 'Token-\nbased', 'DLT', 'Centralized', 'Interest-\nbearing', 'Non-interest']
    wholesale = [90, 30, 60, 80, 50, 50]
    retail = [70, 80, 40, 70, 20, 80]

    x = np.arange(len(choices))
    width = 0.35

    ax2.bar(x - width/2, wholesale, width, label='Wholesale CBDC',
            color='#4A90E2', alpha=0.8, edgecolor='black')
    ax2.bar(x + width/2, retail, width, label='Retail CBDC',
            color='#44A044', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Design Preference (%)', fontsize=11)
    ax2.set_title('CBDC Design Choices (by CB preference)', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(choices, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 100)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('CBDC Technical Architecture', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'cbdc_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
