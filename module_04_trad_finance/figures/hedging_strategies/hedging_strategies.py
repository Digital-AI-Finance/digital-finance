"""
Hedging Strategies
Common derivatives hedging approaches

Output: hedging_strategies.pdf
Module: module_04_trad_finance
Lesson: 45 - Derivatives
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Hedging Strategies',
    'module': 'module_04_trad_finance',
    'lesson': 45,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/hedging_strategies'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    S = np.linspace(70, 130, 100)
    K = 100
    S0 = 100

    # Protective Put vs Stock
    ax1 = axes[0]

    # Stock only
    stock_pnl = S - S0
    ax1.plot(S, stock_pnl, 'b-', linewidth=2, label='Stock Only')

    # Protective put (stock + long put)
    put_premium = 5
    put_payoff = np.maximum(K - S, 0)
    protected_pnl = (S - S0) + put_payoff - put_premium
    ax1.plot(S, protected_pnl, 'g-', linewidth=2, label=f'Protective Put (Premium=${put_premium})')

    ax1.axhline(y=0, color='black', linewidth=0.5)
    ax1.axvline(x=K, color='gray', linestyle='--', alpha=0.5)

    ax1.fill_between(S, stock_pnl, protected_pnl, where=(S < K),
                     alpha=0.2, color='green', label='Protection Value')

    ax1.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax1.set_ylabel('Profit/Loss', fontsize=10)
    ax1.set_title('Protective Put Strategy', fontsize=11, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.set_xlim(70, 130)
    ax1.set_ylim(-35, 35)
    ax1.grid(True, alpha=0.3)

    ax1.annotate('Max Loss\nLimited', xy=(75, -5), xytext=(80, 15),
                fontsize=9, color='green',
                arrowprops=dict(arrowstyle='->', color='green'))

    # Collar Strategy
    ax2 = axes[1]

    # Parameters
    put_strike = 95
    call_strike = 105
    put_premium = 3
    call_premium = 3  # Collar often zero-cost

    # Stock + long put + short call
    collar_pnl = (S - S0) + np.maximum(put_strike - S, 0) - np.maximum(S - call_strike, 0) - put_premium + call_premium

    ax2.plot(S, S - S0, 'b--', linewidth=1.5, alpha=0.5, label='Stock Only')
    ax2.plot(S, collar_pnl, 'purple', linewidth=2, label='Collar (95/105)')

    ax2.axhline(y=0, color='black', linewidth=0.5)
    ax2.axvline(x=put_strike, color='red', linestyle='--', alpha=0.5, label=f'Put K={put_strike}')
    ax2.axvline(x=call_strike, color='green', linestyle='--', alpha=0.5, label=f'Call K={call_strike}')

    ax2.set_xlabel('Stock Price at Expiry', fontsize=10)
    ax2.set_ylabel('Profit/Loss', fontsize=10)
    ax2.set_title('Zero-Cost Collar Strategy', fontsize=11, fontweight='bold')
    ax2.legend(fontsize=9, loc='upper left')
    ax2.set_xlim(70, 130)
    ax2.set_ylim(-15, 15)
    ax2.grid(True, alpha=0.3)

    # Annotate cap and floor
    ax2.annotate('Upside\nCapped', xy=(120, 5), xytext=(112, 12),
                fontsize=9, color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))
    ax2.annotate('Downside\nProtected', xy=(80, -5), xytext=(82, -12),
                fontsize=9, color='green',
                arrowprops=dict(arrowstyle='->', color='green'))

    fig.suptitle('Derivatives Hedging Strategies', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'hedging_strategies.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
