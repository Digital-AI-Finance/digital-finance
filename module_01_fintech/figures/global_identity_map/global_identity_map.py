"""
Global Digital Identity Landscape
Shows adoption of digital identity systems by region

Output: global_identity_map.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Global Digital Identity Landscape',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/global_identity_map'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create global identity landscape chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Global Digital Identity Landscape', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'National Digital ID Systems by Region (2024)', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Regions
    regions = [
        {
            'name': 'Europe',
            'x': 2, 'y': 6.5,
            'color': '#4A90E2',
            'systems': ['eIDAS/EUDI Wallet (EU)', 'BankID (Nordics)', 'itsme (Belgium)'],
            'adoption': '70%+ adult population',
        },
        {
            'name': 'Asia-Pacific',
            'x': 6.5, 'y': 6.5,
            'color': '#44A044',
            'systems': ['Aadhaar (India) - 1.3B', 'MyKad (Malaysia)', 'SingPass (Singapore)'],
            'adoption': 'Highest biometric coverage',
        },
        {
            'name': 'Americas',
            'x': 11, 'y': 6.5,
            'color': '#FF7F0E',
            'systems': ['Login.gov (US-partial)', 'Gov.br (Brazil)', 'Digital ID (Canada-pilot)'],
            'adoption': 'Fragmented adoption',
        },
        {
            'name': 'Africa',
            'x': 2, 'y': 2.5,
            'color': '#6B5B95',
            'systems': ['NIMC (Nigeria)', 'Smart ID (South Africa)', 'Huduma Namba (Kenya)'],
            'adoption': 'Growing mobile-first',
        },
        {
            'name': 'Middle East',
            'x': 6.5, 'y': 2.5,
            'color': '#D62728',
            'systems': ['UAE Pass', 'Absher (Saudi)', 'Smart Qatar'],
            'adoption': 'High gov adoption',
        },
    ]

    for region in regions:
        # Box
        box = mpatches.FancyBboxPatch((region['x']-1.8, region['y']-1.2), 3.6, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=region['color'], alpha=0.15,
                                       edgecolor=region['color'], lw=2)
        ax.add_patch(box)
        ax.text(region['x'], region['y']+1.2, region['name'], ha='center',
               fontsize=11, fontweight='bold', color=region['color'])

        for i, system in enumerate(region['systems']):
            ax.text(region['x'], region['y']+0.5-i*0.4, f'* {system}', ha='center', fontsize=7)

        ax.text(region['x'], region['y']-0.9, region['adoption'], ha='center',
               fontsize=7, style='italic', color='#666666')

    # Key statistics
    stats = """Global Statistics (2024):
    - 5B+ people have digital ID
    - 1B+ still lack legal identity
    - $30B+ market by 2028
    Source: World Bank ID4D, McKinsey"""

    ax.text(11, 2.5, stats, fontsize=7, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: World Bank ID4D Global Dataset 2024, Regional government sources',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'global_identity_map.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
