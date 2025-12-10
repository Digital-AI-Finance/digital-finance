"""
Default Probability Curve
Probability of default vs credit score

Output: default_probability_curve.pdf
Module: module_03_ai_ml
Lesson: 30 - Credit Scoring
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Default Probability Curve',
    'module': 'module_03_ai_ml',
    'lesson': 30,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/default_probability_curve'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # PD Curve
    ax1 = axes[0]
    scores = np.linspace(300, 850, 100)

    # Logistic function for PD
    def pd_curve(score, k=0.02, x0=600):
        return 1 / (1 + np.exp(k * (score - x0)))

    pd = pd_curve(scores) * 0.35  # Scale to max ~35%

    ax1.plot(scores, pd * 100, 'b-', linewidth=3)
    ax1.fill_between(scores, 0, pd * 100, alpha=0.2, color='#4A90E2')

    # Add threshold lines
    ax1.axhline(y=5, color='#44A044', linestyle='--', linewidth=1.5, label='Low Risk (<5%)')
    ax1.axhline(y=15, color='#FF7F0E', linestyle='--', linewidth=1.5, label='Medium Risk (5-15%)')
    ax1.axhline(y=25, color='#D62728', linestyle='--', linewidth=1.5, label='High Risk (>15%)')

    ax1.set_xlabel('Credit Score', fontsize=11)
    ax1.set_ylabel('Probability of Default (%)', fontsize=11)
    ax1.set_title('Default Probability vs. Credit Score', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(300, 850)
    ax1.set_ylim(0, 40)
    ax1.grid(True, alpha=0.3)

    # Annotate key points
    ax1.annotate('Subprime\nRegion', xy=(500, 22), fontsize=9, ha='center',
                color='#D62728', fontweight='bold')
    ax1.annotate('Prime\nRegion', xy=(750, 3), fontsize=9, ha='center',
                color='#44A044', fontweight='bold')

    # Loss Given Default and Expected Loss
    ax2 = axes[1]
    score_buckets = ['300-499', '500-599', '600-699', '700-799', '800-850']
    pd_values = [32, 18, 8, 3, 0.8]
    lgd = [65, 55, 45, 40, 35]  # Loss given default (%)
    el = [pd * lg / 100 for pd, lg in zip(pd_values, lgd)]  # Expected loss

    x = np.arange(len(score_buckets))
    width = 0.35

    bars1 = ax2.bar(x - width/2, pd_values, width, label='PD (%)', color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x + width/2, el, width, label='Expected Loss (%)', color='#D62728', alpha=0.8)

    # Add LGD as line
    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, lgd, 'go-', linewidth=2, markersize=8, label='LGD (%)')
    ax2_twin.set_ylabel('Loss Given Default (%)', fontsize=10, color='#44A044')
    ax2_twin.tick_params(axis='y', labelcolor='#44A044')
    ax2_twin.set_ylim(0, 80)

    ax2.set_xlabel('Credit Score Range', fontsize=11)
    ax2.set_ylabel('Probability / Expected Loss (%)', fontsize=11)
    ax2.set_title('Credit Risk Components by Score', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(score_buckets, fontsize=9)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 40)
    ax2.yaxis.grid(True, alpha=0.3)

    # Formula annotation
    ax2.text(2, 35, 'Expected Loss = PD x LGD x EAD', fontsize=10,
            fontweight='bold', ha='center', style='italic',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    fig.suptitle('Credit Risk: Default Probability Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'default_probability_curve.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
