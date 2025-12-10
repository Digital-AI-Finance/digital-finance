"""
Decision Boundary Visualization
Classification boundary examples

Output: decision_boundary.pdf
Module: module_03_ai_ml
Lesson: 28 - Classification
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Decision Boundary',
    'module': 'module_03_ai_ml',
    'lesson': 28,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/decision_boundary'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    np.random.seed(42)

    # Generate data
    n = 100
    X1_class1 = np.random.randn(n, 2) + [2, 2]
    X1_class2 = np.random.randn(n, 2) + [-2, -2]

    # Logistic Regression (linear)
    ax1 = axes[0]
    ax1.scatter(X1_class1[:, 0], X1_class1[:, 1], c='#4A90E2', s=30, alpha=0.6, label='Low Risk')
    ax1.scatter(X1_class2[:, 0], X1_class2[:, 1], c='#D62728', s=30, alpha=0.6, label='High Risk')
    ax1.axline((0, 0), slope=1, color='k', linewidth=2, linestyle='--')
    ax1.set_title('Logistic Regression\n(Linear Boundary)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    ax1.legend(fontsize=8)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)

    # Random Forest (complex)
    ax2 = axes[1]
    ax2.scatter(X1_class1[:, 0], X1_class1[:, 1], c='#4A90E2', s=30, alpha=0.6)
    ax2.scatter(X1_class2[:, 0], X1_class2[:, 1], c='#D62728', s=30, alpha=0.6)
    # Simulate complex boundary
    theta = np.linspace(0, 2*np.pi, 100)
    r = 2.5 + 0.5 * np.sin(5*theta)
    ax2.plot(r * np.cos(theta), r * np.sin(theta), 'k--', linewidth=2)
    ax2.set_title('Random Forest\n(Non-linear Boundary)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Feature 1')
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)

    # SVM with RBF
    ax3 = axes[2]
    ax3.scatter(X1_class1[:, 0], X1_class1[:, 1], c='#4A90E2', s=30, alpha=0.6)
    ax3.scatter(X1_class2[:, 0], X1_class2[:, 1], c='#D62728', s=30, alpha=0.6)
    circle = plt.Circle((0, 0), 2.8, fill=False, color='k', linewidth=2, linestyle='--')
    ax3.add_patch(circle)
    ax3.set_title('SVM (RBF Kernel)\n(Smooth Boundary)', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Feature 1')
    ax3.set_xlim(-5, 5)
    ax3.set_ylim(-5, 5)
    ax3.set_aspect('equal')

    fig.suptitle('Decision Boundaries: Classification Algorithms', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'decision_boundary.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
