"""
Robo-Advisor Market Leaders
Shows major robo-advisory platforms and their AUM

Output: robo_market_leaders.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Robo-Advisor Market Leaders',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_market_leaders'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create robo market leaders bar chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Data (AUM in $B, 2024 estimates)
    platforms = ['Vanguard\nDigital Advisor', 'Schwab\nIntelligent', 'Betterment',
                 'Wealthfront', 'Fidelity Go', 'SoFi\nInvest', 'Ellevest', 'Acorns']
    aum = [350, 80, 40, 35, 20, 10, 2, 8]
    colors = ['#4A90E2', '#4A90E2', '#44A044', '#44A044', '#4A90E2', '#44A044', '#FF7F0E', '#44A044']

    bars = ax.barh(platforms, aum, color=colors, edgecolor='#333333', lw=1.5)

    ax.set_xlabel('Assets Under Management ($B)', fontsize=14)
    ax.set_title('Robo-Advisor Market Leaders (2024)', fontsize=20, fontweight='bold', pad=15)

    ax.set_xlim(0, 400)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, aum):
        ax.annotate(f'${val}B',
                   xy=(bar.get_width() + 5, bar.get_y() + bar.get_height()/2),
                   va='center', fontsize=12, fontweight='bold')

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#4A90E2', label='Incumbent-owned'),
                       Patch(facecolor='#44A044', label='Pure-play robo'),
                       Patch(facecolor='#FF7F0E', label='Niche focus')]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=11)

    # Note
    ax.text(0.02, 0.02, 'Note: Vanguard includes hybrid digital/human advisory | Source: Company reports, industry estimates',
           transform=ax.transAxes, fontsize=10, style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_market_leaders.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
