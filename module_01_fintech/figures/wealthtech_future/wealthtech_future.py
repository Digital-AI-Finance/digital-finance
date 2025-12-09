"""
WealthTech Future
Shows future trends in WealthTech

Output: wealthtech_future.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Future',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wealthtech_future'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create WealthTech future trends diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The Future of WealthTech', fontsize=20, fontweight='bold', ha='center')

    # Future trends
    trends = [
        {
            'name': 'AI Advisors',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'items': ['LLM chatbots', 'Personalized advice', 'Tax optimization'],
        },
        {
            'name': 'Embedded\nInvesting',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'items': ['Super apps', 'Payroll investing', 'Shopping rewards'],
        },
        {
            'name': 'Tokenized\nAssets',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'items': ['Real estate tokens', 'Art/collectibles', '24/7 trading'],
        },
        {
            'name': 'Hyper-\nPersonalization',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'items': ['Values-based', 'Tax situation', 'Life events'],
        },
        {
            'name': 'Financial\nWellness',
            'x': 4.75, 'y': 2.5,
            'color': '#D62728',
            'items': ['Holistic view', 'Debt + investing', 'Mental health'],
        },
        {
            'name': 'Global\nAccess',
            'x': 9.25, 'y': 2.5,
            'color': '#333333',
            'items': ['Cross-border', 'Emerging markets', 'Stablecoin rails'],
        },
    ]

    for trend in trends:
        box = mpatches.FancyBboxPatch((trend['x']-1.5, trend['y']-1.3), 3, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=trend['color'], alpha=0.15,
                                       edgecolor=trend['color'], lw=2)
        ax.add_patch(box)
        ax.text(trend['x'], trend['y']+1.1, trend['name'], ha='center',
               fontsize=12, fontweight='bold', color=trend['color'])

        for i, item in enumerate(trend['items']):
            ax.text(trend['x'], trend['y']+0.3-i*0.5, f'* {item}', ha='center', fontsize=10)

    # Vision
    vision = "Vision: Investing becomes invisible infrastructure woven into daily financial life"
    ax.text(7, 0.8, vision, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[FORWARD-LOOKING ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealthtech_future.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
