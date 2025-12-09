"""
Giveback Model
Shows Lemonade's unique giveback charity model

Output: giveback_model.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Giveback Model',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/giveback_model'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create giveback model flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, "Lemonade's Giveback Model", fontsize=20, fontweight='bold', ha='center')

    # Premium flow
    # Customer pays premium
    customer_box = mpatches.FancyBboxPatch((0.5, 5.5), 2.5, 2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#4A90E2', alpha=0.2,
                                           edgecolor='#4A90E2', lw=2)
    ax.add_patch(customer_box)
    ax.text(1.75, 6.5, 'Customer\nPays Premium', ha='center', va='center',
           fontsize=13, fontweight='bold')
    ax.text(1.75, 5.8, '$100', ha='center', fontsize=14, fontweight='bold', color='#4A90E2')

    # Arrow to Lemonade
    ax.annotate('', xy=(3.8, 6.5), xytext=(3.1, 6.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Lemonade takes flat fee
    lemonade_box = mpatches.FancyBboxPatch((4, 5), 3, 3,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#FF69B4', alpha=0.2,
                                            edgecolor='#FF69B4', lw=2)
    ax.add_patch(lemonade_box)
    ax.text(5.5, 7.5, 'Lemonade', ha='center', fontsize=14, fontweight='bold', color='#FF69B4')
    ax.text(5.5, 6.8, 'Takes 25%', ha='center', fontsize=12)
    ax.text(5.5, 6.2, 'Flat Fee', ha='center', fontsize=12)
    ax.text(5.5, 5.5, '= $25', ha='center', fontsize=14, fontweight='bold', color='#FF69B4')

    # Remaining goes to pool
    ax.annotate('', xy=(7.8, 6.5), xytext=(7.1, 6.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Claims pool
    pool_box = mpatches.FancyBboxPatch((8, 5), 2.5, 3,
                                        boxstyle='round,pad=0.1',
                                        facecolor='#44A044', alpha=0.2,
                                        edgecolor='#44A044', lw=2)
    ax.add_patch(pool_box)
    ax.text(9.25, 7.5, 'Claims Pool', ha='center', fontsize=14, fontweight='bold', color='#44A044')
    ax.text(9.25, 6.8, 'Reinsurance', ha='center', fontsize=12)
    ax.text(9.25, 6.2, '+ Claims', ha='center', fontsize=12)
    ax.text(9.25, 5.5, '$75', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    # Unclaimed -> Charity
    ax.annotate('', xy=(12.2, 6.5), xytext=(10.6, 6.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    charity_box = mpatches.FancyBboxPatch((11.5, 5.5), 2, 2,
                                          boxstyle='round,pad=0.1',
                                          facecolor='#FFD700', alpha=0.3,
                                          edgecolor='#FFD700', lw=2)
    ax.add_patch(charity_box)
    ax.text(12.5, 6.8, 'Giveback', ha='center', fontsize=13, fontweight='bold', color='#B8860B')
    ax.text(12.5, 6.2, 'Charity', ha='center', fontsize=12)
    ax.text(12.5, 5.8, 'Donation', ha='center', fontsize=11)

    # Key insight box
    insight = """Why It Works:
    1. Removes conflict of interest - Lemonade earns same fee regardless of claims
    2. Reduces fraud - customers less likely to defraud their chosen charity
    3. Creates community - policyholders grouped by charity preference
    4. Social impact - $10M+ donated since 2017"""

    ax.text(7, 2.8, insight, ha='center', fontsize=12, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Lemonade Giveback Report (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'giveback_model.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
