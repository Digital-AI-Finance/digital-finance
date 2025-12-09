"""
Open Banking API Performance Metrics
Shows typical API performance standards and metrics

Output: api_performance.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking API Performance',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/api_performance'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create API performance metrics chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Response time by bank (simulated)
    banks = ['Bank A', 'Bank B', 'Bank C', 'Bank D', 'Bank E', 'Avg Target']
    # Response times in milliseconds
    p50 = [180, 220, 150, 300, 250, 200]
    p95 = [450, 520, 380, 750, 600, 500]
    p99 = [800, 950, 650, 1200, 1000, 1000]

    x = np.arange(len(banks))
    width = 0.25

    bars1 = ax1.bar(x - width, p50, width, label='P50', color='#44A044')
    bars2 = ax1.bar(x, p95, width, label='P95', color='#FF7F0E')
    bars3 = ax1.bar(x + width, p99, width, label='P99', color='#D62728')

    ax1.set_ylabel('Response Time (ms)', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(banks, fontsize=8, rotation=15)
    ax1.set_ylim(0, 1400)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_title('API Response Time Percentiles', fontsize=12, fontweight='bold', pad=10)

    # Add target line
    ax1.axhline(y=500, color='#4A90E2', linestyle='--', lw=2, label='P95 Target')
    ax1.text(5.5, 520, 'P95 Target', fontsize=8, color='#4A90E2')

    ax1.yaxis.grid(True, alpha=0.3)
    ax1.set_axisbelow(True)

    # Right: Availability and error rates
    metrics = ['Availability\n(%)', 'Success\nRate (%)', 'Error\nRate (%)', 'Timeout\nRate (%)']
    target_values = [99.5, 99.0, 1.0, 0.5]
    actual_values = [99.2, 98.5, 1.5, 0.8]

    x2 = np.arange(len(metrics))
    width2 = 0.35

    bars_target = ax2.bar(x2 - width2/2, target_values, width2, label='Target', color='#4A90E2')
    bars_actual = ax2.bar(x2 + width2/2, actual_values, width2, label='Actual', color='#333333')

    ax2.set_xticks(x2)
    ax2.set_xticklabels(metrics, fontsize=9)
    ax2.set_ylim(0, 105)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_title('API Quality Metrics', fontsize=12, fontweight='bold', pad=10)

    # Add value labels
    for bars in [bars_target, bars_actual]:
        for bar in bars:
            height = bar.get_height()
            if height < 10:
                ax2.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width()/2, height),
                            xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8)
            else:
                ax2.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width()/2, height),
                            xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8)

    ax2.yaxis.grid(True, alpha=0.3)
    ax2.set_axisbelow(True)

    # Main title
    fig.suptitle('Open Banking API Performance Standards',
                fontsize=14, fontweight='bold', y=1.02)

    # Performance targets note
    targets = """PSD2/RTS Requirements:
    - Same performance as online banking
    - No degradation during peak hours
    - Dedicated interface must match fallback"""

    fig.text(0.98, 0.15, targets, fontsize=7, ha='right',
            bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[SYNTHETIC DATA FOR ILLUSTRATION]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'api_performance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
