"""
Vanguard Hybrid Advisory
Shows Vanguard's hybrid digital/human model

Output: vanguard_hybrid.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Vanguard Hybrid Advisory',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/vanguard_hybrid'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Vanguard hybrid advisory diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Vanguard: Largest Hybrid Robo-Advisor', fontsize=20, fontweight='bold', ha='center')

    # Tiers
    tiers = [
        {
            'name': 'Digital Advisor',
            'x': 2.2, 'y': 6,
            'color': '#4A90E2',
            'min': '$3,000',
            'fee': '0.20%',
            'features': ['All-digital', 'Automated investing', 'Goal tracking'],
        },
        {
            'name': 'Personal Advisor',
            'x': 7, 'y': 6,
            'color': '#44A044',
            'min': '$50,000',
            'fee': '0.30%',
            'features': ['CFP access', 'Video meetings', 'Full planning'],
        },
        {
            'name': 'Wealth Management',
            'x': 11.8, 'y': 6,
            'color': '#FF7F0E',
            'min': '$5M+',
            'fee': '0.30%',
            'features': ['Dedicated team', 'Tax/estate planning', 'Alternative investments'],
        },
    ]

    for tier in tiers:
        # Box
        box = mpatches.FancyBboxPatch((tier['x']-1.8, tier['y']-2.5), 3.6, 5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=tier['color'], alpha=0.2,
                                       edgecolor=tier['color'], lw=2)
        ax.add_patch(box)
        ax.text(tier['x'], tier['y']+2, tier['name'], ha='center',
               fontsize=13, fontweight='bold', color=tier['color'])
        ax.text(tier['x'], tier['y']+1.3, f"Min: {tier['min']}", ha='center', fontsize=11)
        ax.text(tier['x'], tier['y']+0.7, f"Fee: {tier['fee']}", ha='center', fontsize=12, fontweight='bold')

        for i, feature in enumerate(tier['features']):
            ax.text(tier['x'], tier['y']-0.2-i*0.5, f'* {feature}', ha='center', fontsize=10)

    # Market position
    position = """Vanguard Advisory (2024):
    - $350B+ AUM (largest robo-hybrid)
    - 2M+ clients
    - 89% revenue from advisory fees
    - Market leader in low-cost advisory"""

    ax.text(7, 1.8, position, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Vanguard 2024 annual report, company website',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'vanguard_hybrid.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
