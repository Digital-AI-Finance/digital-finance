"""
Robo-Advisor Onboarding Flow
Shows the typical robo-advisor onboarding process

Output: robo_onboarding.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Robo Onboarding Flow',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_onboarding'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create robo onboarding flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Robo-Advisor Onboarding Flow', fontsize=20, fontweight='bold', ha='center')

    # Steps
    steps = [
        {'name': 'Sign Up', 'x': 2, 'y': 6.5, 'color': '#4A90E2',
         'desc': 'Email, password\nbasic info'},
        {'name': 'Goals', 'x': 5, 'y': 6.5, 'color': '#44A044',
         'desc': 'Retirement,\nsavings, etc.'},
        {'name': 'Risk\nProfile', 'x': 8, 'y': 6.5, 'color': '#FF7F0E',
         'desc': 'Questionnaire\n(5-10 questions)'},
        {'name': 'Portfolio', 'x': 11, 'y': 6.5, 'color': '#6B5B95',
         'desc': 'Auto-allocated\nbased on profile'},
    ]

    for step in steps:
        # Circle
        circle = mpatches.Circle((step['x'], step['y']), 1.2, facecolor=step['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)
        ax.text(step['x'], step['y'], step['name'], ha='center', va='center',
               fontsize=12, fontweight='bold', color='white')
        ax.text(step['x'], step['y']-2, step['desc'], ha='center', fontsize=11)

    # Arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-1.3, steps[i+1]['y']),
                   xytext=(steps[i]['x']+1.3, steps[i]['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Second row - post onboarding
    post_steps = [
        {'name': 'Fund\nAccount', 'x': 3.5, 'y': 2.5, 'color': '#333333',
         'desc': 'Bank link, deposit'},
        {'name': 'Auto\nInvest', 'x': 7, 'y': 2.5, 'color': '#333333',
         'desc': 'Recurring deposits'},
        {'name': 'Monitor &\nRebalance', 'x': 10.5, 'y': 2.5, 'color': '#333333',
         'desc': 'Ongoing management'},
    ]

    for step in post_steps:
        box = mpatches.FancyBboxPatch((step['x']-1.3, step['y']-0.6), 2.6, 1.4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.15,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+0.2, step['name'], ha='center', fontsize=11, fontweight='bold')
        ax.text(step['x'], step['y']-0.6, step['desc'], ha='center', fontsize=10, color='#666666')

    # Arrows for second row
    for i in range(len(post_steps)-1):
        ax.annotate('', xy=(post_steps[i+1]['x']-1.4, post_steps[i+1]['y']),
                   xytext=(post_steps[i]['x']+1.4, post_steps[i]['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=1.5))

    # Time note
    ax.text(7, 0.6, 'Typical onboarding: 5-10 minutes | Account funded in 1-3 days',
           ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL FLOW]', fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_onboarding.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
