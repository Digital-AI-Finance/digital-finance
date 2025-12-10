"""
Algorithmic Bias in Finance
Sources and mitigation of bias

Output: algorithmic_bias.pdf
Module: module_03_ai_ml
Lesson: 36 - AI Regulation
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Algorithmic Bias',
    'module': 'module_03_ai_ml',
    'lesson': 36,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/algorithmic_bias'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Sources of Bias
    ax1 = axes[0]

    sources = ['Historical Data\nBias', 'Sample\nSelection', 'Feature\nEngineering',
               'Label\nBias', 'Proxy\nVariables', 'Feedback\nLoops']
    impact = [85, 70, 65, 75, 80, 60]
    prevalence = [90, 75, 60, 70, 85, 55]

    x = np.arange(len(sources))
    width = 0.35

    bars1 = ax1.bar(x - width/2, impact, width, label='Impact Severity', color='#D62728', alpha=0.8)
    bars2 = ax1.bar(x + width/2, prevalence, width, label='Prevalence', color='#4A90E2', alpha=0.8)

    ax1.set_xlabel('Bias Source', fontsize=11)
    ax1.set_ylabel('Score (0-100)', fontsize=11)
    ax1.set_title('Sources of Algorithmic Bias', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(sources, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 100)
    ax1.yaxis.grid(True, alpha=0.3)

    # Bias Mitigation Pipeline
    ax2 = axes[1]

    stages = ['Pre-processing', 'In-processing', 'Post-processing']
    techniques = [
        ['Reweighting', 'Resampling', 'Fair representation'],
        ['Adversarial debiasing', 'Fairness constraints', 'Regularization'],
        ['Calibration', 'Threshold adjustment', 'Reject option']
    ]
    effectiveness = [75, 85, 70]
    colors = ['#4A90E2', '#44A044', '#FF7F0E']

    for i, (stage, techs, eff, color) in enumerate(zip(stages, techniques, effectiveness, colors)):
        # Stage bar
        ax2.barh(2-i, eff, height=0.5, color=color, alpha=0.8, edgecolor='black')
        ax2.text(eff/2, 2-i, stage, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')

        # Techniques
        for j, tech in enumerate(techs):
            ax2.text(eff + 5 + j*35, 2-i, tech, ha='left', va='center', fontsize=8)

    ax2.set_xlabel('Effectiveness Score', fontsize=11)
    ax2.set_title('Bias Mitigation Techniques', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 130)
    ax2.set_ylim(-0.5, 2.5)
    ax2.set_yticks([])
    ax2.xaxis.grid(True, alpha=0.3)

    # Add header
    ax2.text(100, 2.3, 'Techniques', ha='center', fontsize=10, fontweight='bold')

    fig.suptitle('Algorithmic Bias: Sources and Mitigation', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'algorithmic_bias.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
