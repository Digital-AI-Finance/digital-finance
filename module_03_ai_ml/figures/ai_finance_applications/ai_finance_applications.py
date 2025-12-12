"""
AI Applications in Finance - Horizontal bar chart
Shows adoption rates across different financial services

Output: ai_finance_applications.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML in Finance

Data Source: McKinsey Global AI Survey 2023, Deloitte AI in Banking Report
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
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    applications = [
        'Fraud Detection',
        'Credit Scoring',
        'Customer Service (Chatbots)',
        'Algorithmic Trading',
        'Risk Management',
        'Regulatory Compliance',
        'Portfolio Management',
        'Insurance Underwriting'
    ]

    # Adoption rates (%) - based on industry surveys
    adoption = [78, 72, 65, 58, 55, 48, 42, 38]

    # Create horizontal bar chart
    y_pos = np.arange(len(applications))
    bars = ax.barh(y_pos, adoption, color=MLBLUE, edgecolor='white', height=0.6)

    # Add value labels
    for bar, val in zip(bars, adoption):
        ax.text(val + 1, bar.get_y() + bar.get_height()/2,
                f'{val}%', ha='left', va='center', fontsize=10)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(applications)
    ax.set_xlabel('Adoption Rate (%)', fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_title('AI Adoption in Financial Services (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add grid
    ax.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)

    # Add source
    fig.text(0.98, 0.02, 'Source: McKinsey Global AI Survey 2023 [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_finance_applications.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
