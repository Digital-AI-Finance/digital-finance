"""
Super App Models
Shows super app financial services models

Output: super_app_models.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Super App Models',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/super_app_models'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create super app models diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Super Apps: One App for Everything', fontsize=20, fontweight='bold', ha='center')

    # Super apps
    apps = [
        {
            'name': 'WeChat (China)',
            'x': 2.5, 'y': 6,
            'color': '#44A044',
            'users': '1.3B MAU',
            'services': ['Messaging', 'Payments', 'Shopping', 'Games', 'Banking', 'Govt services']
        },
        {
            'name': 'Grab (SEA)',
            'x': 7, 'y': 6,
            'color': '#4A90E2',
            'users': '35M MAU',
            'services': ['Ride-hail', 'Food delivery', 'Payments', 'Lending', 'Insurance', 'Investing']
        },
        {
            'name': 'Gojek (Indonesia)',
            'x': 11.5, 'y': 6,
            'color': '#FF7F0E',
            'users': '38M MAU',
            'services': ['Transport', 'Delivery', 'GoPay', 'GoInvest', 'Health', 'Entertainment']
        },
    ]

    for app in apps:
        box = mpatches.FancyBboxPatch((app['x']-2, app['y']-2.3), 4, 4.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=app['color'], alpha=0.2,
                                       edgecolor=app['color'], lw=2)
        ax.add_patch(box)
        ax.text(app['x'], app['y']+1.8, app['name'], ha='center',
               fontsize=14, fontweight='bold', color=app['color'])
        ax.text(app['x'], app['y']+1.2, app['users'], ha='center', fontsize=11, style='italic')

        for i, svc in enumerate(app['services']):
            row = i // 2
            col = i % 2
            x_offset = -0.8 if col == 0 else 0.8
            ax.text(app['x']+x_offset, app['y']+0.4-row*0.5, f'* {svc}',
                   ha='center', fontsize=9)

    # Western attempts
    western = """Western Super App Attempts:
    - PayPal expanding services
    - Revolut adding non-finance
    - X (Twitter) payment ambitions
    - Meta Pay integration

    Challenge: Regulatory barriers, privacy concerns, existing app ecosystem"""

    ax.text(7, 1.8, western, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: Company reports, app store data (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'super_app_models.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
