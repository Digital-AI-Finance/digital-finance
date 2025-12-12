"""
Major Stock Index Performance
Shows relative performance of global indices

Output: stock_indices.pdf
Module: module_04_traditional
Lesson: 37 - Financial Markets
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
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)

    # Simulated index performance (normalized to 100)
    months = np.arange(0, 61)  # 5 years monthly

    # Base returns with different characteristics
    sp500 = 100 * np.cumprod(1 + np.random.normal(0.008, 0.04, len(months)))
    nasdaq = 100 * np.cumprod(1 + np.random.normal(0.01, 0.05, len(months)))
    ftse = 100 * np.cumprod(1 + np.random.normal(0.005, 0.035, len(months)))
    nikkei = 100 * np.cumprod(1 + np.random.normal(0.006, 0.045, len(months)))

    ax.plot(months, sp500, color=MLBLUE, linewidth=2, label='S&P 500')
    ax.plot(months, nasdaq, color=MLORANGE, linewidth=2, label='NASDAQ')
    ax.plot(months, ftse, color=MLGREEN, linewidth=2, label='FTSE 100')
    ax.plot(months, nikkei, color=MLPURPLE, linewidth=2, label='Nikkei 225')

    ax.axhline(y=100, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    ax.set_xlabel('Months', fontsize=11)
    ax.set_ylabel('Index Value (Base = 100)', fontsize=11)
    ax.set_title('Major Stock Index Performance (5-Year Simulation)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Monte Carlo simulation]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'stock_indices.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
