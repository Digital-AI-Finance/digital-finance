"""
Neobank Future Scenarios
Shows potential futures for the neobank industry

Output: neobank_future_scenarios.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank Future Scenarios',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/neobank_future_scenarios'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank future scenarios chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Four quadrant scenarios based on two dimensions
    # X-axis: Regulatory stance (permissive to restrictive)
    # Y-axis: Economic conditions (challenging to favorable)

    # Quadrant boxes
    scenarios = [
        {
            'name': 'Golden Age',
            'x': 9, 'y': 7.5,
            'color': '#44A044',
            'description': 'Supportive regulation +\nfavorable economy',
            'outcomes': ['Mass adoption', 'IPO wave', 'Global expansion',
                        'Traditional banks partner'],
            'probability': '25%'
        },
        {
            'name': 'Selective Winners',
            'x': 3.5, 'y': 7.5,
            'color': '#4A90E2',
            'description': 'Stricter regulation +\nfavorable economy',
            'outcomes': ['Consolidation', 'Licensed survivors',
                        'Quality over quantity', 'Bank acquisitions'],
            'probability': '35%'
        },
        {
            'name': 'Survival Mode',
            'x': 9, 'y': 2.5,
            'color': '#FF7F0E',
            'description': 'Supportive regulation +\nchallenging economy',
            'outcomes': ['Cost cutting', 'Niche focus', 'Credit losses',
                        'Delayed profitability'],
            'probability': '20%'
        },
        {
            'name': 'Shakeout',
            'x': 3.5, 'y': 2.5,
            'color': '#D62728',
            'description': 'Stricter regulation +\nchallenging economy',
            'outcomes': ['Many failures', 'Flight to safety',
                        'Regulatory burden', 'M&A at distress prices'],
            'probability': '20%'
        }
    ]

    for scenario in scenarios:
        # Box
        rect = mpatches.FancyBboxPatch((scenario['x']-2, scenario['y']-1.8), 4, 3.6,
                                        boxstyle='round,pad=0.05',
                                        facecolor=scenario['color'], alpha=0.15,
                                        edgecolor=scenario['color'], lw=2)
        ax.add_patch(rect)

        # Title
        ax.text(scenario['x'], scenario['y']+1.2, scenario['name'],
               fontsize=12, fontweight='bold', ha='center', color=scenario['color'])

        # Description
        ax.text(scenario['x'], scenario['y']+0.5, scenario['description'],
               fontsize=8, ha='center', style='italic', color='#666666')

        # Outcomes
        for i, outcome in enumerate(scenario['outcomes']):
            ax.text(scenario['x'], scenario['y']-0.2-i*0.35, f'* {outcome}',
                   fontsize=8, ha='center')

        # Probability
        prob_circle = mpatches.Circle((scenario['x']+1.7, scenario['y']+1.4), 0.35,
                                       facecolor=scenario['color'], edgecolor='white', lw=1)
        ax.add_patch(prob_circle)
        ax.text(scenario['x']+1.7, scenario['y']+1.4, scenario['probability'],
               fontsize=7, ha='center', va='center', color='white', fontweight='bold')

    # Axis labels
    ax.annotate('', xy=(12.5, 5), xytext=(0.5, 5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(6.5, 4.6, 'Regulatory Environment', fontsize=10, ha='center', fontweight='bold')
    ax.text(1.5, 5.3, 'Restrictive', fontsize=9, ha='center', color='#666666')
    ax.text(11.5, 5.3, 'Permissive', fontsize=9, ha='center', color='#666666')

    ax.annotate('', xy=(6.5, 9.5), xytext=(6.5, 0.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(6.2, 9, 'Favorable\nEconomy', fontsize=9, ha='right', color='#666666')
    ax.text(6.2, 1, 'Challenging\nEconomy', fontsize=9, ha='right', color='#666666')

    # Title
    ax.text(6.5, 9.8, 'Neobank Industry Future Scenarios (2025-2030)',
           fontsize=14, fontweight='bold', ha='center')

    # Note
    ax.text(12.5, 0.3, 'Probabilities are illustrative estimates',
           fontsize=7, ha='right', style='italic', color='#999999')

    # Source
    fig.text(0.5, 0.02, '[SCENARIO ANALYSIS - ILLUSTRATIVE]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'neobank_future_scenarios.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
