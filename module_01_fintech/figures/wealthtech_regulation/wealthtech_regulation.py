"""
WealthTech Regulation
Shows regulatory landscape for WealthTech

Output: wealthtech_regulation.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Regulation',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wealthtech_regulation'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create WealthTech regulation diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'WealthTech Regulatory Landscape', fontsize=20, fontweight='bold', ha='center')

    # Key regulatory areas
    areas = [
        {
            'name': 'Broker-Dealer',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'regs': ['SEC registration', 'FINRA membership', 'Net capital rules'],
        },
        {
            'name': 'Investment\nAdviser',
            'x': 5.5, 'y': 6.5,
            'color': '#44A044',
            'regs': ['SEC/State registration', 'Fiduciary duty', 'Form ADV disclosures'],
        },
        {
            'name': 'Payment for\nOrder Flow',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'regs': ['SEC Rule 606', 'Best execution', 'Disclosure requirements'],
        },
        {
            'name': 'Suitability',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'regs': ['Reg BI', 'Know your customer', 'Product appropriateness'],
        },
        {
            'name': 'Digital\nEngagement',
            'x': 4.75, 'y': 2.5,
            'color': '#D62728',
            'regs': ['Gamification scrutiny', 'Marketing rules', 'Social media'],
        },
        {
            'name': 'Crypto',
            'x': 9.25, 'y': 2.5,
            'color': '#333333',
            'regs': ['SEC/CFTC jurisdiction', 'State licenses', 'AML compliance'],
        },
    ]

    for area in areas:
        box = mpatches.FancyBboxPatch((area['x']-1.5, area['y']-1.3), 3, 2.7,
                                       boxstyle='round,pad=0.1',
                                       facecolor=area['color'], alpha=0.15,
                                       edgecolor=area['color'], lw=2)
        ax.add_patch(box)
        ax.text(area['x'], area['y']+1, area['name'], ha='center',
               fontsize=12, fontweight='bold', color=area['color'])

        for i, reg in enumerate(area['regs']):
            ax.text(area['x'], area['y']+0.3-i*0.5, f'* {reg}', ha='center', fontsize=10)

    # Key 2024 developments
    developments = "2024 Focus: SEC best execution rules, FINRA options guidance, gamification review"
    ax.text(7, 0.8, developments, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: SEC, FINRA regulatory guidance (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealthtech_regulation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
