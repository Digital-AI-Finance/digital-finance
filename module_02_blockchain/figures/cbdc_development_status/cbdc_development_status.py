"""
CBDC Development Status
Stacked bar chart showing CBDC progress by region

Output: cbdc_development_status.pdf
Module: module_02_blockchain
Lesson: 24 - Regulation & Future
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'CBDC Development Status',
    'module': 'module_02_blockchain',
    'lesson': 24,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/cbdc_development_status'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 14,
    'ytick.labelsize': 16,
    'legend.fontsize': 14,
})

def create_chart():
    """Create CBDC development status chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    regions = ['Asia\nPacific', 'Europe', 'Americas', 'Africa', 'Middle\nEast']

    # Number of countries in each stage
    launched = [3, 0, 3, 2, 0]
    pilot = [8, 2, 2, 5, 1]
    development = [12, 5, 8, 10, 4]
    research = [15, 20, 15, 12, 8]

    x = np.arange(len(regions))
    width = 0.6

    ax.bar(x, launched, width, label='Launched', color='#27AE60', edgecolor='black', linewidth=1)
    ax.bar(x, pilot, width, bottom=launched, label='Pilot', color='#3498DB', edgecolor='black', linewidth=1)
    ax.bar(x, development, width, bottom=np.array(launched)+np.array(pilot), label='Development', color='#F39C12', edgecolor='black', linewidth=1)
    ax.bar(x, research, width, bottom=np.array(launched)+np.array(pilot)+np.array(development), label='Research', color='#95A5A6', edgecolor='black', linewidth=1)

    ax.set_xlabel('Region', fontsize=20)
    ax.set_ylabel('Number of Countries', fontsize=20)
    ax.set_title('Central Bank Digital Currency (CBDC) Status by Region', fontsize=24, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(regions)
    ax.legend(loc='upper right', fontsize=14)
    ax.grid(axis='y', alpha=0.3)

    # Add totals
    totals = [sum(t) for t in zip(launched, pilot, development, research)]
    for i, total in enumerate(totals):
        ax.text(i, total + 1, str(total), ha='center', fontsize=14, fontweight='bold')

    # Global stat
    ax.text(0.02, 0.98, f'Global: 130+ countries\nexploring CBDCs',
           transform=ax.transAxes, fontsize=14, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    fig.text(0.5, 0.02, 'Source: Atlantic Council CBDC Tracker (Dec 2024)',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'cbdc_development_status.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
