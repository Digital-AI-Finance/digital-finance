"""
AI Hierarchy - Nested concepts visualization
Shows the relationship between AI, ML, and Deep Learning

Output: ai_hierarchy.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

# Colors matching slide theme
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLLAVENDER = '#ADADE0'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create nested circles
    circle_ai = plt.Circle((0.5, 0.5), 0.45, color=MLLAVENDER, alpha=0.6, label='Artificial Intelligence')
    circle_ml = plt.Circle((0.5, 0.45), 0.32, color=MLBLUE, alpha=0.5, label='Machine Learning')
    circle_dl = plt.Circle((0.5, 0.4), 0.18, color=MLORANGE, alpha=0.6, label='Deep Learning')

    ax.add_patch(circle_ai)
    ax.add_patch(circle_ml)
    ax.add_patch(circle_dl)

    # Add labels
    ax.text(0.5, 0.92, 'Artificial Intelligence', ha='center', va='center',
            fontsize=12, fontweight='bold', color=MLPURPLE)
    ax.text(0.5, 0.72, 'Machine Learning', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(0.5, 0.4, 'Deep\nLearning', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Add descriptions on the sides
    ax.text(0.02, 0.85, 'Rule-based systems\nExpert systems\nPlanning & search',
            ha='left', va='top', fontsize=9, color='#555555')
    ax.text(0.98, 0.7, 'Decision trees\nSVM, Random Forest\nLinear regression',
            ha='right', va='top', fontsize=9, color='#555555')
    ax.text(0.98, 0.4, 'Neural networks\nCNNs, RNNs\nTransformers',
            ha='right', va='center', fontsize=9, color='#555555')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('AI Hierarchy: Nested Concepts', fontsize=14, fontweight='bold',
                 color=MLPURPLE, pad=10)

    # Add synthetic data label
    fig.text(0.98, 0.02, '[CONCEPTUAL DIAGRAM]', fontsize=7, color='#999999',
             ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_hierarchy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
