"""
KYC Process Efficiency
Shows time and cost reduction with automation

Output: kyc_process.pdf
Module: module_04_traditional
Lesson: 43 - RegTech Compliance
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

def create_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    processes = ['Manual', 'Semi-\nAutomated', 'Fully\nAutomated']

    # Time to complete KYC (days)
    time_days = [14, 5, 1]

    # Cost per KYC check ($)
    cost = [100, 40, 15]

    colors = [MLORANGE, MLBLUE, MLGREEN]

    # Time chart
    bars1 = ax1.bar(processes, time_days, color=colors, edgecolor='white', linewidth=2)
    for bar, val in zip(bars1, time_days):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{val} days', ha='center', fontsize=10, fontweight='bold')
    ax1.set_ylabel('Days to Complete', fontsize=11)
    ax1.set_title('KYC Processing Time', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax1.set_ylim(0, 18)

    # Cost chart
    bars2 = ax2.bar(processes, cost, color=colors, edgecolor='white', linewidth=2)
    for bar, val in zip(bars2, cost):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'${val}', ha='center', fontsize=10, fontweight='bold')
    ax2.set_ylabel('Cost per Check ($)', fontsize=11)
    ax2.set_title('KYC Cost per Customer', fontsize=12, fontweight='bold', color=MLPURPLE)
    ax2.set_ylim(0, 130)

    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    fig.suptitle('KYC Process Automation Benefits', fontsize=14,
                 fontweight='bold', color=MLPURPLE, y=1.02)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Industry benchmarks]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'kyc_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
