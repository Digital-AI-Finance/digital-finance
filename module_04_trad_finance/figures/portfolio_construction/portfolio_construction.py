"""
Portfolio Construction Process
Investment policy to implementation

Output: portfolio_construction.pdf
Module: module_04_trad_finance
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Portfolio Construction',
    'module': 'module_04_trad_finance',
    'lesson': 46,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/portfolio_construction'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Strategic vs Tactical Allocation
    ax1 = axes[0]

    asset_classes = ['Equities', 'Fixed\nIncome', 'Alternatives', 'Real\nAssets', 'Cash']
    strategic = [50, 30, 10, 5, 5]
    tactical = [55, 25, 12, 3, 5]

    x = np.arange(len(asset_classes))
    width = 0.35

    bars1 = ax1.bar(x - width/2, strategic, width, label='Strategic (Long-term)',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, tactical, width, label='Tactical (Current)',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Allocation (%)', fontsize=11)
    ax1.set_title('Strategic vs. Tactical Asset Allocation', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(asset_classes, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 70)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add deviation indicators
    for i, (s, t) in enumerate(zip(strategic, tactical)):
        diff = t - s
        if diff != 0:
            color = '#44A044' if diff > 0 else '#D62728'
            sign = '+' if diff > 0 else ''
            ax1.text(i, max(s, t) + 3, f'{sign}{diff}%', ha='center',
                    fontsize=9, fontweight='bold', color=color)

    # Risk-Return by Profile
    ax2 = axes[1]

    profiles = ['Conservative', 'Moderate\nConservative', 'Balanced', 'Growth', 'Aggressive']
    expected_return = [4, 5.5, 7, 8.5, 10]
    expected_risk = [5, 8, 12, 16, 22]
    equity_pct = [20, 35, 50, 70, 90]

    colors = ['#4A90E2', '#44A044', '#FFD700', '#FF7F0E', '#D62728']
    sizes = [s * 3 + 100 for s in equity_pct]

    scatter = ax2.scatter(expected_risk, expected_return, s=sizes, c=colors, alpha=0.7, edgecolors='black')

    for i, (x, y, profile, eq) in enumerate(zip(expected_risk, expected_return, profiles, equity_pct)):
        ax2.annotate(f'{profile}\n({eq}% equity)', xy=(x, y), xytext=(x+1, y+0.3),
                    fontsize=8, ha='left')

    ax2.set_xlabel('Expected Risk (Std Dev %)', fontsize=11)
    ax2.set_ylabel('Expected Return (%)', fontsize=11)
    ax2.set_title('Risk-Return by Investment Profile', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 28)
    ax2.set_ylim(2, 12)
    ax2.grid(True, alpha=0.3)

    # Efficient frontier line
    x_ef = np.linspace(3, 25, 50)
    y_ef = 2.5 + 0.35 * x_ef - 0.002 * x_ef**2
    ax2.plot(x_ef, y_ef, '--', color='#888888', alpha=0.5, label='Efficient Frontier')
    ax2.legend(loc='lower right', fontsize=9)

    fig.suptitle('Portfolio Construction Framework', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'portfolio_construction.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
