"""
Legacy System Modernization
Migration strategies and approaches

Output: legacy_modernization.pdf
Module: module_04_trad_finance
Lesson: 38 - Core Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Legacy Modernization',
    'module': 'module_04_trad_finance',
    'lesson': 38,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/legacy_modernization'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Modernization Approaches
    ax1 = axes[0]

    approaches = ['Big Bang\nReplacement', 'Gradual\nMigration', 'Encapsulation\n(API Wrap)', 'Strangler\nPattern', 'Cloud\nLift & Shift']
    risk = [95, 45, 25, 35, 50]
    cost = [90, 70, 40, 60, 55]
    duration = [85, 75, 30, 65, 45]  # Months normalized

    x = np.arange(len(approaches))
    width = 0.25

    ax1.bar(x - width, risk, width, label='Risk Level', color='#D62728', alpha=0.8)
    ax1.bar(x, cost, width, label='Total Cost', color='#FF7F0E', alpha=0.8)
    ax1.bar(x + width, duration, width, label='Duration', color='#4A90E2', alpha=0.8)

    ax1.set_xlabel('Modernization Approach', fontsize=11)
    ax1.set_ylabel('Relative Score (0-100)', fontsize=11)
    ax1.set_title('Modernization Approach Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(approaches, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 110)
    ax1.yaxis.grid(True, alpha=0.3)

    # Migration Timeline
    ax2 = axes[1]

    phases = ['Assessment', 'Planning', 'Development', 'Testing', 'Migration', 'Optimization']
    duration_months = [2, 3, 12, 6, 4, 6]
    cumulative = np.cumsum([0] + duration_months[:-1])

    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#17BECF']

    for i, (phase, dur, start) in enumerate(zip(phases, duration_months, cumulative)):
        ax2.barh(0, dur, left=start, height=0.4, color=colors[i], alpha=0.8, edgecolor='black')
        ax2.text(start + dur/2, 0, f'{phase}\n({dur}mo)', ha='center', va='center', fontsize=8, fontweight='bold')

    ax2.set_xlabel('Months', fontsize=11)
    ax2.set_title('Typical Core Banking Modernization Timeline', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 35)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_yticks([])

    # Total duration
    ax2.text(16.5, 0.35, f'Total: {sum(duration_months)} months', fontsize=11, fontweight='bold', ha='center')

    fig.suptitle('Core Banking Legacy Modernization', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'legacy_modernization.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
