"""
CBDC Design Choices
Shows key design dimensions for CBDCs

Output: cbdc_design.pdf
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # CBDC design spectrum
    dimensions = ['Architecture', 'Infrastructure', 'Access', 'Interlinkages', 'Data Access']

    # Position on spectrum (0 = left option, 1 = right option)
    china = [0.2, 0.3, 0.8, 0.4, 0.2]  # e-CNY
    eu = [0.6, 0.5, 0.5, 0.7, 0.6]  # Digital Euro (proposed)
    bahamas = [0.4, 0.6, 0.9, 0.3, 0.5]  # Sand Dollar

    y_pos = np.arange(len(dimensions))

    ax.scatter(china, y_pos, s=200, c=MLRED, label='e-CNY (China)', marker='o', zorder=3)
    ax.scatter(eu, y_pos, s=200, c=MLBLUE, label='Digital Euro (proposed)', marker='s', zorder=3)
    ax.scatter(bahamas, y_pos, s=200, c=MLGREEN, label='Sand Dollar (Bahamas)', marker='^', zorder=3)

    # Add spectrum lines
    for y in y_pos:
        ax.plot([0, 1], [y, y], color='gray', linewidth=1, alpha=0.3, zorder=1)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(dimensions)
    ax.set_xlim(-0.1, 1.1)

    # Add spectrum labels
    labels_left = ['Direct', 'DLT', 'Wholesale', 'Domestic', 'Full Privacy']
    labels_right = ['Indirect', 'Conventional', 'Retail', 'Cross-border', 'Full Traceability']

    for y, (left, right) in enumerate(zip(labels_left, labels_right)):
        ax.text(-0.05, y, left, ha='right', va='center', fontsize=8, color='#555555')
        ax.text(1.05, y, right, ha='left', va='center', fontsize=8, color='#555555')

    ax.set_title('CBDC Design Choices: Country Comparison', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, framealpha=0.9)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])

    fig.text(0.98, 0.02, 'Source: BIS CBDC Handbook [SYNTHETIC POSITIONING]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'cbdc_design.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

MLRED = '#D62728'

if __name__ == '__main__':
    create_chart()
