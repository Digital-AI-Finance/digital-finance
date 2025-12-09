"""
Default Rates by Grade
Shows cumulative default rates by risk grade over time

Output: default_rate_by_grade.pdf
Module: module_01_fintech
Lesson: 7 - P2P Lending
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Default Rates by Grade',
    'module': 'module_01_fintech',
    'lesson': 7,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/default_rate_by_grade'
}

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
})

def create_chart():
    """Create default rate by grade chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Months since origination
    months = np.array([0, 6, 12, 18, 24, 30, 36])

    # Cumulative default rates by grade (typical 3-year loan)
    grade_a = [0, 0.3, 0.8, 1.5, 2.2, 2.8, 3.2]
    grade_b = [0, 0.6, 1.5, 3.0, 4.5, 5.5, 6.2]
    grade_c = [0, 1.0, 3.0, 6.0, 9.0, 11.0, 12.5]
    grade_d = [0, 1.5, 5.0, 10.0, 14.0, 17.0, 19.0]
    grade_e = [0, 2.0, 7.0, 14.0, 20.0, 25.0, 28.0]

    ax.plot(months, grade_a, 'o-', label='Grade A', color='#44A044', lw=2, markersize=7)
    ax.plot(months, grade_b, 's-', label='Grade B', color='#4A90E2', lw=2, markersize=7)
    ax.plot(months, grade_c, '^-', label='Grade C', color='#FF7F0E', lw=2, markersize=7)
    ax.plot(months, grade_d, 'D-', label='Grade D', color='#D62728', lw=2, markersize=7)
    ax.plot(months, grade_e, 'v-', label='Grade E', color='#6B5B95', lw=2, markersize=7)

    ax.set_xlabel('Months Since Origination', fontsize=12)
    ax.set_ylabel('Cumulative Default Rate (%)', fontsize=12)
    ax.set_title('Cumulative Default Rates by Risk Grade', fontsize=17, fontweight='bold', pad=15)

    ax.legend(loc='upper left', fontsize=10)
    ax.set_xlim(-1, 38)
    ax.set_ylim(0, 32)

    ax.yaxis.grid(True, alpha=0.3)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Annotation
    ax.annotate('Most defaults occur\nin first 18 months', xy=(18, 14), xytext=(25, 10),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#333333'),
               bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: LendingClub historical vintage analysis [ILLUSTRATIVE]',
            fontsize=9, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'default_rate_by_grade.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
