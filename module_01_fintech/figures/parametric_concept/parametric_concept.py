"""
Parametric Insurance Concept
Shows how parametric/index-based insurance works

Output: parametric_concept.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Parametric Insurance Concept',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/parametric_concept'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create parametric insurance concept diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Parametric (Index-Based) Insurance', fontsize=20, fontweight='bold', ha='center')

    # Traditional vs Parametric comparison
    ax.text(3.5, 8.2, 'Traditional Insurance', fontsize=15, fontweight='bold', ha='center', color='#D62728')
    ax.text(10.5, 8.2, 'Parametric Insurance', fontsize=15, fontweight='bold', ha='center', color='#44A044')

    # Dividing line
    ax.plot([7, 7], [1, 8], color='#CCCCCC', lw=2, ls='--')

    # Traditional process
    trad_steps = [
        'Event occurs',
        'File claim',
        'Adjuster inspection',
        'Loss assessment',
        'Negotiation',
        'Payout (weeks/months)'
    ]
    for i, step in enumerate(trad_steps):
        ax.text(3.5, 7.2 - i*0.9, f'{i+1}. {step}', fontsize=12, ha='center')

    # Parametric process
    param_steps = [
        'Event occurs',
        'Index triggered',
        'Automatic verification',
        'Instant payout',
        '',
        ''
    ]
    for i, step in enumerate(param_steps[:4]):
        ax.text(10.5, 7.2 - i*0.9, f'{i+1}. {step}', fontsize=12, ha='center',
               color='#44A044' if step else 'white')

    # Key difference highlight
    diff_box = mpatches.FancyBboxPatch((8, 3.5), 5, 2,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#44A044', alpha=0.15,
                                        edgecolor='#44A044', lw=2)
    ax.add_patch(diff_box)
    ax.text(10.5, 5.1, 'Key Innovation:', fontsize=13, fontweight='bold', ha='center', color='#44A044')
    ax.text(10.5, 4.5, 'No loss adjustment!', fontsize=14, fontweight='bold', ha='center')
    ax.text(10.5, 3.9, 'Payout based on trigger\nnot actual loss', fontsize=11, ha='center')

    # Example triggers
    triggers = """Common Triggers:
    - Weather: rainfall, temperature, wind speed
    - Seismic: earthquake magnitude
    - Financial: index levels, commodity prices
    - Event: flight delays, pandemic cases"""

    ax.text(3.5, 2.2, triggers, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Benefits
    benefits = "Benefits: Transparency, speed (hours not months), lower costs, no moral hazard"
    ax.text(7, 0.8, benefits, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL DIAGRAM]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'parametric_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
