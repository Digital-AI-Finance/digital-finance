"""
Bloomberg Terminal Features
Functionality overview

Output: bloomberg_terminal.pdf
Module: module_04_trad_finance
Lesson: 47 - Data Vendors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Bloomberg Terminal',
    'module': 'module_04_trad_finance',
    'lesson': 47,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/bloomberg_terminal'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Terminal user segments
    ax1 = axes[0]

    segments = ['Asset\nManagers', 'Banks\n(Sales/Trading)', 'Hedge\nFunds', 'Corporates', 'Government\n& Central Banks', 'Other']
    users = [95, 85, 55, 40, 15, 30]  # Thousands of terminals
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#888888']

    bars = ax1.bar(segments, users, color=colors, alpha=0.8, edgecolor='black')

    ax1.set_ylabel('Terminals (000s)', fontsize=11)
    ax1.set_title('Bloomberg Terminal Users by Segment', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 120)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 2,
                f'{int(height)}K', ha='center', fontsize=10, fontweight='bold')

    # Total annotation
    ax1.text(2.5, 110, f'Total: ~320K terminals globally', fontsize=10, style='italic', color='#666666')

    # Feature categories
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')

    categories = [
        ('Market Data', 1.5, 8, ['Real-time quotes', 'Historical data', 'News feeds', 'Economic data'], '#4A90E2'),
        ('Analytics', 5, 8, ['Charting', 'Screening', 'Portfolio analytics', 'Risk models'], '#44A044'),
        ('Execution', 8.5, 8, ['EMSX trading', 'FX execution', 'Fixed income', 'Derivatives'], '#FF7F0E'),
        ('Communication', 1.5, 4, ['IB Chat', 'Email', 'Voice trading', 'Market commentary'], '#9B59B6'),
        ('Research', 5, 4, ['Company analysis', 'Industry reports', 'Credit ratings', 'ESG data'], '#D62728'),
        ('Reference', 8.5, 4, ['Security master', 'Corporate actions', 'Pricing', 'Identifiers'], '#E91E63'),
    ]

    for name, x, y, features, color in categories:
        rect = mpatches.FancyBboxPatch((x-1.3, y-1.5), 2.6, 3,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.2, edgecolor=color, linewidth=2)
        ax2.add_patch(rect)
        ax2.text(x, y + 1, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color=color)
        for i, feat in enumerate(features):
            ax2.text(x, y - 0.1 - i*0.4, f'• {feat}', ha='center', va='center',
                    fontsize=8, color='#333333')

    ax2.text(5, 9.5, 'Bloomberg Terminal Feature Categories', ha='center',
            fontsize=12, fontweight='bold')

    # Pricing note
    ax2.text(5, 0.5, 'Pricing: ~$24,000/year per terminal', ha='center',
            fontsize=10, style='italic', color='#666666')

    fig.suptitle('Bloomberg Terminal Overview', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'bloomberg_terminal.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
