"""
Client Segmentation
Wealth management client tiers

Output: client_segmentation.pdf
Module: module_04_trad_finance
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Client Segmentation',
    'module': 'module_04_trad_finance',
    'lesson': 46,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/client_segmentation'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Client pyramid
    ax1 = axes[0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    # Pyramid segments
    segments = [
        ('UHNW\n>$30M', 1, 8, 2, 1, '#D62728', '0.5%', '$350K'),
        ('HNW\n$1-30M', 2, 6.2, 4, 1.3, '#FF7F0E', '4%', '$15K'),
        ('Affluent\n$250K-1M', 3, 4, 6, 1.7, '#9B59B6', '15%', '$3K'),
        ('Mass Affluent\n$100-250K', 4, 1.5, 8, 2, '#4A90E2', '30%', '$500'),
        ('Mass Market\n<$100K', 4.5, -1, 9, 2, '#44A044', '50%', '<$100'),
    ]

    for name, x, y, width, height, color, pct, rev in segments:
        # Draw trapezoid
        from matplotlib.patches import Polygon
        pts = np.array([
            [5 - width/2, y],
            [5 + width/2, y],
            [5 + width/2 - 0.5, y + height],
            [5 - width/2 + 0.5, y + height]
        ])
        poly = Polygon(pts, facecolor=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax1.add_patch(poly)
        ax1.text(5, y + height/2, name, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

        # Add stats on right
        ax1.text(9.5, y + height/2 + 0.3, f'Pop: {pct}', ha='right', fontsize=9, color=color)
        ax1.text(9.5, y + height/2 - 0.3, f'Rev/client: {rev}', ha='right', fontsize=8, color='#666666')

    ax1.text(5, 9.5, 'Client Wealth Pyramid', ha='center', fontsize=12, fontweight='bold')

    # Service model by segment
    ax2 = axes[1]

    segments = ['UHNW', 'HNW', 'Affluent', 'Mass\nAffluent', 'Mass\nMarket']
    human_touch = [95, 80, 50, 20, 5]
    digital = [5, 20, 50, 80, 95]

    x = np.arange(len(segments))
    width = 0.6

    ax2.bar(x, human_touch, width, label='Human-Led', color='#4A90E2', alpha=0.8)
    ax2.bar(x, digital, width, bottom=human_touch, label='Digital/Robo', color='#44A044', alpha=0.8)

    ax2.set_ylabel('Service Mix (%)', fontsize=11)
    ax2.set_title('Service Model by Segment', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(segments, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 110)

    # Add labels
    for i, (h, d) in enumerate(zip(human_touch, digital)):
        ax2.text(i, h/2, f'{h}%', ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        ax2.text(i, h + d/2, f'{d}%', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

    fig.suptitle('Wealth Management Client Segmentation', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'client_segmentation.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
