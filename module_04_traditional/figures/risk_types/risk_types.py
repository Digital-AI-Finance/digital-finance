"""
Risk Types in Finance - Stacked bar chart
Shows different risk categories and their relative importance

Output: risk_types.pdf
Module: module_04_traditional
Lesson: 42 - Risk Management
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

    institutions = ['Investment\nBank', 'Commercial\nBank', 'Asset\nManager', 'Insurance\nCo.', 'Hedge\nFund']

    # Risk allocation percentages by institution type
    market_risk = [35, 15, 40, 20, 55]
    credit_risk = [25, 50, 10, 25, 15]
    operational_risk = [20, 20, 25, 15, 10]
    liquidity_risk = [15, 10, 20, 10, 15]
    other_risk = [5, 5, 5, 30, 5]

    x = np.arange(len(institutions))
    width = 0.6

    ax.bar(x, market_risk, width, label='Market Risk', color=MLBLUE)
    ax.bar(x, credit_risk, width, bottom=market_risk, label='Credit Risk', color=MLORANGE)
    ax.bar(x, operational_risk, width, bottom=np.array(market_risk)+np.array(credit_risk),
           label='Operational Risk', color=MLGREEN)
    ax.bar(x, liquidity_risk, width,
           bottom=np.array(market_risk)+np.array(credit_risk)+np.array(operational_risk),
           label='Liquidity Risk', color=MLPURPLE)
    ax.bar(x, other_risk, width,
           bottom=np.array(market_risk)+np.array(credit_risk)+np.array(operational_risk)+np.array(liquidity_risk),
           label='Other (Insurance, Model)', color=MLLAVENDER)

    ax.set_ylabel('Risk Allocation (%)', fontsize=11)
    ax.set_title('Risk Profile by Financial Institution Type', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(institutions)
    ax.legend(loc='upper right', framealpha=0.9)

    ax.set_ylim(0, 110)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative allocation]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
