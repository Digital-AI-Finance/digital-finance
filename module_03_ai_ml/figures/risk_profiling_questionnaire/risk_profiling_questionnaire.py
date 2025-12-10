"""
Risk Profiling Questionnaire Analysis
ML-based risk assessment

Output: risk_profiling_questionnaire.pdf
Module: module_03_ai_ml
Lesson: 33 - Robo-Advisors ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Risk Profiling Questionnaire',
    'module': 'module_03_ai_ml',
    'lesson': 33,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/risk_profiling_questionnaire'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Risk Profile Distribution
    ax1 = axes[0]

    profiles = ['Conservative', 'Moderately\nConservative', 'Moderate',
                'Moderately\nAggressive', 'Aggressive']
    percentages = [15, 22, 35, 18, 10]
    colors = ['#4A90E2', '#6AAAF0', '#888888', '#FF9966', '#D62728']

    bars = ax1.bar(profiles, percentages, color=colors, edgecolor='black', alpha=0.8)

    for bar, pct in zip(bars, percentages):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{pct}%', ha='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Risk Profile', fontsize=11)
    ax1.set_ylabel('Percentage of Users (%)', fontsize=11)
    ax1.set_title('Client Risk Profile Distribution', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 45)
    ax1.yaxis.grid(True, alpha=0.3)

    # Risk Score vs Asset Allocation
    ax2 = axes[1]

    risk_scores = np.arange(1, 11)
    equity = [20, 30, 40, 50, 60, 70, 75, 80, 85, 90]
    bonds = [70, 60, 50, 40, 30, 22, 18, 14, 10, 6]
    alternatives = [10, 10, 10, 10, 10, 8, 7, 6, 5, 4]

    ax2.stackplot(risk_scores, equity, bonds, alternatives,
                  labels=['Equity', 'Bonds', 'Alternatives'],
                  colors=['#4A90E2', '#44A044', '#FF7F0E'], alpha=0.8)

    ax2.set_xlabel('Risk Score (1-10)', fontsize=11)
    ax2.set_ylabel('Asset Allocation (%)', fontsize=11)
    ax2.set_title('Risk Score to Asset Allocation Mapping', fontsize=12, fontweight='bold')
    ax2.legend(loc='center right', fontsize=9)
    ax2.set_xlim(1, 10)
    ax2.set_ylim(0, 100)

    # Add profile labels
    ax2.text(2, 50, 'Conservative', fontsize=9, fontweight='bold', ha='center')
    ax2.text(5.5, 50, 'Moderate', fontsize=9, fontweight='bold', ha='center')
    ax2.text(9, 50, 'Aggressive', fontsize=9, fontweight='bold', ha='center')

    fig.suptitle('Robo-Advisor Risk Profiling System', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_profiling_questionnaire.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
