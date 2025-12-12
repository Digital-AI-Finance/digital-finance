"""
Market Maker Economics
Shows bid-ask spread profit and inventory risk

Output: market_makers.pdf
Module: module_04_traditional
Lesson: 41 - Market Microstructure
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

    # Simulated market maker P&L over a trading day (minutes)
    minutes = np.arange(0, 390)  # 6.5 hours

    # Spread capture (positive) vs inventory risk (volatile)
    spread_pnl = np.cumsum(np.random.uniform(0.5, 1.5, len(minutes)))  # Consistent small gains
    inventory_pnl = np.cumsum(np.random.normal(0, 5, len(minutes)))  # Volatile
    total_pnl = spread_pnl + inventory_pnl

    ax.plot(minutes, spread_pnl, color=MLGREEN, linewidth=2, label='Spread Capture')
    ax.plot(minutes, inventory_pnl, color=MLRED, linewidth=2, alpha=0.7, label='Inventory P&L')
    ax.plot(minutes, total_pnl, color=MLBLUE, linewidth=2.5, label='Total P&L')
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1)

    ax.set_xlabel('Trading Day (Minutes)', fontsize=11)
    ax.set_ylabel('Cumulative P&L ($)', fontsize=11)
    ax.set_title('Market Maker P&L Components', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)

    # Add time labels
    ax.set_xticks([0, 60, 120, 180, 240, 300, 360])
    ax.set_xticklabels(['9:30', '10:30', '11:30', '12:30', '13:30', '14:30', '15:30'])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Monte Carlo simulation]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_makers.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
