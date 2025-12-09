"""
Insurance Regulation
Shows regulatory landscape for InsurTech

Output: insurance_regulation.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Insurance Regulation',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/insurance_regulation'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create insurance regulation diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'InsurTech Regulatory Landscape', fontsize=20, fontweight='bold', ha='center')

    # Regulatory areas
    areas = [
        {
            'name': 'Licensing',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'points': ['Full carrier license', 'MGA/MGU model', 'Fronting arrangements'],
        },
        {
            'name': 'Capital\nRequirements',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'points': ['Solvency II (EU)', 'RBC requirements (US)', 'Surplus lines'],
        },
        {
            'name': 'Data &\nPrivacy',
            'x': 11.8, 'y': 6.5,
            'color': '#FF7F0E',
            'points': ['GDPR compliance', 'CCPA requirements', 'Telematics consent'],
        },
        {
            'name': 'Algorithm\nFairness',
            'x': 2.2, 'y': 2.5,
            'color': '#6B5B95',
            'points': ['AI bias testing', 'Explainability rules', 'Protected variables'],
        },
        {
            'name': 'Rate\nFilings',
            'x': 7, 'y': 2.5,
            'color': '#D62728',
            'points': ['State approval (US)', 'File-and-use vs prior', 'Dynamic pricing limits'],
        },
        {
            'name': 'Cross-Border',
            'x': 11.8, 'y': 2.5,
            'color': '#333333',
            'points': ['Passporting (EU)', 'Admitted vs non-admitted', 'Regulatory arbitrage'],
        },
    ]

    for area in areas:
        # Box
        box = mpatches.FancyBboxPatch((area['x']-1.8, area['y']-1.4), 3.6, 2.9,
                                       boxstyle='round,pad=0.1',
                                       facecolor=area['color'], alpha=0.15,
                                       edgecolor=area['color'], lw=2)
        ax.add_patch(box)
        ax.text(area['x'], area['y']+1.1, area['name'], ha='center',
               fontsize=13, fontweight='bold', color=area['color'])

        for i, point in enumerate(area['points']):
            ax.text(area['x'], area['y']+0.2-i*0.5, f'* {point}', ha='center', fontsize=10)

    # Regulatory sandboxes note
    sandbox = "InsurTech Sandboxes: UK FCA (first), Singapore MAS, Arizona, NAIC Innovation Track"
    ax.text(7, 0.8, sandbox, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: NAIC, EIOPA, Lloyd\'s regulatory guidance (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'insurance_regulation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
