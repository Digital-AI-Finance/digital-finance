"""
Incumbent Banks Digital Investment
Shows how traditional banks are responding to neobank competition

Output: incumbent_digital_investment.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Incumbent Bank Digital Investment',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/incumbent_digital_investment'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create incumbent bank digital investment chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Technology spending by major banks ($ billions)
    banks = ['JPMorgan', 'Bank of\nAmerica', 'Wells\nFargo', 'Citi', 'Goldman\nSachs']
    # Based on annual report disclosures 2023
    tech_spend_2023 = [15.3, 12.0, 9.0, 8.5, 5.0]
    tech_spend_2020 = [12.0, 10.0, 7.5, 7.0, 4.0]

    x = np.arange(len(banks))
    width = 0.35

    bars1 = ax1.bar(x - width/2, tech_spend_2020, width, label='2020', color='#999999')
    bars2 = ax1.bar(x + width/2, tech_spend_2023, width, label='2023', color='#4A90E2')

    ax1.set_ylabel('Technology Spending ($ Billions)', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(banks, fontsize=9)
    ax1.set_ylim(0, 18)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_title('Major Bank Tech Spending', fontsize=12, fontweight='bold', pad=10)

    # Value labels
    for bar in bars2:
        height = bar.get_height()
        ax1.annotate(f'${height:.1f}B',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax1.yaxis.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Right: Digital response strategies
    ax2.axis('off')

    strategies = [
        {
            'name': 'Build Own Digital Bank',
            'examples': 'Marcus (Goldman), Zelle, Chase Digital',
            'approach': 'Create separate digital brand',
            'color': '#4A90E2',
            'y': 7.5
        },
        {
            'name': 'Acquire FinTech',
            'examples': 'Visa-Plaid*, JPM-WePay, Goldman-GreenSky',
            'approach': 'Buy innovation and talent',
            'color': '#44A044',
            'y': 5.5
        },
        {
            'name': 'Partner/Invest',
            'examples': 'Strategic VC arms, accelerators',
            'approach': 'Monitor and collaborate',
            'color': '#FF7F0E',
            'y': 3.5
        },
        {
            'name': 'Modernize Core',
            'examples': 'Cloud migration, API platforms',
            'approach': 'Transform from within',
            'color': '#6B5B95',
            'y': 1.5
        }
    ]

    for strat in strategies:
        # Strategy box
        rect = mpatches.FancyBboxPatch((0.5, strat['y']-0.6), 9, 1.5,
                                        boxstyle='round,pad=0.05',
                                        facecolor=strat['color'], alpha=0.2,
                                        edgecolor=strat['color'], lw=2)
        ax2.add_patch(rect)

        ax2.text(0.7, strat['y']+0.4, strat['name'], fontsize=10, fontweight='bold',
                color=strat['color'])
        ax2.text(0.7, strat['y'], strat['approach'], fontsize=9, style='italic')
        ax2.text(0.7, strat['y']-0.35, f"Examples: {strat['examples']}", fontsize=8,
                color='#666666')

    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 9)
    ax2.set_title('Incumbent Response Strategies', fontsize=12, fontweight='bold', pad=10)

    # Note about Plaid deal
    ax2.text(5, 0.3, '*Visa-Plaid deal terminated (antitrust)', fontsize=7,
            style='italic', color='#999999', ha='center')

    # Main title
    fig.suptitle('How Incumbent Banks Respond to Neobank Competition',
                fontsize=14, fontweight='bold', y=1.02)

    # Source
    fig.text(0.5, 0.02, 'Source: Bank annual reports (2023), press releases',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'incumbent_digital_investment.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
