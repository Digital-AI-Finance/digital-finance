"""
Alternative Data Sources in Finance
Shows growth and types of alternative data

Output: alternative_data.pdf
Module: module_04_traditional
Lesson: 47 - Data Vendors
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

    # Alternative data types and their adoption
    data_types = ['Satellite\nImagery', 'Web\nScraping', 'Social\nMedia', 'Credit Card\nData', 'Geolocation', 'IoT/\nSensors']
    adoption = [35, 55, 45, 30, 40, 20]  # Percentage of funds using
    growth = [45, 30, 25, 35, 50, 60]  # YoY growth rate

    x = np.arange(len(data_types))
    width = 0.35

    bars1 = ax.bar(x - width/2, adoption, width, label='Current Adoption (%)', color=MLBLUE)
    bars2 = ax.bar(x + width/2, growth, width, label='YoY Growth (%)', color=MLORANGE)

    ax.set_ylabel('Percentage', fontsize=11)
    ax.set_title('Alternative Data: Adoption & Growth by Type', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(data_types)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 75)

    # Add market size
    ax.text(0.02, 0.95, 'Alt Data Market: ~$7B (2024)',
            transform=ax.transAxes, ha='left', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Greenwich Associates, Opimas [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'alternative_data.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
