"""
Compliance Costs in Financial Services
Shows growth in regulatory compliance spending

Output: compliance_costs.pdf
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
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

    # Global compliance spending in billions USD
    compliance_spending = [180, 195, 215, 240, 270, 290, 320, 350, 380, 410]

    # RegTech spending as subset
    regtech_spending = [5, 8, 12, 18, 28, 42, 58, 75, 95, 120]

    ax.bar(years, compliance_spending, color=MLBLUE, alpha=0.7, label='Total Compliance', width=0.8)
    ax.bar(years, regtech_spending, color=MLORANGE, alpha=0.9, label='RegTech Solutions', width=0.8)

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Spending (USD Billions)', fontsize=11)
    ax.set_title('Global Financial Compliance Spending', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.legend(loc='upper left', framealpha=0.9)
    ax.set_ylim(0, 500)

    # Add growth annotation
    ax.annotate('RegTech CAGR: ~40%', xy=(2024, 120), xytext=(2020, 200),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'),
                color='#555555')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: Deloitte, KPMG estimates [SYNTHETIC DATA]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'compliance_costs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
