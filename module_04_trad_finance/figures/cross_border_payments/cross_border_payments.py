"""
Cross-Border Payment Challenges
International payment friction

Output: cross_border_payments.pdf
Module: module_04_trad_finance
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Cross Border Payments',
    'module': 'module_04_trad_finance',
    'lesson': 39,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/cross_border_payments'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Pain Points
    ax1 = axes[0]

    issues = ['High Costs\n(3-7%)', 'Slow Speed\n(2-5 days)', 'Lack of\nTransparency',
             'Limited\nTracking', 'FX Spread\nCosts', 'Compliance\nComplexity']
    impact = [85, 80, 70, 65, 75, 60]
    colors = ['#D62728', '#FF7F0E', '#FFD700', '#90EE90', '#FF7F0E', '#4A90E2']

    bars = ax1.barh(issues, impact, color=colors, alpha=0.8, edgecolor='black')

    for bar, imp in zip(bars, impact):
        ax1.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                f'{imp}%', va='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Pain Point Severity (%)', fontsize=11)
    ax1.set_title('Cross-Border Payment Challenges', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 100)
    ax1.xaxis.grid(True, alpha=0.3)

    # Corridor Costs
    ax2 = axes[1]

    corridors = ['US-MX', 'EU-UK', 'US-IN', 'UAE-PH', 'ZA-NG', 'Global Avg']
    cost = [4.5, 2.1, 5.2, 6.8, 8.5, 6.2]
    time = [2, 1, 3, 3, 4, 3]  # Days

    x = np.arange(len(corridors))
    width = 0.35

    bars1 = ax2.bar(x - width/2, cost, width, label='Cost (%)', color='#D62728', alpha=0.8)
    bars2 = ax2.bar(x + width/2, time, width, label='Time (days)', color='#4A90E2', alpha=0.8)

    ax2.set_xlabel('Payment Corridor', fontsize=11)
    ax2.set_ylabel('Value', fontsize=11)
    ax2.set_title('Cost and Time by Corridor', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(corridors, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 10)
    ax2.yaxis.grid(True, alpha=0.3)

    # G20 Target
    ax2.axhline(y=3, color='#44A044', linestyle='--', linewidth=2, alpha=0.7)
    ax2.text(5.5, 3.3, 'G20 Target: <3%', fontsize=9, color='#44A044', fontweight='bold')

    fig.suptitle('Cross-Border Payment Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'cross_border_payments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
