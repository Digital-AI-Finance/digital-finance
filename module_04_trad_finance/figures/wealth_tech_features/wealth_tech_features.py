"""
WealthTech Features
Key technology capabilities

Output: wealth_tech_features.pdf
Module: module_04_trad_finance
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'WealthTech Features',
    'module': 'module_04_trad_finance',
    'lesson': 46,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/wealth_tech_features'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Feature adoption rates
    ax1 = axes[0]

    features = ['Portfolio\nVisualization', 'Goal\nTracking', 'Risk\nAnalytics', 'Tax\nOptimization',
                'ESG\nScoring', 'Alternative\nInvestments', 'AI\nRecommendations', 'Voice/Chat\nInterface']
    adoption = [92, 85, 78, 65, 58, 45, 42, 25]
    priority = [75, 82, 70, 88, 65, 55, 85, 60]  # Client priority score

    x = np.arange(len(features))
    width = 0.35

    bars1 = ax1.bar(x - width/2, adoption, width, label='Current Adoption',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, priority, width, label='Client Priority',
                    color='#FF7F0E', alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Score (%)', fontsize=11)
    ax1.set_title('WealthTech Features: Adoption vs. Priority', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(features, fontsize=8)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 100)
    ax1.yaxis.grid(True, alpha=0.3)

    # Highlight gaps
    for i, (a, p) in enumerate(zip(adoption, priority)):
        if p > a:
            ax1.annotate('', xy=(i + width/2, p), xytext=(i - width/2, a),
                        arrowprops=dict(arrowstyle='<->', color='#D62728', lw=1.5))

    # Technology investment priorities
    ax2 = axes[1]

    priorities = ['Client\nExperience', 'Data &\nAnalytics', 'Automation', 'Regulatory\nCompliance',
                  'Integration', 'Security']
    investment = [28, 22, 18, 15, 10, 7]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#E91E63', '#D62728']

    wedges, texts, autotexts = ax2.pie(investment, labels=priorities, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    for text in texts:
        text.set_fontsize(9)

    ax2.set_title('Technology Investment Priorities', fontsize=12, fontweight='bold')

    fig.suptitle('WealthTech Capabilities & Investment', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'wealth_tech_features.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
