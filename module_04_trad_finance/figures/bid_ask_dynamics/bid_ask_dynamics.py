"""
Bid-Ask Spread Dynamics
Spread behavior and determinants

Output: bid_ask_dynamics.pdf
Module: module_04_trad_finance
Lesson: 41 - Market Microstructure
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Bid Ask Dynamics',
    'module': 'module_04_trad_finance',
    'lesson': 41,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/bid_ask_dynamics'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Spread throughout the day
    ax1 = axes[0]

    # Generate intraday pattern
    time_minutes = np.arange(0, 390)  # 6.5 hours
    # U-shaped pattern: wider at open/close
    base_spread = 0.02
    intraday_pattern = 0.015 * (1 + 2 * np.exp(-0.01 * time_minutes) +
                                 1.5 * np.exp(-0.01 * (390 - time_minutes)))
    noise = np.random.randn(390) * 0.003
    spread = base_spread + intraday_pattern + noise
    spread = np.clip(spread, 0.01, 0.08)

    hours = time_minutes / 60 + 9.5  # Start at 9:30

    ax1.plot(hours, spread * 100, 'b-', linewidth=1.5, alpha=0.7)
    ax1.fill_between(hours, spread * 100, alpha=0.2, color='blue')

    ax1.axvline(x=9.5, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=16, color='gray', linestyle='--', alpha=0.5)

    ax1.text(9.7, 6, 'Open', fontsize=9)
    ax1.text(15.5, 6, 'Close', fontsize=9)

    ax1.set_xlabel('Time of Day', fontsize=11)
    ax1.set_ylabel('Bid-Ask Spread (%)', fontsize=11)
    ax1.set_title('Intraday Spread Pattern (U-Shape)', fontsize=12, fontweight='bold')
    ax1.set_xlim(9.5, 16)
    ax1.grid(True, alpha=0.3)

    # Spread Components
    ax2 = axes[1]

    components = ['Adverse\nSelection', 'Inventory\nRisk', 'Order\nProcessing', 'Market\nMaker Profit']
    contribution = [40, 25, 15, 20]
    colors = ['#D62728', '#FF7F0E', '#4A90E2', '#44A044']

    bars = ax2.bar(components, contribution, color=colors, alpha=0.8, edgecolor='black')

    for bar, pct in zip(bars, contribution):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{pct}%', ha='center', fontsize=11, fontweight='bold')

    ax2.set_xlabel('Spread Component', fontsize=11)
    ax2.set_ylabel('Contribution (%)', fontsize=11)
    ax2.set_title('Bid-Ask Spread Components', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 50)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Bid-Ask Spread Dynamics', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'bid_ask_dynamics.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
