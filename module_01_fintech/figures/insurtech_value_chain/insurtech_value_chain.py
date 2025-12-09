"""
InsurTech Value Chain
Shows where InsurTech disrupts the insurance value chain

Output: insurtech_value_chain.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'InsurTech Value Chain',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/insurtech_value_chain'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create insurtech value chain diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'InsurTech Disruption Across the Value Chain', fontsize=20, fontweight='bold', ha='center')

    # Value chain stages
    stages = [
        {'name': 'Product\nDesign', 'x': 1.5, 'color': '#4A90E2',
         'traditional': 'Standard products', 'insurtech': 'On-demand, usage-based'},
        {'name': 'Distribution', 'x': 4, 'color': '#44A044',
         'traditional': 'Agents, brokers', 'insurtech': 'Digital, embedded'},
        {'name': 'Underwriting', 'x': 6.5, 'color': '#FF7F0E',
         'traditional': 'Manual assessment', 'insurtech': 'AI/ML automated'},
        {'name': 'Policy Admin', 'x': 9, 'color': '#6B5B95',
         'traditional': 'Legacy systems', 'insurtech': 'Cloud, APIs'},
        {'name': 'Claims', 'x': 11.5, 'color': '#D62728',
         'traditional': 'Manual processing', 'insurtech': 'AI instant payout'},
    ]

    # Draw flow arrows
    for i in range(len(stages)-1):
        ax.annotate('', xy=(stages[i+1]['x']-0.8, 6), xytext=(stages[i]['x']+0.8, 6),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    for stage in stages:
        # Stage box
        box = mpatches.FancyBboxPatch((stage['x']-1, 5), 2, 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=stage['color'], alpha=0.2,
                                       edgecolor=stage['color'], lw=2)
        ax.add_patch(box)
        ax.text(stage['x'], 6.5, stage['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=stage['color'])

        # Traditional approach
        ax.text(stage['x'], 4.3, 'Traditional:', ha='center', fontsize=10, fontweight='bold', color='#666666')
        ax.text(stage['x'], 3.8, stage['traditional'], ha='center', fontsize=11)

        # InsurTech approach
        ax.text(stage['x'], 2.8, 'InsurTech:', ha='center', fontsize=10, fontweight='bold', color='#44A044')
        ax.text(stage['x'], 2.3, stage['insurtech'], ha='center', fontsize=11, color='#44A044')

    # Key insight
    insight = "InsurTech Impact: 40% cost reduction potential, 70% faster claims, 3x customer satisfaction"
    ax.text(7, 1.2, insight, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: McKinsey Insurance Practice (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'insurtech_value_chain.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
