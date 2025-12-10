"""
Compliance Costs Analysis
Industry-wide compliance spending

Output: compliance_costs.pdf
Module: module_04_trad_finance
Lesson: 43 - RegTech Compliance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Compliance Costs',
    'module': 'module_04_trad_finance',
    'lesson': 43,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/compliance_costs'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Compliance cost trends
    ax1 = axes[0]

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    total_costs = [230, 250, 280, 320, 350, 380, 410]
    regtech_spend = [15, 22, 32, 48, 68, 95, 130]

    ax1.fill_between(years, total_costs, alpha=0.3, color='#D62728', label='Total Compliance Cost')
    ax1.plot(years, total_costs, 'o-', color='#D62728', linewidth=2, markersize=8)

    ax1.fill_between(years, regtech_spend, alpha=0.5, color='#44A044', label='RegTech Investment')
    ax1.plot(years, regtech_spend, 's-', color='#44A044', linewidth=2, markersize=8)

    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Global Spending ($B)', fontsize=11)
    ax1.set_title('Compliance Costs vs. RegTech Investment', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_ylim(0, 500)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add growth annotation
    ax1.annotate('RegTech CAGR: 42%', xy=(5, 95), xytext=(3, 200),
                fontsize=10, fontweight='bold', color='#44A044',
                arrowprops=dict(arrowstyle='->', color='#44A044'))

    # Cost breakdown by category
    ax2 = axes[1]

    categories = ['Personnel', 'Technology', 'Training', 'Legal &\nConsulting', 'Penalties\n& Fines']
    percentages = [45, 25, 10, 12, 8]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728']

    wedges, texts, autotexts = ax2.pie(percentages, labels=categories, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.02, 0.02, 0.02, 0.02, 0.05])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    for text in texts:
        text.set_fontsize(9)

    ax2.set_title('Compliance Cost Breakdown', fontsize=12, fontweight='bold')

    # Add center annotation
    centre_circle = plt.Circle((0, 0), 0.4, fc='white')
    ax2.add_patch(centre_circle)
    ax2.text(0, 0, 'Avg. Bank:\n$300M/yr', ha='center', va='center',
            fontsize=10, fontweight='bold')

    fig.suptitle('Financial Industry Compliance Costs', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'compliance_costs.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
