"""
Identity Verification Provider Landscape
Shows the competitive landscape of IDV providers

Output: idv_provider_landscape.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'IDV Provider Landscape',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/idv_provider_landscape'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create IDV provider landscape chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Provider data: (name, coverage, capability_breadth, size, color)
    # Coverage: global reach (1-5)
    # Capability: breadth of services (1-5)
    providers = [
        ('Jumio', 4.5, 4.5, 300, '#4A90E2', 'Full-stack'),
        ('Onfido', 4.2, 4.3, 280, '#4A90E2', 'Full-stack'),
        ('Veriff', 4.0, 4.0, 200, '#4A90E2', 'Full-stack'),
        ('iProov', 3.5, 3.0, 150, '#44A044', 'Biometrics'),
        ('ID.me', 3.8, 3.5, 180, '#FF7F0E', 'Govt/Healthcare'),
        ('Trulioo', 4.5, 3.8, 220, '#6B5B95', 'Database'),
        ('Mitek', 4.0, 4.2, 250, '#4A90E2', 'Full-stack'),
        ('Socure', 3.5, 3.2, 160, '#999999', 'ML/Risk'),
        ('Au10tix', 4.0, 3.8, 180, '#4A90E2', 'Full-stack'),
        ('Shufti Pro', 3.8, 3.5, 120, '#44A044', 'Emerging'),
    ]

    for name, coverage, capability, size, color, category in providers:
        ax.scatter(coverage, capability, s=size, c=color, edgecolor='#333333',
                  lw=1.5, alpha=0.8, zorder=3)
        ax.annotate(name, (coverage, capability), xytext=(5, 5),
                   textcoords='offset points', fontsize=8, fontweight='bold')

    # Quadrant dividers
    ax.axhline(y=3.75, color='#CCCCCC', linestyle='--', lw=1.5, zorder=1)
    ax.axvline(x=4, color='#CCCCCC', linestyle='--', lw=1.5, zorder=1)

    # Quadrant labels
    ax.text(3, 4.8, 'Regional\nSpecialists', fontsize=9, ha='center',
           fontweight='bold', color='#999999')
    ax.text(4.7, 4.8, 'Global\nLeaders', fontsize=9, ha='center',
           fontweight='bold', color='#44A044')
    ax.text(3, 3, 'Niche\nPlayers', fontsize=9, ha='center',
           fontweight='bold', color='#999999')
    ax.text(4.7, 3, 'Emerging\nChallengers', fontsize=9, ha='center',
           fontweight='bold', color='#FF7F0E')

    ax.set_xlabel('Global Coverage (Document/Country Support)', fontsize=11)
    ax.set_ylabel('Capability Breadth (Services Offered)', fontsize=11)
    ax.set_xlim(2.5, 5.2)
    ax.set_ylim(2.5, 5.2)

    ax.set_title('Identity Verification Provider Landscape',
                fontsize=14, fontweight='bold', pad=15)

    # Legend for bubble size
    ax.text(5.1, 2.7, 'Bubble size = Market presence', fontsize=7, style='italic')

    # Category legend
    legend_elements = [
        mpatches.Patch(facecolor='#4A90E2', edgecolor='#333333', label='Full-stack IDV'),
        mpatches.Patch(facecolor='#44A044', edgecolor='#333333', label='Biometrics Focus'),
        mpatches.Patch(facecolor='#6B5B95', edgecolor='#333333', label='Database/KYC'),
        mpatches.Patch(facecolor='#FF7F0E', edgecolor='#333333', label='Specialized'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8, title='Focus Area')

    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Market size note
    market = """Global IDV Market:
    - 2024: ~$12B
    - 2028: ~$24B (est.)
    - CAGR: ~15%
    Source: Grand View Research"""

    ax.text(2.6, 5, market, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    plt.tight_layout()

    output_path = Path(__file__).parent / 'idv_provider_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
