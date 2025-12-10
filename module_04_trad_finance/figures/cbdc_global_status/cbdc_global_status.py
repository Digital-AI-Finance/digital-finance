"""
Global CBDC Development Status
Country-by-country progress

Output: cbdc_global_status.pdf
Module: module_04_trad_finance
Lesson: 48 - CBDC
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'CBDC Global Status',
    'module': 'module_04_trad_finance',
    'lesson': 48,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/cbdc_global_status'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Development stage by count
    ax1 = axes[0]

    stages = ['Launched', 'Pilot', 'Development', 'Research', 'No Activity']
    counts = [4, 36, 68, 46, 40]  # Approximate numbers
    colors = ['#44A044', '#4A90E2', '#FF7F0E', '#FFD700', '#D3D3D3']

    wedges, texts, autotexts = ax1.pie(counts, labels=stages, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0.02, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    for text in texts:
        text.set_fontsize(9)

    ax1.set_title('CBDC Projects by Stage (194 countries)', fontsize=12, fontweight='bold')

    # Add center
    centre_circle = plt.Circle((0, 0), 0.35, fc='white')
    ax1.add_patch(centre_circle)
    ax1.text(0, 0, '134\nActive', ha='center', va='center', fontsize=10, fontweight='bold')

    # Major projects timeline/status
    ax2 = axes[1]

    projects = ['e-CNY\n(China)', 'Digital\nRuble', 'e-Euro\n(ECB)', 'Digital\nPound', 'Digital\nReal', 'FedNow*']
    stages = [4, 3, 2, 2, 3, 1]  # 1=Research, 2=Dev, 3=Pilot, 4=Launched
    populations = [1400, 145, 340, 67, 215, 335]  # Millions

    x = np.arange(len(projects))
    colors = ['#44A044' if s == 4 else '#4A90E2' if s == 3 else '#FF7F0E' if s == 2 else '#FFD700' for s in stages]

    bars = ax2.bar(x, stages, color=colors, alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Development Stage', fontsize=11)
    ax2.set_title('Major CBDC Projects Status', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(projects, fontsize=9)
    ax2.set_ylim(0, 5)
    ax2.set_yticks([1, 2, 3, 4])
    ax2.set_yticklabels(['Research', 'Development', 'Pilot', 'Launched'], fontsize=9)
    ax2.yaxis.grid(True, alpha=0.3)

    # Add population labels
    for bar, pop in zip(bars, populations):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 0.15,
                f'{pop}M pop', ha='center', fontsize=8, color='#666666')

    ax2.text(5, 1.3, '*Payment system,\nnot CBDC', fontsize=8, style='italic', color='#888888')

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#44A044', label='Launched'),
        Patch(facecolor='#4A90E2', label='Pilot'),
        Patch(facecolor='#FF7F0E', label='Development'),
        Patch(facecolor='#FFD700', label='Research')
    ]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=8)

    fig.suptitle('Global CBDC Development (2024)', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'cbdc_global_status.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
