"""
Bitcoin Supply Curve and Halving Events
Visualization of Bitcoin's supply schedule with halving milestones

Required libraries: matplotlib, numpy
Output: bitcoin_halving.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Bitcoin Supply Curve and Halving Events',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_02_blockchain/bitcoin_halving'
}

def create_bitcoin_halving_chart():
    """Create visualization of Bitcoin supply curve with halving events"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

    # Bitcoin halving data
    halving_events = [
        {'year': 2009, 'block': 0, 'reward': 50.0},
        {'year': 2012, 'block': 210000, 'reward': 25.0},
        {'year': 2016, 'block': 420000, 'reward': 12.5},
        {'year': 2020, 'block': 630000, 'reward': 6.25},
        {'year': 2024, 'block': 840000, 'reward': 3.125},
        {'year': 2028, 'block': 1050000, 'reward': 1.5625},
        {'year': 2032, 'block': 1260000, 'reward': 0.78125},
        {'year': 2036, 'block': 1470000, 'reward': 0.390625},
        {'year': 2040, 'block': 1680000, 'reward': 0.1953125}
    ]

    # Calculate cumulative supply
    years = np.array([h['year'] for h in halving_events])
    rewards = np.array([h['reward'] for h in halving_events])

    # Generate smooth supply curve
    all_years = np.arange(2009, 2141)
    supply = np.zeros_like(all_years, dtype=float)

    for i, year in enumerate(all_years):
        cumulative = 0
        for j, halving in enumerate(halving_events):
            if year >= halving['year']:
                if j < len(halving_events) - 1:
                    years_in_period = min(year - halving['year'],
                                        halving_events[j+1]['year'] - halving['year'])
                else:
                    years_in_period = year - halving['year']

                # Approximately 52560 blocks per year (10 min blocks)
                blocks_per_year = 52560
                cumulative += years_in_period * blocks_per_year * halving['reward']

        supply[i] = min(cumulative, 21000000)

    # Top panel: Supply curve
    ax1.plot(all_years, supply / 1e6, color='black', linewidth=1.5, label='Total Supply')
    ax1.axhline(y=21, color='gray', linestyle='--', linewidth=1, label='21M Cap')

    # Mark halving events
    for halving in halving_events[:5]:  # Show first 5 halvings
        idx = halving['year'] - 2009
        if idx < len(supply):
            ax1.plot(halving['year'], supply[idx] / 1e6, 'o',
                    color='black', markersize=5, markerfacecolor='white',
                    markeredgewidth=1.5)
            ax1.annotate(f"{halving['year']}\nReward: {halving['reward']} BTC",
                        xy=(halving['year'], supply[idx] / 1e6),
                        xytext=(10, 10), textcoords='offset points',
                        fontsize=6, ha='left',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                edgecolor='gray', linewidth=0.5),
                        arrowprops=dict(arrowstyle='->', lw=0.5))

    ax1.set_xlabel('Year', fontsize=8)
    ax1.set_ylabel('Supply (Million BTC)', fontsize=8)
    ax1.set_title('Bitcoin Supply Curve with Halving Events', fontsize=10, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=7)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.set_xlim(2008, 2050)
    ax1.set_ylim(0, 22)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Bottom panel: Block reward over time
    halving_years = [h['year'] for h in halving_events]
    halving_rewards = [h['reward'] for h in halving_events]

    ax2.step(halving_years, halving_rewards, where='post', color='black',
            linewidth=1.5, label='Block Reward')
    ax2.plot(halving_years, halving_rewards, 'o', color='black',
            markersize=5, markerfacecolor='white', markeredgewidth=1.5)

    ax2.set_xlabel('Year', fontsize=8)
    ax2.set_ylabel('Block Reward (BTC)', fontsize=8)
    ax2.set_title('Bitcoin Block Reward Halving Schedule', fontsize=10, fontweight='bold')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.set_xlim(2008, 2050)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    # Add halving interval annotation
    ax2.text(0.98, 0.95, 'Halving occurs every\n~210,000 blocks\n(~4 years)',
            transform=ax2.transAxes, fontsize=7,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightgray',
                     edgecolor='black', linewidth=0.5))

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'bitcoin_halving.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_bitcoin_halving_chart()
