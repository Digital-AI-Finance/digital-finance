"""
Data Leakage in Finance
Common sources and prevention

Output: data_leakage.pdf
Module: module_03_ai_ml
Lesson: 34 - Prediction Limitations
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Data Leakage',
    'module': 'module_03_ai_ml',
    'lesson': 34,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/data_leakage'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Types of Data Leakage
    ax1 = axes[0]

    types = ['Look-Ahead\nBias', 'Target\nLeakage', 'Train-Test\nContamination',
             'Survivorship\nBias', 'Time-Travel\nBias']
    severity = [95, 85, 80, 70, 65]
    frequency = [40, 35, 45, 30, 50]

    colors = ['#D62728', '#FF7F0E', '#FF7F0E', '#FFD700', '#FFD700']

    x = np.arange(len(types))
    width = 0.35

    bars1 = ax1.barh(x - width/2, severity, height=width, label='Severity', color=colors, alpha=0.8)
    bars2 = ax1.barh(x + width/2, frequency, height=width, label='Frequency', color='#4A90E2', alpha=0.6)

    ax1.set_xlabel('Score (0-100)', fontsize=11)
    ax1.set_title('Data Leakage Types in Finance', fontsize=12, fontweight='bold')
    ax1.set_yticks(x)
    ax1.set_yticklabels(types, fontsize=10)
    ax1.legend(loc='lower right', fontsize=9)
    ax1.set_xlim(0, 110)
    ax1.xaxis.grid(True, alpha=0.3)

    # Correct vs Incorrect Timeline
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)

    # Incorrect (with leakage)
    rect1 = mpatches.FancyBboxPatch((0.5, 5), 9, 2.5,
                                     boxstyle="round,pad=0.1",
                                     facecolor='#FFE4E4', edgecolor='#D62728', linewidth=2)
    ax2.add_patch(rect1)
    ax2.text(5, 7, 'WRONG: Random Train/Test Split', ha='center', fontsize=11,
            fontweight='bold', color='#D62728')

    # Wrong timeline bars
    ax2.barh(6, 3, left=1, height=0.4, color='#4A90E2', alpha=0.7, label='Train')
    ax2.barh(6, 1.5, left=4.5, height=0.4, color='#D62728', alpha=0.7, label='Test')
    ax2.barh(6, 2, left=6.5, height=0.4, color='#4A90E2', alpha=0.7)
    ax2.text(5, 5.3, 'Future data leaks into training!', fontsize=9, ha='center', style='italic')

    # Correct (time-series split)
    rect2 = mpatches.FancyBboxPatch((0.5, 0.5), 9, 2.5,
                                     boxstyle="round,pad=0.1",
                                     facecolor='#E4FFE4', edgecolor='#44A044', linewidth=2)
    ax2.add_patch(rect2)
    ax2.text(5, 2.5, 'CORRECT: Time-Series Split', ha='center', fontsize=11,
            fontweight='bold', color='#44A044')

    # Correct timeline bars
    ax2.barh(1.5, 5, left=1, height=0.4, color='#4A90E2', alpha=0.7)
    ax2.barh(1.5, 2.5, left=6.5, height=0.4, color='#D62728', alpha=0.7)
    ax2.text(3.5, 1.1, 'Train (Past)', fontsize=9, ha='center')
    ax2.text(7.75, 1.1, 'Test (Future)', fontsize=9, ha='center')

    # Time arrow
    ax2.annotate('', xy=(9.5, 4), xytext=(0.5, 4),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax2.text(5, 4.3, 'Time', fontsize=10, ha='center', fontweight='bold')

    ax2.set_title('Proper Time-Series Train/Test Split', fontsize=12, fontweight='bold')
    ax2.axis('off')

    fig.suptitle('Data Leakage: A Critical ML Pitfall', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'data_leakage.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
