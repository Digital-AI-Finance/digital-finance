"""
Financial Data Types
Categories of market data

Output: data_types.pdf
Module: module_04_trad_finance
Lesson: 47 - Data Vendors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Data Types',
    'module': 'module_04_trad_finance',
    'lesson': 47,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/data_types'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Data types by latency requirement
    ax1 = axes[0]

    data_types = ['Tick Data', 'Real-time\nQuotes', 'Delayed\nQuotes', 'End-of-Day', 'Historical', 'Reference\nData']
    latency = [0.001, 0.1, 900, 86400, np.nan, 86400]  # Seconds (EOD = 24h)
    cost_index = [100, 80, 20, 10, 25, 30]

    x = np.arange(len(data_types))

    colors = ['#D62728', '#FF7F0E', '#FFD700', '#44A044', '#4A90E2', '#9B59B6']
    bars = ax1.bar(x, cost_index, color=colors, alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Relative Cost Index', fontsize=11)
    ax1.set_title('Data Types by Cost', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(data_types, fontsize=9)
    ax1.set_ylim(0, 120)
    ax1.yaxis.grid(True, alpha=0.3)

    # Latency labels
    latency_labels = ['<1ms', '<100ms', '15min', 'T+1', 'Batch', 'Daily']
    for bar, lat in zip(bars, latency_labels):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 3,
                lat, ha='center', fontsize=9, style='italic', color='#666666')

    ax1.text(3, 110, 'Latency requirement', fontsize=9, color='#666666', style='italic')

    # Data usage by firm type
    ax2 = axes[1]

    firm_types = ['HFT', 'Hedge Fund', 'Asset Mgr', 'Bank', 'Corporate']
    tick = [95, 60, 20, 40, 5]
    realtime = [100, 90, 70, 85, 30]
    delayed = [5, 30, 60, 50, 80]
    eod = [100, 100, 100, 100, 100]

    x = np.arange(len(firm_types))
    width = 0.2

    ax2.bar(x - 1.5*width, tick, width, label='Tick Data', color='#D62728', alpha=0.8)
    ax2.bar(x - 0.5*width, realtime, width, label='Real-time', color='#FF7F0E', alpha=0.8)
    ax2.bar(x + 0.5*width, delayed, width, label='Delayed', color='#FFD700', alpha=0.8)
    ax2.bar(x + 1.5*width, eod, width, label='EOD', color='#44A044', alpha=0.8)

    ax2.set_ylabel('Usage Rate (%)', fontsize=11)
    ax2.set_title('Data Type Usage by Firm Type', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(firm_types, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Financial Data Types & Usage', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
