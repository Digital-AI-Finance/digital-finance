"""
Volatility Term Structure
Shows implied volatility across different expirations

Output: volatility_term_structure.pdf
Module: module_04_traditional
Lesson: 45 - Derivatives Technology
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
    fig, ax = plt.subplots(figsize=(10, 6))

    # Term structure (days to expiration)
    expirations = [7, 30, 60, 90, 180, 365]
    exp_labels = ['1W', '1M', '2M', '3M', '6M', '1Y']

    # Different market conditions
    normal = [18, 17, 16.5, 16, 15.5, 15]  # Contango
    stressed = [35, 30, 27, 25, 23, 21]  # Backwardation after shock
    calm = [12, 12.5, 13, 13.5, 14, 14.5]  # Low vol environment

    ax.plot(range(len(expirations)), normal, 'o-', color=MLBLUE, linewidth=2,
            markersize=8, label='Normal Market')
    ax.plot(range(len(expirations)), stressed, 's--', color=MLORANGE, linewidth=2,
            markersize=8, label='Post-Shock (Backwardation)')
    ax.plot(range(len(expirations)), calm, '^:', color=MLGREEN, linewidth=2,
            markersize=8, label='Low Vol Environment')

    ax.set_xticks(range(len(expirations)))
    ax.set_xticklabels(exp_labels)

    ax.set_xlabel('Time to Expiration', fontsize=11)
    ax.set_ylabel('Implied Volatility (%)', fontsize=11)
    ax.set_title('VIX Futures Term Structure', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(10, 40)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative term structures]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'volatility_term_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
