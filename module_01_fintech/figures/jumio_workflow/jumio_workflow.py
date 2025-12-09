"""
Jumio Identity Verification Workflow
Shows the end-to-end IDV process using Jumio as example

Output: jumio_workflow.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Jumio IDV Workflow',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/jumio_workflow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create Jumio workflow diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Identity Verification Workflow (Jumio Example)', fontsize=14, fontweight='bold', ha='center')

    # Workflow steps
    steps = [
        {'name': 'SDK\nIntegration', 'x': 1.5, 'y': 7, 'color': '#4A90E2',
         'desc': 'Mobile SDK or\nWeb redirect'},
        {'name': 'Document\nCapture', 'x': 4, 'y': 7, 'color': '#44A044',
         'desc': 'ID front/back\nwith guidance'},
        {'name': 'Selfie\nCapture', 'x': 6.5, 'y': 7, 'color': '#FF7F0E',
         'desc': 'Liveness\ndetection'},
        {'name': 'AI\nProcessing', 'x': 9, 'y': 7, 'color': '#6B5B95',
         'desc': 'Automated\nverification'},
        {'name': 'Result &\nDecision', 'x': 11.5, 'y': 7, 'color': '#333333',
         'desc': 'Pass/Fail +\nConfidence score'},
    ]

    for step in steps:
        # Box
        box = mpatches.FancyBboxPatch((step['x']-0.8, step['y']-0.5), 1.6, 1.3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], edgecolor='#333333', lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+0.15, step['name'], ha='center', va='center',
               fontsize=8, fontweight='bold', color='white')
        ax.text(step['x'], step['y']-1.1, step['desc'], ha='center', fontsize=7)

    # Arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-0.9, steps[i+1]['y']),
                   xytext=(steps[i]['x']+0.9, steps[i]['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Processing details
    processing = mpatches.FancyBboxPatch((2, 2.5), 9, 2.5, boxstyle='round,pad=0.1',
                                          facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1.5)
    ax.add_patch(processing)
    ax.text(6.5, 4.7, 'AI Processing Components', ha='center', fontsize=10, fontweight='bold')

    components = [
        ('Document Authentication', 'Security features, template matching, fraud signals'),
        ('Data Extraction', 'OCR + NFC (if available), MRZ parsing'),
        ('Biometric Comparison', 'Face match between selfie and ID photo'),
        ('Risk Scoring', 'Device signals, velocity checks, behavioral analysis'),
    ]
    for i, (comp, desc) in enumerate(components):
        ax.text(2.5, 4.1-i*0.45, f'* {comp}:', fontsize=8, fontweight='bold')
        ax.text(5.5, 4.1-i*0.45, desc, fontsize=7)

    # Metrics
    metrics = """Jumio Performance (2024):
    - 200+ countries/territories
    - 5,000+ document types
    - <60 second average completion
    - 98%+ pass-through rate
    Source: Jumio public data"""

    ax.text(0.3, 2, metrics, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Output options
    outputs = """Output Options:
    - Real-time webhook
    - Batch API response
    - Manual review queue
    - Audit trail/evidence"""

    ax.text(12.7, 2, outputs, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F0FE', edgecolor='#4A90E2'))

    # Source
    fig.text(0.5, 0.02, 'Source: Jumio product documentation (2024)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'jumio_workflow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
