"""
Investment App Comparison
Compares major retail investment apps

Output: investment_app_comparison.pdf
Module: module_01_fintech
Lesson: 11 - WealthTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Investment App Comparison',
    'module': 'module_01_fintech',
    'lesson': 11,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/investment_app_comparison'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create investment app comparison diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Retail Investment App Comparison', fontsize=20, fontweight='bold', ha='center')

    # Apps
    apps = [
        {
            'name': 'Robinhood',
            'x': 2.5, 'y': 6,
            'color': '#44A044',
            'users': '23M+',
            'min': 'USD 0',
            'features': 'Stocks, options, crypto',
            'revenue': 'PFOF, margin, Gold'
        },
        {
            'name': 'eToro',
            'x': 7, 'y': 6,
            'color': '#4A90E2',
            'users': '30M+',
            'min': 'USD 10',
            'features': 'Copy trading, stocks, crypto',
            'revenue': 'Spreads, fees'
        },
        {
            'name': 'Acorns',
            'x': 11.5, 'y': 6,
            'color': '#FF7F0E',
            'users': '10M+',
            'min': 'Round-ups',
            'features': 'Auto-invest, banking',
            'revenue': 'USD 3-5/mo subscription'
        },
        {
            'name': 'Public',
            'x': 2.5, 'y': 2.5,
            'color': '#6B5B95',
            'users': '3M+',
            'min': 'USD 1',
            'features': 'Social, fractional, no PFOF',
            'revenue': 'Tipping, Alpha subscription'
        },
        {
            'name': 'Webull',
            'x': 7, 'y': 2.5,
            'color': '#D62728',
            'users': '15M+',
            'min': 'USD 0',
            'features': 'Advanced charts, options',
            'revenue': 'PFOF, margin'
        },
        {
            'name': 'Stash',
            'x': 11.5, 'y': 2.5,
            'color': '#333333',
            'users': '6M+',
            'min': 'USD 5',
            'features': 'Fractional, education',
            'revenue': 'Subscription'
        },
    ]

    for app in apps:
        box = mpatches.FancyBboxPatch((app['x']-1.8, app['y']-1.5), 3.6, 3.1,
                                       boxstyle='round,pad=0.1',
                                       facecolor=app['color'], alpha=0.15,
                                       edgecolor=app['color'], lw=2)
        ax.add_patch(box)
        ax.text(app['x'], app['y']+1.2, app['name'], ha='center',
               fontsize=14, fontweight='bold', color=app['color'])
        ax.text(app['x'], app['y']+0.6, f"Users: {app['users']}", ha='center', fontsize=11)
        ax.text(app['x'], app['y']+0.1, f"Min: {app['min']}", ha='center', fontsize=10)
        ax.text(app['x'], app['y']-0.4, app['features'], ha='center', fontsize=10)
        ax.text(app['x'], app['y']-0.9, app['revenue'], ha='center', fontsize=9, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Company filings, app store data (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'investment_app_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
