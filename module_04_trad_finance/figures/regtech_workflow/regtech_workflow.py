"""
RegTech Compliance Workflow
End-to-end compliance automation

Output: regtech_workflow.pdf
Module: module_04_trad_finance
Lesson: 43 - RegTech Compliance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Workflow',
    'module': 'module_04_trad_finance',
    'lesson': 43,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/regtech_workflow'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Workflow stages
    stages = [
        ('Data\nIngestion', 1.5, 6, '#4A90E2'),
        ('Validation\n& Cleansing', 4, 6, '#44A044'),
        ('Rule\nEngine', 6.5, 6, '#FF7F0E'),
        ('Risk\nAnalysis', 9, 6, '#9B59B6'),
        ('Reporting\n& Filing', 11.5, 6, '#D62728'),
    ]

    # Draw stages
    for name, x, y, color in stages:
        rect = mpatches.FancyBboxPatch((x-1, y-0.6), 2, 1.2,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')

    # Arrows between stages
    for i in range(len(stages)-1):
        ax.annotate('', xy=(stages[i+1][1]-1, stages[i+1][2]),
                   xytext=(stages[i][1]+1, stages[i][2]),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))

    # Data sources (bottom left)
    sources = ['Core Banking', 'Trading Systems', 'CRM', 'External Data']
    for i, src in enumerate(sources):
        rect = mpatches.FancyBboxPatch((0.3, 3.5-i*0.9), 2.2, 0.7,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#E8E8E8', edgecolor='#888888')
        ax.add_patch(rect)
        ax.text(1.4, 3.85-i*0.9, src, ha='center', va='center', fontsize=9)

    # Arrow from sources to ingestion
    ax.annotate('', xy=(1.5, 5.4), xytext=(1.5, 4.2),
               arrowprops=dict(arrowstyle='->', lw=2, color='#4A90E2'))

    # Regulatory outputs (right side)
    outputs = ['SEC Reports', 'CFTC Filings', 'Fed Reports', 'AML Reports', 'MiFID II']
    for i, out in enumerate(outputs):
        rect = mpatches.FancyBboxPatch((12.5, 4-i*0.8), 1.4, 0.6,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#FFE4E1', edgecolor='#D62728')
        ax.add_patch(rect)
        ax.text(13.2, 4.3-i*0.8, out, ha='center', va='center', fontsize=8)

    # Arrow from reporting to outputs
    ax.annotate('', xy=(12.5, 3.5), xytext=(11.5, 5.4),
               arrowprops=dict(arrowstyle='->', lw=2, color='#D62728'))

    # ML/AI enhancement box
    ml_box = mpatches.FancyBboxPatch((5, 3), 4, 1.2,
                                      boxstyle="round,pad=0.05",
                                      facecolor='#E6F3FF', edgecolor='#4A90E2', linewidth=2, linestyle='--')
    ax.add_patch(ml_box)
    ax.text(7, 3.6, 'AI/ML Enhancement Layer', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#4A90E2')
    ax.text(7, 3.2, 'Pattern Detection | Anomaly Alerts | Predictive Analytics',
            ha='center', va='center', fontsize=8, color='#666666')

    # Arrows to/from ML layer
    ax.annotate('', xy=(7, 4.2), xytext=(7, 5.4),
               arrowprops=dict(arrowstyle='<->', lw=1.5, color='#4A90E2', linestyle='--'))

    # Title and metrics
    ax.text(7, 7.5, 'RegTech Compliance Workflow', ha='center', va='center',
            fontsize=14, fontweight='bold')

    # Key metrics box
    metrics_box = mpatches.FancyBboxPatch((0.3, 0.3), 4.5, 1.8,
                                           boxstyle="round,pad=0.05",
                                           facecolor='#F5F5F5', edgecolor='#888888')
    ax.add_patch(metrics_box)
    ax.text(2.55, 1.9, 'Key Metrics', ha='center', va='center', fontsize=10, fontweight='bold')
    metrics = ['Processing: <5 min per report', 'Accuracy: 99.5%+', 'Cost reduction: 60-80%']
    for i, m in enumerate(metrics):
        ax.text(0.5, 1.5-i*0.4, f'• {m}', ha='left', va='center', fontsize=9)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'regtech_workflow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
