"""
FinTech 2030 Vision
Shows future vision for FinTech in 2030

Output: fintech_2030_vision.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'FinTech 2030 Vision',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_2030_vision'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech 2030 vision diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'FinTech 2030: A Vision', fontsize=20, fontweight='bold', ha='center')

    # Future themes
    themes = [
        {
            'name': 'Invisible\nFinance',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'desc': 'Embedded everywhere\nSeamless, contextual'
        },
        {
            'name': 'AI\nFirst',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'desc': 'LLM advisors\nHyper-personalization'
        },
        {
            'name': 'Token\nEconomy',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'desc': 'Asset tokenization\nProgrammable money'
        },
        {
            'name': 'Global\nAccess',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'desc': 'Financial inclusion\nCross-border instant'
        },
        {
            'name': 'Regulatory\nTech',
            'x': 4.75, 'y': 2.5,
            'color': '#D62728',
            'desc': 'Machine-readable regs\nReal-time compliance'
        },
        {
            'name': 'Sustainable\nFinance',
            'x': 9.25, 'y': 2.5,
            'color': '#17BECF',
            'desc': 'ESG integration\nCarbon tracking'
        },
    ]

    for theme in themes:
        box = mpatches.FancyBboxPatch((theme['x']-1.5, theme['y']-1.2), 3, 2.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=theme['color'], alpha=0.15,
                                       edgecolor=theme['color'], lw=2)
        ax.add_patch(box)
        ax.text(theme['x'], theme['y']+0.9, theme['name'], ha='center',
               fontsize=12, fontweight='bold', color=theme['color'])
        ax.text(theme['x'], theme['y']-0.1, theme['desc'], ha='center', fontsize=10)

    # Vision statement
    vision = "2030 Vision: Finance becomes infrastructure - invisible, instant, intelligent, inclusive"
    ax.text(7, 0.8, vision, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[FORWARD-LOOKING VISION]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fintech_2030_vision.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
