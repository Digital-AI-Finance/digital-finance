"""
AI Advisor Future
Shows the future evolution of AI-powered advisory

Output: ai_advisor_future.pdf
Module: module_01_fintech
Lesson: 8 - Robo-Advisors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'AI Advisor Future',
    'module': 'module_01_fintech',
    'lesson': 8,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ai_advisor_future'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create AI advisor future diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Future of AI-Powered Advisory', fontsize=20, fontweight='bold', ha='center')

    # Timeline evolution
    phases = [
        {
            'name': 'Current\n(2024)',
            'x': 2, 'y': 6,
            'color': '#4A90E2',
            'features': ['Rule-based portfolios', 'Basic risk questionnaires', 'Automated rebalancing'],
        },
        {
            'name': 'Near-term\n(2025-2027)',
            'x': 7, 'y': 6,
            'color': '#FF7F0E',
            'features': ['LLM chat advisors', 'Behavioral nudges', 'Hyper-personalization'],
        },
        {
            'name': 'Future\n(2028+)',
            'x': 12, 'y': 6,
            'color': '#44A044',
            'features': ['Autonomous AI agents', 'Holistic life planning', 'Real-time adaptation'],
        },
    ]

    for phase in phases:
        # Box
        box = mpatches.FancyBboxPatch((phase['x']-1.6, phase['y']-2), 3.2, 4,
                                       boxstyle='round,pad=0.1',
                                       facecolor=phase['color'], alpha=0.2,
                                       edgecolor=phase['color'], lw=2)
        ax.add_patch(box)
        ax.text(phase['x'], phase['y']+1.5, phase['name'], ha='center',
               fontsize=13, fontweight='bold', color=phase['color'])

        for i, feature in enumerate(phase['features']):
            ax.text(phase['x'], phase['y']+0.5-i*0.6, f'* {feature}', ha='center', fontsize=11)

    # Arrow connecting phases
    ax.annotate('', xy=(4.5, 6), xytext=(3.7, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.annotate('', xy=(9.5, 6), xytext=(8.7, 6),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Key technologies
    tech = """Enabling Technologies:
    - Large Language Models (GPT, Claude)
    - Real-time data integration (open banking)
    - Advanced ML for risk/return modeling
    - Voice/multimodal interfaces"""

    ax.text(7, 2.3, tech, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[FORWARD-LOOKING ANALYSIS]',
            fontsize=10, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ai_advisor_future.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
