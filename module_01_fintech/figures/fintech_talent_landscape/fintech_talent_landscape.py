"""
FinTech Talent Landscape
Shows FinTech talent and hiring trends

Output: fintech_talent_landscape.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Talent Landscape',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_talent_landscape'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech talent landscape diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'FinTech Talent Landscape', fontsize=20, fontweight='bold', ha='center')

    # In-demand roles
    roles = [
        {
            'name': 'Engineering',
            'x': 2.5, 'y': 6.5,
            'color': '#4A90E2',
            'skills': ['Full-stack', 'Cloud/DevOps', 'API development', 'Security']
        },
        {
            'name': 'Data/AI',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'skills': ['ML engineers', 'Data scientists', 'Risk modelers', 'Analytics']
        },
        {
            'name': 'Product',
            'x': 11.5, 'y': 6.5,
            'color': '#FF7F0E',
            'skills': ['Product managers', 'UX designers', 'Growth hackers', 'Strategy']
        },
        {
            'name': 'Compliance',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'skills': ['BSA/AML', 'Risk managers', 'Regulatory experts', 'Legal']
        },
        {
            'name': 'Operations',
            'x': 9.25, 'y': 2.5,
            'color': '#D62728',
            'skills': ['Ops managers', 'Customer success', 'Partner managers', 'Finance']
        },
    ]

    for role in roles:
        box = mpatches.FancyBboxPatch((role['x']-1.8, role['y']-1.5), 3.6, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=role['color'], alpha=0.15,
                                       edgecolor=role['color'], lw=2)
        ax.add_patch(box)
        ax.text(role['x'], role['y']+1.2, role['name'], ha='center',
               fontsize=13, fontweight='bold', color=role['color'])

        for i, skill in enumerate(role['skills']):
            ax.text(role['x'], role['y']+0.4-i*0.5, f'* {skill}', ha='center', fontsize=10)

    # 2024 trend
    trend = "2024 Trend: Layoffs at growth-stage, hiring at profitable fintechs | AI skills premium"
    ax.text(7, 0.8, trend, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: LinkedIn, Glassdoor FinTech hiring data (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_talent_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
