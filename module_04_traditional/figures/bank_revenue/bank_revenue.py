"""
Bank Revenue Sources
Shows breakdown of typical commercial bank revenue

Output: bank_revenue.pdf
Module: module_04_traditional
Lesson: 38 - Core Banking
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

    # Revenue sources for typical commercial bank
    sources = ['Net Interest\nIncome', 'Fee &\nCommission', 'Trading\nIncome', 'Wealth\nManagement', 'Other']
    percentages = [55, 25, 10, 7, 3]

    colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE, MLLAVENDER]

    wedges, texts, autotexts = ax.pie(percentages, labels=sources, colors=colors,
                                       autopct='%1.0f%%', startangle=90,
                                       explode=[0.02, 0, 0, 0, 0],
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 2})

    for autotext in autotexts:
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')

    ax.set_title('Commercial Bank Revenue Breakdown', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.text(0, -1.3, 'Net Interest Income (NII) = Interest earned on loans - Interest paid on deposits',
            ha='center', fontsize=9, color='#555555', style='italic')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Typical bank structure]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'bank_revenue.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
