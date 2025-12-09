"""
Insurance Distribution Channels
Shows evolution of insurance distribution

Output: distribution_channels.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Insurance Distribution Channels',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/distribution_channels'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create distribution channels comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    channels = ['Captive\nAgents', 'Independent\nAgents', 'Direct\n(Phone/Mail)', 'Digital\nDirect', 'Embedded']
    share_2015 = [35, 30, 20, 10, 5]
    share_2024 = [25, 28, 15, 20, 12]
    share_2030 = [15, 20, 10, 25, 30]

    x = np.arange(len(channels))
    width = 0.25

    bars1 = ax.bar(x - width, share_2015, width, label='2015', color='#4A90E2',
                   edgecolor='#333333', lw=1.5)
    bars2 = ax.bar(x, share_2024, width, label='2024', color='#44A044',
                   edgecolor='#333333', lw=1.5)
    bars3 = ax.bar(x + width, share_2030, width, label='2030E', color='#FF7F0E',
                   edgecolor='#333333', lw=1.5)

    ax.set_ylabel('Market Share (%)', fontsize=14)
    ax.set_title('Insurance Distribution Channel Evolution', fontsize=20, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(channels, fontsize=12)
    ax.legend(fontsize=12)
    ax.set_ylim(0, 45)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}%',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3), textcoords="offset points",
                       ha='center', va='bottom', fontsize=10)

    # Key insight
    ax.text(0.98, 0.98, 'Digital + Embedded:\n47% by 2030\n(from 15% in 2015)',
           transform=ax.transAxes, fontsize=12, va='top', ha='right',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: McKinsey Insurance Distribution (2024) [PROJECTIONS]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'distribution_channels.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
