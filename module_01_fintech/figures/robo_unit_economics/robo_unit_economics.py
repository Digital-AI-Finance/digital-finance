"""
Robo-Advisor Unit Economics
Shows the business economics of robo-advisory platforms

Output: robo_unit_economics.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Robo Unit Economics',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/robo_unit_economics'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create robo unit economics diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Robo-Advisor Unit Economics', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, '(Per $100K AUM Account)', fontsize=12, ha='center', style='italic', color='#666666')

    # Revenue (left)
    rev_box = mpatches.FancyBboxPatch((0.5, 3.5), 4, 4.5, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.2,
                                       edgecolor='#44A044', lw=2)
    ax.add_patch(rev_box)
    ax.text(2.5, 7.5, 'REVENUE', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    revenues = [
        ('Management fee (0.25%)', '$250/year'),
        ('Premium tier (if)', '+$100-200'),
        ('Cash sweep interest', '+$50-100'),
    ]
    for i, (item, amount) in enumerate(revenues):
        ax.text(0.8, 6.8-i*0.8, item, fontsize=11)
        ax.text(4.2, 6.8-i*0.8, amount, fontsize=11, ha='right', color='#44A044', fontweight='bold')

    ax.text(2.5, 4.2, 'Total: $300-450/year', ha='center', fontsize=13, fontweight='bold', color='#44A044')

    # Costs (center)
    cost_box = mpatches.FancyBboxPatch((5, 3.5), 4, 4.5, boxstyle='round,pad=0.1',
                                        facecolor='#D62728', alpha=0.2,
                                        edgecolor='#D62728', lw=2)
    ax.add_patch(cost_box)
    ax.text(7, 7.5, 'COSTS', ha='center', fontsize=14, fontweight='bold', color='#D62728')

    costs = [
        ('Customer acquisition', '$150-300'),
        ('Tech infrastructure', '$30-50'),
        ('Compliance/regulatory', '$20-30'),
        ('Customer support', '$20-40'),
    ]
    for i, (item, amount) in enumerate(costs):
        ax.text(5.3, 6.8-i*0.8, item, fontsize=11)
        ax.text(8.7, 6.8-i*0.8, amount, fontsize=11, ha='right', color='#D62728', fontweight='bold')

    ax.text(7, 4.2, 'Year 1: $220-420', ha='center', fontsize=13, fontweight='bold', color='#D62728')

    # Profitability (right)
    profit_box = mpatches.FancyBboxPatch((9.5, 3.5), 4, 4.5, boxstyle='round,pad=0.1',
                                          facecolor='#4A90E2', alpha=0.2,
                                          edgecolor='#4A90E2', lw=2)
    ax.add_patch(profit_box)
    ax.text(11.5, 7.5, 'PROFITABILITY', ha='center', fontsize=14, fontweight='bold', color='#4A90E2')

    profits = [
        ('Year 1', 'Break-even to loss'),
        ('Year 2', 'Marginally profitable'),
        ('Year 3+', '$150-250/year profit'),
        ('LTV:CAC', '3-5x (target)'),
    ]
    for i, (period, status) in enumerate(profits):
        ax.text(9.8, 6.8-i*0.8, f'{period}:', fontsize=11, fontweight='bold')
        ax.text(11, 6.8-i*0.8, status, fontsize=11)

    # Key insight
    insight = """Key Insight: Profitability requires scale ($50B+ AUM) and customer retention (5+ years)
    Average account size matters: $5K account = unprofitable | $100K+ = profitable"""

    ax.text(7, 2, insight, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: Industry analysis [ILLUSTRATIVE]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'robo_unit_economics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
