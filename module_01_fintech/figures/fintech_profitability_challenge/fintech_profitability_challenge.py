"""
FinTech Profitability Challenge
Shows FinTech path to profitability

Output: fintech_profitability_challenge.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Profitability Challenge',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_profitability_challenge'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech profitability challenge diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The FinTech Profitability Challenge', fontsize=20, fontweight='bold', ha='center')

    # Problem areas
    problems = [
        {
            'name': 'High CAC',
            'x': 2.2, 'y': 6.5,
            'color': '#D62728',
            'issues': ['USD 100-300 per customer', 'Expensive marketing', 'Low switching costs'],
        },
        {
            'name': 'Low ARPU',
            'x': 5.5, 'y': 6.5,
            'color': '#FF7F0E',
            'issues': ['Free services', 'Thin interchange', 'Price-sensitive users'],
        },
        {
            'name': 'Compliance\nCosts',
            'x': 8.5, 'y': 6.5,
            'color': '#6B5B95',
            'issues': ['AML/KYC overhead', 'State-by-state regs', 'Partner bank fees'],
        },
        {
            'name': 'Competition',
            'x': 11.8, 'y': 6.5,
            'color': '#333333',
            'issues': ['Race to zero fees', 'Feature parity', 'Big Tech entry'],
        },
    ]

    for prob in problems:
        box = mpatches.FancyBboxPatch((prob['x']-1.5, prob['y']-1.3), 3, 2.7,
                                       boxstyle='round,pad=0.1',
                                       facecolor=prob['color'], alpha=0.15,
                                       edgecolor=prob['color'], lw=2)
        ax.add_patch(box)
        ax.text(prob['x'], prob['y']+1, prob['name'], ha='center',
               fontsize=12, fontweight='bold', color=prob['color'])

        for i, issue in enumerate(prob['issues']):
            ax.text(prob['x'], prob['y']+0.3-i*0.5, f'* {issue}', ha='center', fontsize=10)

    # Paths to profitability
    paths = """Paths to Profitability:
    1. Premium/subscription tiers (Robinhood Gold, Acorns)
    2. B2B pivot (enterprise, BaaS licensing)
    3. Interest income (deposits, lending)
    4. Cross-selling (insurance, investing, credit)
    5. Operational efficiency (AI, automation)"""

    ax.text(7, 2.5, paths, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Note
    note = "2024 Shift: Investors demand path to profitability, not just growth"
    ax.text(7, 0.8, note, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, '[INDUSTRY ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_profitability_challenge.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
