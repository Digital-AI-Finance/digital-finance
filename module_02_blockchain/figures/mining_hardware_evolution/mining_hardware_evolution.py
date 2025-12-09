"""
Mining Hardware Evolution
Shows the progression of Bitcoin mining hardware from CPUs to ASICs

Output: mining_hardware_evolution.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Mining Hardware Evolution',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/mining_hardware_evolution'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create mining hardware evolution chart"""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Hardware generations data
    hardware = ['CPU\n(2009-2010)', 'GPU\n(2010-2013)', 'FPGA\n(2011-2013)', 'ASIC\n(2013-Now)']
    hashrate = [10, 800, 25000, 200000000]  # MH/s typical
    efficiency = [0.001, 0.1, 1, 100]  # relative efficiency (MH/J)
    years = [2009, 2010, 2012, 2013]
    colors = ['#3498DB', '#27AE60', '#F39C12', '#E74C3C']

    # Log scale bar chart
    x = np.arange(len(hardware))
    bars = ax.bar(x, hashrate, color=colors, alpha=0.8, edgecolor='black', linewidth=2)

    ax.set_yscale('log')
    ax.set_ylabel('Typical Hashrate (MH/s)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(hardware, fontsize=12)
    ax.set_title('Bitcoin Mining Hardware Evolution', fontsize=20, fontweight='bold', pad=20)

    # Add hashrate labels
    for bar, hr in zip(bars, hashrate):
        height = bar.get_height()
        if hr >= 1000000:
            label = f'{hr/1000000:.0f} TH/s'
        elif hr >= 1000:
            label = f'{hr/1000:.0f} GH/s'
        else:
            label = f'{hr} MH/s'
        ax.text(bar.get_x() + bar.get_width()/2, height * 1.5, label,
               ha='center', fontsize=12, fontweight='bold')

    # Add improvement factors
    improvements = ['1x', '80x', '31x', '8,000x']
    for i, (bar, imp) in enumerate(zip(bars, improvements)):
        if i > 0:
            ax.annotate(f'{imp}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height() * 0.3),
                       fontsize=11, ha='center', color='white', fontweight='bold')

    # Details box
    details = [
        ('CPU', 'Any computer', '~10 MH/s', '$0/dedicated'),
        ('GPU', 'Gaming cards', '~800 MH/s', '$500-2000'),
        ('FPGA', 'Programmable chips', '~25 GH/s', '$1000-5000'),
        ('ASIC', 'Purpose-built', '~200 TH/s', '$2000-15000'),
    ]

    # Create table below
    table_y = -0.25
    ax.text(0.5, table_y + 0.08, 'Hardware Comparison', transform=ax.transAxes,
           fontsize=14, fontweight='bold', ha='center')

    col_labels = ['Type', 'Hardware', 'Hashrate', 'Cost']
    for j, label in enumerate(col_labels):
        ax.text(0.15 + j*0.22, table_y, label, transform=ax.transAxes,
               fontsize=11, fontweight='bold', ha='center')

    for i, row in enumerate(details):
        for j, val in enumerate(row):
            ax.text(0.15 + j*0.22, table_y - 0.05 - i*0.04, val, transform=ax.transAxes,
                   fontsize=10, ha='center')

    # Key insight
    ax.text(0.5, -0.48, 'ASIC dominance: Only specialized hardware is profitable today',
           transform=ax.transAxes, fontsize=12, ha='center', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(1, 1e9)

    # Source
    fig.text(0.5, 0.02, 'Source: CoinDesk Research, Bitmain Product Specifications (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.35)

    output_path = Path(__file__).parent / 'mining_hardware_evolution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
