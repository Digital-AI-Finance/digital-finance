"""
Robo-Advisor Global Adoption
Shows robo-advisory market by region

Output: robo_global_adoption.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Robo Global Adoption',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_global_adoption'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create global robo adoption chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    regions = ['United\nStates', 'Europe', 'China', 'UK', 'Japan', 'Rest of\nWorld']
    aum = [900, 200, 150, 80, 50, 100]  # $B
    colors = ['#4A90E2', '#44A044', '#D62728', '#FF7F0E', '#6B5B95', '#999999']

    bars = ax.bar(regions, aum, color=colors, edgecolor='#333333', lw=2)

    ax.set_ylabel('Assets Under Management ($B)', fontsize=14)
    ax.set_title('Global Robo-Advisory Market by Region (2024)', fontsize=20, fontweight='bold', pad=15)

    ax.set_ylim(0, 1100)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, aum):
        ax.annotate(f'${val}B',
                   xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=13, fontweight='bold')

    # Key players by region
    players = """Key Players:
    US: Vanguard, Schwab, Betterment, Wealthfront
    Europe: Scalable Capital, Nutmeg, Moneyfarm
    China: Lufax, Ant Fortune
    UK: Nutmeg, Wealthify
    Japan: WealthNavi, THEO"""

    ax.text(0.98, 0.98, players, transform=ax.transAxes, fontsize=10,
           va='top', ha='right',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Market projection
    ax.text(0.02, 0.98, 'Global Total: ~$1.5T (2024)\nProjected: $3T+ by 2028\nCAGR: ~15-20%',
           transform=ax.transAxes, fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Statista, Backend Benchmarking, Industry reports',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_global_adoption.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
