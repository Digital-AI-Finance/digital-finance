"""
FinTech Unicorns
Shows major FinTech unicorns by valuation

Output: fintech_unicorns.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'FinTech Unicorns',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/fintech_unicorns'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create FinTech unicorns chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    companies = ['Stripe', 'Revolut', 'Plaid', 'Chime', 'Checkout.com',
                'Brex', 'Rapyd', 'Figure', 'Ramp', 'Deel']
    valuations = [50, 33, 13.4, 25, 40, 12.3, 8.75, 6.5, 7.65, 12]  # USD B

    colors = ['#4A90E2', '#FF7F0E', '#44A044', '#6B5B95', '#D62728',
             '#17BECF', '#4A90E2', '#44A044', '#FF7F0E', '#6B5B95']

    bars = ax.barh(companies, valuations, color=colors, edgecolor='#333333', lw=1.5)

    ax.set_xlabel('Valuation (USD B)', fontsize=14)
    ax.set_title('Top FinTech Unicorns by Valuation (2024)', fontsize=20, fontweight='bold', pad=15)
    ax.set_xlim(0, 60)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels
    for bar, val in zip(bars, valuations):
        ax.annotate(f'USD {val}B',
                   xy=(bar.get_width(), bar.get_y() + bar.get_height()/2),
                   xytext=(5, 0), textcoords="offset points",
                   ha='left', va='center', fontsize=11, fontweight='bold')

    # Category annotations
    ax.text(55, 9, 'Payments', fontsize=10, ha='right', color='#4A90E2')
    ax.text(55, 8, 'Neobank', fontsize=10, ha='right', color='#FF7F0E')
    ax.text(55, 7, 'Infrastructure', fontsize=10, ha='right', color='#44A044')
    ax.text(55, 6, 'Banking', fontsize=10, ha='right', color='#6B5B95')

    # Total count
    ax.text(0.02, 0.02, 'Total FinTech Unicorns: 270+ globally\nCombined valuation: USD 1T+',
           transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: CB Insights Unicorn Tracker (Dec 2024) [Valuations may be from last funding round]',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'fintech_unicorns.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
