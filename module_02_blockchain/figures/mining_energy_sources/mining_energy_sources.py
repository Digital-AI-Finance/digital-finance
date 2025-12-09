"""
Mining Energy Sources
Shows the breakdown of energy sources used in Bitcoin mining

Output: mining_energy_sources.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Mining Energy Sources',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/mining_energy_sources'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create mining energy sources chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Energy mix pie chart
    sources = ['Hydro', 'Natural Gas', 'Coal', 'Nuclear', 'Wind', 'Solar', 'Other']
    percentages = [23, 22, 21, 12, 9, 8, 5]
    colors = ['#3498DB', '#F39C12', '#7F8C8D', '#9B59B6', '#1ABC9C', '#F1C40F', '#95A5A6']

    wedges, texts, autotexts = ax1.pie(percentages, labels=sources, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0, 0])
    ax1.set_title('Bitcoin Mining Energy Mix (2024)', fontsize=16, fontweight='bold')

    for text in texts:
        text.set_fontsize(11)
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')

    # Sustainable vs non-sustainable
    sustainable = 23 + 12 + 9 + 8  # Hydro + Nuclear + Wind + Solar = 52%
    non_sustainable = 22 + 21 + 5  # Gas + Coal + Other = 48%

    bars = ax2.bar(['Sustainable\nEnergy', 'Non-Sustainable\nEnergy'],
                   [sustainable, non_sustainable],
                   color=['#27AE60', '#E74C3C'], alpha=0.8, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Percentage of Mining (%)', fontsize=14)
    ax2.set_title('Sustainability Breakdown', fontsize=16, fontweight='bold')
    ax2.set_ylim(0, 70)

    # Add value labels
    for bar, val in zip(bars, [sustainable, non_sustainable]):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{val}%', ha='center', fontsize=16, fontweight='bold')

    # Add trend annotation
    ax2.annotate('52% sustainable\n(up from 39% in 2020)',
                xy=(0, sustainable), xytext=(0.3, 55),
                fontsize=11, ha='center',
                arrowprops=dict(arrowstyle='->', color='#27AE60'),
                bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    ax2.grid(axis='y', alpha=0.3)

    # Add note about methodology
    fig.text(0.5, 0.02, 'Source: Bitcoin Mining Council Q4 2024 Survey, Cambridge Bitcoin Electricity Consumption Index [ILLUSTRATIVE DATA]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mining_energy_sources.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
