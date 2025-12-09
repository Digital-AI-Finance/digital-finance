"""
Global Sandboxes
Shows regulatory sandboxes around the world

Output: global_sandboxes.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Global Sandboxes',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/global_sandboxes'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create global sandboxes overview"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Global Regulatory Sandboxes', fontsize=20, fontweight='bold', ha='center')

    # Regions
    regions = [
        {
            'name': 'Europe',
            'x': 2.5, 'y': 6.5,
            'color': '#4A90E2',
            'sandboxes': ['UK FCA (2016)', 'Netherlands DNB', 'Lithuania', 'Denmark'],
            'firms': '500+'
        },
        {
            'name': 'Asia-Pacific',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'sandboxes': ['Singapore MAS', 'Hong Kong HKMA', 'Australia ASIC', 'Japan FSA'],
            'firms': '300+'
        },
        {
            'name': 'Americas',
            'x': 11.5, 'y': 6.5,
            'color': '#FF7F0E',
            'sandboxes': ['US (State-level)', 'Arizona, Wyoming', 'Brazil BCB', 'Canada CSA'],
            'firms': '150+'
        },
        {
            'name': 'Middle East',
            'x': 4.75, 'y': 2.5,
            'color': '#6B5B95',
            'sandboxes': ['UAE ADGM', 'Bahrain CBB', 'Saudi SAMA', 'Israel ISA'],
            'firms': '100+'
        },
        {
            'name': 'Africa',
            'x': 9.25, 'y': 2.5,
            'color': '#D62728',
            'sandboxes': ['Kenya CMA', 'Nigeria SEC', 'South Africa FSCA', 'Rwanda BNR'],
            'firms': '50+'
        },
    ]

    for region in regions:
        box = mpatches.FancyBboxPatch((region['x']-1.8, region['y']-1.5), 3.6, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=region['color'], alpha=0.15,
                                       edgecolor=region['color'], lw=2)
        ax.add_patch(box)
        ax.text(region['x'], region['y']+1.2, region['name'], ha='center',
               fontsize=13, fontweight='bold', color=region['color'])

        for i, sb in enumerate(region['sandboxes'][:3]):
            ax.text(region['x'], region['y']+0.5-i*0.4, f'* {sb}', ha='center', fontsize=10)

        ax.text(region['x'], region['y']-1, f"Firms: {region['firms']}", ha='center',
               fontsize=11, fontweight='bold', color=region['color'])

    # Global initiative
    global_init = "GFIN (Global Financial Innovation Network): 60+ regulators collaborating on cross-border sandbox"
    ax.text(7, 0.8, global_init, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: World Bank, BIS, individual regulator websites (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'global_sandboxes.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
