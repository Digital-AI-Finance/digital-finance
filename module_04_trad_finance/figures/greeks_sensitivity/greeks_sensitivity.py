"""
Option Greeks Sensitivity
Delta, Gamma, Theta, Vega

Output: greeks_sensitivity.pdf
Module: module_04_trad_finance
Lesson: 45 - Derivatives
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

CHART_METADATA = {
    'title': 'Greeks Sensitivity',
    'module': 'module_04_trad_finance',
    'lesson': 45,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/greeks_sensitivity'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def black_scholes_greeks(S, K, T, r, sigma):
    """Calculate Black-Scholes Greeks"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(d2)
    vega = S * norm.pdf(d1) * np.sqrt(T)

    return delta, gamma, theta / 365, vega / 100  # Theta per day, Vega per 1%

def create_chart():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    S = np.linspace(70, 130, 100)
    K = 100
    r = 0.05
    sigma = 0.2

    # Different times to expiry
    times = [0.5, 0.25, 0.1, 0.02]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728']
    labels = ['6 months', '3 months', '1 month', '1 week']

    # Delta
    ax1 = axes[0, 0]
    for T, color, label in zip(times, colors, labels):
        delta, _, _, _ = black_scholes_greeks(S, K, T, r, sigma)
        ax1.plot(S, delta, color=color, linewidth=2, label=label)

    ax1.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax1.set_xlabel('Stock Price', fontsize=10)
    ax1.set_ylabel('Delta', fontsize=10)
    ax1.set_title('Delta (Call Option)', fontsize=11, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 1)
    ax1.text(K+2, 0.52, 'ATM', fontsize=9, color='gray')

    # Gamma
    ax2 = axes[0, 1]
    for T, color, label in zip(times, colors, labels):
        _, gamma, _, _ = black_scholes_greeks(S, K, T, r, sigma)
        ax2.plot(S, gamma, color=color, linewidth=2, label=label)

    ax2.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Stock Price', fontsize=10)
    ax2.set_ylabel('Gamma', fontsize=10)
    ax2.set_title('Gamma', fontsize=11, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.text(K-15, ax2.get_ylim()[1]*0.85, 'Peak at ATM,\nnear expiry', fontsize=9, color='#D62728')

    # Theta
    ax3 = axes[1, 0]
    for T, color, label in zip(times, colors, labels):
        _, _, theta, _ = black_scholes_greeks(S, K, T, r, sigma)
        ax3.plot(S, theta, color=color, linewidth=2, label=label)

    ax3.axhline(y=0, color='black', linewidth=0.5)
    ax3.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax3.set_xlabel('Stock Price', fontsize=10)
    ax3.set_ylabel('Theta (per day)', fontsize=10)
    ax3.set_title('Theta (Time Decay)', fontsize=11, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.text(K+5, ax3.get_ylim()[0]*0.7, 'Accelerates\nnear expiry', fontsize=9, color='#D62728')

    # Vega
    ax4 = axes[1, 1]
    for T, color, label in zip(times, colors, labels):
        _, _, _, vega = black_scholes_greeks(S, K, T, r, sigma)
        ax4.plot(S, vega, color=color, linewidth=2, label=label)

    ax4.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax4.set_xlabel('Stock Price', fontsize=10)
    ax4.set_ylabel('Vega (per 1% vol)', fontsize=10)
    ax4.set_title('Vega (Volatility Sensitivity)', fontsize=11, fontweight='bold')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
    ax4.text(K+10, ax4.get_ylim()[1]*0.8, 'Higher for\nlonger-dated', fontsize=9, color='#4A90E2')

    fig.suptitle('Option Greeks: Sensitivity Analysis (K=$100, r=5%, vol=20%)',
                fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'greeks_sensitivity.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
