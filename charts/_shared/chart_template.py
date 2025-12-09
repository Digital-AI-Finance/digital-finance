"""
Chart Template for Digital Finance Course
Copy this file and modify for new charts

Output: {chart_name}.pdf
Module: {module_name}
Lesson: {lesson_number}
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Import shared utilities
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / '_shared'))
try:
    from colors import COLORS, ACCENTS, SERIES_COLORS
    from styles import apply_chart_style, add_synthetic_label
except ImportError:
    # Fallback if imports fail
    COLORS = {'primary': '#333333', 'secondary': '#666666'}
    ACCENTS = {'blue': '#4A90E2', 'green': '#44A044'}
    SERIES_COLORS = ['#333333', '#666666', '#999999']
    def apply_chart_style():
        plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})
    def add_synthetic_label(ax, position='lower right'):
        pass

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Chart Title Here',
    'module': 'module_XX_name',
    'lesson': 0,
    'description': 'Brief description of the chart',
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/charts/...'
}


def create_chart():
    """Create the chart visualization"""
    # Set random seed for reproducibility
    np.random.seed(42)

    # Apply standard style
    apply_chart_style()

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # ==========================================================
    # YOUR CHART CODE HERE
    # ==========================================================

    # Example: Simple bar chart
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [25, 40, 30, 35]

    bars = ax.bar(categories, values, color=COLORS['primary'], edgecolor='white')

    # Add value labels on bars
    for bar, val in zip(bars, values):
        ax.annotate(
            f'{val}%',
            xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
            ha='center',
            va='bottom',
            fontsize=9,
            fontweight='bold'
        )

    # Labels and title
    ax.set_xlabel('Categories')
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Chart Title', fontweight='bold', fontsize=12)

    # Add synthetic data label
    add_synthetic_label(ax)

    # ==========================================================
    # END CHART CODE
    # ==========================================================

    # Tight layout
    plt.tight_layout()

    # Save to PDF
    output_path = Path(__file__).parent / f'{Path(__file__).stem}.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Chart saved to: {output_path}")
    return output_path


if __name__ == '__main__':
    create_chart()
