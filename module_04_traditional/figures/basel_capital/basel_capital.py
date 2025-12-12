"""
Basel Capital Requirements Evolution
Shows how bank capital requirements have increased

Output: basel_capital.pdf
Module: module_04_traditional
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    frameworks = ['Basel I\n(1988)', 'Basel II\n(2004)', 'Basel III\n(2010)', 'Basel III.1\n(2023)']

    # Capital ratios as percentage of risk-weighted assets
    tier1_min = [4.0, 4.0, 6.0, 6.0]
    conservation_buffer = [0, 0, 2.5, 2.5]
    countercyclical = [0, 0, 0, 2.5]  # Max
    gsib_buffer = [0, 0, 0, 2.5]  # Max for G-SIBs

    x = np.arange(len(frameworks))
    width = 0.6

    ax.bar(x, tier1_min, width, label='Tier 1 Minimum', color=MLBLUE)
    ax.bar(x, conservation_buffer, width, bottom=tier1_min,
           label='Conservation Buffer', color=MLORANGE)
    ax.bar(x, countercyclical, width,
           bottom=np.array(tier1_min)+np.array(conservation_buffer),
           label='Countercyclical (max)', color=MLGREEN)
    ax.bar(x, gsib_buffer, width,
           bottom=np.array(tier1_min)+np.array(conservation_buffer)+np.array(countercyclical),
           label='G-SIB Buffer (max)', color=MLLAVENDER)

    # Add total labels
    totals = [t + c + cc + g for t, c, cc, g in zip(tier1_min, conservation_buffer, countercyclical, gsib_buffer)]
    for i, total in enumerate(totals):
        ax.text(i, total + 0.3, f'{total:.1f}%', ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('Capital Ratio (% of RWA)', fontsize=11)
    ax.set_title('Basel Capital Requirements Evolution', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(frameworks)
    ax.legend(loc='upper left', framealpha=0.9, fontsize=8)
    ax.set_ylim(0, 16)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: BIS Basel Framework [SYNTHETIC ILLUSTRATION]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'basel_capital.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
