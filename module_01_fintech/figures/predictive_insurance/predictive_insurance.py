"""
Predictive Insurance
Shows the future of AI-driven predictive insurance

Output: predictive_insurance.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Predictive Insurance',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/predictive_insurance'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create predictive insurance future diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The Future: Predictive & Preventive Insurance', fontsize=20, fontweight='bold', ha='center')

    # Evolution timeline
    phases = [
        {
            'name': 'Today\nReactive',
            'x': 2.5, 'y': 6,
            'color': '#D62728',
            'features': ['Pay after loss', 'Annual renewals', 'Static pricing'],
        },
        {
            'name': 'Near-Term\nPredictive',
            'x': 7, 'y': 6,
            'color': '#FF7F0E',
            'features': ['Risk prediction', 'Dynamic pricing', 'Behavior incentives'],
        },
        {
            'name': 'Future\nPreventive',
            'x': 11.5, 'y': 6,
            'color': '#44A044',
            'features': ['Loss prevention', 'Continuous coverage', 'Risk elimination'],
        },
    ]

    for phase in phases:
        # Box
        box = mpatches.FancyBboxPatch((phase['x']-1.7, phase['y']-2), 3.4, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=phase['color'], alpha=0.2,
                                       edgecolor=phase['color'], lw=2)
        ax.add_patch(box)
        ax.text(phase['x'], phase['y']+1.5, phase['name'], ha='center',
               fontsize=13, fontweight='bold', color=phase['color'])

        for i, feature in enumerate(phase['features']):
            ax.text(phase['x'], phase['y']+0.4-i*0.6, f'* {feature}', ha='center', fontsize=11)

    # Arrow connecting phases
    ax.annotate('', xy=(4.7, 6), xytext=(4, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.annotate('', xy=(9.2, 6), xytext=(8.5, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Technologies enabling future
    tech = """Enabling Technologies:
    - IoT sensors (home, health, auto)
    - Real-time data analytics
    - AI/ML risk models
    - Smart contracts
    - Digital twins"""

    ax.text(4, 2, tech, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Vision
    vision = """The Vision: Insurance Shifts from
    "Indemnify Loss" to "Prevent Loss"

    Insurers become risk management partners,
    not just claims payers"""

    ax.text(10, 2.2, vision, ha='center', fontsize=12, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[FORWARD-LOOKING ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'predictive_insurance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
