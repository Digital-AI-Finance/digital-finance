"""
UK Open Banking Implementation
Shows the UK's CMA-led open banking implementation

Output: uk_open_banking.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'UK Open Banking Implementation',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/uk_open_banking'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create UK open banking implementation chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Adoption growth
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    # Based on OBIE statistics
    users_millions = [0.3, 1.0, 2.5, 4.5, 6.0, 7.0, 7.5]
    api_calls_millions = [67, 1000, 5800, 9500, 24000, 36000, 45000]

    ax1.plot(years, users_millions, 'o-', color='#4A90E2', lw=2, markersize=8, label='Active users (M)')
    ax1.fill_between(years, users_millions, alpha=0.2, color='#4A90E2')

    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('Active Users (Millions)', fontsize=10, color='#4A90E2')
    ax1.tick_params(axis='y', labelcolor='#4A90E2')
    ax1.set_ylim(0, 10)

    # Second y-axis for API calls
    ax1_twin = ax1.twinx()
    ax1_twin.bar([y + 0.3 for y in years], [a/1000 for a in api_calls_millions],
                 width=0.5, alpha=0.5, color='#44A044', label='API calls (B)')
    ax1_twin.set_ylabel('API Calls (Billions monthly)', fontsize=10, color='#44A044')
    ax1_twin.tick_params(axis='y', labelcolor='#44A044')
    ax1_twin.set_ylim(0, 50)

    ax1.set_title('UK Open Banking Growth', fontsize=12, fontweight='bold', pad=10)
    ax1.grid(True, alpha=0.3)

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax1_twin.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)

    # Right: UK structure
    ax2.axis('off')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)

    # CMA Order box
    cma_box = mpatches.FancyBboxPatch((2.5, 7.5), 5, 1.5, boxstyle='round,pad=0.1',
                                       facecolor='#D62728', edgecolor='#333333', lw=2)
    ax2.add_patch(cma_box)
    ax2.text(5, 8.25, 'CMA Order 2017', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax2.text(5, 7.8, 'Competition remedy', ha='center', fontsize=8, color='white')

    # OBIE box
    obie_box = mpatches.FancyBboxPatch((2.5, 5.2), 5, 1.8, boxstyle='round,pad=0.1',
                                        facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax2.add_patch(obie_box)
    ax2.text(5, 6.3, 'OBIE', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax2.text(5, 5.7, 'Open Banking Implementation Entity\n(Industry body, standards setter)',
            ha='center', fontsize=8, color='white')

    # CMA9 banks
    cma9_box = mpatches.FancyBboxPatch((0.5, 2.5), 4, 2.2, boxstyle='round,pad=0.1',
                                        facecolor='#333333', edgecolor='#333333', lw=2)
    ax2.add_patch(cma9_box)
    ax2.text(2.5, 4.2, 'CMA9 Banks', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax2.text(2.5, 3.5, 'Barclays, HSBC, Lloyds,\nNatWest, Santander,\nNationwide, AIB, BoI, Danske',
            ha='center', fontsize=7, color='white')

    # TPPs
    tpp_box = mpatches.FancyBboxPatch((5.5, 2.5), 4, 2.2, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', edgecolor='#333333', lw=2)
    ax2.add_patch(tpp_box)
    ax2.text(7.5, 4.2, '300+ TPPs', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax2.text(7.5, 3.5, 'Plaid, TrueLayer, Tink,\nYolt, Experian,\nGoCardless, etc.',
            ha='center', fontsize=7, color='white')

    # Arrows
    ax2.annotate('', xy=(5, 7.5), xytext=(5, 7),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax2.annotate('', xy=(2.5, 5.2), xytext=(2.5, 4.7),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax2.annotate('', xy=(7.5, 5.2), xytext=(7.5, 4.7),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    ax2.set_title('UK Open Banking Structure', fontsize=12, fontweight='bold', pad=10)

    # Key facts
    ax2.text(5, 1.5, 'UK differentiators: CMA mandate, standardized APIs, directory of providers',
            ha='center', fontsize=8, style='italic', color='#666666')

    # Main title
    fig.suptitle('UK Open Banking: World-Leading Implementation',
                fontsize=14, fontweight='bold', y=1.02)

    # Source
    fig.text(0.5, 0.02, 'Source: Open Banking Implementation Entity (OBIE) statistics, 2024',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'uk_open_banking.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
