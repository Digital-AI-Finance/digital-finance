"""
Telematics Data
Shows data points collected for insurance telematics

Output: telematics_data.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Telematics Data',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/telematics_data'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create telematics data diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Telematics: Data Points for Risk Assessment', fontsize=20, fontweight='bold', ha='center')

    # Central vehicle icon area
    vehicle_box = mpatches.FancyBboxPatch((5.5, 4.5), 3, 2,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#333333', alpha=0.1,
                                          edgecolor='#333333', lw=2)
    ax.add_patch(vehicle_box)
    ax.text(7, 5.5, 'VEHICLE\nTELEMATICS', ha='center', va='center',
           fontsize=14, fontweight='bold')

    # Data categories
    categories = [
        {'name': 'Driving Behavior', 'x': 2.5, 'y': 7.5, 'color': '#4A90E2',
         'points': ['Speed', 'Acceleration', 'Braking', 'Cornering']},
        {'name': 'Trip Data', 'x': 11.5, 'y': 7.5, 'color': '#44A044',
         'points': ['Distance', 'Duration', 'Time of day', 'Route type']},
        {'name': 'Location', 'x': 2.5, 'y': 2.5, 'color': '#FF7F0E',
         'points': ['GPS coords', 'Road type', 'Weather', 'Traffic']},
        {'name': 'Vehicle Health', 'x': 11.5, 'y': 2.5, 'color': '#6B5B95',
         'points': ['Engine status', 'Diagnostics', 'Fuel level', 'Maintenance']},
    ]

    for cat in categories:
        # Category box
        box = mpatches.FancyBboxPatch((cat['x']-1.8, cat['y']-1.5), 3.6, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(cat['x'], cat['y']+1.1, cat['name'], ha='center',
               fontsize=13, fontweight='bold', color=cat['color'])

        for i, point in enumerate(cat['points']):
            ax.text(cat['x'], cat['y']+0.3-i*0.5, f'* {point}', ha='center', fontsize=11)

        # Arrow to center
        dx = 7 - cat['x']
        dy = 5.5 - cat['y']
        ax.annotate('', xy=(7 - dx*0.4, 5.5 - dy*0.4),
                   xytext=(cat['x'] + dx*0.3, cat['y'] + dy*0.3),
                   arrowprops=dict(arrowstyle='->', color='#999999', lw=1.5, ls='--'))

    # Risk score output
    ax.text(7, 3.2, 'Risk Score', fontsize=14, fontweight='bold', ha='center', color='#D62728')
    ax.annotate('', xy=(7, 3.5), xytext=(7, 4.3),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2))

    # Privacy note
    privacy = "Privacy Considerations: Opt-in consent, data anonymization, GDPR compliance, limited retention"
    ax.text(7, 0.8, privacy, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: LexisNexis Risk Solutions, Verisk Analytics (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'telematics_data.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
