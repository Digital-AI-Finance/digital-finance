"""
KYC RegTech Flow
Shows automated KYC process flow

Output: kyc_regtech_flow.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'KYC RegTech Flow',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/kyc_regtech_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create KYC RegTech flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Automated KYC/CDD Process', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Know Your Customer / Customer Due Diligence', fontsize=13, ha='center', color='#666666')

    # Process flow
    steps = [
        {'name': 'Customer\nData Input', 'x': 2, 'y': 6, 'color': '#4A90E2',
         'time': '2 min', 'method': 'Mobile/web form'},
        {'name': 'Document\nVerification', 'x': 5, 'y': 6, 'color': '#44A044',
         'time': '30 sec', 'method': 'AI/OCR'},
        {'name': 'Identity\nProofing', 'x': 8, 'y': 6, 'color': '#FF7F0E',
         'time': '15 sec', 'method': 'Biometrics'},
        {'name': 'Risk\nAssessment', 'x': 11, 'y': 6, 'color': '#6B5B95',
         'time': '10 sec', 'method': 'ML scoring'},
    ]

    for i, step in enumerate(steps):
        box = mpatches.FancyBboxPatch((step['x']-1.3, step['y']-1.5), 2.6, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1, step['name'], ha='center',
               fontsize=12, fontweight='bold', color=step['color'])
        ax.text(step['x'], step['y']+0.1, step['method'], ha='center', fontsize=10)
        ax.text(step['x'], step['y']-0.6, step['time'], ha='center',
               fontsize=13, fontweight='bold', color='#44A044')

        if i < len(steps) - 1:
            ax.annotate('', xy=(steps[i+1]['x']-1.4, 6), xytext=(step['x']+1.4, 6),
                       arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Outcome branch
    ax.annotate('', xy=(7, 3.5), xytext=(11, 4.3),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    outcomes = [
        {'name': 'Low Risk\nAuto-Approve', 'x': 4, 'y': 2.5, 'color': '#44A044', 'pct': '70%'},
        {'name': 'Medium Risk\nEnhanced DD', 'x': 8, 'y': 2.5, 'color': '#FF7F0E', 'pct': '25%'},
        {'name': 'High Risk\nManual Review', 'x': 12, 'y': 2.5, 'color': '#D62728', 'pct': '5%'},
    ]

    for out in outcomes:
        box = mpatches.FancyBboxPatch((out['x']-1.5, out['y']-0.8), 3, 1.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=out['color'], alpha=0.15,
                                       edgecolor=out['color'], lw=1.5)
        ax.add_patch(box)
        ax.text(out['x'], out['y']+0.3, out['name'], ha='center', fontsize=11, fontweight='bold')
        ax.text(out['x'], out['y']-0.3, out['pct'], ha='center', fontsize=12, color=out['color'])

    # Total time
    total = "Total Time: ~3 minutes vs 3-5 days traditional | Cost: $5 vs $50+ manual"
    ax.text(7, 0.8, total, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Jumio, Onfido customer case studies (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'kyc_regtech_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
