"""
Banking Integration Patterns
System integration approaches

Output: banking_integration.pdf
Module: module_04_trad_finance
Lesson: 38 - Core Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Banking Integration',
    'module': 'module_04_trad_finance',
    'lesson': 38,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/banking_integration'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Integration Patterns
    ax1 = axes[0]

    patterns = ['Point-to-Point', 'ESB', 'API Gateway', 'Event-Driven', 'Microservices']
    complexity = [80, 50, 40, 35, 30]
    scalability = [20, 60, 75, 85, 90]
    maintenance = [85, 55, 45, 40, 35]

    x = np.arange(len(patterns))
    width = 0.25

    ax1.bar(x - width, complexity, width, label='Complexity', color='#D62728', alpha=0.8)
    ax1.bar(x, scalability, width, label='Scalability', color='#44A044', alpha=0.8)
    ax1.bar(x + width, maintenance, width, label='Maintenance Cost', color='#FF7F0E', alpha=0.8)

    ax1.set_xlabel('Integration Pattern', fontsize=11)
    ax1.set_ylabel('Score (0-100)', fontsize=11)
    ax1.set_title('Integration Patterns Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(patterns, rotation=20, ha='right', fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 100)
    ax1.yaxis.grid(True, alpha=0.3)

    # API Usage Trend
    ax2 = axes[1]

    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
    api_calls = [100, 180, 350, 550, 850, 1200, 1600]  # Index
    legacy_calls = [100, 95, 85, 75, 60, 45, 30]

    ax2.plot(years, api_calls, 'g-', linewidth=2.5, marker='o', label='API-Based Integration')
    ax2.plot(years, legacy_calls, 'r-', linewidth=2.5, marker='s', label='Legacy Integration')

    ax2.fill_between(years, api_calls, alpha=0.2, color='green')
    ax2.fill_between(years, legacy_calls, alpha=0.2, color='red')

    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Integration Volume (Index)', fontsize=11)
    ax2.set_title('Integration Method Adoption Trend', fontsize=12, fontweight='bold')
    ax2.legend(loc='center right', fontsize=9)
    ax2.grid(True, alpha=0.3)

    # Crossover annotation
    ax2.annotate('API overtakes\nlegacy', xy=(3, 550), xytext=(4, 800),
                fontsize=9, fontweight='bold', color='#44A044',
                arrowprops=dict(arrowstyle='->', color='#44A044'))

    fig.suptitle('Banking System Integration Approaches', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'banking_integration.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
