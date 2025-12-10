"""
Real-Time Fraud Scoring
Latency and throughput in fraud detection

Output: real_time_scoring.pdf
Module: module_03_ai_ml
Lesson: 31 - Fraud Detection
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Real Time Scoring',
    'module': 'module_03_ai_ml',
    'lesson': 31,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/real_time_scoring'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Latency breakdown
    ax1 = axes[0]

    components = ['Data Fetch', 'Feature Calc', 'ML Inference', 'Rules Engine',
                  'Decision', 'Logging']
    latencies = [8, 15, 25, 12, 5, 10]  # milliseconds
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#888888']

    bars = ax1.barh(components, latencies, color=colors, edgecolor='black', alpha=0.8)

    for bar, lat in zip(bars, latencies):
        ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{lat}ms', va='center', fontsize=10, fontweight='bold')

    # Total line
    total = sum(latencies)
    ax1.axvline(x=total, color='#D62728', linestyle='--', linewidth=2)
    ax1.text(total + 2, 3, f'Total: {total}ms', fontsize=10, fontweight='bold', color='#D62728')

    # SLA line
    ax1.axvline(x=100, color='#44A044', linestyle=':', linewidth=2)
    ax1.text(100 + 2, 5, 'SLA: 100ms', fontsize=10, fontweight='bold', color='#44A044')

    ax1.set_xlabel('Latency (milliseconds)', fontsize=11)
    ax1.set_title('Real-Time Scoring Latency Breakdown', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 120)
    ax1.xaxis.grid(True, alpha=0.3)

    # Throughput over time
    ax2 = axes[1]

    hours = np.arange(0, 24)
    # Typical daily pattern
    base_tps = 1000
    pattern = np.sin((hours - 6) * np.pi / 12) * 0.4 + 0.6
    pattern = np.clip(pattern, 0.2, 1)
    throughput = base_tps * pattern * (1 + np.random.randn(24) * 0.05)

    ax2.fill_between(hours, throughput, alpha=0.3, color='#4A90E2')
    ax2.plot(hours, throughput, 'b-', linewidth=2)

    # Peak hours
    ax2.axhline(y=1200, color='#D62728', linestyle='--', linewidth=1.5, label='Peak Capacity')
    ax2.axhline(y=800, color='#FF7F0E', linestyle='--', linewidth=1.5, label='Normal Capacity')

    # Annotate peaks
    ax2.annotate('Peak Hours', xy=(14, throughput[14]), xytext=(16, throughput[14] + 150),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    ax2.set_xlabel('Hour of Day', fontsize=11)
    ax2.set_ylabel('Transactions per Second', fontsize=11)
    ax2.set_title('Fraud Scoring Throughput (24hr Pattern)', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 23)
    ax2.set_ylim(0, 1500)
    ax2.set_xticks([0, 6, 12, 18, 23])
    ax2.set_xticklabels(['12am', '6am', '12pm', '6pm', '11pm'])
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3)

    fig.suptitle('Real-Time Fraud Detection Performance', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'real_time_scoring.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
