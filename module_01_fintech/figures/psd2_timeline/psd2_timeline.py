"""
PSD2 Implementation Timeline
Shows the rollout timeline of PSD2 regulation in Europe

Output: psd2_timeline.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'PSD2 Implementation Timeline',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/psd2_timeline'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create PSD2 implementation timeline"""
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.set_xlim(2014, 2025)
    ax.set_ylim(0, 10)

    # Timeline base
    ax.axhline(y=5, color='#333333', lw=3, zorder=1)

    # Milestones
    milestones = [
        (2015.8, 'PSD2 Adopted\n(Nov 2015)', 7, '#4A90E2', 'EU adopts directive'),
        (2016.0, 'Member States\nTranspose', 3.5, '#999999', '2-year deadline'),
        (2018.0, 'PSD2 Effective\n(Jan 2018)', 7.5, '#44A044', 'Enters into force'),
        (2019.3, 'RTS Applied\n(Mar 2019)', 3, '#FF7F0E', 'Technical standards'),
        (2019.7, 'SCA Deadline\n(Sep 2019)', 7, '#D62728', 'Original deadline'),
        (2020.0, 'SCA Extended\n(2020)', 3.5, '#D62728', 'COVID delays'),
        (2021.0, 'Full SCA\nEnforcement', 7.5, '#44A044', 'Final compliance'),
        (2023.5, 'PSD3 Proposal\n(Jun 2023)', 3, '#6B5B95', 'Next revision'),
    ]

    for year, label, y_pos, color, desc in milestones:
        # Marker
        ax.plot(year, 5, 'o', color=color, markersize=14, zorder=3, markeredgecolor='white', markeredgewidth=2)

        # Connector line
        if y_pos > 5:
            ax.plot([year, year], [5.3, y_pos-0.3], color=color, lw=1.5, zorder=2)
            va = 'bottom'
        else:
            ax.plot([year, year], [4.7, y_pos+0.3], color=color, lw=1.5, zorder=2)
            va = 'top'

        # Label
        ax.text(year, y_pos, label, ha='center', va=va, fontsize=8,
               fontweight='bold', color=color)

    # Phase labels
    phases = [
        (2016.5, 8.8, 'Adoption Phase', '#4A90E2'),
        (2018.5, 8.8, 'Implementation', '#44A044'),
        (2020.5, 8.8, 'SCA Rollout', '#D62728'),
        (2023, 8.8, 'Evolution', '#6B5B95'),
    ]

    for x, y, label, color in phases:
        ax.text(x, y, label, ha='center', fontsize=9, fontweight='bold',
               color=color, style='italic')

    # Key dates annotation box
    key_dates = """Key Dates:
    - Nov 2015: Directive adopted
    - Jan 2018: PSD2 in force
    - Sep 2019: Original SCA deadline
    - Dec 2020: SCA e-commerce deadline
    - Jun 2023: PSD3 proposal published"""

    ax.text(2023.5, 5.5, key_dates, fontsize=7, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    ax.set_xlabel('Year', fontsize=11)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Title
    ax.set_title('PSD2 Implementation Timeline (2015-2024)',
                fontsize=14, fontweight='bold', pad=15)

    # Legend
    ax.text(2015, 1.5, 'Above line: Major milestones | Below line: Secondary events',
           fontsize=8, style='italic', color='#666666')

    # Source
    fig.text(0.5, 0.02, 'Source: European Banking Authority, EUR-Lex',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'psd2_timeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
