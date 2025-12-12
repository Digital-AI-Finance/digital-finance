"""
CBDC Adoption Status - World map-style bar chart
Shows countries at different stages of CBDC development

Output: cbdc_adoption.pdf
Module: module_04_traditional
Lesson: 48 - CBDC and Future
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    stages = ['Launched', 'Pilot', 'Development', 'Research', 'Inactive/\nCancelled']
    counts = [11, 21, 33, 68, 14]
    colors = [MLGREEN, MLBLUE, MLORANGE, MLLAVENDER, '#cccccc']

    bars = ax.bar(stages, counts, color=colors, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, val in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                str(val), ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add example countries for key stages
    examples = [
        'Nigeria, Bahamas,\nJamaica, China (pilot)',
        'Brazil, Russia,\nIndia, Australia',
        'EU, UK, Japan,\nSouth Korea',
        'USA, Canada,\nMost others',
        'Denmark,\nEcuador'
    ]

    for i, (bar, example) in enumerate(zip(bars, examples)):
        ax.text(bar.get_x() + bar.get_width()/2, -5,
                example, ha='center', va='top', fontsize=7, color='#555555')

    ax.set_ylabel('Number of Countries', fontsize=11)
    ax.set_title('Central Bank Digital Currency (CBDC) Status (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 85)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add total annotation
    ax.text(0.98, 0.95, f'Total: {sum(counts)} countries tracked',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.text(0.98, 0.02, 'Source: Atlantic Council CBDC Tracker [Data as of 2024]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)

    output_path = Path(__file__).parent / 'cbdc_adoption.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
