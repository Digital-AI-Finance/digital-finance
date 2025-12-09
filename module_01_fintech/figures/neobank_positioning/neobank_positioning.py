"""
Neobank Market Positioning Map
Shows how different neobanks position themselves in the market

Output: neobank_positioning.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank Market Positioning',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/neobank_positioning'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank positioning scatter plot"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Positioning data: (name, simplicity, product_breadth, size_bubble, color, segment)
    neobanks = [
        ('Chime', 4.5, 2, 800, '#44A044', 'Mass Market'),
        ('Revolut', 3, 5, 900, '#333333', 'Super App'),
        ('N26', 4, 3, 500, '#4A90E2', 'Premium'),
        ('Monzo', 4.2, 3.5, 450, '#FF7F0E', 'Premium'),
        ('Nubank', 4.3, 4, 1000, '#6B5B95', 'Mass Market'),
        ('Cash App', 4.5, 3.5, 700, '#44A044', 'P2P/Mass'),
        ('Starling', 3.5, 4, 300, '#D62728', 'SMB Focus'),
        ('Mercury', 2.5, 3, 200, '#999999', 'Startup/SMB'),
        ('Current', 4.2, 2.5, 250, '#4A90E2', 'Mass Market'),
        ('Greenlight', 4, 2, 200, '#FF7F0E', 'Kids/Family'),
    ]

    # Quadrant dividers
    ax.axhline(y=3, color='#CCCCCC', linestyle='--', lw=1.5, zorder=1)
    ax.axvline(x=3.5, color='#CCCCCC', linestyle='--', lw=1.5, zorder=1)

    # Plot neobanks
    for name, simplicity, breadth, size, color, segment in neobanks:
        ax.scatter(simplicity, breadth, s=size, c=color, edgecolor='#333333',
                  lw=1.5, alpha=0.8, zorder=3)
        ax.annotate(name, (simplicity, breadth), xytext=(5, 5),
                   textcoords='offset points', fontsize=9, fontweight='bold')

    # Quadrant labels
    ax.text(2.2, 4.8, 'Complex &\nFull-Featured', fontsize=10, ha='center',
           fontweight='bold', color='#6B5B95', alpha=0.7)
    ax.text(4.5, 4.8, 'Simple &\nFull-Featured', fontsize=10, ha='center',
           fontweight='bold', color='#44A044', alpha=0.7)
    ax.text(2.2, 1.5, 'Complex &\nFocused', fontsize=10, ha='center',
           fontweight='bold', color='#999999', alpha=0.7)
    ax.text(4.5, 1.5, 'Simple &\nFocused', fontsize=10, ha='center',
           fontweight='bold', color='#4A90E2', alpha=0.7)

    ax.set_xlabel('Simplicity of Experience (1=Complex, 5=Simple)', fontsize=11)
    ax.set_ylabel('Product Breadth (1=Focused, 5=Comprehensive)', fontsize=11)
    ax.set_xlim(1.5, 5.5)
    ax.set_ylim(1, 5.5)

    ax.set_title('Neobank Market Positioning Map', fontsize=14, fontweight='bold', pad=15)

    # Legend for bubble size
    ax.text(5.3, 1.3, 'Bubble size = Customers', fontsize=8, style='italic')

    # Segment legend
    legend_elements = [
        mpatches.Patch(facecolor='#44A044', edgecolor='#333333', label='Mass Market'),
        mpatches.Patch(facecolor='#4A90E2', edgecolor='#333333', label='Premium/Focused'),
        mpatches.Patch(facecolor='#333333', edgecolor='#333333', label='Super App'),
        mpatches.Patch(facecolor='#D62728', edgecolor='#333333', label='SMB Focus'),
        mpatches.Patch(facecolor='#FF7F0E', edgecolor='#333333', label='Niche/Family'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8, title='Segments')

    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Source
    fig.text(0.5, 0.02, 'Source: Author analysis based on product offerings and market positioning',
            fontsize=7, ha='center', style='italic', color='#666666')

    # Synthetic label
    fig.text(0.98, 0.02, '[ILLUSTRATIVE POSITIONING]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'neobank_positioning.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
