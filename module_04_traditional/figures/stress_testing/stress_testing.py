"""
Bank Stress Test Scenarios
Shows impact of stress scenarios on capital

Output: stress_testing.pdf
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

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Stress test scenarios and capital impact
    scenarios = ['Baseline', 'Mild\nRecession', 'Severe\nRecession', 'Market\nCrash', 'Stagflation']

    # CET1 ratio under different scenarios (starting at 12%)
    bank_a = [12.5, 11.2, 9.5, 8.2, 9.8]
    bank_b = [11.8, 10.5, 8.8, 7.5, 9.0]
    bank_c = [13.2, 11.8, 10.2, 9.0, 10.5]

    x = np.arange(len(scenarios))
    width = 0.25

    ax.bar(x - width, bank_a, width, label='Bank A', color=MLBLUE)
    ax.bar(x, bank_b, width, label='Bank B', color=MLORANGE)
    ax.bar(x + width, bank_c, width, label='Bank C', color=MLGREEN)

    # Minimum requirement line
    ax.axhline(y=7.0, color=MLRED, linestyle='--', linewidth=2, label='Min Requirement (7%)')

    ax.set_ylabel('CET1 Capital Ratio (%)', fontsize=11)
    ax.set_title('Stress Test Results: CET1 Ratio by Scenario', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(scenarios)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 15)

    # Add danger zone
    ax.axhspan(0, 7, alpha=0.1, color=MLRED)
    ax.text(4.3, 3.5, 'Below\nMinimum', fontsize=8, color=MLRED, ha='center')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative stress test]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'stress_testing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
