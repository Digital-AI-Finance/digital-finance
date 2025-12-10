"""
Data Preprocessing Pipeline
Steps for preparing financial data

Output: data_preprocessing_pipeline.pdf
Module: module_03_ai_ml
Lesson: 26 - Financial Data
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Data Preprocessing Pipeline',
    'module': 'module_03_ai_ml',
    'lesson': 26,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/data_preprocessing_pipeline'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 6))

    steps = [
        ('Raw Data\nIngestion', '#E74C3C'),
        ('Missing Value\nHandling', '#F39C12'),
        ('Outlier\nDetection', '#F1C40F'),
        ('Feature\nScaling', '#2ECC71'),
        ('Feature\nEncoding', '#3498DB'),
        ('Train/Test\nSplit', '#9B59B6')
    ]

    box_width = 0.12
    box_height = 0.25

    for i, (label, color) in enumerate(steps):
        x = 0.05 + i * 0.155
        rect = mpatches.FancyBboxPatch((x, 0.4), box_width, box_height,
                                        boxstyle="round,pad=0.02", facecolor=color,
                                        edgecolor='#333333', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + box_width/2, 0.525, label, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

        if i < len(steps) - 1:
            ax.annotate('', xy=(x + box_width + 0.03, 0.525),
                       xytext=(x + box_width + 0.01, 0.525),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Add descriptions below
    descriptions = [
        'CSV, API, DB',
        'Imputation,\nDeletion',
        'Z-score,\nIQR method',
        'StandardScaler,\nMinMax',
        'One-Hot,\nLabel Encoding',
        '80/20 or\nTime-based'
    ]
    for i, desc in enumerate(descriptions):
        x = 0.05 + i * 0.155 + box_width/2
        ax.text(x, 0.25, desc, ha='center', va='center', fontsize=8, color='#666666')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.8)
    ax.axis('off')
    ax.set_title('Financial Data Preprocessing Pipeline', fontsize=14, fontweight='bold', pad=20)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_preprocessing_pipeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
