"""
Open Banking Concept Overview
Illustrates the fundamental concept of open banking and data sharing

Output: open_banking_concept.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking Concept',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/open_banking_concept'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open banking concept diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Customer at center
    customer_circle = mpatches.Circle((6.5, 5), 1, facecolor='#4A90E2',
                                       edgecolor='#333333', lw=2)
    ax.add_patch(customer_circle)
    ax.text(6.5, 5, 'Customer', ha='center', va='center', fontsize=11,
           fontweight='bold', color='white')
    ax.text(6.5, 4, 'Owns\nTheir Data', ha='center', va='top', fontsize=8,
           color='#4A90E2')

    # Traditional banks (left)
    banks = [
        ('Bank A', 1.5, 7),
        ('Bank B', 1.5, 5),
        ('Bank C', 1.5, 3),
    ]

    for name, x, y in banks:
        rect = mpatches.FancyBboxPatch((x-0.7, y-0.5), 1.4, 1,
                                        boxstyle='round,pad=0.05',
                                        facecolor='#333333', edgecolor='none')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')

    # Third-party providers (right)
    tpps = [
        ('Budgeting\nApp', 11.5, 8, '#44A044'),
        ('Payment\nInitiator', 11.5, 6, '#FF7F0E'),
        ('Lending\nPlatform', 11.5, 4, '#6B5B95'),
        ('Investment\nApp', 11.5, 2, '#D62728'),
    ]

    for name, x, y, color in tpps:
        rect = mpatches.FancyBboxPatch((x-0.8, y-0.6), 1.6, 1.2,
                                        boxstyle='round,pad=0.05',
                                        facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=8,
               fontweight='bold', color='white')

    # API layer in middle
    api_box = mpatches.FancyBboxPatch((4, 2), 5, 6,
                                       boxstyle='round,pad=0.1',
                                       facecolor='none', edgecolor='#4A90E2',
                                       lw=2, linestyle='--')
    ax.add_patch(api_box)
    ax.text(6.5, 8.3, 'Open Banking APIs', ha='center', fontsize=11,
           fontweight='bold', color='#4A90E2')

    # Arrows from banks to customer (through API)
    for name, x, y in banks:
        ax.annotate('', xy=(5.5, 5), xytext=(x+0.7, y),
                   arrowprops=dict(arrowstyle='->', color='#999999', lw=1.5,
                                  connectionstyle='arc3,rad=0.1'))

    # Arrows from customer to TPPs (through API)
    for name, x, y, color in tpps:
        ax.annotate('', xy=(x-0.8, y), xytext=(7.5, 5),
                   arrowprops=dict(arrowstyle='->', color=color, lw=1.5,
                                  connectionstyle='arc3,rad=-0.1'))

    # Key concepts box
    concepts = """Key Principles:
    1. Customer consent required
    2. Standardized APIs (not screen scraping)
    3. Strong authentication (SCA)
    4. Regulated third parties
    5. Data minimization"""

    ax.text(3.5, 0.8, concepts, fontsize=8, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Benefits box
    benefits = """Customer Benefits:
    - Unified view of finances
    - Better product comparison
    - Innovative services
    - Greater control"""

    ax.text(9.5, 0.8, benefits, fontsize=8, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Title
    ax.text(6.5, 9.7, 'Open Banking: Customer-Centric Financial Data Sharing',
           fontsize=14, fontweight='bold', ha='center')

    # Data flow labels
    ax.text(3, 6.5, 'Account\nData', fontsize=7, ha='center', color='#999999')
    ax.text(10, 7, 'With\nConsent', fontsize=7, ha='center', color='#44A044')

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL DIAGRAM]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'open_banking_concept.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
