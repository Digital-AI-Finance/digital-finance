"""
Machine Learning Hierarchy Pyramid
Visualization of AI/ML/DL conceptual hierarchy

Required libraries: matplotlib, numpy
Output: ml_hierarchy.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Machine Learning Hierarchy Pyramid',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_03_ai_ml/ml_hierarchy'
}

def create_ml_hierarchy():
    """Create a pyramid visualization of AI/ML/DL hierarchy"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, ax = plt.subplots(figsize=(10, 7))

    # Pyramid layers (from bottom to top)
    layers = [
        {
            'name': 'Artificial Intelligence (AI)',
            'description': 'Machines mimicking human cognitive functions',
            'examples': 'Expert Systems, Game Playing, Natural Language Processing',
            'y_bottom': 0,
            'y_top': 2,
            'color': 'lightgray'
        },
        {
            'name': 'Machine Learning (ML)',
            'description': 'Algorithms that learn from data without explicit programming',
            'examples': 'Linear Regression, Decision Trees, SVM, Random Forests',
            'y_bottom': 2,
            'y_top': 3.5,
            'color': 'gray'
        },
        {
            'name': 'Deep Learning (DL)',
            'description': 'Neural networks with multiple layers',
            'examples': 'CNNs, RNNs, Transformers, LLMs',
            'y_bottom': 3.5,
            'y_top': 4.5,
            'color': 'darkgray'
        }
    ]

    # Calculate pyramid coordinates
    pyramid_base = 8
    pyramid_top = 2

    for i, layer in enumerate(layers):
        y_bottom = layer['y_bottom']
        y_top = layer['y_top']

        # Calculate width at this height
        # Linear interpolation from base to top
        total_height = 4.5
        width_bottom = pyramid_base - (pyramid_base - pyramid_top) * (y_bottom / total_height)
        width_top = pyramid_base - (pyramid_base - pyramid_top) * (y_top / total_height)

        # Create trapezoid
        vertices = [
            [-width_bottom/2, y_bottom],
            [width_bottom/2, y_bottom],
            [width_top/2, y_top],
            [-width_top/2, y_top]
        ]

        polygon = Polygon(vertices,
                         closed=True,
                         facecolor=layer['color'],
                         edgecolor='black',
                         linewidth=2)
        ax.add_patch(polygon)

        # Add text
        y_center = (y_bottom + y_top) / 2

        # Layer name
        ax.text(0, y_center + 0.3, layer['name'],
               ha='center', va='center',
               fontsize=10, fontweight='bold')

        # Description
        ax.text(0, y_center, layer['description'],
               ha='center', va='center',
               fontsize=7, style='italic')

        # Examples
        ax.text(0, y_center - 0.3, layer['examples'],
               ha='center', va='center',
               fontsize=6)

    # Add arrows showing relationship
    arrow_props = dict(arrowstyle='->', lw=1.5, color='black')

    # Add side annotations
    annotations = [
        (5.5, 3.0, 'Increasing\nSpecialization'),
        (5.5, 2.5, 'Decreasing\nInterpretability'),
        (-5.5, 3.0, 'Increasing\nComplexity'),
        (-5.5, 2.5, 'Higher\nPerformance')
    ]

    for x, y, text in annotations:
        ax.annotate(text,
                   xy=(0, y), xytext=(x, y),
                   fontsize=7, ha='center',
                   bbox=dict(boxstyle='round,pad=0.4',
                           facecolor='white',
                           edgecolor='gray',
                           linewidth=0.5))

    # Title
    ax.text(0, 5.2, 'Artificial Intelligence Hierarchy',
           ha='center', va='center',
           fontsize=12, fontweight='bold')

    # Add timeline at bottom
    timeline_text = 'Timeline: AI (1950s) → ML (1980s) → DL (2010s)'
    ax.text(0, -0.5, timeline_text,
           ha='center', va='center',
           fontsize=7,
           bbox=dict(boxstyle='round,pad=0.3',
                    facecolor='white',
                    edgecolor='black',
                    linewidth=0.5))

    # Set axis properties
    ax.set_xlim(-7, 7)
    ax.set_ylim(-1, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'ml_hierarchy.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_ml_hierarchy()
