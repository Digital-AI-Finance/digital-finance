"""
Mobile Wallet Penetration by Region
Shows global adoption rates of mobile wallets by region

Output: mobile_wallet_penetration.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Mobile Wallet Penetration by Region',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/mobile_wallet_penetration'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create mobile wallet penetration by region chart"""
    fig, ax = plt.subplots(figsize=(11, 6))

    regions = ['China', 'India', 'Southeast\nAsia', 'Africa', 'Latin\nAmerica',
               'Middle\nEast', 'Europe', 'North\nAmerica']
    penetration_2023 = [87, 45, 55, 40, 35, 28, 42, 38]
    penetration_2020 = [72, 28, 38, 25, 22, 18, 28, 25]
    projected_2026 = [92, 65, 72, 58, 52, 45, 55, 48]

    x = np.arange(len(regions))
    width = 0.25

    bars1 = ax.bar(x - width, penetration_2020, width, label='2020', color='#999999')
    bars2 = ax.bar(x, penetration_2023, width, label='2023', color='#4A90E2')
    bars3 = ax.bar(x + width, projected_2026, width, label='2026 (Projected)',
                   color='#44A044', alpha=0.7, hatch='//')

    ax.set_xlabel('Region', fontsize=11)
    ax.set_ylabel('Penetration Rate (%)', fontsize=11)
    ax.set_title('Mobile Wallet Penetration by Region', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(regions, fontsize=9)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper right', fontsize=9)

    # Add value labels on 2023 bars
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Add grid
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Key drivers annotation
    ax.annotate('China leads due to\nWeChat Pay & Alipay',
               xy=(0, 87), xytext=(1.5, 95),
               fontsize=8, ha='center',
               arrowprops=dict(arrowstyle='->', color='#666666', lw=0.5))

    ax.annotate('Rapid growth driven by\nUPI and digital India',
               xy=(1, 45), xytext=(1, 70),
               fontsize=8, ha='center',
               arrowprops=dict(arrowstyle='->', color='#666666', lw=0.5))

    # Synthetic label
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mobile_wallet_penetration.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
