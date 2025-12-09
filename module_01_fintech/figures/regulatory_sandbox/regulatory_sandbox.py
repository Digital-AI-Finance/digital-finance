"""
Regulatory Sandbox
Shows concept of regulatory sandboxes

Output: regulatory_sandbox.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Regulatory Sandbox',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regulatory_sandbox'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create regulatory sandbox concept diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Regulatory Sandbox Concept', fontsize=20, fontweight='bold', ha='center')

    # Main sandbox box
    sandbox = mpatches.FancyBboxPatch((2, 2.5), 10, 5.5,
                                       boxstyle='round,pad=0.2',
                                       facecolor='#FFD700', alpha=0.1,
                                       edgecolor='#FFD700', lw=3)
    ax.add_patch(sandbox)
    ax.text(7, 7.5, 'REGULATORY SANDBOX', fontsize=16, fontweight='bold',
           ha='center', color='#B8860B')

    # Benefits inside sandbox
    benefits = [
        {'name': 'Controlled Testing', 'x': 4, 'y': 5.5, 'color': '#4A90E2',
         'desc': 'Test innovations with\nreal customers'},
        {'name': 'Regulatory Relief', 'x': 7, 'y': 5.5, 'color': '#44A044',
         'desc': 'Temporary exemptions\nor modified rules'},
        {'name': 'Regulator Learning', 'x': 10, 'y': 5.5, 'color': '#FF7F0E',
         'desc': 'Understand new tech\nbefore full regulation'},
    ]

    for ben in benefits:
        box = mpatches.FancyBboxPatch((ben['x']-1.3, ben['y']-1), 2.6, 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor=ben['color'], alpha=0.2,
                                       edgecolor=ben['color'], lw=2)
        ax.add_patch(box)
        ax.text(ben['x'], ben['y']+0.6, ben['name'], ha='center',
               fontsize=11, fontweight='bold', color=ben['color'])
        ax.text(ben['x'], ben['y']-0.2, ben['desc'], ha='center', fontsize=10)

    # Entry requirements
    ax.text(4.5, 3.2, 'Entry Requirements:', fontsize=12, fontweight='bold', ha='center')
    reqs = ['Genuine innovation', 'Consumer benefit', 'Need for sandbox', 'Ready to test']
    for i, req in enumerate(reqs):
        ax.text(4.5, 2.7-i*0.4, f'* {req}', ha='center', fontsize=10)

    # Exit outcomes
    ax.text(9.5, 3.2, 'Exit Outcomes:', fontsize=12, fontweight='bold', ha='center')
    outcomes = ['Full authorization', 'Rule changes', 'Guidance issued', 'Product discontinued']
    for i, out in enumerate(outcomes):
        ax.text(9.5, 2.7-i*0.4, f'* {out}', ha='center', fontsize=10)

    # Pioneer info
    pioneer = "Pioneer: UK FCA (2016) | Now: 50+ countries with sandboxes | 700+ firms have participated"
    ax.text(7, 0.8, pioneer, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: FCA, BIS regulatory sandbox report (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regulatory_sandbox.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
