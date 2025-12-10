"""
Fraud Types Distribution
Types and frequency of financial fraud

Output: fraud_types_distribution.pdf
Module: module_03_ai_ml
Lesson: 31 - Fraud Detection
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Fraud Types Distribution',
    'module': 'module_03_ai_ml',
    'lesson': 31,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/fraud_types_distribution'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Fraud types pie chart
    ax1 = axes[0]
    types = ['Card-Not-Present', 'Account Takeover', 'Identity Theft',
             'Synthetic ID', 'First-Party Fraud', 'Other']
    percentages = [35, 22, 18, 12, 8, 5]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#888888']

    wedges, texts, autotexts = ax1.pie(percentages, labels=types, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax1.set_title('Distribution of Fraud Types', fontsize=12, fontweight='bold')

    # Year-over-year trends
    ax2 = axes[1]
    years = ['2019', '2020', '2021', '2022', '2023']
    cnp = [28, 32, 38, 42, 35]
    ato = [15, 18, 22, 25, 22]
    identity = [12, 14, 16, 18, 18]

    x = np.arange(len(years))
    width = 0.25

    ax2.bar(x - width, cnp, width, label='Card-Not-Present', color='#4A90E2', alpha=0.8)
    ax2.bar(x, ato, width, label='Account Takeover', color='#44A044', alpha=0.8)
    ax2.bar(x + width, identity, width, label='Identity Theft', color='#FF7F0E', alpha=0.8)

    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Fraud Volume Index', fontsize=11)
    ax2.set_title('Fraud Type Trends Over Time', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(years)
    ax2.legend(loc='upper left', fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    # COVID annotation
    ax2.annotate('COVID-19\nImpact', xy=(1, 32), xytext=(1.5, 40),
                fontsize=9, fontweight='bold', color='#D62728',
                arrowprops=dict(arrowstyle='->', color='#D62728'))

    fig.suptitle('Financial Fraud Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'fraud_types_distribution.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
