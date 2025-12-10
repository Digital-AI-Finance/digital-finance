"""
CBDC Design Choices
Key design decisions for CBDCs

Output: cbdc_design_choices.pdf
Module: module_04_trad_finance
Lesson: 48 - CBDC
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'CBDC Design Choices',
    'module': 'module_04_trad_finance',
    'lesson': 48,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/cbdc_design_choices'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Design dimensions
    dimensions = [
        ('Access', 2, 6.5, ['Retail', 'Wholesale', 'Hybrid'], [60, 25, 15]),
        ('Technology', 6, 6.5, ['DLT-based', 'Centralized', 'Hybrid'], [40, 35, 25]),
        ('Architecture', 10, 6.5, ['Two-tier', 'Direct', 'Hybrid'], [75, 10, 15]),
        ('Identity', 2, 3.5, ['Account-based', 'Token-based', 'Hybrid'], [55, 30, 15]),
        ('Interest', 6, 3.5, ['Non-remunerated', 'Tiered', 'Full rate'], [65, 25, 10]),
        ('Privacy', 10, 3.5, ['Full KYC', 'Tiered privacy', 'Anonymous'], [50, 40, 10]),
    ]

    colors = ['#4A90E2', '#44A044', '#FF7F0E']

    for dim_name, x, y, options, percentages in dimensions:
        # Title
        ax.text(x, y + 1, dim_name, ha='center', va='center',
                fontsize=11, fontweight='bold')

        # Options as stacked bar
        left = x - 1.3
        for i, (opt, pct) in enumerate(zip(options, percentages)):
            width = pct * 2.6 / 100
            rect = mpatches.FancyBboxPatch((left, y - 0.3), width, 0.6,
                                            boxstyle="square,pad=0",
                                            facecolor=colors[i], alpha=0.8, edgecolor='black')
            ax.add_patch(rect)
            if pct >= 20:
                ax.text(left + width/2, y, f'{opt}\n({pct}%)', ha='center', va='center',
                        fontsize=7, fontweight='bold', color='white')
            left += width

    # Title
    ax.text(7, 7.5, 'CBDC Design Decision Matrix', ha='center', va='center',
            fontsize=14, fontweight='bold')

    # Legend
    ax.text(2, 0.8, 'Based on survey of 90+ central banks exploring CBDCs',
            ha='left', fontsize=10, style='italic', color='#666666')

    # Key considerations box
    box = mpatches.FancyBboxPatch((0.5, 1.5), 4, 1.5,
                                   boxstyle="round,pad=0.05",
                                   facecolor='#F5F5F5', edgecolor='#888888')
    ax.add_patch(box)
    ax.text(2.5, 2.7, 'Key Trade-offs', ha='center', va='center',
            fontsize=10, fontweight='bold')
    ax.text(2.5, 2.1, 'Privacy vs. AML compliance\nInnovation vs. Stability\nInclusion vs. Security',
            ha='center', va='center', fontsize=9)

    # Trends box
    box2 = mpatches.FancyBboxPatch((9, 1.5), 4.5, 1.5,
                                    boxstyle="round,pad=0.05",
                                    facecolor='#E6F3FF', edgecolor='#4A90E2')
    ax.add_patch(box2)
    ax.text(11.25, 2.7, 'Emerging Trends', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#4A90E2')
    ax.text(11.25, 2.1, 'Offline capability priority\nProgrammability interest\nInteroperability focus',
            ha='center', va='center', fontsize=9)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'cbdc_design_choices.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
