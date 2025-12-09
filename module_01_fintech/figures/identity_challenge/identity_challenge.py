"""
Digital Identity Challenge
Shows the core challenges in digital identity verification

Output: identity_challenge.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Digital Identity Challenge',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/identity_challenge'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create digital identity challenge diagram"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'The Digital Identity Challenge', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.5, 9, 'How do you prove who you are online?', fontsize=11, ha='center',
           style='italic', color='#666666')

    # Three core questions
    questions = [
        {'q': 'Are you REAL?', 'x': 2.5, 'color': '#D62728',
         'issues': ['Synthetic identities', 'Bots & automation', 'Deepfakes']},
        {'q': 'Are you WHO\nyou claim?', 'x': 6.5, 'color': '#FF7F0E',
         'issues': ['Identity theft', 'Document fraud', 'Account takeover']},
        {'q': 'Are you the SAME\nperson over time?', 'x': 10.5, 'color': '#4A90E2',
         'issues': ['Session hijacking', 'Credential sharing', 'Continuous auth']},
    ]

    for q in questions:
        # Question circle
        circle = mpatches.Circle((q['x'], 6.5), 1.3, facecolor=q['color'],
                                  edgecolor='#333333', lw=2)
        ax.add_patch(circle)
        ax.text(q['x'], 6.5, q['q'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        # Issues below
        for i, issue in enumerate(q['issues']):
            ax.text(q['x'], 4.5 - i*0.5, f'* {issue}', ha='center', fontsize=8)

    # Statistics box
    stats = """Identity Fraud Statistics (2023):
    - $43B lost to identity fraud globally
    - 1.4M identity theft reports (US FTC)
    - 15% of adults affected by ID theft
    - 80% increase in synthetic ID fraud"""

    ax.text(0.5, 2.5, stats, fontsize=8, va='top',
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Solution categories
    solutions = """Digital Identity Solutions:
    - Document verification (OCR, NFC)
    - Biometrics (face, fingerprint)
    - Liveness detection
    - Knowledge-based verification
    - Database cross-checks
    - Behavioral analytics"""

    ax.text(12.5, 2.5, solutions, fontsize=8, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Stakeholders
    ax.text(6.5, 1.5, 'Stakeholders: Financial institutions | Governments | Consumers | Regulators',
           ha='center', fontsize=9, style='italic', color='#666666')

    # Source
    fig.text(0.5, 0.02, 'Source: Javelin Strategy, FTC Consumer Sentinel Network (2023)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'identity_challenge.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
