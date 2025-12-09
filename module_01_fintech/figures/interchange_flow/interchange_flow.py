"""
Interchange Fee Flow Diagram
Shows how interchange fees flow between parties in card transactions

Output: interchange_flow.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Interchange Fee Flow',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/interchange_flow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create interchange fee flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Entities
    entities = [
        ('Customer', 1.5, 5, '#4A90E2'),
        ('Neobank\n(Issuer)', 4, 5, '#333333'),
        ('Card\nNetwork', 6.5, 5, '#FF7F0E'),
        ('Acquirer', 9, 5, '#44A044'),
        ('Merchant', 11.5, 5, '#6B5B95'),
    ]

    # Draw entities
    for name, x, y, color in entities:
        rect = mpatches.FancyBboxPatch((x-0.8, y-0.6), 1.6, 1.2,
                                        boxstyle='round,pad=0.05',
                                        facecolor=color, edgecolor='#333333', lw=1.5)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')

    # Transaction flow (top arrows)
    ax.annotate('', xy=(3.1, 5.8), xytext=(2.4, 5.8),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(2.75, 6.2, '1. Swipe/Tap\nCard', ha='center', fontsize=8)

    ax.annotate('', xy=(5.6, 5.8), xytext=(4.9, 5.8),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(5.25, 6.2, '2. Auth\nRequest', ha='center', fontsize=8)

    ax.annotate('', xy=(8.1, 5.8), xytext=(7.4, 5.8),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(7.75, 6.2, '3. Route', ha='center', fontsize=8)

    ax.annotate('', xy=(10.6, 5.8), xytext=(9.9, 5.8),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(10.25, 6.2, '4. Capture', ha='center', fontsize=8)

    # Money flow (bottom arrows - reverse direction)
    ax.annotate('', xy=(2.4, 4.2), xytext=(3.1, 4.2),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    ax.annotate('', xy=(4.9, 4.2), xytext=(5.6, 4.2),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    ax.annotate('', xy=(7.4, 4.2), xytext=(8.1, 4.2),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    ax.annotate('', xy=(9.9, 4.2), xytext=(10.6, 4.2),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))

    # Fee breakdown box
    fee_box = """Fee Breakdown (typical $100 transaction):

    Merchant pays: $2.50 (2.5% MDR)

    Distribution:
    - Interchange to Issuer: $1.80 (1.8%)
    - Network fee: $0.20 (0.2%)
    - Acquirer margin: $0.50 (0.5%)

    EU Interchange Cap: 0.3% credit, 0.2% debit
    (EU Interchange Regulation 2015/751)"""

    ax.text(6.5, 1.8, fee_box, ha='center', va='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'),
           family='monospace')

    # Why this matters for neobanks
    neobank_box = """Why Interchange Matters for Neobanks:
    - Primary revenue source (40-70% of revenue)
    - Higher spend = higher revenue
    - Premium cards = higher interchange
    - EU caps limit European neobanks"""

    ax.text(11, 8, neobank_box, ha='right', va='top', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Title
    ax.text(6.5, 9.5, 'Card Payment Interchange Flow', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'How neobanks earn revenue from card transactions', fontsize=10,
           ha='center', style='italic', color='#666666')

    # Money flow label
    ax.text(6.5, 3.6, 'Settlement & Fee Flow', fontsize=9, ha='center',
           style='italic', color='#44A044')

    # Source
    ax.text(6.5, 0.3, 'Source: EU Regulation 2015/751, Visa/Mastercard published rates',
           fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'interchange_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
