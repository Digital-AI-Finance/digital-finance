"""
Venture Funding Cycles
Shows FinTech venture funding cycles

Output: venture_funding_cycles.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Venture Funding Cycles',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/venture_funding_cycles'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create venture funding cycles chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    seed_early = [8, 7, 15, 12, 8, 7]  # USD B
    late_stage = [44, 38, 117, 73, 44, 51]  # USD B

    x = np.arange(len(years))
    width = 0.35

    bars1 = ax.bar(x - width/2, seed_early, width, label='Seed/Early Stage',
                   color='#44A044', edgecolor='#333333', lw=1.5)
    bars2 = ax.bar(x + width/2, late_stage, width, label='Late Stage',
                   color='#4A90E2', edgecolor='#333333', lw=1.5)

    ax.set_ylabel('Funding (USD B)', fontsize=14)
    ax.set_title('FinTech Venture Funding by Stage', fontsize=20, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=12)
    ax.legend(fontsize=12)
    ax.set_ylim(0, 140)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # 2021 peak annotation
    ax.annotate('2021 Peak:\nZero rates, stimulus,\ndigital acceleration',
               xy=(2, 117), xytext=(3.5, 125),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='#666666'))

    # Current state annotation
    ax.text(0.98, 0.25, '2024: Reset to sustainable levels\nFocus on fundamentals',
           transform=ax.transAxes, fontsize=11, ha='right',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CB Insights, PitchBook FinTech data (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'venture_funding_cycles.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
