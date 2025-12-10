"""
Wealth Management Platform Architecture
Technology stack for wealth management

Output: wealth_platform_architecture.pdf
Module: module_04_trad_finance
Lesson: 46 - Wealth Management
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Wealth Platform Architecture',
    'module': 'module_04_trad_finance',
    'lesson': 46,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/wealth_platform_architecture'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Client layer
    ax.text(7, 8.5, 'Wealth Management Platform Architecture', ha='center',
            fontsize=14, fontweight='bold')

    # Client channels
    channels = [
        ('Mobile\nApp', 2, 7.5, '#4A90E2'),
        ('Web\nPortal', 5, 7.5, '#4A90E2'),
        ('Advisor\nWorkstation', 8, 7.5, '#4A90E2'),
        ('API\nPartners', 11, 7.5, '#4A90E2'),
    ]

    for name, x, y, color in channels:
        rect = mpatches.FancyBboxPatch((x-1, y-0.4), 2, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

    # Integration layer
    int_box = mpatches.FancyBboxPatch((1, 5.8), 12, 1,
                                       boxstyle="round,pad=0.02",
                                       facecolor='#44A044', alpha=0.3, edgecolor='#44A044', linewidth=2)
    ax.add_patch(int_box)
    ax.text(7, 6.3, 'API Gateway / Integration Layer', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#44A044')

    # Core services
    services = [
        ('Client\nOnboarding', 2, 4.8, '#FF7F0E'),
        ('Portfolio\nMgmt', 4.5, 4.8, '#FF7F0E'),
        ('Order\nExecution', 7, 4.8, '#FF7F0E'),
        ('Risk &\nCompliance', 9.5, 4.8, '#FF7F0E'),
        ('Reporting', 12, 4.8, '#FF7F0E'),
    ]

    for name, x, y, color in services:
        rect = mpatches.FancyBboxPatch((x-1, y-0.4), 2, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

    # Analytics layer
    analytics = [
        ('Goals\nPlanning', 2.5, 3.3, '#9B59B6'),
        ('Asset\nAllocation', 5, 3.3, '#9B59B6'),
        ('Performance\nAttribution', 7.5, 3.3, '#9B59B6'),
        ('Tax\nOptimization', 10, 3.3, '#9B59B6'),
        ('ML\nInsights', 12.5, 3.3, '#9B59B6'),
    ]

    for name, x, y, color in analytics:
        rect = mpatches.FancyBboxPatch((x-1, y-0.4), 2, 0.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor=color, alpha=0.8, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')

    # Data layer
    data_box = mpatches.FancyBboxPatch((1, 1.5), 12, 1,
                                        boxstyle="round,pad=0.02",
                                        facecolor='#D62728', alpha=0.3, edgecolor='#D62728', linewidth=2)
    ax.add_patch(data_box)
    ax.text(7, 2, 'Data Layer: Client Data | Holdings | Market Data | Reference Data',
            ha='center', va='center', fontsize=10, fontweight='bold', color='#D62728')

    # External connections
    externals = ['Custodians', 'Exchanges', 'Market\nData', 'Regulators']
    for i, ext in enumerate(externals):
        rect = mpatches.FancyBboxPatch((1.5 + i*3.2, 0.3), 2.5, 0.7,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#E8E8E8', edgecolor='#888888')
        ax.add_patch(rect)
        ax.text(2.75 + i*3.2, 0.65, ext, ha='center', va='center', fontsize=9)

    # Labels
    ax.text(0.3, 7.5, 'Channels', ha='left', va='center', fontsize=10,
            fontweight='bold', color='#4A90E2', rotation=90)
    ax.text(0.3, 4.8, 'Core', ha='left', va='center', fontsize=10,
            fontweight='bold', color='#FF7F0E', rotation=90)
    ax.text(0.3, 3.3, 'Analytics', ha='left', va='center', fontsize=10,
            fontweight='bold', color='#9B59B6', rotation=90)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'wealth_platform_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
