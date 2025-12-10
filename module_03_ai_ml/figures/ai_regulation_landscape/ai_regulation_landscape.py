"""
AI Regulation Landscape
Global regulatory frameworks for AI in finance

Output: ai_regulation_landscape.pdf
Module: module_03_ai_ml
Lesson: 36 - AI Regulation
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'AI Regulation Landscape',
    'module': 'module_03_ai_ml',
    'lesson': 36,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/ai_regulation_landscape'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Regulatory Strictness by Region
    ax1 = axes[0]

    regions = ['EU\n(AI Act)', 'UK\n(FCA)', 'USA\n(SEC/Fed)', 'Singapore\n(MAS)',
               'China\n(PBOC)', 'Switzerland\n(FINMA)']

    # Scores for different aspects (0-10)
    explainability = [9, 7, 5, 7, 6, 6]
    fairness = [9, 8, 6, 7, 5, 7]
    transparency = [10, 7, 5, 8, 4, 8]
    risk_mgmt = [8, 8, 7, 8, 7, 9]

    x = np.arange(len(regions))
    width = 0.2

    ax1.bar(x - 1.5*width, explainability, width, label='Explainability', color='#4A90E2', alpha=0.8)
    ax1.bar(x - 0.5*width, fairness, width, label='Fairness', color='#44A044', alpha=0.8)
    ax1.bar(x + 0.5*width, transparency, width, label='Transparency', color='#FF7F0E', alpha=0.8)
    ax1.bar(x + 1.5*width, risk_mgmt, width, label='Risk Management', color='#9B59B6', alpha=0.8)

    ax1.set_xlabel('Jurisdiction', fontsize=11)
    ax1.set_ylabel('Regulatory Requirement Score (0-10)', fontsize=11)
    ax1.set_title('AI Regulatory Requirements by Region', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(regions, fontsize=9)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_ylim(0, 11)
    ax1.yaxis.grid(True, alpha=0.3)

    # AI Risk Categories
    ax2 = axes[1]

    risk_levels = ['Unacceptable\nRisk', 'High\nRisk', 'Limited\nRisk', 'Minimal\nRisk']
    colors = ['#D62728', '#FF7F0E', '#FFD700', '#44A044']

    # Examples per risk level
    examples = [
        'Social scoring\nManipulation',
        'Credit scoring\nEmployment AI\nBiometric ID',
        'Chatbots\nDeepfakes\nEmotion AI',
        'AI games\nSpam filters\nInventory AI'
    ]

    requirements = [
        'BANNED',
        'Conformity assessment\nRisk management\nData governance\nTransparency',
        'Transparency\nobligations',
        'No specific\nrequirements'
    ]

    y = [4, 3, 2, 1]
    bar_heights = [0.8] * 4

    for i, (level, color, example, req) in enumerate(zip(risk_levels, colors, examples, requirements)):
        ax2.barh(y[i], 3, height=0.6, color=color, alpha=0.8, edgecolor='black')
        ax2.text(1.5, y[i], level, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax2.text(3.5, y[i], example, ha='left', va='center', fontsize=8)
        ax2.text(7, y[i], req, ha='left', va='center', fontsize=8, color='#333333')

    # Headers
    ax2.text(1.5, 4.7, 'Risk Level', ha='center', fontsize=10, fontweight='bold')
    ax2.text(4.5, 4.7, 'Examples', ha='center', fontsize=10, fontweight='bold')
    ax2.text(8, 4.7, 'Requirements', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlim(0, 11)
    ax2.set_ylim(0.3, 5)
    ax2.set_title('EU AI Act: Risk-Based Classification', fontsize=12, fontweight='bold')
    ax2.axis('off')

    fig.suptitle('Global AI Regulation in Financial Services', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_regulation_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
