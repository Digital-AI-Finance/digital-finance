"""
ComplyAdvantage Workflow
Shows ComplyAdvantage AML solution workflow

Output: complyadvantage_workflow.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'ComplyAdvantage Workflow',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/complyadvantage_workflow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create ComplyAdvantage workflow diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'ComplyAdvantage: AI-Powered AML', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Real-world RegTech Case Study', fontsize=13, ha='center', color='#666666')

    # Process flow
    steps = [
        {'name': 'Entity\nInput', 'x': 1.8, 'y': 6, 'color': '#4A90E2',
         'desc': 'Names, addresses,\nidentifiers'},
        {'name': 'AI\nScreening', 'x': 4.6, 'y': 6, 'color': '#44A044',
         'desc': 'NLP matching,\nfuzzy logic'},
        {'name': 'Risk\nProfile', 'x': 7.4, 'y': 6, 'color': '#FF7F0E',
         'desc': 'Automated\nscoring'},
        {'name': 'Alert\nTriage', 'x': 10.2, 'y': 6, 'color': '#6B5B95',
         'desc': 'ML prioritization'},
        {'name': 'Case\nMgmt', 'x': 13, 'y': 6, 'color': '#D62728',
         'desc': 'Investigation\nworkflow'},
    ]

    for i, step in enumerate(steps):
        box = mpatches.FancyBboxPatch((step['x']-1.1, step['y']-1.5), 2.2, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1, step['name'], ha='center',
               fontsize=12, fontweight='bold', color=step['color'])
        ax.text(step['x'], step['y']-0.5, step['desc'], ha='center', fontsize=10)

        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-1.2, 6), xytext=(step['x']+1.2, 6),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Data sources
    ax.text(7, 3.8, 'ComplyAdvantage Data Sources:', fontsize=14, fontweight='bold', ha='center')
    sources = [
        '10,000+ sanctions & watchlists',
        'Adverse media (50+ languages)',
        'PEP databases (1.4M+ profiles)',
        'State-owned enterprises',
        'Crypto wallets & exchanges'
    ]
    for i, src in enumerate(sources):
        ax.text(7, 3.2-i*0.5, f'* {src}', ha='center', fontsize=11)

    # Results
    results = "Results: 70% reduction in false positives | 60% faster screening | Used by 1,000+ FIs"
    ax.text(7, 0.8, results, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: ComplyAdvantage company materials (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'complyadvantage_workflow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
