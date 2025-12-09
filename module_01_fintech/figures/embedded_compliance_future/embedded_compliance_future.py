"""
Embedded Compliance Future
Shows future of embedded/automated compliance

Output: embedded_compliance_future.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Embedded Compliance Future',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/embedded_compliance_future'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create embedded compliance future diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'The Future: Embedded Compliance', fontsize=20, fontweight='bold', ha='center')

    # Evolution phases
    phases = [
        {
            'name': 'Today\nReactive',
            'x': 2.5, 'y': 6,
            'color': '#D62728',
            'features': ['Post-trade monitoring', 'Manual reporting', 'Periodic audits'],
        },
        {
            'name': 'Near-Term\nProactive',
            'x': 7, 'y': 6,
            'color': '#FF7F0E',
            'features': ['Real-time monitoring', 'Auto-reporting', 'Continuous controls'],
        },
        {
            'name': 'Future\nEmbedded',
            'x': 11.5, 'y': 6,
            'color': '#44A044',
            'features': ['Compliance by design', 'Smart contracts', 'Zero friction'],
        },
    ]

    for phase in phases:
        box = mpatches.FancyBboxPatch((phase['x']-1.7, phase['y']-2), 3.4, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=phase['color'], alpha=0.2,
                                       edgecolor=phase['color'], lw=2)
        ax.add_patch(box)
        ax.text(phase['x'], phase['y']+1.5, phase['name'], ha='center',
               fontsize=13, fontweight='bold', color=phase['color'])

        for i, feature in enumerate(phase['features']):
            ax.text(phase['x'], phase['y']+0.4-i*0.6, f'* {feature}', ha='center', fontsize=11)

    # Arrows
    ax.annotate('', xy=(4.7, 6), xytext=(4, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.annotate('', xy=(9.2, 6), xytext=(8.5, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Key enablers
    enablers = """Key Enablers:
    - Machine-readable regulations (XBRL, RegML)
    - API-first regulatory reporting
    - Blockchain for immutable audit trails
    - AI for interpretation & advice
    - Regulatory nodes in DeFi"""

    ax.text(4, 2, enablers, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Vision
    vision = """The Vision:
    Compliance becomes invisible infrastructure
    - Built into products from day one
    - Automated, not checked
    - Real-time, not periodic
    - Cost: approaching zero marginal cost"""

    ax.text(10, 2.2, vision, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[FORWARD-LOOKING ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'embedded_compliance_future.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
