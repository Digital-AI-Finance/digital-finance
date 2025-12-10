"""
Automated Rebalancing Strategy
Portfolio drift and rebalancing triggers

Output: automated_rebalancing.pdf
Module: module_03_ai_ml
Lesson: 33 - Robo-Advisors ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Automated Rebalancing',
    'module': 'module_03_ai_ml',
    'lesson': 33,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/automated_rebalancing'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Portfolio Drift
    ax1 = axes[0]

    days = np.arange(0, 365)
    target = 60  # Target equity allocation

    # Simulate drift
    drift = target + np.cumsum(np.random.randn(365) * 0.3)

    # Rebalancing events (when drift exceeds threshold)
    threshold = 5
    rebalance_points = []
    current_alloc = target
    rebalanced_drift = [target]

    for i in range(1, 365):
        current_alloc += np.random.randn() * 0.3
        if abs(current_alloc - target) > threshold:
            rebalance_points.append(i)
            current_alloc = target
        rebalanced_drift.append(current_alloc)

    ax1.plot(days, drift, 'b-', linewidth=1.5, alpha=0.7, label='Without Rebalancing')
    ax1.plot(days, rebalanced_drift, 'g-', linewidth=2, label='With Rebalancing')

    # Threshold bands
    ax1.axhline(y=target, color='black', linestyle='-', linewidth=1.5, label='Target (60%)')
    ax1.axhline(y=target + threshold, color='#D62728', linestyle='--', linewidth=1.5, alpha=0.7)
    ax1.axhline(y=target - threshold, color='#D62728', linestyle='--', linewidth=1.5, alpha=0.7)
    ax1.fill_between(days, target - threshold, target + threshold, alpha=0.1, color='#D62728')

    # Mark rebalancing events
    for rp in rebalance_points[:10]:  # Show first 10
        ax1.axvline(x=rp, color='#44A044', linestyle=':', alpha=0.5)

    ax1.set_xlabel('Days', fontsize=11)
    ax1.set_ylabel('Equity Allocation (%)', fontsize=11)
    ax1.set_title('Portfolio Drift and Rebalancing', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_xlim(0, 365)
    ax1.set_ylim(45, 75)
    ax1.grid(True, alpha=0.3)

    # Rebalancing Strategies Comparison
    ax2 = axes[1]

    strategies = ['Calendar\n(Quarterly)', 'Threshold\n(5%)', 'Threshold\n(3%)', 'Hybrid', 'ML-Optimal']
    trades_year = [4, 8, 15, 10, 6]
    tracking_error = [2.1, 1.2, 0.8, 0.9, 0.7]
    tax_efficiency = [85, 75, 60, 80, 90]

    x = np.arange(len(strategies))
    width = 0.25

    bars1 = ax2.bar(x - width, trades_year, width, label='Trades/Year', color='#4A90E2', alpha=0.8)
    bars2 = ax2.bar(x, [te * 5 for te in tracking_error], width, label='Tracking Error (x5)', color='#D62728', alpha=0.8)
    bars3 = ax2.bar(x + width, [te / 10 for te in tax_efficiency], width, label='Tax Efficiency (/10)', color='#44A044', alpha=0.8)

    ax2.set_xlabel('Rebalancing Strategy', fontsize=11)
    ax2.set_ylabel('Metric Value', fontsize=11)
    ax2.set_title('Rebalancing Strategy Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(strategies, fontsize=9)
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_ylim(0, 18)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Automated Portfolio Rebalancing', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'automated_rebalancing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
