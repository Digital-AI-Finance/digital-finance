"""
Option Payoff Diagrams
Shows call and put option payoffs at expiration

Output: option_payoff.pdf
Module: module_04_traditional
Lesson: 45 - Derivatives Technology
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Stock prices
    S = np.linspace(60, 140, 100)
    K = 100  # Strike price
    premium_call = 5
    premium_put = 4

    # Long Call payoff
    call_payoff = np.maximum(S - K, 0) - premium_call
    ax1.plot(S, call_payoff, color=MLBLUE, linewidth=2.5, label='Long Call')
    ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax1.axvline(x=K, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax1.fill_between(S, call_payoff, 0, where=(call_payoff > 0), alpha=0.3, color=MLGREEN)
    ax1.fill_between(S, call_payoff, 0, where=(call_payoff < 0), alpha=0.3, color=MLRED)

    ax1.set_xlabel('Stock Price at Expiration', fontsize=10)
    ax1.set_ylabel('Profit/Loss', fontsize=10)
    ax1.set_title('Call Option (Strike=$100)', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax1.set_xlim(60, 140)
    ax1.set_ylim(-15, 35)
    ax1.text(K, -12, f'K=${K}', ha='center', fontsize=9)
    ax1.text(105, -7, f'Premium: ${premium_call}', fontsize=8, color='#555555')

    # Long Put payoff
    put_payoff = np.maximum(K - S, 0) - premium_put
    ax2.plot(S, put_payoff, color=MLORANGE, linewidth=2.5, label='Long Put')
    ax2.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax2.axvline(x=K, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax2.fill_between(S, put_payoff, 0, where=(put_payoff > 0), alpha=0.3, color=MLGREEN)
    ax2.fill_between(S, put_payoff, 0, where=(put_payoff < 0), alpha=0.3, color=MLRED)

    ax2.set_xlabel('Stock Price at Expiration', fontsize=10)
    ax2.set_ylabel('Profit/Loss', fontsize=10)
    ax2.set_title('Put Option (Strike=$100)', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax2.set_xlim(60, 140)
    ax2.set_ylim(-15, 35)
    ax2.text(K, -12, f'K=${K}', ha='center', fontsize=9)
    ax2.text(95, -7, f'Premium: ${premium_put}', fontsize=8, color='#555555')

    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.3)

    fig.text(0.98, 0.02, '[CONCEPTUAL ILLUSTRATION]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'option_payoff.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
