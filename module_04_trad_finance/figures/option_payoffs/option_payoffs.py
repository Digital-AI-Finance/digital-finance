"""
Option Payoff Diagrams
Call and put option payoffs

Output: option_payoffs.pdf
Module: module_04_trad_finance
Lesson: 45 - Derivatives
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Option Payoffs',
    'module': 'module_04_trad_finance',
    'lesson': 45,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/option_payoffs'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    S = np.linspace(50, 150, 100)  # Stock price range
    K = 100  # Strike price
    premium = 5  # Option premium

    # Long Call
    ax1 = axes[0, 0]
    payoff = np.maximum(S - K, 0) - premium
    ax1.plot(S, payoff, 'b-', linewidth=2, label='Long Call')
    ax1.axhline(y=0, color='black', linewidth=0.5)
    ax1.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax1.fill_between(S, payoff, 0, where=(payoff > 0), alpha=0.3, color='green')
    ax1.fill_between(S, payoff, 0, where=(payoff < 0), alpha=0.3, color='red')
    ax1.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax1.set_ylabel('Profit/Loss', fontsize=10)
    ax1.set_title('Long Call', fontsize=11, fontweight='bold')
    ax1.set_xlim(50, 150)
    ax1.set_ylim(-20, 50)
    ax1.grid(True, alpha=0.3)
    ax1.text(K, -18, f'K={K}', ha='center', fontsize=9)
    ax1.text(130, 20, f'Max Loss: ${premium}', fontsize=9, color='red')
    ax1.text(130, 35, 'Unlimited Upside', fontsize=9, color='green')

    # Long Put
    ax2 = axes[0, 1]
    payoff = np.maximum(K - S, 0) - premium
    ax2.plot(S, payoff, 'r-', linewidth=2, label='Long Put')
    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax2.fill_between(S, payoff, 0, where=(payoff > 0), alpha=0.3, color='green')
    ax2.fill_between(S, payoff, 0, where=(payoff < 0), alpha=0.3, color='red')
    ax2.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax2.set_ylabel('Profit/Loss', fontsize=10)
    ax2.set_title('Long Put', fontsize=11, fontweight='bold')
    ax2.set_xlim(50, 150)
    ax2.set_ylim(-20, 50)
    ax2.grid(True, alpha=0.3)
    ax2.text(K, -18, f'K={K}', ha='center', fontsize=9)
    ax2.text(70, 35, f'Max Profit: ${K-premium}', fontsize=9, color='green')

    # Short Call
    ax3 = axes[1, 0]
    payoff = -np.maximum(S - K, 0) + premium
    ax3.plot(S, payoff, 'b-', linewidth=2, linestyle='--', label='Short Call')
    ax3.axhline(y=0, color='black', linewidth=0.5)
    ax3.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax3.fill_between(S, payoff, 0, where=(payoff > 0), alpha=0.3, color='green')
    ax3.fill_between(S, payoff, 0, where=(payoff < 0), alpha=0.3, color='red')
    ax3.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax3.set_ylabel('Profit/Loss', fontsize=10)
    ax3.set_title('Short Call', fontsize=11, fontweight='bold')
    ax3.set_xlim(50, 150)
    ax3.set_ylim(-50, 20)
    ax3.grid(True, alpha=0.3)
    ax3.text(K, 15, f'K={K}', ha='center', fontsize=9)
    ax3.text(70, 10, f'Max Profit: ${premium}', fontsize=9, color='green')
    ax3.text(130, -35, 'Unlimited Downside', fontsize=9, color='red')

    # Short Put
    ax4 = axes[1, 1]
    payoff = -np.maximum(K - S, 0) + premium
    ax4.plot(S, payoff, 'r-', linewidth=2, linestyle='--', label='Short Put')
    ax4.axhline(y=0, color='black', linewidth=0.5)
    ax4.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax4.fill_between(S, payoff, 0, where=(payoff > 0), alpha=0.3, color='green')
    ax4.fill_between(S, payoff, 0, where=(payoff < 0), alpha=0.3, color='red')
    ax4.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax4.set_ylabel('Profit/Loss', fontsize=10)
    ax4.set_title('Short Put', fontsize=11, fontweight='bold')
    ax4.set_xlim(50, 150)
    ax4.set_ylim(-50, 20)
    ax4.grid(True, alpha=0.3)
    ax4.text(K, 15, f'K={K}', ha='center', fontsize=9)
    ax4.text(130, 10, f'Max Profit: ${premium}', fontsize=9, color='green')
    ax4.text(60, -35, f'Max Loss: ${K-premium}', fontsize=9, color='red')

    fig.suptitle('Option Payoff Diagrams (K=$100, Premium=$5)', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'option_payoffs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
