"""
Tax-Loss Harvesting
Shows how robo-advisors implement tax-loss harvesting

Output: tax_loss_harvesting.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Tax-Loss Harvesting',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/tax_loss_harvesting'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create tax-loss harvesting diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Tax-Loss Harvesting', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Automated Tax Optimization Strategy', fontsize=12, ha='center',
           style='italic', color='#666666')

    # Process flow
    # Step 1: Identify loss
    step1 = mpatches.FancyBboxPatch((0.5, 4.5), 3.5, 3, boxstyle='round,pad=0.1',
                                     facecolor='#D62728', alpha=0.2,
                                     edgecolor='#D62728', lw=2)
    ax.add_patch(step1)
    ax.text(2.25, 7, '1. Identify Loss', ha='center', fontsize=13, fontweight='bold', color='#D62728')
    ax.text(2.25, 6, 'VTI down 10%', ha='center', fontsize=12)
    ax.text(2.25, 5.4, '$10K position', ha='center', fontsize=12)
    ax.text(2.25, 4.8, '= $1K loss', ha='center', fontsize=12, fontweight='bold')

    ax.annotate('', xy=(4.5, 6), xytext=(4.1, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Step 2: Sell & Replace
    step2 = mpatches.FancyBboxPatch((4.8, 4.5), 4, 3, boxstyle='round,pad=0.1',
                                     facecolor='#FF7F0E', alpha=0.2,
                                     edgecolor='#FF7F0E', lw=2)
    ax.add_patch(step2)
    ax.text(6.8, 7, '2. Sell & Replace', ha='center', fontsize=13, fontweight='bold', color='#FF7F0E')
    ax.text(6.8, 6, 'Sell: VTI (Vanguard)', ha='center', fontsize=12)
    ax.text(6.8, 5.4, 'Buy: ITOT (iShares)', ha='center', fontsize=12)
    ax.text(6.8, 4.8, 'Similar exposure', ha='center', fontsize=11, style='italic')

    ax.annotate('', xy=(9.3, 6), xytext=(8.9, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Step 3: Tax benefit
    step3 = mpatches.FancyBboxPatch((9.5, 4.5), 4, 3, boxstyle='round,pad=0.1',
                                     facecolor='#44A044', alpha=0.2,
                                     edgecolor='#44A044', lw=2)
    ax.add_patch(step3)
    ax.text(11.5, 7, '3. Tax Benefit', ha='center', fontsize=13, fontweight='bold', color='#44A044')
    ax.text(11.5, 6, '$1K loss offsets gains', ha='center', fontsize=12)
    ax.text(11.5, 5.4, 'Tax savings: $200-370', ha='center', fontsize=12)
    ax.text(11.5, 4.8, '(at 20-37% rate)', ha='center', fontsize=11, style='italic')

    # Rules box
    rules = """Key Rules:
    - Wash Sale Rule: Cannot repurchase
      "substantially identical" security
      within 30 days before/after sale
    - Works for taxable accounts only
    - Losses can offset gains + $3K income"""

    ax.text(2.5, 3, rules, fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Robo benefit
    robo = """Robo-Advisor Advantage:
    - Daily monitoring for opportunities
    - Automatic execution
    - Wash sale compliance
    - Can add 0.5-1.0% annual return"""

    ax.text(11.5, 3, robo, fontsize=11, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: IRS Publication 550, Industry estimates',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'tax_loss_harvesting.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
