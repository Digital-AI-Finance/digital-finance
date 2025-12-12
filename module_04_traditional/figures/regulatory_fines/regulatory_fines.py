"""
Regulatory Fines in Financial Services
Shows major fines by category

Output: regulatory_fines.pdf
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

    # Fines by category (billions USD)
    aml_sanctions = [8, 10, 6, 5, 7, 12, 9]
    market_manipulation = [3, 4, 2, 3, 5, 4, 3]
    consumer_protection = [2, 3, 4, 5, 4, 6, 5]
    data_privacy = [0.5, 1, 2, 3, 4, 5, 6]
    other = [1, 1.5, 2, 2, 3, 3, 4]

    ax.stackplot(years, aml_sanctions, market_manipulation, consumer_protection,
                 data_privacy, other,
                 labels=['AML/Sanctions', 'Market Manipulation', 'Consumer Protection',
                        'Data Privacy', 'Other'],
                 colors=[MLRED, MLORANGE, MLBLUE, MLGREEN, MLLAVENDER], alpha=0.85)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Fines (USD Billions)', fontsize=11)
    ax.set_title('Global Financial Regulatory Fines by Category', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9, fontsize=8)
    ax.set_xlim(2018, 2024)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Industry estimates [SYNTHETIC DATA]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regulatory_fines.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
