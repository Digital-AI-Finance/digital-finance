"""
InsurTech Segments
Shows major InsurTech market segments

Output: insurtech_segments.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'InsurTech Segments',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/insurtech_segments'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create InsurTech segments diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'InsurTech Market Segments', fontsize=20, fontweight='bold', ha='center')

    # Segments
    segments = [
        {
            'name': 'Full-Stack\nInsurers',
            'x': 2.2, 'y': 6.5,
            'color': '#4A90E2',
            'examples': 'Lemonade, Root,\nHippo, Oscar',
            'desc': 'Own license, full risk'
        },
        {
            'name': 'Distribution\n& MGA',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'examples': 'Policygenius,\nCover, Embroker',
            'desc': 'Sell others\' products'
        },
        {
            'name': 'B2B\nEnablers',
            'x': 11.8, 'y': 6.5,
            'color': '#FF7F0E',
            'examples': 'Socotra, Duck Creek,\nGuidewire',
            'desc': 'Tech for incumbents'
        },
        {
            'name': 'Claims\nTech',
            'x': 2.2, 'y': 2.5,
            'color': '#6B5B95',
            'examples': 'Tractable, Shift,\nSnapsheet',
            'desc': 'AI claims processing'
        },
        {
            'name': 'Data &\nAnalytics',
            'x': 7, 'y': 2.5,
            'color': '#D62728',
            'examples': 'Cape Analytics,\nHazard Hub',
            'desc': 'Risk data & insights'
        },
        {
            'name': 'IoT &\nTelematics',
            'x': 11.8, 'y': 2.5,
            'color': '#333333',
            'examples': 'Cambridge Mobile,\nDriveWealth',
            'desc': 'Connected devices'
        },
    ]

    for seg in segments:
        # Box
        box = mpatches.FancyBboxPatch((seg['x']-1.8, seg['y']-1.4), 3.6, 2.9,
                                       boxstyle='round,pad=0.1',
                                       facecolor=seg['color'], alpha=0.15,
                                       edgecolor=seg['color'], lw=2)
        ax.add_patch(box)
        ax.text(seg['x'], seg['y']+1.1, seg['name'], ha='center',
               fontsize=13, fontweight='bold', color=seg['color'])
        ax.text(seg['x'], seg['y']+0.2, seg['examples'], ha='center', fontsize=10, style='italic')
        ax.text(seg['x'], seg['y']-0.8, seg['desc'], ha='center', fontsize=11)

    # Investment data
    invest = "InsurTech Funding (2024): $4.5B | 300+ deals | Focus shifting to profitability"
    ax.text(7, 0.8, invest, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CB Insights, Gallagher Re InsurTech report (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'insurtech_segments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
