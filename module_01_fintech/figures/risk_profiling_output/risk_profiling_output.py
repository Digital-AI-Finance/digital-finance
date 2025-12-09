"""
Risk Profiling Output
Shows how risk questionnaires translate to portfolio allocation

Output: risk_profiling_output.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Risk Profiling Output',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/risk_profiling_output'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create risk profiling output diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Risk Profiling: From Questions to Portfolio', fontsize=20, fontweight='bold', ha='center')

    # Input questions (left)
    questions_box = mpatches.FancyBboxPatch((0.5, 3), 4, 5.5, boxstyle='round,pad=0.1',
                                             facecolor='#4A90E2', alpha=0.15,
                                             edgecolor='#4A90E2', lw=2)
    ax.add_patch(questions_box)
    ax.text(2.5, 8, 'Risk Questions', ha='center', fontsize=14, fontweight='bold', color='#4A90E2')

    questions = [
        '1. Investment timeline?',
        '2. Risk tolerance?',
        '3. Financial goals?',
        '4. Income stability?',
        '5. Market reaction?',
    ]
    for i, q in enumerate(questions):
        ax.text(0.8, 7.2-i*0.8, q, fontsize=11)

    # Processing (center)
    ax.annotate('', xy=(5.5, 5.5), xytext=(4.7, 5.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    process_box = mpatches.FancyBboxPatch((5.5, 4.5), 3, 2, boxstyle='round,pad=0.1',
                                           facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(process_box)
    ax.text(7, 5.8, 'Algorithm', ha='center', fontsize=12, fontweight='bold', color='white')
    ax.text(7, 5.2, 'Risk Score', ha='center', fontsize=12, color='white')

    ax.annotate('', xy=(9.3, 5.5), xytext=(8.7, 5.5),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Output profiles (right)
    output_box = mpatches.FancyBboxPatch((9.5, 1.5), 4, 7, boxstyle='round,pad=0.1',
                                          facecolor='#44A044', alpha=0.15,
                                          edgecolor='#44A044', lw=2)
    ax.add_patch(output_box)
    ax.text(11.5, 8, 'Portfolio Allocation', ha='center', fontsize=14, fontweight='bold', color='#44A044')

    profiles = [
        ('Conservative', '20% stocks / 80% bonds'),
        ('Moderate-Cons', '40% stocks / 60% bonds'),
        ('Moderate', '60% stocks / 40% bonds'),
        ('Moderate-Agg', '80% stocks / 20% bonds'),
        ('Aggressive', '90% stocks / 10% bonds'),
    ]
    for i, (profile, alloc) in enumerate(profiles):
        ax.text(9.8, 7.2-i*1, f'{profile}:', fontsize=11, fontweight='bold')
        ax.text(9.8, 6.7-i*1, alloc, fontsize=11)

    # Factors considered
    factors = """Factors in Risk Score:
    - Time horizon (longer = more risk capacity)
    - Financial cushion / emergency fund
    - Emotional response to volatility
    - Income needs from portfolio"""

    ax.text(2.5, 1.8, factors, fontsize=11, ha='center', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL PROCESS]', fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'risk_profiling_output.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
