"""
Account Aggregation Flow
Shows how account aggregation works through open banking APIs

Output: account_aggregation_flow.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Account Aggregation Flow',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/account_aggregation_flow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create account aggregation flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Account Aggregation: Multi-Bank View', fontsize=14, fontweight='bold', ha='center')

    # User at center-left
    user_circle = mpatches.Circle((1.5, 5), 0.8, facecolor='#6B5B95', edgecolor='#333333', lw=2)
    ax.add_patch(user_circle)
    ax.text(1.5, 5, 'User', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # Aggregator app
    app_box = mpatches.FancyBboxPatch((3.5, 4), 2, 2, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(app_box)
    ax.text(4.5, 5.3, 'Aggregator', ha='center', fontsize=10, fontweight='bold', color='white')
    ax.text(4.5, 4.8, 'App', ha='center', fontsize=9, color='white')
    ax.text(4.5, 4.3, '(AISP)', ha='center', fontsize=8, color='#CCE5FF')

    # Multiple banks
    banks = [
        ('Bank A', 8, 7.5, '#333333'),
        ('Bank B', 10.5, 7.5, '#44A044'),
        ('Bank C', 8, 2.5, '#FF7F0E'),
        ('Bank D', 10.5, 2.5, '#D62728'),
    ]

    for name, x, y, color in banks:
        bank_box = mpatches.FancyBboxPatch((x-0.8, y-0.6), 1.6, 1.2,
                                            boxstyle='round,pad=0.1',
                                            facecolor=color, edgecolor='#333333', lw=2)
        ax.add_patch(bank_box)
        ax.text(x, y, name, ha='center', va='center', fontsize=9, fontweight='bold', color='white')

    # API hub
    hub_box = mpatches.FancyBboxPatch((6, 4), 1.5, 2, boxstyle='round,pad=0.1',
                                       facecolor='#999999', edgecolor='#333333', lw=2)
    ax.add_patch(hub_box)
    ax.text(6.75, 5.3, 'API', ha='center', fontsize=9, fontweight='bold', color='white')
    ax.text(6.75, 4.8, 'Hub', ha='center', fontsize=9, color='white')

    # Arrows from user to app
    ax.annotate('', xy=(3.5, 5), xytext=(2.3, 5),
               arrowprops=dict(arrowstyle='->', color='#6B5B95', lw=2))
    ax.text(2.9, 5.4, '1. Link\naccounts', fontsize=7, ha='center')

    # Arrows from app to hub
    ax.annotate('', xy=(6, 5), xytext=(5.5, 5),
               arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))

    # Arrows from hub to banks
    ax.annotate('', xy=(8, 6.9), xytext=(7.5, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=1.5))
    ax.annotate('', xy=(10.5, 6.9), xytext=(7.5, 5.5),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=1.5))
    ax.annotate('', xy=(8, 3.1), xytext=(7.5, 4),
               arrowprops=dict(arrowstyle='->', color='#FF7F0E', lw=1.5))
    ax.annotate('', xy=(10.5, 3.1), xytext=(7.5, 4.5),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=1.5))

    # Consolidated view bubble
    view_box = mpatches.FancyBboxPatch((0.5, 7), 4.5, 2, boxstyle='round,pad=0.1',
                                        facecolor='#E8F4EA', edgecolor='#44A044', lw=2)
    ax.add_patch(view_box)
    ax.text(2.75, 8.5, 'Unified Dashboard', ha='center', fontsize=10, fontweight='bold', color='#44A044')
    ax.text(2.75, 7.9, 'Total Balance: $45,230', ha='center', fontsize=9)
    ax.text(2.75, 7.5, 'All transactions | Spending insights', ha='center', fontsize=8, color='#666666')

    # Arrow from app to dashboard
    ax.annotate('', xy=(2.75, 7), xytext=(4.5, 6),
               arrowprops=dict(arrowstyle='->', color='#44A044', lw=2))
    ax.text(3.3, 6.7, '5. Display', fontsize=7, color='#44A044')

    # Process steps box
    steps = """Process Flow:
    1. User links accounts in app
    2. App redirects to each bank for consent
    3. User authenticates at each bank (SCA)
    4. Banks return access tokens
    5. App fetches data via APIs
    6. Unified view presented to user"""

    ax.text(12.5, 5, steps, fontsize=8, ha='right', va='center',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL FLOW DIAGRAM]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'account_aggregation_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
