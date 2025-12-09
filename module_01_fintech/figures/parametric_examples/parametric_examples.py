"""
Parametric Insurance Examples
Shows real-world parametric insurance products

Output: parametric_examples.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Parametric Insurance Examples',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/parametric_examples'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create parametric examples diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Parametric Insurance: Real-World Examples', fontsize=20, fontweight='bold', ha='center')

    # Examples
    examples = [
        {
            'name': 'Caribbean Hurricane',
            'x': 2.5, 'y': 6.5,
            'color': '#4A90E2',
            'trigger': 'Cat 4+ hurricane',
            'payout': '$50-200M',
            'provider': 'CCRIF (Caribbean)'
        },
        {
            'name': 'Crop Weather',
            'x': 7, 'y': 6.5,
            'color': '#44A044',
            'trigger': 'Rainfall < threshold',
            'payout': 'Per-acre coverage',
            'provider': 'ACRE Africa'
        },
        {
            'name': 'Earthquake',
            'x': 11.5, 'y': 6.5,
            'color': '#D62728',
            'trigger': 'Magnitude > 6.0',
            'payout': 'Tiered by severity',
            'provider': 'Global Parametrics'
        },
        {
            'name': 'Flight Delay',
            'x': 2.5, 'y': 2.5,
            'color': '#FF7F0E',
            'trigger': 'Delay > 2 hours',
            'payout': '$50-500 instant',
            'provider': 'Revolut, Blink'
        },
        {
            'name': 'Solar Radiation',
            'x': 7, 'y': 2.5,
            'color': '#6B5B95',
            'trigger': 'Solar output drop',
            'payout': 'Revenue protection',
            'provider': 'kWh Analytics'
        },
        {
            'name': 'Pandemic',
            'x': 11.5, 'y': 2.5,
            'color': '#333333',
            'trigger': 'WHO declaration',
            'payout': 'Business interruption',
            'provider': 'World Bank PEF'
        },
    ]

    for ex in examples:
        # Box
        box = mpatches.FancyBboxPatch((ex['x']-1.8, ex['y']-1.4), 3.6, 2.9,
                                       boxstyle='round,pad=0.1',
                                       facecolor=ex['color'], alpha=0.15,
                                       edgecolor=ex['color'], lw=2)
        ax.add_patch(box)
        ax.text(ex['x'], ex['y']+1.1, ex['name'], ha='center',
               fontsize=13, fontweight='bold', color=ex['color'])
        ax.text(ex['x'], ex['y']+0.4, f"Trigger: {ex['trigger']}", ha='center', fontsize=11)
        ax.text(ex['x'], ex['y']-0.2, f"Payout: {ex['payout']}", ha='center', fontsize=11)
        ax.text(ex['x'], ex['y']-0.8, ex['provider'], ha='center', fontsize=10, style='italic')

    # Market size
    market = "Parametric Market: $15B+ (2024) | Growth: 15% CAGR | Climate risk driving adoption"
    ax.text(7, 0.8, market, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Swiss Re, Munich Re, Aon parametric reports (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'parametric_examples.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
