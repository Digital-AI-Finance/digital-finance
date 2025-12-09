"""
RegTech Categories
Shows detailed RegTech solution categories

Output: regtech_categories.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Categories',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regtech_categories'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create RegTech categories diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'RegTech Solution Categories', fontsize=20, fontweight='bold', ha='center')

    # Central hub
    hub = plt.Circle((7, 5), 1.2, facecolor='#4A90E2', alpha=0.3,
                     edgecolor='#4A90E2', lw=3)
    ax.add_patch(hub)
    ax.text(7, 5, 'RegTech\nSolutions', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#4A90E2')

    # Categories around the hub
    categories = [
        {'name': 'Know Your\nCustomer (KYC)', 'angle': 60, 'color': '#44A044',
         'tech': 'AI, biometrics, data aggregation'},
        {'name': 'Anti-Money\nLaundering (AML)', 'angle': 120, 'color': '#FF7F0E',
         'tech': 'ML pattern detection, network analysis'},
        {'name': 'Regulatory\nReporting', 'angle': 180, 'color': '#6B5B95',
         'tech': 'NLP, automated data extraction'},
        {'name': 'Risk Data\nAggregation', 'angle': 240, 'color': '#D62728',
         'tech': 'Big data, real-time processing'},
        {'name': 'Transaction\nMonitoring', 'angle': 300, 'color': '#17BECF',
         'tech': 'Real-time ML, anomaly detection'},
        {'name': 'Compliance\nTracking', 'angle': 0, 'color': '#333333',
         'tech': 'NLP for regulatory change mgmt'},
    ]

    radius = 3.5
    for cat in categories:
        angle_rad = np.radians(cat['angle'])
        x = 7 + radius * np.cos(angle_rad)
        y = 5 + radius * np.sin(angle_rad)

        # Box
        box = mpatches.FancyBboxPatch((x-1.5, y-0.9), 3, 1.8,
                                       boxstyle='round,pad=0.1',
                                       facecolor=cat['color'], alpha=0.15,
                                       edgecolor=cat['color'], lw=2)
        ax.add_patch(box)
        ax.text(x, y+0.4, cat['name'], ha='center', fontsize=11, fontweight='bold', color=cat['color'])
        ax.text(x, y-0.3, cat['tech'], ha='center', fontsize=9, style='italic')

        # Line to center
        line_x = 7 + 1.3 * np.cos(angle_rad)
        line_y = 5 + 1.3 * np.sin(angle_rad)
        ax.plot([line_x, x - 1.3*np.cos(angle_rad)], [line_y, y - 0.8*np.sin(angle_rad)],
               color='#CCCCCC', lw=1.5, ls='--')

    # Source
    fig.text(0.5, 0.02, 'Source: Deloitte RegTech Universe (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'regtech_categories.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
