"""
Types of Financial Data
Overview of structured vs unstructured data

Output: financial_data_types.pdf
Module: module_03_ai_ml
Lesson: 26 - Financial Data
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Financial Data Types',
    'module': 'module_03_ai_ml',
    'lesson': 26,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/financial_data_types'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(12, 7))

    categories = ['Market Data', 'Fundamental\nData', 'Alternative\nData', 'Text Data', 'Transaction\nData']
    structured = [95, 90, 40, 15, 85]
    unstructured = [5, 10, 60, 85, 15]

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, structured, width, label='Structured', color='#4A90E2')
    bars2 = ax.bar(x + width/2, unstructured, width, label='Unstructured', color='#FF7F0E')

    ax.set_xlabel('Data Category', fontsize=11)
    ax.set_ylabel('Percentage (%)', fontsize=11)
    ax.set_title('Financial Data: Structured vs Unstructured', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 110)

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'financial_data_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
