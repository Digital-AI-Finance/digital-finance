"""
Social Trading Platform
Shows social trading concept and features

Output: social_trading_platform.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Social Trading Platform',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/social_trading_platform'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create social trading platform diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Social Trading: Learning from the Crowd', fontsize=20, fontweight='bold', ha='center')

    # Central platform
    platform_box = mpatches.FancyBboxPatch((5, 4.5), 4, 3,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#4A90E2', alpha=0.2,
                                            edgecolor='#4A90E2', lw=3)
    ax.add_patch(platform_box)
    ax.text(7, 6.5, 'Social Trading', ha='center', fontsize=16, fontweight='bold', color='#4A90E2')
    ax.text(7, 5.9, 'Platform', ha='center', fontsize=16, fontweight='bold', color='#4A90E2')
    ax.text(7, 5.2, '(eToro, Public)', ha='center', fontsize=12, style='italic')

    # Features around platform
    features = [
        {'name': 'Feed & Posts', 'x': 2, 'y': 8, 'color': '#44A044',
         'desc': 'See what others\nare trading'},
        {'name': 'Copy Trading', 'x': 12, 'y': 8, 'color': '#FF7F0E',
         'desc': 'Auto-replicate\nexpert portfolios'},
        {'name': 'Leaderboards', 'x': 2, 'y': 2, 'color': '#6B5B95',
         'desc': 'Track top\nperformers'},
        {'name': 'Discussion', 'x': 12, 'y': 2, 'color': '#D62728',
         'desc': 'Stock-specific\nconversations'},
    ]

    for feat in features:
        box = mpatches.FancyBboxPatch((feat['x']-1.3, feat['y']-0.8), 2.6, 1.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=feat['color'], alpha=0.2,
                                       edgecolor=feat['color'], lw=2)
        ax.add_patch(box)
        ax.text(feat['x'], feat['y']+0.5, feat['name'], ha='center',
               fontsize=12, fontweight='bold', color=feat['color'])
        ax.text(feat['x'], feat['y']-0.2, feat['desc'], ha='center', fontsize=10)

        # Arrow to center
        dx = 7 - feat['x']
        dy = 6 - feat['y']
        ax.annotate('', xy=(7 - dx*0.4, 6 - dy*0.3),
                   xytext=(feat['x'] + dx*0.3, feat['y'] + dy*0.2),
                   arrowprops=dict(arrowstyle='<->', color='#999999', lw=1.5))

    # Benefits and risks
    ax.text(7, 3.5, 'Benefits: Learn from experts, community insights, reduce isolation',
           ha='center', fontsize=11, color='#44A044')
    ax.text(7, 3, 'Risks: Herding behavior, FOMO trading, unsuitable copying',
           ha='center', fontsize=11, color='#D62728')

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL DIAGRAM]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'social_trading_platform.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
