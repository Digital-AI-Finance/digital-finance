"""
Lemonade Business Model
Shows Lemonade's unique insurance model

Output: lemonade_model.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Lemonade Business Model',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/lemonade_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Lemonade business model diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Lemonade: AI-First Insurance Model', fontsize=20, fontweight='bold', ha='center')

    # Core components
    components = [
        {
            'name': 'AI Maya',
            'x': 2.5, 'y': 6.5,
            'color': '#FF69B4',
            'desc': 'AI chatbot for\nonboarding &\npolicy purchase',
            'stat': '90 sec signup'
        },
        {
            'name': 'AI Jim',
            'x': 7, 'y': 6.5,
            'color': '#4A90E2',
            'desc': 'AI claims bot\ninstant payout\nfraud detection',
            'stat': '3 sec claims'
        },
        {
            'name': 'Flat Fee',
            'x': 11.5, 'y': 6.5,
            'color': '#44A044',
            'desc': '25% flat fee\nno underwriting\nprofit motive',
            'stat': 'Aligned incentives'
        },
    ]

    for comp in components:
        # Circle for icon area
        circle = plt.Circle((comp['x'], comp['y']+0.3), 0.8,
                            facecolor=comp['color'], alpha=0.3,
                            edgecolor=comp['color'], lw=2)
        ax.add_patch(circle)
        ax.text(comp['x'], comp['y']+0.3, comp['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=comp['color'])

        # Description
        ax.text(comp['x'], comp['y']-1.2, comp['desc'], ha='center', va='center', fontsize=11)

        # Stat highlight
        ax.text(comp['x'], comp['y']-2.2, comp['stat'], ha='center', fontsize=12,
               fontweight='bold', color=comp['color'])

    # Giveback model box
    giveback_box = mpatches.FancyBboxPatch((3, 1.5), 8, 1.8,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#FFD700', alpha=0.2,
                                           edgecolor='#FFD700', lw=2)
    ax.add_patch(giveback_box)
    ax.text(7, 2.8, 'Giveback Program', ha='center', fontsize=14, fontweight='bold', color='#B8860B')
    ax.text(7, 2.1, 'Unclaimed premiums donated to charity chosen by policyholder\n'
           'Removes adversarial relationship - Lemonade profits same regardless of claims',
           ha='center', fontsize=11)

    # Key metrics
    metrics = "Founded: 2015 | IPO: 2020 | Products: Renters, Home, Pet, Car, Life | Markets: US, EU"
    ax.text(7, 0.8, metrics, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Lemonade company filings (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'lemonade_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
