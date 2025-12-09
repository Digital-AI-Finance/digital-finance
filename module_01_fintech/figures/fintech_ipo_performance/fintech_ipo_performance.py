"""
FinTech IPO Performance
Shows FinTech IPO performance over time

Output: fintech_ipo_performance.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'FinTech IPO Performance',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_ipo_performance'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech IPO performance chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    companies = ['Nubank', 'Robinhood', 'Coinbase', 'Affirm', 'SoFi',
                'Lemonade', 'Marqeta', 'Toast']
    ipo_price = [100, 100, 100, 100, 100, 100, 100, 100]  # Normalized to 100
    current_vs_ipo = [45, 58, 175, 42, 95, 30, 35, 85]  # % of IPO price (illustrative)

    colors = ['#44A044' if c >= 100 else '#D62728' for c in current_vs_ipo]

    x = np.arange(len(companies))
    width = 0.35

    bars1 = ax.bar(x - width/2, ipo_price, width, label='IPO Price (=100)',
                   color='#4A90E2', edgecolor='#333333', lw=1.5)
    bars2 = ax.bar(x + width/2, current_vs_ipo, width, label='Current vs IPO (%)',
                   color=colors, edgecolor='#333333', lw=1.5)

    ax.set_ylabel('Indexed Price (IPO = 100)', fontsize=14)
    ax.set_title('FinTech IPO Performance vs IPO Price', fontsize=20, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(companies, fontsize=11, rotation=20, ha='right')
    ax.legend(fontsize=11)
    ax.set_ylim(0, 200)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add 100 line
    ax.axhline(y=100, color='#333333', linestyle='--', lw=1, alpha=0.5)

    # Key insight
    ax.text(0.98, 0.95, '6 of 8 below IPO price\n(as of late 2024)',
           transform=ax.transAxes, fontsize=12, fontweight='bold',
           ha='right', va='top', color='#D62728',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#D62728'))

    # Source
    fig.text(0.5, 0.02, 'Source: Yahoo Finance, company stock data (Dec 2024) [ILLUSTRATIVE]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'fintech_ipo_performance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
