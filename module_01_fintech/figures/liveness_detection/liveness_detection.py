"""
Liveness Detection Methods
Compares active vs passive liveness detection approaches

Output: liveness_detection.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Liveness Detection Methods',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/liveness_detection'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create liveness detection comparison chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Liveness Detection Methods', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'Preventing Presentation Attacks', fontsize=10, ha='center',
           style='italic', color='#666666')

    # Active Liveness
    active_box = mpatches.FancyBboxPatch((0.5, 4), 5.5, 4.5, boxstyle='round,pad=0.1',
                                          facecolor='#4A90E2', alpha=0.15,
                                          edgecolor='#4A90E2', lw=2)
    ax.add_patch(active_box)
    ax.text(3.25, 8, 'Active Liveness', ha='center', fontsize=12, fontweight='bold', color='#4A90E2')

    active_methods = [
        ('Challenge-Response', 'User performs actions on demand'),
        ('Blink detection', 'Ask user to blink eyes'),
        ('Head movement', 'Turn head left/right/up/down'),
        ('Smile/expression', 'Change facial expression'),
        ('Random prompts', 'Speak numbers or words'),
    ]
    for i, (method, desc) in enumerate(active_methods):
        ax.text(1, 7.2-i*0.6, f'* {method}:', fontsize=8, fontweight='bold')
        ax.text(3.5, 7.2-i*0.6, desc, fontsize=8)

    # Passive Liveness
    passive_box = mpatches.FancyBboxPatch((7, 4), 5.5, 4.5, boxstyle='round,pad=0.1',
                                           facecolor='#44A044', alpha=0.15,
                                           edgecolor='#44A044', lw=2)
    ax.add_patch(passive_box)
    ax.text(9.75, 8, 'Passive Liveness', ha='center', fontsize=12, fontweight='bold', color='#44A044')

    passive_methods = [
        ('Texture analysis', 'Detect screen/paper patterns'),
        ('3D depth mapping', 'Verify face dimensionality'),
        ('Motion analysis', 'Natural micro-movements'),
        ('Light reflection', 'Eye/skin reflection patterns'),
        ('ML/AI detection', 'Deep learning classifiers'),
    ]
    for i, (method, desc) in enumerate(passive_methods):
        ax.text(7.5, 7.2-i*0.6, f'* {method}:', fontsize=8, fontweight='bold')
        ax.text(10, 7.2-i*0.6, desc, fontsize=8)

    # Comparison table
    comparison = [
        ['Aspect', 'Active', 'Passive'],
        ['User friction', 'Higher', 'Lower'],
        ['Time required', '5-15 sec', '1-3 sec'],
        ['Spoof resistance', 'High', 'Medium-High'],
        ['Accessibility', 'Limited', 'Better'],
        ['Drop-off rate', '10-20%', '2-5%'],
    ]

    table_y = 3.2
    for i, row in enumerate(comparison):
        color = '#E8E8E8' if i == 0 else ('white' if i % 2 == 1 else '#F8F8F8')
        weight = 'bold' if i == 0 else 'normal'
        ax.add_patch(mpatches.Rectangle((3, table_y-i*0.5), 7, 0.5,
                                         facecolor=color, edgecolor='#CCCCCC'))
        ax.text(4.5, table_y-i*0.5+0.25, row[0], ha='center', va='center', fontsize=8, fontweight=weight)
        ax.text(7, table_y-i*0.5+0.25, row[1], ha='center', va='center', fontsize=8, fontweight=weight,
               color='#4A90E2' if i > 0 else 'black')
        ax.text(9.5, table_y-i*0.5+0.25, row[2], ha='center', va='center', fontsize=8, fontweight=weight,
               color='#44A044' if i > 0 else 'black')

    # Attack types
    attacks = "Common Attacks: Photo attacks | Video replay | 3D masks | Deepfakes | Screen replay"
    ax.text(6.5, 0.5, attacks, ha='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: Industry liveness detection standards (ISO/IEC 30107)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'liveness_detection.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
