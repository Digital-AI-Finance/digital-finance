"""
Robo-Advisor Challenges
Shows key challenges facing robo-advisory industry

Output: robo_challenges.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Robo-Advisor Challenges',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_challenges'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create robo challenges diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Robo-Advisor Industry Challenges', fontsize=20, fontweight='bold', ha='center')

    # Challenges
    challenges = [
        {
            'name': 'Unit Economics',
            'x': 2.2, 'y': 6.5,
            'color': '#D62728',
            'issues': ['Low fees = thin margins', 'High CAC ($150-300)', 'Small accounts unprofitable'],
        },
        {
            'name': 'Market Volatility',
            'x': 7, 'y': 6.5,
            'color': '#FF7F0E',
            'issues': ['Client panic in downturns', 'Algorithm trust tested', 'Behavioral coaching gap'],
        },
        {
            'name': 'Competition',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'issues': ['Incumbents copying', 'Race to zero fees', 'Feature commoditization'],
        },
        {
            'name': 'Differentiation',
            'x': 2.2, 'y': 2.5,
            'color': '#4A90E2',
            'issues': ['Similar portfolios', 'Limited personalization', 'Generic experience'],
        },
        {
            'name': 'Regulation',
            'x': 7, 'y': 2.5,
            'color': '#44A044',
            'issues': ['Fiduciary requirements', 'Algorithm audits', 'Cross-border complexity'],
        },
        {
            'name': 'Customer Retention',
            'x': 11.8, 'y': 2.5,
            'color': '#333333',
            'issues': ['Easy to switch', 'Low engagement', 'Churn in bull markets'],
        },
    ]

    for challenge in challenges:
        # Box
        box = mpatches.FancyBboxPatch((challenge['x']-1.8, challenge['y']-1.3), 3.6, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=challenge['color'], alpha=0.15,
                                       edgecolor=challenge['color'], lw=2)
        ax.add_patch(box)
        ax.text(challenge['x'], challenge['y']+1.1, challenge['name'], ha='center',
               fontsize=12, fontweight='bold', color=challenge['color'])

        for i, issue in enumerate(challenge['issues']):
            ax.text(challenge['x'], challenge['y']+0.3-i*0.5, f'* {issue}', ha='center', fontsize=10)

    # Source
    fig.text(0.5, 0.02, '[INDUSTRY ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_challenges.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
