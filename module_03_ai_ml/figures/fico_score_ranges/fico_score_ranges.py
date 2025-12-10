"""
FICO Score Ranges and Lending Criteria
Score thresholds for different loan products

Output: fico_score_ranges.pdf
Module: module_03_ai_ml
Lesson: 30 - Credit Scoring
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'FICO Score Ranges',
    'module': 'module_03_ai_ml',
    'lesson': 30,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/fico_score_ranges'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))

    # Score ranges
    ranges = [
        ('Excellent', 800, 850, '#44A044'),
        ('Very Good', 740, 799, '#90EE90'),
        ('Good', 670, 739, '#FFD700'),
        ('Fair', 580, 669, '#FF7F0E'),
        ('Poor', 300, 579, '#D62728')
    ]

    # Loan products and their typical minimum scores
    products = [
        ('Prime Mortgage', 760, '#4A90E2'),
        ('Conventional Mortgage', 680, '#5A9AE8'),
        ('FHA Loan', 580, '#6AAAF0'),
        ('Auto Loan (Best Rate)', 720, '#7ABAF8'),
        ('Auto Loan (Available)', 600, '#8ACAFF'),
        ('Personal Loan', 640, '#9ADAFF'),
        ('Credit Card (Premium)', 750, '#AAEAFF'),
        ('Credit Card (Standard)', 670, '#BBFAFF'),
        ('Credit Card (Secured)', 500, '#CCFFFF'),
    ]

    # Draw score range bars
    bar_height = 0.15
    for i, (label, low, high, color) in enumerate(ranges):
        ax.barh(y=0.5, width=high-low, left=low, height=bar_height,
                color=color, alpha=0.7, edgecolor='black')
        ax.text((low + high) / 2, 0.5, f'{label}\n{low}-{high}',
                ha='center', va='center', fontsize=8, fontweight='bold')

    # Draw product thresholds
    y_positions = np.linspace(0.7, 1.3, len(products))
    for i, (product, min_score, color) in enumerate(products):
        ax.plot([min_score, 850], [y_positions[i], y_positions[i]],
                color=color, linewidth=8, alpha=0.6, solid_capstyle='round')
        ax.plot([min_score], [y_positions[i]], 'ko', markersize=8)
        ax.text(min_score - 5, y_positions[i], f'{product} (min: {min_score})',
                ha='right', va='center', fontsize=9)

    # Add interest rate impact
    ax.text(820, 1.4, 'Higher Scores =\nLower Interest Rates', fontsize=10,
            ha='center', va='bottom', fontweight='bold', color='#44A044')
    ax.text(450, 1.4, 'Lower Scores =\nLimited Options', fontsize=10,
            ha='center', va='bottom', fontweight='bold', color='#D62728')

    ax.set_xlim(250, 880)
    ax.set_ylim(0.3, 1.5)
    ax.set_xlabel('FICO Credit Score', fontsize=12)
    ax.set_title('Credit Score Requirements by Loan Product', fontsize=14, fontweight='bold', pad=15)

    # Remove y-axis
    ax.yaxis.set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add score scale
    for score in [300, 400, 500, 580, 670, 740, 800, 850]:
        ax.axvline(x=score, color='gray', linestyle=':', alpha=0.3)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'fico_score_ranges.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
