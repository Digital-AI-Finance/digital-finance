"""
Robo-Advisor vs Traditional Advisor
Compares robo-advisors with traditional financial advisors

Output: robo_vs_traditional.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Robo vs Traditional Advisor',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_vs_traditional'
}

# 40% larger fonts
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create robo vs traditional comparison diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Robo-Advisor vs Traditional Advisor', fontsize=20, fontweight='bold', ha='center')

    # Traditional Advisor (left)
    trad_box = mpatches.FancyBboxPatch((0.5, 3), 6, 5.5, boxstyle='round,pad=0.1',
                                        facecolor='#4A90E2', alpha=0.2,
                                        edgecolor='#4A90E2', lw=2)
    ax.add_patch(trad_box)
    ax.text(3.5, 8, 'Traditional Advisor', ha='center', fontsize=17, fontweight='bold', color='#4A90E2')

    trad_features = [
        ('Fees', '1-2% AUM + commissions'),
        ('Minimum', '$100K-$1M+'),
        ('Service', 'Human relationship'),
        ('Planning', 'Holistic financial plan'),
        ('Access', 'Office hours, calls'),
    ]
    for i, (feat, desc) in enumerate(trad_features):
        ax.text(0.8, 7.2-i*0.9, f'{feat}:', fontsize=12, fontweight='bold')
        ax.text(2.5, 7.2-i*0.9, desc, fontsize=12)

    # Robo-Advisor (right)
    robo_box = mpatches.FancyBboxPatch((7.5, 3), 6, 5.5, boxstyle='round,pad=0.1',
                                        facecolor='#44A044', alpha=0.2,
                                        edgecolor='#44A044', lw=2)
    ax.add_patch(robo_box)
    ax.text(10.5, 8, 'Robo-Advisor', ha='center', fontsize=17, fontweight='bold', color='#44A044')

    robo_features = [
        ('Fees', '0.25-0.50% AUM'),
        ('Minimum', '$0-$500'),
        ('Service', 'Algorithm-driven'),
        ('Planning', 'Goal-based portfolios'),
        ('Access', '24/7 app/web'),
    ]
    for i, (feat, desc) in enumerate(robo_features):
        ax.text(7.8, 7.2-i*0.9, f'{feat}:', fontsize=12, fontweight='bold')
        ax.text(9.5, 7.2-i*0.9, desc, fontsize=12)

    # Key insight
    insight = "Key Insight: Robos democratize investing | Traditional advisors offer personalized guidance"
    ax.text(7, 2.2, insight, ha='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Market size
    market = """US Robo-Advisory AUM: $1.4T (2024)
    Projected: $2.5T by 2028
    Source: Statista, Deloitte"""
    ax.text(7, 1, market, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_vs_traditional.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
