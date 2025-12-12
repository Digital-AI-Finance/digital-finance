"""
AML Transaction Monitoring Alerts
Shows alert volumes and investigation rates

Output: aml_transaction_monitoring.pdf
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
MLRED = '#D62728'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # AML alert funnel
    stages = ['Total\nTransactions', 'Rules\nTriggered', 'Alerts\nGenerated', 'Investigated', 'SARs\nFiled']
    volumes = [10000000, 50000, 5000, 2000, 100]

    # Use log scale for visualization
    log_volumes = [np.log10(v) for v in volumes]

    colors = [MLBLUE, MLORANGE, MLORANGE, MLGREEN, MLRED]

    bars = ax.bar(stages, log_volumes, color=colors, edgecolor='white', linewidth=2)

    # Add actual numbers as labels
    for bar, vol in zip(bars, volumes):
        if vol >= 1000000:
            label = f'{vol/1000000:.0f}M'
        elif vol >= 1000:
            label = f'{vol/1000:.0f}K'
        else:
            label = str(vol)
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                label, ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('Volume (log scale)', fontsize=11)
    ax.set_title('AML Transaction Monitoring Funnel', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    # Add conversion rates
    ax.text(0.5, 0.85, 'False Positive Rate: ~98%',
            transform=ax.transAxes, ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#fff0f0', edgecolor=MLRED))

    ax.set_ylim(0, 8)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical bank ratios]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'aml_transaction_monitoring.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
