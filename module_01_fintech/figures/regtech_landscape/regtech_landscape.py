"""
RegTech Landscape
Shows the RegTech market overview

Output: regtech_landscape.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Landscape',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regtech_landscape'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create RegTech landscape diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'RegTech Landscape Overview', fontsize=20, fontweight='bold', ha='center')

    # Definition
    ax.text(7, 8.5, 'RegTech = Technology solutions for regulatory compliance', fontsize=13, ha='center',
           style='italic', color='#666666')

    # Market segments
    segments = [
        {
            'name': 'Compliance\nManagement',
            'x': 2.2, 'y': 6,
            'color': '#4A90E2',
            'players': 'Ascent, NICE Actimize',
            'use': 'Policy tracking'
        },
        {
            'name': 'Identity\n& KYC',
            'x': 5.5, 'y': 6,
            'color': '#44A044',
            'players': 'Jumio, Onfido',
            'use': 'Customer verification'
        },
        {
            'name': 'Transaction\nMonitoring',
            'x': 8.5, 'y': 6,
            'color': '#FF7F0E',
            'players': 'ComplyAdvantage, Chainalysis',
            'use': 'AML/fraud detection'
        },
        {
            'name': 'Regulatory\nReporting',
            'x': 11.8, 'y': 6,
            'color': '#6B5B95',
            'players': 'Workiva, AxiomSL',
            'use': 'Automated filings'
        },
        {
            'name': 'Risk\nManagement',
            'x': 3.8, 'y': 2.5,
            'color': '#D62728',
            'players': 'Moody\'s, SAS',
            'use': 'Risk assessment'
        },
        {
            'name': 'Trade\nSurveillance',
            'x': 7, 'y': 2.5,
            'color': '#333333',
            'players': 'Nasdaq, Eventus',
            'use': 'Market abuse detection'
        },
        {
            'name': 'Data\nPrivacy',
            'x': 10.2, 'y': 2.5,
            'color': '#17BECF',
            'players': 'BigID, OneTrust',
            'use': 'GDPR/privacy compliance'
        },
    ]

    for seg in segments:
        # Box
        box = mpatches.FancyBboxPatch((seg['x']-1.5, seg['y']-1.3), 3, 2.7,
                                       boxstyle='round,pad=0.1',
                                       facecolor=seg['color'], alpha=0.15,
                                       edgecolor=seg['color'], lw=2)
        ax.add_patch(box)
        ax.text(seg['x'], seg['y']+1, seg['name'], ha='center',
               fontsize=12, fontweight='bold', color=seg['color'])
        ax.text(seg['x'], seg['y']+0.1, seg['players'], ha='center', fontsize=10, style='italic')
        ax.text(seg['x'], seg['y']-0.6, seg['use'], ha='center', fontsize=10)

    # Market size
    market = "Global RegTech Market: USD 15B (2024) | CAGR: 18% | Projected: USD 40B by 2030"
    ax.text(7, 0.8, market, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Grand View Research, Juniper Research (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regtech_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
