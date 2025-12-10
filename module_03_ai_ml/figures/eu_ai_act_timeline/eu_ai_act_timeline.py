"""
EU AI Act Timeline
Implementation timeline and requirements

Output: eu_ai_act_timeline.pdf
Module: module_03_ai_ml
Lesson: 36 - AI Regulation
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'EU AI Act Timeline',
    'module': 'module_03_ai_ml',
    'lesson': 36,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/eu_ai_act_timeline'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    # Timeline base
    ax.plot([1, 15], [4, 4], 'k-', linewidth=3)

    # Key dates
    events = [
        (2, 'Apr 2021', 'Proposal\nPublished', '#4A90E2'),
        (4.5, 'Dec 2023', 'Political\nAgreement', '#44A044'),
        (7, 'Jul 2024', 'Entry into\nForce', '#FF7F0E'),
        (9.5, 'Feb 2025', 'Prohibited AI\nBans Apply', '#D62728'),
        (12, 'Aug 2025', 'GPAI Rules\nApply', '#9B59B6'),
        (14.5, 'Aug 2026', 'Full\nApplication', '#D62728')
    ]

    for x, date, event, color in events:
        ax.plot([x, x], [3.5, 4.5], color=color, linewidth=3)
        ax.plot(x, 4, 'o', color=color, markersize=15, markeredgecolor='black', markeredgewidth=2)

        # Date above
        ax.text(x, 5, date, ha='center', fontsize=9, fontweight='bold')

        # Event below
        rect = mpatches.FancyBboxPatch((x-0.9, 1.5), 1.8, 1.5,
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, alpha=0.3,
                                        edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 2.25, event, ha='center', va='center', fontsize=8)

    # Financial Services specific
    ax.text(8, 6.5, 'Key Requirements for Financial AI', fontsize=12, fontweight='bold', ha='center')

    requirements = [
        'Credit scoring: High-risk classification',
        'Fraud detection: Risk assessment required',
        'Trading algorithms: Transparency obligations',
        'Insurance pricing: Fairness requirements',
        'KYC/AML: Human oversight mandatory'
    ]

    for i, req in enumerate(requirements):
        ax.text(8, 6 - i*0.35, f'- {req}', ha='center', fontsize=9)

    # Now marker
    ax.axvline(x=8.5, color='#D62728', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(8.5, 5.5, 'NOW', fontsize=10, fontweight='bold', color='#D62728', ha='center')

    ax.set_title('EU AI Act: Implementation Timeline', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'eu_ai_act_timeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
