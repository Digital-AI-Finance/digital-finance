"""
WealthTech Demographics
Shows demographic breakdown of WealthTech users

Output: wealthtech_demographics.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Demographics',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wealthtech_demographics'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create WealthTech demographics chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Chart 1: Age distribution
    ax1 = axes[0]
    ages = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    traditional = [5, 15, 22, 25, 20, 13]
    wealthtech = [22, 35, 23, 12, 6, 2]

    x = np.arange(len(ages))
    width = 0.35

    bars1 = ax1.bar(x - width/2, traditional, width, label='Traditional Advisory',
                    color='#4A90E2', edgecolor='#333333', lw=1.5)
    bars2 = ax1.bar(x + width/2, wealthtech, width, label='WealthTech Apps',
                    color='#44A044', edgecolor='#333333', lw=1.5)

    ax1.set_ylabel('User Share (%)', fontsize=14)
    ax1.set_title('Age Distribution', fontsize=17, fontweight='bold', pad=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(ages, fontsize=11)
    ax1.legend(fontsize=11)
    ax1.set_ylim(0, 45)
    ax1.yaxis.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Chart 2: First-time investors
    ax2 = axes[1]
    categories = ['Robinhood', 'Acorns', 'Stash', 'Betterment', 'Traditional']
    first_time_pct = [50, 68, 72, 35, 8]
    colors = ['#44A044', '#FF7F0E', '#6B5B95', '#4A90E2', '#D62728']

    bars = ax2.barh(categories, first_time_pct, color=colors, edgecolor='#333333', lw=1.5)
    ax2.set_xlabel('First-Time Investors (%)', fontsize=14)
    ax2.set_title('First-Time Investor Share', fontsize=17, fontweight='bold', pad=10)
    ax2.set_xlim(0, 100)
    ax2.xaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, first_time_pct):
        ax2.annotate(f'{val}%',
                    xy=(bar.get_width(), bar.get_y() + bar.get_height()/2),
                    xytext=(5, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=12, fontweight='bold')

    # Source
    fig.text(0.5, 0.02, 'Source: JD Power, Schwab RIA study, company reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'wealthtech_demographics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
