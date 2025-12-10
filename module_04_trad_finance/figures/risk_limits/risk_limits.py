"""
Risk Limits Framework
Trading and position limits

Output: risk_limits.pdf
Module: module_04_trad_finance
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Risk Limits',
    'module': 'module_04_trad_finance',
    'lesson': 42,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/risk_limits'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Limit Utilization
    ax1 = axes[0]

    desks = ['Equity\nTrading', 'Fixed\nIncome', 'FX', 'Derivatives', 'Credit']
    limit = [100, 100, 100, 100, 100]
    utilization = [78, 92, 65, 88, 45]

    x = np.arange(len(desks))
    width = 0.6

    bars = ax1.bar(x, utilization, width, color=['#44A044' if u < 80 else '#FF7F0E' if u < 90 else '#D62728' for u in utilization],
                  alpha=0.8, edgecolor='black')

    # Limit line
    ax1.axhline(y=100, color='#D62728', linestyle='--', linewidth=2, label='Limit')
    ax1.axhline(y=80, color='#FF7F0E', linestyle='--', linewidth=1.5, label='Warning (80%)')

    for bar, util in zip(bars, utilization):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{util}%', ha='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Trading Desk', fontsize=11)
    ax1.set_ylabel('Limit Utilization (%)', fontsize=11)
    ax1.set_title('VaR Limit Utilization by Desk', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(desks, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 120)
    ax1.yaxis.grid(True, alpha=0.3)

    # Limit Breach History
    ax2 = axes[1]

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    breaches = [2, 1, 3, 0, 1, 2, 4, 3, 1, 2, 1, 0]
    warnings = [5, 4, 8, 3, 6, 7, 10, 8, 5, 6, 4, 3]

    x = np.arange(len(months))
    width = 0.35

    ax2.bar(x - width/2, breaches, width, label='Limit Breaches', color='#D62728', alpha=0.8)
    ax2.bar(x + width/2, warnings, width, label='Warning Triggers', color='#FF7F0E', alpha=0.8)

    ax2.set_xlabel('Month', fontsize=11)
    ax2.set_ylabel('Count', fontsize=11)
    ax2.set_title('Risk Limit Events (2024)', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(months, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 12)
    ax2.yaxis.grid(True, alpha=0.3)

    # Trend note
    ax2.annotate('Market volatility\nspike', xy=(6, 4), xytext=(8, 8),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    fig.suptitle('Risk Limits and Monitoring', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_limits.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
