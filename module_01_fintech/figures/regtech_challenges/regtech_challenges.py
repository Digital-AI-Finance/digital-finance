"""
RegTech Challenges
Shows challenges facing RegTech adoption

Output: regtech_challenges.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Challenges',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regtech_challenges'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create RegTech challenges diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'RegTech Adoption Challenges', fontsize=20, fontweight='bold', ha='center')

    # Challenges
    challenges = [
        {
            'name': 'Integration',
            'x': 2.2, 'y': 6.5,
            'color': '#D62728',
            'issues': ['Legacy system compatibility', 'Data silos', 'API limitations'],
        },
        {
            'name': 'Model Risk',
            'x': 7, 'y': 6.5,
            'color': '#FF7F0E',
            'issues': ['AI explainability', 'Bias concerns', 'Validation requirements'],
        },
        {
            'name': 'Data Quality',
            'x': 11.8, 'y': 6.5,
            'color': '#6B5B95',
            'issues': ['Inconsistent formats', 'Missing data', 'Cross-system reconciliation'],
        },
        {
            'name': 'Vendor Risk',
            'x': 2.2, 'y': 2.5,
            'color': '#4A90E2',
            'issues': ['Concentration risk', 'Business continuity', 'Exit planning'],
        },
        {
            'name': 'Regulatory\nAcceptance',
            'x': 7, 'y': 2.5,
            'color': '#44A044',
            'issues': ['Regulator familiarity', 'Audit trail needs', 'Liability questions'],
        },
        {
            'name': 'Change\nManagement',
            'x': 11.8, 'y': 2.5,
            'color': '#333333',
            'issues': ['Staff reskilling', 'Process redesign', 'Cultural resistance'],
        },
    ]

    for ch in challenges:
        box = mpatches.FancyBboxPatch((ch['x']-1.8, ch['y']-1.3), 3.6, 2.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=ch['color'], alpha=0.15,
                                       edgecolor=ch['color'], lw=2)
        ax.add_patch(box)
        ax.text(ch['x'], ch['y']+1.1, ch['name'], ha='center',
               fontsize=13, fontweight='bold', color=ch['color'])

        for i, issue in enumerate(ch['issues']):
            ax.text(ch['x'], ch['y']+0.3-i*0.5, f'* {issue}', ha='center', fontsize=10)

    # Mitigation note
    mitigation = "Success Factors: Executive sponsorship, phased rollout, vendor due diligence, regulator dialogue"
    ax.text(7, 0.8, mitigation, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[INDUSTRY ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regtech_challenges.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
