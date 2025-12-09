"""
Facial Recognition Verification Flow
Shows how facial recognition works in identity verification

Output: facial_recognition_flow.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Facial Recognition Flow',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/facial_recognition_flow'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create facial recognition verification flow diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Facial Recognition Verification Flow', fontsize=14, fontweight='bold', ha='center')

    # Flow steps (left to right)
    steps = [
        {'name': 'Capture\nSelfie', 'x': 1.5, 'y': 5.5, 'color': '#4A90E2',
         'desc': 'User takes photo\nvia mobile/webcam'},
        {'name': 'Liveness\nDetection', 'x': 4, 'y': 5.5, 'color': '#44A044',
         'desc': 'Verify real person\n(not photo/video)'},
        {'name': 'Face\nExtraction', 'x': 6.5, 'y': 5.5, 'color': '#FF7F0E',
         'desc': 'Extract facial\nfeatures/landmarks'},
        {'name': 'Template\nMatching', 'x': 9, 'y': 5.5, 'color': '#6B5B95',
         'desc': 'Compare to\nID document photo'},
        {'name': 'Decision', 'x': 11.5, 'y': 5.5, 'color': '#333333',
         'desc': 'Match score\nabove threshold'},
    ]

    for step in steps:
        # Circle
        circle = mpatches.Circle((step['x'], step['y']), 0.9, facecolor=step['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)
        ax.text(step['x'], step['y'], step['name'], ha='center', va='center',
               fontsize=8, fontweight='bold', color='white')

        # Description
        ax.text(step['x'], step['y']-1.5, step['desc'], ha='center', fontsize=7)

    # Arrows between steps
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-0.9, steps[i+1]['y']),
                   xytext=(steps[i]['x']+0.9, steps[i]['y']),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Liveness techniques
    liveness = """Liveness Detection Methods:
    - Active: Ask user to blink, smile, turn
    - Passive: Analyze texture, depth, motion
    - 3D: Structured light, stereo vision
    - Challenge-response: Random prompts"""

    ax.text(0.5, 2.5, liveness, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Matching metrics
    metrics = """Match Metrics:
    - FAR: False Accept Rate
    - FRR: False Reject Rate
    - Typical threshold: 99% confidence
    - Industry standard: FAR < 0.1%"""

    ax.text(12.5, 2.5, metrics, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F0FE', edgecolor='#4A90E2'))

    # Attack vectors
    attacks = """Spoofing Attacks: Photo attacks | Video replay | 3D masks | Deepfakes"""
    ax.text(6.5, 1, attacks, ha='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL PROCESS FLOW]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'facial_recognition_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
