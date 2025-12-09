"""
Neobank Business Models Comparison
Compares different neobank approaches and value propositions

Output: neobank_business_models.pdf
Module: module_01_fintech
Lesson: 4 - Neobanks
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Neobank Business Models',
    'module': 'module_01_fintech',
    'lesson': 4,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/neobank_business_models'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create neobank business models comparison chart"""
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis('off')

    # Model categories
    models = [
        {
            'name': 'Full-Stack\nNeobank',
            'examples': 'N26, Monzo, Chime',
            'characteristics': ['Own banking license', 'Full deposit-taking',
                               'Credit products', 'Regulatory compliance'],
            'revenue': 'Interchange + Interest + Fees',
            'color': '#4A90E2',
            'x': 1.5
        },
        {
            'name': 'BaaS-Based\nNeobank',
            'examples': 'Current, Varo (early)',
            'characteristics': ['Partner bank license', 'Faster launch',
                               'Limited product control', 'Revenue share'],
            'revenue': 'Interchange + Subscription',
            'color': '#44A044',
            'x': 4.5
        },
        {
            'name': 'Vertical\nNeobank',
            'examples': 'Greenlight, Step',
            'characteristics': ['Specific segment focus', 'Tailored features',
                               'Niche marketing', 'Higher engagement'],
            'revenue': 'Subscription + Interchange',
            'color': '#FF7F0E',
            'x': 7.5
        },
        {
            'name': 'Super App\nModel',
            'examples': 'Revolut, Cash App',
            'characteristics': ['Multiple services', 'Ecosystem lock-in',
                               'Cross-selling', 'Data monetization'],
            'revenue': 'Diverse: Trading + FX + Crypto',
            'color': '#6B5B95',
            'x': 10.5
        }
    ]

    # Draw model boxes
    for model in models:
        # Main box
        rect = mpatches.FancyBboxPatch((model['x']-1.2, 2), 2.4, 5,
                                        boxstyle='round,pad=0.05',
                                        facecolor=model['color'],
                                        edgecolor='#333333', lw=1.5, alpha=0.9)
        ax.add_patch(rect)

        # Model name
        ax.text(model['x'], 6.5, model['name'], ha='center', va='center',
               fontsize=11, fontweight='bold', color='white')

        # Examples
        ax.text(model['x'], 5.7, model['examples'], ha='center', va='center',
               fontsize=8, style='italic', color='white')

        # Characteristics
        y_start = 5.0
        for i, char in enumerate(model['characteristics']):
            ax.text(model['x'], y_start - i*0.5, f'* {char}', ha='center', va='center',
                   fontsize=7, color='white')

        # Revenue box
        rev_rect = mpatches.FancyBboxPatch((model['x']-1.1, 2.1), 2.2, 0.8,
                                            boxstyle='round,pad=0.02',
                                            facecolor='white', edgecolor=model['color'], lw=1)
        ax.add_patch(rev_rect)
        ax.text(model['x'], 2.5, model['revenue'], ha='center', va='center',
               fontsize=7, fontweight='bold', color=model['color'])

    # Header
    ax.text(6, 8, 'Neobank Business Model Spectrum', fontsize=14, fontweight='bold', ha='center')
    ax.text(6, 7.5, 'From licensed banks to ecosystem platforms', fontsize=10,
           ha='center', style='italic', color='#666666')

    # Complexity arrow at bottom
    ax.annotate('', xy=(11, 1.3), xytext=(1, 1.3),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.text(6, 1.0, 'Increasing Product Complexity & Revenue Diversification',
           ha='center', fontsize=9, style='italic')

    # Regulation arrow at top
    ax.annotate('', xy=(1, 7.2), xytext=(11, 7.2),
               arrowprops=dict(arrowstyle='->', color='#D62728', lw=2))
    ax.text(6, 7.8, 'Regulatory Burden', ha='center', fontsize=9,
           color='#D62728', style='italic')

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)

    # Synthetic label
    ax.text(11.8, 0.2, '[ILLUSTRATIVE]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'neobank_business_models.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
