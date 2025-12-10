"""
Risk Dashboard Overview
Real-time risk monitoring

Output: risk_dashboard.pdf
Module: module_04_trad_finance
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Risk Dashboard',
    'module': 'module_04_trad_finance',
    'lesson': 42,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/risk_dashboard'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig = plt.figure(figsize=(16, 10))

    # Create grid
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

    np.random.seed(42)

    # 1. VaR Gauge
    ax1 = fig.add_subplot(gs[0, 0])
    current_var = 2.8
    limit_var = 4.0
    pct = current_var / limit_var

    colors = ['#44A044', '#FFD700', '#FF7F0E', '#D62728']
    ax1.pie([pct, 1-pct], colors=[colors[int(pct*3)], '#E0E0E0'], startangle=90,
            wedgeprops=dict(width=0.3))
    ax1.text(0, 0, f'{current_var}%\nVaR', ha='center', va='center', fontsize=14, fontweight='bold')
    ax1.set_title('Daily VaR (Limit: 4%)', fontsize=11, fontweight='bold')

    # 2. P&L Distribution
    ax2 = fig.add_subplot(gs[0, 1])
    daily_pnl = np.random.normal(0.5, 2, 30)
    colors = ['#44A044' if p > 0 else '#D62728' for p in daily_pnl]
    ax2.bar(range(30), daily_pnl, color=colors, alpha=0.7)
    ax2.axhline(y=0, color='black', linewidth=1)
    ax2.set_xlabel('Trading Day', fontsize=9)
    ax2.set_ylabel('P&L ($M)', fontsize=9)
    ax2.set_title('30-Day P&L History', fontsize=11, fontweight='bold')

    # 3. Risk Metrics Summary
    ax3 = fig.add_subplot(gs[0, 2])
    metrics = ['VaR 99%', 'ES 99%', 'Greeks\nDelta', 'Liquidity\nRisk']
    values = [2.8, 4.2, 0.85, 0.65]
    limits = [4.0, 6.0, 1.0, 1.0]
    usage = [v/l*100 for v, l in zip(values, limits)]

    bars = ax3.barh(metrics, usage, color=['#44A044' if u < 70 else '#FF7F0E' if u < 90 else '#D62728' for u in usage])
    ax3.axvline(x=100, color='#D62728', linestyle='--', linewidth=2)
    ax3.set_xlabel('Limit Utilization (%)', fontsize=9)
    ax3.set_title('Key Risk Metrics', fontsize=11, fontweight='bold')
    ax3.set_xlim(0, 120)

    # 4. Position Concentration
    ax4 = fig.add_subplot(gs[1, 0])
    sectors = ['Tech', 'Finance', 'Health', 'Energy', 'Other']
    weights = [35, 25, 18, 12, 10]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#888888']
    ax4.pie(weights, labels=sectors, autopct='%1.0f%%', colors=colors, startangle=90)
    ax4.set_title('Portfolio Concentration', fontsize=11, fontweight='bold')

    # 5. VaR Trend
    ax5 = fig.add_subplot(gs[1, 1])
    days = np.arange(60)
    var_trend = 2.5 + np.cumsum(np.random.randn(60) * 0.05)
    var_trend = np.clip(var_trend, 1.5, 3.5)

    ax5.plot(days, var_trend, 'b-', linewidth=2)
    ax5.fill_between(days, var_trend, alpha=0.2, color='blue')
    ax5.axhline(y=4.0, color='#D62728', linestyle='--', linewidth=2, label='Limit')
    ax5.axhline(y=3.2, color='#FF7F0E', linestyle='--', linewidth=1.5, label='Warning')
    ax5.set_xlabel('Days', fontsize=9)
    ax5.set_ylabel('VaR (%)', fontsize=9)
    ax5.set_title('VaR Trend (60 days)', fontsize=11, fontweight='bold')
    ax5.legend(loc='upper right', fontsize=8)

    # 6. Alert Summary
    ax6 = fig.add_subplot(gs[1, 2])
    alert_types = ['Critical', 'Warning', 'Info']
    alert_counts = [1, 5, 12]
    colors = ['#D62728', '#FF7F0E', '#4A90E2']

    bars = ax6.bar(alert_types, alert_counts, color=colors, alpha=0.8, edgecolor='black')
    for bar, count in zip(bars, alert_counts):
        ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                str(count), ha='center', fontsize=12, fontweight='bold')

    ax6.set_ylabel('Count', fontsize=9)
    ax6.set_title('Active Risk Alerts', fontsize=11, fontweight='bold')
    ax6.set_ylim(0, 15)

    fig.suptitle('Enterprise Risk Dashboard', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'risk_dashboard.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
