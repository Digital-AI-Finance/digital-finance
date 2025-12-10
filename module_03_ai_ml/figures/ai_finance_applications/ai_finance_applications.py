"""
AI/ML Applications in Finance
Overview of key use cases

Output: ai_finance_applications.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'AI/ML Applications in Finance',
    'module': 'module_03_ai_ml',
    'lesson': 25,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/ai_finance_applications'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(12, 7))

    applications = [
        'Fraud Detection', 'Credit Scoring', 'Algorithmic Trading',
        'Risk Management', 'Customer Service', 'Portfolio Optimization',
        'Regulatory Compliance', 'Market Prediction'
    ]
    adoption_rate = [85, 78, 72, 68, 65, 58, 52, 45]
    impact_score = [92, 88, 75, 82, 70, 78, 65, 55]

    colors = ['#4A90E2' if a > 60 else '#999999' for a in adoption_rate]

    bars = ax.barh(applications, adoption_rate, color=colors, alpha=0.8, height=0.6)

    # Add impact markers
    for i, (app, impact) in enumerate(zip(applications, impact_score)):
        ax.scatter(impact, i, color='#D62728', s=100, zorder=5, marker='D')

    ax.set_xlabel('Adoption Rate (%)', fontsize=11)
    ax.set_title('AI/ML Applications in Finance: Adoption & Impact', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 100)

    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [
        plt.Rectangle((0,0), 1, 1, facecolor='#4A90E2', alpha=0.8, label='High Adoption (>60%)'),
        plt.Rectangle((0,0), 1, 1, facecolor='#999999', alpha=0.8, label='Moderate Adoption'),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='#D62728', markersize=10, label='Business Impact')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_finance_applications.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
