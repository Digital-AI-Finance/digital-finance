"""
Robo-Advisor vs Human Advisor
Performance and cost comparison

Output: robo_vs_human.pdf
Module: module_03_ai_ml
Lesson: 33 - Robo-Advisors ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Robo vs Human',
    'module': 'module_03_ai_ml',
    'lesson': 33,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/robo_vs_human'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Cost Comparison
    ax1 = axes[0]

    categories = ['Management\nFee (%)', 'Minimum\nInvestment ($K)', 'Tax-Loss\nHarvesting', 'Rebalancing\nFrequency', '24/7\nAccess']
    robo = [0.25, 0.5, 1, 1, 1]  # Normalized scores
    human = [1.0, 25, 0.5, 0.3, 0.2]

    x = np.arange(len(categories))
    width = 0.35

    # Invert for "lower is better" metrics
    robo_display = [0.25, 0.5, 90, 100, 100]
    human_display = [1.0, 25, 50, 30, 20]

    bars1 = ax1.bar(x - width/2, robo_display, width, label='Robo-Advisor', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x + width/2, human_display, width, label='Human Advisor', color='#FF7F0E', alpha=0.8)

    # Add value labels
    labels_robo = ['0.25%', '$500', 'Yes', 'Automatic', 'Yes']
    labels_human = ['1.0%', '$25K', 'Limited', 'Quarterly', 'Business hrs']

    for bar, label in zip(bars1, labels_robo):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                label, ha='center', fontsize=8, fontweight='bold', color='#4A90E2')
    for bar, label in zip(bars2, labels_human):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                label, ha='center', fontsize=8, fontweight='bold', color='#FF7F0E')

    ax1.set_xlabel('Feature', fontsize=11)
    ax1.set_ylabel('Score (Higher = Better)', fontsize=11)
    ax1.set_title('Robo vs Human Advisor: Feature Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 120)

    # Long-term Performance (Net of Fees)
    ax2 = axes[1]

    years = np.arange(0, 21)

    # Starting with $100K, 7% gross return
    gross_return = 0.07
    robo_fee = 0.0025
    human_fee = 0.01

    robo_value = 100 * (1 + gross_return - robo_fee) ** years
    human_value = 100 * (1 + gross_return - human_fee) ** years
    diy_value = 100 * (1 + gross_return - 0.001) ** years  # DIY with low-cost ETFs

    ax2.plot(years, robo_value, 'b-', linewidth=2.5, label=f'Robo (0.25% fee)')
    ax2.plot(years, human_value, '-', color='#FF7F0E', linewidth=2.5, label=f'Human (1.0% fee)')
    ax2.plot(years, diy_value, 'g--', linewidth=2, label=f'DIY ETFs (0.1% fee)')

    # Final values annotation
    ax2.annotate(f'${robo_value[-1]:.0f}K', xy=(20, robo_value[-1]),
                xytext=(17, robo_value[-1]+30), fontsize=9, fontweight='bold', color='#4A90E2')
    ax2.annotate(f'${human_value[-1]:.0f}K', xy=(20, human_value[-1]),
                xytext=(17, human_value[-1]-30), fontsize=9, fontweight='bold', color='#FF7F0E')

    ax2.set_xlabel('Years', fontsize=11)
    ax2.set_ylabel('Portfolio Value ($K)', fontsize=11)
    ax2.set_title('$100K Investment: 20-Year Projection', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 20)

    # Difference annotation
    diff = robo_value[-1] - human_value[-1]
    ax2.annotate(f'Fee Impact: ${diff:.0f}K', xy=(15, 300),
                fontsize=10, fontweight='bold', color='#D62728',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

    fig.suptitle('Robo-Advisor vs Human Advisor Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_vs_human.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
