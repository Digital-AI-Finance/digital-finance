"""
Asset Class Correlation Matrix
Shows correlations between major asset classes

Output: correlation_matrix.pdf
Module: module_04_traditional
Lesson: 42 - Risk Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 8))

    assets = ['US Equities', 'Intl Equities', 'US Bonds', 'Commodities', 'Real Estate', 'Gold']

    # Correlation matrix (typical values)
    corr = np.array([
        [1.00, 0.85, 0.05, 0.35, 0.60, 0.05],
        [0.85, 1.00, 0.10, 0.40, 0.55, 0.10],
        [0.05, 0.10, 1.00, -0.10, 0.20, 0.25],
        [0.35, 0.40, -0.10, 1.00, 0.30, 0.35],
        [0.60, 0.55, 0.20, 0.30, 1.00, 0.15],
        [0.05, 0.10, 0.25, 0.35, 0.15, 1.00]
    ])

    # Create heatmap
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlBu_r',
                xticklabels=assets, yticklabels=assets,
                center=0, vmin=-1, vmax=1, ax=ax,
                annot_kws={'fontsize': 10, 'fontweight': 'bold'})

    ax.set_title('Asset Class Correlation Matrix', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical historical correlations]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'correlation_matrix.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
