"""
ML Types - Supervised, Unsupervised, Reinforcement Learning comparison
Bar chart showing key characteristics and use cases

Output: ml_types.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML in Finance
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

    categories = ['Supervised\nLearning', 'Unsupervised\nLearning', 'Reinforcement\nLearning']

    # Data: approximate usage in finance (%)
    usage = [65, 25, 10]
    colors = [MLBLUE, MLORANGE, MLGREEN]

    bars = ax.bar(categories, usage, color=colors, edgecolor='white', linewidth=2)

    # Add value labels on bars
    for bar, val in zip(bars, usage):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{val}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Add example use cases below each bar
    examples = [
        'Credit scoring\nFraud detection\nPrice prediction',
        'Customer segmentation\nAnomaly detection\nPattern discovery',
        'Trading strategies\nPortfolio optimization\nDynamic pricing'
    ]

    for i, (bar, example) in enumerate(zip(bars, examples)):
        ax.text(bar.get_x() + bar.get_width()/2, -8,
                example, ha='center', va='top', fontsize=8, color='#555555')

    ax.set_ylabel('Usage in Finance (%)', fontsize=11)
    ax.set_ylim(0, 85)
    ax.set_title('Machine Learning Types in Finance', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add synthetic data label
    fig.text(0.98, 0.02, '[SYNTHETIC DATA - Illustrative estimates]', fontsize=7,
             color='#999999', ha='right', style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.22)

    output_path = Path(__file__).parent / 'ml_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
