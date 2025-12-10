"""
Structured Products Overview
Common structured product types

Output: structured_products.pdf
Module: module_04_trad_finance
Lesson: 45 - Derivatives
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Structured Products',
    'module': 'module_04_trad_finance',
    'lesson': 45,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/structured_products'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Structured Products Market
    ax1 = axes[0]

    products = ['Equity-Linked\nNotes', 'Principal\nProtected', 'Auto-\nCallables', 'Reverse\nConvertibles', 'Range\nAccruals', 'CLN/CDO']
    issuance = [180, 150, 220, 95, 45, 75]  # In billions
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#E91E63', '#D62728']

    bars = ax1.bar(products, issuance, color=colors, alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Annual Issuance ($B)', fontsize=11)
    ax1.set_title('Structured Products by Type', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 280)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 5,
                f'${height}B', ha='center', fontsize=9, fontweight='bold')

    # Risk-return profile
    risk_levels = ['Low', 'Medium', 'Low-Med', 'High', 'Medium', 'High']
    for i, (bar, risk) in enumerate(zip(bars, risk_levels)):
        color = '#44A044' if risk == 'Low' else '#FF7F0E' if 'Med' in risk else '#D62728'
        ax1.text(bar.get_x() + bar.get_width()/2, 10,
                f'Risk:\n{risk}', ha='center', fontsize=8, color=color)

    # Autocallable Payoff Example
    ax2 = axes[1]

    # Simulate autocallable
    S = np.linspace(60, 140, 100)
    S0 = 100
    barrier = 70  # Knock-in barrier
    autocall = 105  # Autocall trigger
    coupon = 8  # Annual coupon %

    # Payoff at maturity (if not autocalled)
    payoff = np.where(S >= barrier,
                      coupon,  # Receive coupon if above barrier
                      (S/S0 - 1) * 100)  # Loss if below barrier

    ax2.plot(S, payoff, 'b-', linewidth=2, label='Maturity Payoff')
    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axhline(y=coupon, color='green', linestyle='--', alpha=0.5)
    ax2.axvline(x=barrier, color='red', linestyle='--', linewidth=2, label=f'Barrier ({barrier}%)')
    ax2.axvline(x=autocall, color='green', linestyle='--', linewidth=2, label=f'Autocall ({autocall}%)')

    ax2.fill_between(S, payoff, 0, where=(S < barrier), alpha=0.3, color='red', label='Loss Zone')
    ax2.fill_between(S, 0, coupon, where=(S >= barrier), alpha=0.3, color='green', label='Coupon Zone')

    ax2.set_xlabel('Underlying Price (% of Initial)', fontsize=10)
    ax2.set_ylabel('Return (%)', fontsize=10)
    ax2.set_title('Autocallable Note Payoff', fontsize=11, fontweight='bold')
    ax2.legend(fontsize=9, loc='lower right')
    ax2.set_xlim(60, 140)
    ax2.set_ylim(-45, 20)
    ax2.grid(True, alpha=0.3)

    # Add annotations
    ax2.annotate('If autocalled:\nReceive principal\n+ coupon', xy=(110, 10),
                xytext=(120, 12), fontsize=9, color='green')
    ax2.annotate('Below barrier:\n1:1 loss', xy=(65, -30),
                xytext=(72, -35), fontsize=9, color='red')

    fig.suptitle('Structured Products Overview', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'structured_products.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
