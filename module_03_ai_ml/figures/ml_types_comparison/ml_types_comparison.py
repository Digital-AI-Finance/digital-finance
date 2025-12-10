"""
Supervised vs Unsupervised vs Reinforcement Learning
Comparison of ML paradigms

Output: ml_types_comparison.pdf
Module: module_03_ai_ml
Lesson: 25 - Introduction to AI/ML
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'ML Types Comparison',
    'module': 'module_03_ai_ml',
    'lesson': 25,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/ml_types_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))

    # Supervised Learning
    ax1 = axes[0]
    np.random.seed(42)
    x1 = np.random.randn(30) + 2
    y1 = np.random.randn(30) + 2
    x2 = np.random.randn(30) - 2
    y2 = np.random.randn(30) - 2
    ax1.scatter(x1, y1, c='#4A90E2', s=50, label='Class A', alpha=0.7)
    ax1.scatter(x2, y2, c='#D62728', s=50, label='Class B', alpha=0.7)
    ax1.axline((0, 0), slope=1, color='#333333', linestyle='--', label='Decision Boundary')
    ax1.set_title('Supervised Learning', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    ax1.legend(fontsize=8)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)

    # Unsupervised Learning
    ax2 = axes[1]
    from matplotlib.patches import Ellipse
    centers = [(2, 2), (-2, -2), (2, -2)]
    colors = ['#4A90E2', '#44A044', '#FF7F0E']
    for center, color in zip(centers, colors):
        x = np.random.randn(20) * 0.8 + center[0]
        y = np.random.randn(20) * 0.8 + center[1]
        ax2.scatter(x, y, c=color, s=50, alpha=0.7)
        ellipse = Ellipse(center, 2.5, 2.5, fill=False, color=color, linestyle='--', linewidth=2)
        ax2.add_patch(ellipse)
    ax2.set_title('Unsupervised Learning', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Feature 1')
    ax2.set_ylabel('Feature 2')
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)

    # Reinforcement Learning
    ax3 = axes[2]
    states = ['S1', 'S2', 'S3', 'S4', 'Goal']
    positions = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 0)]
    for pos, state in zip(positions, states):
        color = '#44A044' if state == 'Goal' else '#4A90E2'
        ax3.scatter(pos[0], pos[1], s=800, c=color, zorder=5)
        ax3.text(pos[0], pos[1], state, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    # Arrows
    arrows = [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (2, 0))]
    for start, end in arrows:
        ax3.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax3.set_title('Reinforcement Learning', fontsize=12, fontweight='bold')
    ax3.set_xlim(-0.5, 2.5)
    ax3.set_ylim(-0.5, 1.5)
    ax3.axis('off')

    fig.suptitle('Machine Learning Paradigms', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'ml_types_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
