"""
Revolut Product Ecosystem
Shows the range of products and services offered by Revolut

Output: revolut_products.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Revolut Product Ecosystem',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/revolut_products'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create Revolut product ecosystem chart"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Center: Revolut core
    center = mpatches.FancyBboxPatch((4.5, 4), 3, 2, boxstyle='round,pad=0.1',
                                      facecolor='#333333', edgecolor='none')
    ax.add_patch(center)
    ax.text(6, 5, 'REVOLUT\nCore App', ha='center', va='center',
           fontsize=14, fontweight='bold', color='white')

    # Product categories with their products
    categories = [
        # Top row
        ('Banking', 2, 8, ['Current Account', 'Savings Vaults', 'Joint Accounts', 'Business Accounts'],
         '#4A90E2'),
        ('Payments', 6, 8.5, ['P2P Transfers', 'International', 'Bill Split', 'Request Money'],
         '#44A044'),
        ('Trading', 10, 8, ['Stocks', 'Crypto', 'Commodities', 'Options'],
         '#FF7F0E'),

        # Bottom row
        ('Insurance', 1.5, 1.5, ['Travel', 'Device', 'Medical', 'Pet'],
         '#6B5B95'),
        ('Lifestyle', 5, 0.8, ['Lounges', 'Cashback', 'Rewards', 'Concierge'],
         '#D62728'),
        ('Premium', 8.5, 1.5, ['Metal Card', 'Priority Support', 'Exclusive Rates', 'Higher Limits'],
         '#999999'),
    ]

    for cat_name, x, y, products, color in categories:
        # Category box
        box = mpatches.FancyBboxPatch((x-1.3, y-0.8), 2.6, 1.6, boxstyle='round,pad=0.05',
                                       facecolor=color, edgecolor='none', alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y+0.3, cat_name, ha='center', va='center',
               fontsize=11, fontweight='bold', color='white')

        # Products list
        products_text = '\n'.join([f'- {p}' for p in products])
        ax.text(x, y-0.3, products_text, ha='center', va='top',
               fontsize=7, color='white')

        # Connection line to center
        if y > 5:
            ax.annotate('', xy=(6, 6), xytext=(x, y-0.8),
                       arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=1.5))
        else:
            ax.annotate('', xy=(6, 4), xytext=(x, y+0.8),
                       arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=1.5))

    # Stats box
    stats = """Key Metrics (2024):
    - 45M+ customers globally
    - 38 countries
    - $45B+ valued
    - Banking licenses: UK, EU, US"""

    ax.text(11.5, 5, stats, fontsize=8, ha='right', va='center',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Title
    ax.text(6, 9.5, 'Revolut: From Neobank to Financial Super App',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6, 9.1, 'Product ecosystem evolution since 2015',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Synthetic label
    ax.text(11.8, 0.3, '[ILLUSTRATIVE]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'revolut_products.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
