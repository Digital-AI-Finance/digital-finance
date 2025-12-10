"""
CSD Landscape
Central Securities Depositories globally

Output: csd_landscape.pdf
Module: module_04_trad_finance
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'CSD Landscape',
    'module': 'module_04_trad_finance',
    'lesson': 44,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/csd_landscape'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Major CSDs by assets
    ax1 = axes[0]

    csds = ['DTCC\n(US)', 'Euroclear', 'Clearstream', 'JSD\n(Japan)', 'CSD Russia', 'CCDC\n(China)']
    assets = [63, 37, 16, 8, 4, 20]  # Trillions USD
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#E91E63']

    bars = ax1.bar(csds, assets, color=colors, alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Assets Under Custody ($T)', fontsize=11)
    ax1.set_title('Major CSDs by Assets', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 75)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 1.5,
                f'${height}T', ha='center', fontsize=10, fontweight='bold')

    # CSD functions comparison
    ax2 = axes[1]

    functions = ['Safekeeping', 'Settlement', 'Asset\nServicing', 'Collateral\nMgmt', 'Securities\nLending', 'Reporting']
    dtcc = [100, 100, 85, 90, 80, 95]
    euroclear = [100, 100, 95, 95, 90, 90]
    emerging = [95, 90, 70, 60, 40, 75]

    x = np.arange(len(functions))
    width = 0.25

    ax2.bar(x - width, dtcc, width, label='DTCC', color='#4A90E2', alpha=0.8)
    ax2.bar(x, euroclear, width, label='Euroclear', color='#44A044', alpha=0.8)
    ax2.bar(x + width, emerging, width, label='Emerging CSDs', color='#FF7F0E', alpha=0.8)

    ax2.set_ylabel('Capability Score (%)', fontsize=11)
    ax2.set_title('CSD Capabilities Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(functions, fontsize=9)
    ax2.legend(loc='lower right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add trend line for modernization
    ax2.axhline(y=90, color='#888888', linestyle='--', alpha=0.5)
    ax2.text(5, 92, 'Target Level', fontsize=8, color='#888888', style='italic')

    fig.suptitle('Central Securities Depositories (CSDs)', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'csd_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
