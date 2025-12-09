"""
Mobile Wallet Regulatory Landscape Map
Shows regulatory approaches across major markets

Output: wallet_regulatory_map.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Mobile Wallet Regulatory Landscape',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/wallet_regulatory_map'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create mobile wallet regulatory landscape chart"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Data: Region, Strictness (1-5), Openness (1-5), License Type
    regions = [
        ('US', 3.5, 3.5, 'State MTL'),
        ('EU', 4, 4, 'PSD2/EMI'),
        ('UK', 3.8, 4.2, 'FCA E-Money'),
        ('China', 4.5, 2.5, 'PBOC License'),
        ('India', 3, 4, 'RBI PPI'),
        ('Singapore', 3.5, 4.5, 'MAS PS Act'),
        ('Brazil', 3, 4, 'BCB PIX'),
        ('Kenya', 2.5, 4, 'CBK Mobile'),
        ('Australia', 3.5, 4, 'ASIC/APRA'),
        ('Japan', 4, 3.5, 'FSA License'),
    ]

    # Plot
    colors = {'Strict': '#D62728', 'Moderate': '#FF7F0E', 'Permissive': '#44A044'}

    for region, strict, openness, license_type in regions:
        if strict > 4:
            c = colors['Strict']
        elif strict > 3:
            c = colors['Moderate']
        else:
            c = colors['Permissive']

        ax.scatter(strict, openness, s=200, c=c, edgecolor='#333333', lw=1.5, zorder=3)
        ax.annotate(region, (strict, openness), xytext=(5, 5), textcoords='offset points',
                   fontsize=9, fontweight='bold')

    # Quadrant labels
    ax.axhline(y=3.5, color='#CCCCCC', linestyle='--', lw=1, zorder=1)
    ax.axvline(x=3.5, color='#CCCCCC', linestyle='--', lw=1, zorder=1)

    ax.text(2.2, 4.8, 'Permissive &\nInnovation-friendly', fontsize=9, ha='center',
           color='#44A044', fontweight='bold')
    ax.text(4.8, 4.8, 'Strict but\nOpen', fontsize=9, ha='center',
           color='#FF7F0E', fontweight='bold')
    ax.text(2.2, 2.2, 'Limited\nFramework', fontsize=9, ha='center',
           color='#999999', fontweight='bold')
    ax.text(4.8, 2.2, 'Restrictive', fontsize=9, ha='center',
           color='#D62728', fontweight='bold')

    ax.set_xlabel('Regulatory Strictness (1=Permissive, 5=Strict)', fontsize=11)
    ax.set_ylabel('Market Openness (1=Closed, 5=Open)', fontsize=11)
    ax.set_xlim(1.5, 5.5)
    ax.set_ylim(1.5, 5.5)

    ax.set_title('Mobile Wallet Regulatory Landscape by Region',
                fontsize=14, fontweight='bold', pad=15)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=colors['Strict'], edgecolor='#333333', label='Strict (>4)'),
        mpatches.Patch(facecolor=colors['Moderate'], edgecolor='#333333', label='Moderate (3-4)'),
        mpatches.Patch(facecolor=colors['Permissive'], edgecolor='#333333', label='Permissive (<3)'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=9)

    # Grid
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Synthetic label
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'wallet_regulatory_map.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
