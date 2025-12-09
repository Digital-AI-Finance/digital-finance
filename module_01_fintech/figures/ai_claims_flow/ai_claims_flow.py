"""
AI Claims Flow
Shows AI-powered insurance claims processing

Output: ai_claims_flow.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'AI Claims Flow',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ai_claims_flow'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create AI claims flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'AI-Powered Claims Processing', fontsize=20, fontweight='bold', ha='center')

    # Process steps
    steps = [
        {'name': '1. Claim\nSubmission', 'x': 1.5, 'y': 6.5, 'color': '#4A90E2',
         'desc': 'Mobile app\nPhoto/video\nVoice description'},
        {'name': '2. AI\nAnalysis', 'x': 4.5, 'y': 6.5, 'color': '#FF7F0E',
         'desc': 'NLP processing\nImage recognition\nFraud detection'},
        {'name': '3. Auto\nDecision', 'x': 7.5, 'y': 6.5, 'color': '#44A044',
         'desc': 'ML model scoring\nPolicy check\nApprove/escalate'},
        {'name': '4. Instant\nPayout', 'x': 10.5, 'y': 6.5, 'color': '#6B5B95',
         'desc': 'Direct deposit\nReal-time\n3 seconds avg'},
    ]

    # Draw flow arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-1, 6.5), xytext=(steps[i]['x']+1, 6.5),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    for step in steps:
        # Step box
        box = mpatches.FancyBboxPatch((step['x']-1.2, step['y']-1.5), 2.4, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1, step['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=step['color'])
        ax.text(step['x'], step['y']-0.5, step['desc'], ha='center', va='center', fontsize=11)

    # Fraud detection branch
    ax.annotate('', xy=(7.5, 4), xytext=(7.5, 4.8),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2, ls='--'))

    fraud_box = mpatches.FancyBboxPatch((6, 2.5), 3, 1.3,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#D62728', alpha=0.15,
                                         edgecolor='#D62728', lw=2)
    ax.add_patch(fraud_box)
    ax.text(7.5, 3.4, 'Fraud Flag?', ha='center', fontsize=12, fontweight='bold', color='#D62728')
    ax.text(7.5, 2.8, 'Human review', ha='center', fontsize=11)

    # Statistics
    stats = """Performance Metrics:
    - 30% of claims: instant approval (no human)
    - Average processing: 3 seconds vs 3 days traditional
    - Fraud detection: 13x more accurate than manual
    - Customer satisfaction: 4.9/5 rating"""

    ax.text(7, 1.5, stats, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Lemonade, Tractable AI case studies (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_claims_flow.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
