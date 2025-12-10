"""
Order Routing Logic
Smart order routing decisions

Output: order_routing.pdf
Module: module_04_trad_finance
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Order Routing',
    'module': 'module_04_trad_finance',
    'lesson': 40,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/order_routing'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Routing Decision Factors
    ax1 = axes[0]

    factors = ['Price', 'Liquidity', 'Speed', 'Rebates', 'Fill Rate', 'Market Impact']
    weights = [30, 25, 18, 10, 10, 7]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#888888']

    wedges, texts, autotexts = ax1.pie(weights, labels=factors, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax1.set_title('SOR Decision Factors', fontsize=12, fontweight='bold')

    # Venue Selection
    ax2 = axes[1]

    venues = ['NYSE', 'NASDAQ', 'BATS', 'IEX', 'Dark Pool A', 'Dark Pool B']
    routed_pct = [28, 25, 18, 8, 12, 9]
    fill_rate = [92, 94, 91, 88, 75, 72]

    x = np.arange(len(venues))
    width = 0.35

    bars1 = ax2.bar(x - width/2, routed_pct, width, label='Orders Routed (%)', color='#4A90E2', alpha=0.8)

    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, fill_rate, 'ro-', linewidth=2, markersize=8, label='Fill Rate (%)')
    ax2_twin.set_ylabel('Fill Rate (%)', fontsize=10, color='#D62728')
    ax2_twin.tick_params(axis='y', labelcolor='#D62728')
    ax2_twin.set_ylim(60, 100)

    ax2.set_xlabel('Trading Venue', fontsize=11)
    ax2.set_ylabel('Orders Routed (%)', fontsize=11)
    ax2.set_title('Order Routing Distribution', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(venues, rotation=20, ha='right', fontsize=9)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 35)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Smart Order Routing (SOR) Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'order_routing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
