"""
Fractional Shares Flow
Shows how fractional share investing works

Output: fractional_shares_flow.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Fractional Shares Flow',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fractional_shares_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create fractional shares flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Fractional Shares: Own Any Stock', fontsize=20, fontweight='bold', ha='center')

    # Traditional vs Fractional
    ax.text(3.5, 8, 'Traditional', fontsize=15, fontweight='bold', ha='center', color='#D62728')
    ax.text(10.5, 8, 'Fractional', fontsize=15, fontweight='bold', ha='center', color='#44A044')

    # Traditional side
    trad_box = mpatches.FancyBboxPatch((1, 5), 5, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#D62728', alpha=0.1,
                                        edgecolor='#D62728', lw=2)
    ax.add_patch(trad_box)
    ax.text(3.5, 7, 'Amazon Stock: USD 180/share', ha='center', fontsize=12)
    ax.text(3.5, 6.3, 'You have: USD 50', ha='center', fontsize=12)
    ax.text(3.5, 5.5, 'Result: Cannot buy', ha='center', fontsize=14, fontweight='bold', color='#D62728')

    # Fractional side
    frac_box = mpatches.FancyBboxPatch((8, 5), 5, 2.5,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#44A044', alpha=0.1,
                                        edgecolor='#44A044', lw=2)
    ax.add_patch(frac_box)
    ax.text(10.5, 7, 'Amazon Stock: USD 180/share', ha='center', fontsize=12)
    ax.text(10.5, 6.3, 'You have: USD 50', ha='center', fontsize=12)
    ax.text(10.5, 5.5, 'Result: Buy 0.278 shares!', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    # How it works
    ax.text(7, 4, 'How Fractional Shares Work:', fontsize=14, fontweight='bold', ha='center')

    methods = [
        {'method': 'Broker Inventory', 'desc': 'Broker buys full shares, sells fractions', 'x': 3.5},
        {'method': 'Omnibus Account', 'desc': 'Pooled holdings, book-entry ownership', 'x': 10.5},
    ]

    for m in methods:
        box = mpatches.FancyBboxPatch((m['x']-2, 2), 4, 1.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=1.5)
        ax.add_patch(box)
        ax.text(m['x'], 3.2, m['method'], ha='center', fontsize=12, fontweight='bold')
        ax.text(m['x'], 2.5, m['desc'], ha='center', fontsize=10)

    # Impact
    impact = "Impact: 62% of Gen Z investors started with fractional shares"
    ax.text(7, 0.8, impact, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[ILLUSTRATIVE EXAMPLE]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'fractional_shares_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
