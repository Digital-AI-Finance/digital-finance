"""
Regulatory Reporting
Shows regulatory reporting landscape

Output: regulatory_reporting.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Regulatory Reporting',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regulatory_reporting'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create regulatory reporting diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Regulatory Reporting Requirements', fontsize=20, fontweight='bold', ha='center')

    # Major reporting regimes
    reports = [
        {
            'name': 'AML/SAR',
            'x': 2.2, 'y': 6.5,
            'color': '#D62728',
            'regs': ['FinCEN (US)', 'FCA (UK)', 'BaFin (DE)'],
            'freq': 'Event-driven'
        },
        {
            'name': 'Prudential',
            'x': 5.5, 'y': 6.5,
            'color': '#4A90E2',
            'regs': ['Basel III/IV', 'CRD IV', 'CCAR'],
            'freq': 'Quarterly'
        },
        {
            'name': 'Transaction',
            'x': 8.5, 'y': 6.5,
            'color': '#44A044',
            'regs': ['MiFID II', 'EMIR', 'Dodd-Frank'],
            'freq': 'T+1 daily'
        },
        {
            'name': 'Tax',
            'x': 11.8, 'y': 6.5,
            'color': '#FF7F0E',
            'regs': ['FATCA', 'CRS', '1099s'],
            'freq': 'Annual'
        },
    ]

    for rep in reports:
        box = mpatches.FancyBboxPatch((rep['x']-1.5, rep['y']-1.5), 3, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=rep['color'], alpha=0.15,
                                       edgecolor=rep['color'], lw=2)
        ax.add_patch(box)
        ax.text(rep['x'], rep['y']+1.2, rep['name'], ha='center',
               fontsize=14, fontweight='bold', color=rep['color'])

        for i, reg in enumerate(rep['regs']):
            ax.text(rep['x'], rep['y']+0.4-i*0.4, f'* {reg}', ha='center', fontsize=10)

        ax.text(rep['x'], rep['y']-1, f"Freq: {rep['freq']}", ha='center',
               fontsize=10, style='italic', color='#666666')

    # Challenges
    challenges = """Reporting Challenges:
    - 60+ regulators for global banks
    - Varying formats (XML, XBRL, CSV)
    - Different data taxonomies
    - Manual reconciliation errors
    - Penalties for late/incorrect filings"""

    ax.text(4, 2.2, challenges, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFEBEB', edgecolor='#D62728'))

    # Solution
    solution = """RegTech Solution:
    - Automated data extraction
    - Format transformation
    - Validation rules
    - Audit trails
    - On-time submission"""

    ax.text(10, 2.2, solution, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: BIS, FSB regulatory reporting surveys (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regulatory_reporting.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
