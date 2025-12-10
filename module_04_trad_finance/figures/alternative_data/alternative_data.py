"""
Alternative Data Sources
Non-traditional data for finance

Output: alternative_data.pdf
Module: module_04_trad_finance
Lesson: 47 - Data Vendors
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Alternative Data',
    'module': 'module_04_trad_finance',
    'lesson': 47,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/alternative_data'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Alt data market growth
    ax1 = axes[0]

    years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025E']
    market_size = [1.1, 1.5, 2.2, 3.2, 4.5, 6.2, 8.5]

    ax1.fill_between(years, market_size, alpha=0.3, color='#4A90E2')
    ax1.plot(years, market_size, 'o-', color='#4A90E2', linewidth=2, markersize=8)

    ax1.set_ylabel('Market Size ($B)', fontsize=11)
    ax1.set_title('Alternative Data Market Growth', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 10)
    ax1.yaxis.grid(True, alpha=0.3)

    # Add CAGR
    ax1.annotate('CAGR: 42%', xy=(4, 4.5), xytext=(2, 7),
                fontsize=11, fontweight='bold', color='#4A90E2',
                arrowprops=dict(arrowstyle='->', color='#4A90E2'))

    # Data source breakdown
    ax2 = axes[1]

    sources = ['Web/\nSocial Media', 'Satellite/\nGeolocation', 'Transaction\nData', 'Sentiment/\nNews', 'IoT/\nSensors', 'Other']
    adoption = [65, 45, 55, 70, 25, 35]
    alpha_potential = [60, 75, 80, 55, 85, 50]  # Perceived alpha generation
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#888888']

    x = np.arange(len(sources))
    width = 0.35

    bars1 = ax2.bar(x - width/2, adoption, width, label='Adoption Rate',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax2.bar(x + width/2, alpha_potential, width, label='Alpha Potential',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Score (%)', fontsize=11)
    ax2.set_title('Alternative Data Sources', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(sources, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 100)
    ax2.yaxis.grid(True, alpha=0.3)

    # Highlight opportunity areas
    for i, (a, p) in enumerate(zip(adoption, alpha_potential)):
        if p > a + 15:  # Underutilized with high potential
            ax2.annotate('', xy=(i - width/2, a), xytext=(i + width/2, p),
                        arrowprops=dict(arrowstyle='<-', color='#D62728', lw=1.5))

    ax2.text(3.5, 92, 'Gap = Opportunity', fontsize=9, color='#D62728', style='italic')

    fig.suptitle('Alternative Data in Finance', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'alternative_data.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
