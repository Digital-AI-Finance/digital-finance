"""
Gamification Concerns
Shows concerns about gamification in trading apps

Output: gamification_concerns.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Gamification Concerns',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/gamification_concerns'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create gamification concerns diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Gamification in Trading Apps: Concerns', fontsize=20, fontweight='bold', ha='center')

    # Gamification elements
    ax.text(3.5, 8.2, 'Gamification Elements', fontsize=15, fontweight='bold', ha='center', color='#4A90E2')
    elements = ['Confetti animations', 'Leaderboards', 'Streaks & badges', 'Push notifications', 'Social features']
    for i, elem in enumerate(elements):
        ax.text(3.5, 7.5-i*0.6, f'* {elem}', ha='center', fontsize=11)

    # Concerns
    ax.text(10.5, 8.2, 'Regulatory Concerns', fontsize=15, fontweight='bold', ha='center', color='#D62728')
    concerns = ['Encourages overtrading', 'Targets inexperienced', 'Gambling-like behavior', 'FOMO exploitation', 'Information asymmetry']
    for i, concern in enumerate(concerns):
        ax.text(10.5, 7.5-i*0.6, f'* {concern}', ha='center', fontsize=11, color='#D62728')

    # Research findings
    findings = """Research Findings:
    - Robinhood users trade 40x more than Schwab users
    - Average Robinhood account: USD 240 (2020)
    - 50% of users trade options (vs 10% industry avg)
    - Higher losses among gamified app users"""

    ax.text(4, 3, findings, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFEBEB', edgecolor='#D62728'))

    # Regulatory response
    response = """Regulatory Response:
    - SEC requesting info on gamification
    - FINRA guidance on digital engagement
    - Massachusetts lawsuit vs Robinhood
    - UK FCA scrutiny of trading apps
    - EU MiFID II suitability rules"""

    ax.text(10, 3, response, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Balance note
    balance = "Challenge: Balance innovation & engagement with investor protection"
    ax.text(7, 0.8, balance, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: SEC Request for Information, FINRA guidance, academic studies (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'gamification_concerns.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
