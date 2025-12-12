"""
Option Greeks Sensitivity
Shows how Delta and Gamma change with stock price

Output: option_greeks.pdf
Module: module_04_traditional
Lesson: 45 - Derivatives Technology
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

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

def create_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Parameters
    K = 100  # Strike
    T = 0.5  # Time to expiration (6 months)
    r = 0.05  # Risk-free rate
    sigma = 0.2  # Volatility

    S = np.linspace(70, 130, 100)

    # Calculate d1 for Black-Scholes
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))

    # Delta for call option
    delta_call = norm.cdf(d1)

    # Gamma (same for call and put)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

    # Plot Delta
    ax1.plot(S, delta_call, color=MLBLUE, linewidth=2.5)
    ax1.axhline(y=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax1.axvline(x=K, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    ax1.set_xlabel('Stock Price', fontsize=10)
    ax1.set_ylabel('Delta', fontsize=10)
    ax1.set_title('Call Option Delta', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax1.set_xlim(70, 130)
    ax1.set_ylim(0, 1)
    ax1.text(K+2, 0.52, 'ATM: Delta ~ 0.5', fontsize=8, color='#555555')

    # Plot Gamma
    ax2.plot(S, gamma, color=MLORANGE, linewidth=2.5)
    ax2.axvline(x=K, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    ax2.set_xlabel('Stock Price', fontsize=10)
    ax2.set_ylabel('Gamma', fontsize=10)
    ax2.set_title('Option Gamma', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax2.set_xlim(70, 130)
    ax2.text(K+2, max(gamma)*0.9, 'Peak at ATM', fontsize=8, color='#555555')

    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=0.3)

    fig.text(0.98, 0.02, '[Black-Scholes Model: K=100, T=0.5, sigma=20%]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'option_greeks.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
