"""
Credit Score Distribution
Distribution of FICO scores in population

Output: credit_score_distribution.pdf
Module: module_03_ai_ml
Lesson: 30 - Credit Scoring
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Credit Score Distribution',
    'module': 'module_03_ai_ml',
    'lesson': 30,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/credit_score_distribution'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Score distribution
    ax1 = axes[0]
    # Generate bimodal distribution (good and bad borrowers)
    scores_good = np.random.normal(720, 50, 7000)
    scores_bad = np.random.normal(580, 60, 3000)
    all_scores = np.concatenate([scores_good, scores_bad])
    all_scores = np.clip(all_scores, 300, 850)

    # Define score ranges
    ranges = [(300, 580, 'Poor', '#D62728'),
              (580, 670, 'Fair', '#FF7F0E'),
              (670, 740, 'Good', '#FFD700'),
              (740, 800, 'Very Good', '#90EE90'),
              (800, 850, 'Excellent', '#44A044')]

    bins = np.arange(300, 860, 10)
    n, bins_out, patches = ax1.hist(all_scores, bins=bins, edgecolor='white', alpha=0.8)

    # Color bars by range
    for patch, left_edge in zip(patches, bins[:-1]):
        for low, high, _, color in ranges:
            if low <= left_edge < high:
                patch.set_facecolor(color)
                break

    # Add range labels
    for low, high, label, color in ranges:
        mid = (low + high) / 2
        ax1.axvline(x=low, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
        ax1.text(mid, ax1.get_ylim()[1] * 0.95, label, ha='center', fontsize=8,
                fontweight='bold', color=color)

    ax1.set_xlabel('Credit Score', fontsize=11)
    ax1.set_ylabel('Number of Borrowers', fontsize=11)
    ax1.set_title('Credit Score Distribution in Population', fontsize=12, fontweight='bold')
    ax1.set_xlim(300, 850)

    # Default rates by score range
    ax2 = axes[1]
    score_ranges = ['300-579\n(Poor)', '580-669\n(Fair)', '670-739\n(Good)',
                   '740-799\n(Very Good)', '800-850\n(Excellent)']
    default_rates = [28.5, 12.3, 5.2, 1.8, 0.6]
    colors = ['#D62728', '#FF7F0E', '#FFD700', '#90EE90', '#44A044']

    bars = ax2.bar(score_ranges, default_rates, color=colors, edgecolor='black', alpha=0.8)

    for bar, rate in zip(bars, default_rates):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{rate}%', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlabel('Credit Score Range', fontsize=11)
    ax2.set_ylabel('Default Rate (%)', fontsize=11)
    ax2.set_title('Default Rate by Credit Score Range', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 35)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Credit Score Analysis: Risk Assessment', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'credit_score_distribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
