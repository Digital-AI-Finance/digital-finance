"""
Trading Latency Comparison
Speed in electronic trading

Output: latency_comparison.pdf
Module: module_04_trad_finance
Lesson: 40 - Electronic Trading
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Latency Comparison',
    'module': 'module_04_trad_finance',
    'lesson': 40,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/latency_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Latency by Component
    ax1 = axes[0]

    components = ['Network\n(Fiber)', 'Network\n(Microwave)', 'Order\nValidation',
                 'Risk Check', 'Matching\nEngine', 'Confirmation']
    latency_us = [3000, 1500, 50, 100, 10, 25]  # microseconds

    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#17BECF']

    bars = ax1.barh(components, latency_us, color=colors, alpha=0.8, edgecolor='black')

    for bar, lat in zip(bars, latency_us):
        label = f'{lat} us' if lat < 1000 else f'{lat/1000:.1f} ms'
        ax1.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=9, fontweight='bold')

    ax1.set_xlabel('Latency (microseconds)', fontsize=11)
    ax1.set_title('Trading Latency by Component', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 4000)
    ax1.xaxis.grid(True, alpha=0.3)

    # HFT vs Traditional
    ax2 = axes[1]

    categories = ['Order to\nExchange', 'Market Data\nProcessing', 'Strategy\nDecision',
                 'Total Round\nTrip']

    hft = [0.05, 0.01, 0.005, 0.1]  # milliseconds
    traditional = [5, 2, 50, 100]

    x = np.arange(len(categories))
    width = 0.35

    # Use log scale
    ax2.bar(x - width/2, hft, width, label='HFT (ms)', color='#44A044', alpha=0.8)
    ax2.bar(x + width/2, traditional, width, label='Traditional (ms)', color='#4A90E2', alpha=0.8)

    ax2.set_yscale('log')
    ax2.set_xlabel('Trading Phase', fontsize=11)
    ax2.set_ylabel('Latency (milliseconds, log scale)', fontsize=11)
    ax2.set_title('HFT vs. Traditional Trading Speed', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    # Speed difference annotation
    ax2.text(1.5, 30, '1000x faster', fontsize=11, fontweight='bold',
            color='#D62728', rotation=0, ha='center')

    fig.suptitle('Trading Latency: The Need for Speed', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'latency_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
