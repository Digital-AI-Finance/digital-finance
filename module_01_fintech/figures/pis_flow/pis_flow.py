"""
Payment Initiation Service (PIS) Flow
Shows how PISPs initiate payments under PSD2

Output: pis_flow.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Payment Initiation Service Flow',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/pis_flow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create PIS flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Entities arranged horizontally
    # Customer
    customer = mpatches.FancyBboxPatch((0.3, 5), 1.8, 1.5, boxstyle='round,pad=0.1',
                                        facecolor='#6B5B95', edgecolor='#333333', lw=2)
    ax.add_patch(customer)
    ax.text(1.2, 5.75, 'Customer', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # Merchant
    merchant = mpatches.FancyBboxPatch((3, 5), 1.8, 1.5, boxstyle='round,pad=0.1',
                                        facecolor='#D62728', edgecolor='#333333', lw=2)
    ax.add_patch(merchant)
    ax.text(3.9, 5.75, 'Merchant', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # PISP
    pisp = mpatches.FancyBboxPatch((5.7, 5), 1.8, 1.5, boxstyle='round,pad=0.1',
                                    facecolor='#44A044', edgecolor='#333333', lw=2)
    ax.add_patch(pisp)
    ax.text(6.6, 5.75, 'PISP', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # Bank API
    api = mpatches.FancyBboxPatch((8.4, 5), 1.8, 1.5, boxstyle='round,pad=0.1',
                                   facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(api)
    ax.text(9.3, 5.75, 'Bank API', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # Bank
    bank = mpatches.FancyBboxPatch((11.1, 5), 1.8, 1.5, boxstyle='round,pad=0.1',
                                    facecolor='#333333', edgecolor='#333333', lw=2)
    ax.add_patch(bank)
    ax.text(12, 5.75, 'Bank', ha='center', va='center', fontsize=10,
           fontweight='bold', color='white')

    # Flow steps (numbered)
    # Step 1: Customer initiates checkout
    ax.annotate('', xy=(3, 5.75), xytext=(2.1, 5.75),
               arrowprops=dict(arrowstyle='->', color='#6B5B95', lw=2))
    ax.text(2.55, 6.3, '1. Checkout', fontsize=7, ha='center', color='#6B5B95')

    # Step 2: Merchant calls PISP
    ax.annotate('', xy=(5.7, 5.75), xytext=(4.8, 5.75),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2))
    ax.text(5.25, 6.3, '2. Init payment', fontsize=7, ha='center', color='#D62728')

    # Step 3: PISP calls bank API
    ax.annotate('', xy=(8.4, 5.75), xytext=(7.5, 5.75),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(7.95, 6.3, '3. POST /payments', fontsize=7, ha='center', color='#44A044')

    # Step 4: Bank API to Bank
    ax.annotate('', xy=(11.1, 5.75), xytext=(10.2, 5.75),
               arrowprops=dict(arrowstyle='->', color='#FF7F0E', lw=2))
    ax.text(10.65, 6.3, '4. Process', fontsize=7, ha='center', color='#FF7F0E')

    # Step 5: SCA redirect (curved arrow back to customer)
    ax.annotate('', xy=(1.2, 6.5), xytext=(12, 6.5),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2,
                              connectionstyle='arc3,rad=-0.25'))
    ax.text(6.6, 8, '5. Redirect customer for bank authentication (SCA)',
           fontsize=9, ha='center', color='#4A90E2', fontweight='bold')

    # Step 6: Payment execution (below the main flow)
    ax.annotate('', xy=(7.5, 4.5), xytext=(10.2, 4.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(8.85, 4, '6. Payment confirmed', fontsize=7, ha='center', color='#44A044')

    # Step 7: Status to merchant
    ax.annotate('', xy=(4.8, 4.5), xytext=(5.7, 4.5),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2))
    ax.text(5.25, 4, '7. Status callback', fontsize=7, ha='center', color='#D62728')

    # Step 8: Confirmation to customer
    ax.annotate('', xy=(2.1, 4.5), xytext=(3, 4.5),
               arrowprops=dict(arrowstyle='->', color='#6B5B95', lw=2))
    ax.text(2.55, 4, '8. Confirmation', fontsize=7, ha='center', color='#6B5B95')

    # Title
    ax.text(6.5, 9.5, 'Payment Initiation Service (PIS) Flow',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'Bank-to-bank transfer via open banking',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Comparison box
    comparison = """PIS vs Card Payment:
    - No interchange fees (0% vs 1.5-3%)
    - Direct bank transfer (instant settlement)
    - Irrevocable (no chargebacks)
    - Lower fraud risk"""

    ax.text(0.3, 2.5, comparison, fontsize=8, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Use cases
    use_cases = """PIS Use Cases:
    - E-commerce checkout
    - Bill payments
    - Account funding
    - Recurring payments"""

    ax.text(12.7, 2.5, use_cases, fontsize=8, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL FLOW DIAGRAM]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'pis_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
