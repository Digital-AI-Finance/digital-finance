"""
Account Information Service (AIS) Flow
Shows how AIS providers access account data under PSD2

Output: ais_flow.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Account Information Service Flow',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ais_flow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create AIS flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Entities
    # Customer
    customer = mpatches.FancyBboxPatch((0.5, 4), 2, 2, boxstyle='round,pad=0.1',
                                        facecolor='#6B5B95', edgecolor='#333333', lw=2)
    ax.add_patch(customer)
    ax.text(1.5, 5, 'Customer', ha='center', va='center', fontsize=11,
           fontweight='bold', color='white')

    # AISP App
    aisp = mpatches.FancyBboxPatch((4, 4), 2, 2, boxstyle='round,pad=0.1',
                                    facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(aisp)
    ax.text(5, 5, 'AISP\nApp', ha='center', va='center', fontsize=11,
           fontweight='bold', color='white')

    # Bank API
    api = mpatches.FancyBboxPatch((7.5, 4), 2, 2, boxstyle='round,pad=0.1',
                                   facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(api)
    ax.text(8.5, 5, 'Bank\nAPI', ha='center', va='center', fontsize=11,
           fontweight='bold', color='white')

    # Bank
    bank = mpatches.FancyBboxPatch((10.5, 4), 2, 2, boxstyle='round,pad=0.1',
                                    facecolor='#333333', edgecolor='#333333', lw=2)
    ax.add_patch(bank)
    ax.text(11.5, 5, 'Bank\n(ASPSP)', ha='center', va='center', fontsize=11,
           fontweight='bold', color='white')

    # Flow arrows with numbered steps
    steps = [
        (1, 2.5, 4, 5, '1. Request\naccount access', '#6B5B95'),
        (2, 6, 5.8, 7.5, '2. Forward with\nconsent request', '#4A90E2'),
        (3, 9.5, 5.8, 10.5, '3. Redirect to\nbank login', '#FF7F0E'),
        (4, 11.5, 6.5, 11.5, '4. Customer\nauthenticates', '#333333'),
        (5, 10.5, 5, 9.5, '5. Return token', '#333333'),
        (6, 7.5, 4.2, 6, '6. Access token', '#FF7F0E'),
        (7, 6, 3.5, 7.5, '7. Request\naccount data', '#4A90E2'),
        (8, 9.5, 3.5, 10.5, '8. Return data', '#FF7F0E'),
    ]

    # Step 1: Customer to AISP
    ax.annotate('', xy=(4, 5), xytext=(2.5, 5),
               arrowprops=dict(arrowstyle='->', color='#6B5B95', lw=2))
    ax.text(3.25, 5.7, '1. Request\naccount view', fontsize=7, ha='center', color='#6B5B95')

    # Step 2: AISP to Bank API
    ax.annotate('', xy=(7.5, 5.5), xytext=(6, 5.5),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))
    ax.text(6.75, 6.3, '2. Request consent', fontsize=7, ha='center', color='#4A90E2')

    # Step 3: Bank API to Bank (auth redirect)
    ax.annotate('', xy=(10.5, 5.5), xytext=(9.5, 5.5),
               arrowprops=dict(arrowstyle='->', color='#FF7F0E', lw=2))
    ax.text(10, 6.3, '3. Auth', fontsize=7, ha='center', color='#FF7F0E')

    # Step 4: Customer authenticates (curved arrow from bank back to customer)
    ax.annotate('', xy=(1.5, 6), xytext=(11.5, 6.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2,
                              connectionstyle='arc3,rad=-0.3'))
    ax.text(6.5, 8, '4. Bank redirects customer for SCA', fontsize=8,
           ha='center', color='#44A044')

    # Step 5: Consent granted (back through system)
    ax.annotate('', xy=(6, 4.5), xytext=(7.5, 4.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(6.75, 3.8, '5. Access token', fontsize=7, ha='center', color='#44A044')

    # Step 6: AISP requests data
    ax.annotate('', xy=(7.5, 4), xytext=(6, 4),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))
    ax.text(6.75, 3.2, '6. GET /accounts', fontsize=7, ha='center', color='#4A90E2')

    # Step 7: Data returned
    ax.annotate('', xy=(6, 3.5), xytext=(7.5, 3.5),
               arrowprops=dict(arrowstyle='->', color='#FF7F0E', lw=2))
    ax.text(6.75, 2.7, '7. Account data', fontsize=7, ha='center', color='#FF7F0E')

    # Step 8: Display to customer
    ax.annotate('', xy=(2.5, 4.5), xytext=(4, 4.5),
               arrowprops=dict(arrowstyle='->', color='#6B5B95', lw=2))
    ax.text(3.25, 3.8, '8. Display', fontsize=7, ha='center', color='#6B5B95')

    # Title
    ax.text(6.5, 9.5, 'Account Information Service (AIS) Flow',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'Read-only access to account data',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Data types box
    data_types = """Data Accessible via AIS:
    - Account balances
    - Transaction history
    - Account details
    - Standing orders
    - Direct debits"""

    ax.text(0.5, 1.5, data_types, fontsize=8, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#E8F0FE', edgecolor='#4A90E2'))

    # Use cases
    use_cases = """Common Use Cases:
    - Account aggregation
    - Personal finance apps
    - Credit scoring
    - Accounting software"""

    ax.text(12.5, 1.5, use_cases, fontsize=8, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL FLOW DIAGRAM]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ais_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
