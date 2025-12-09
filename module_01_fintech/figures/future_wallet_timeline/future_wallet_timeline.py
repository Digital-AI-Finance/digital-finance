"""
Future of Mobile Wallets Timeline
Shows evolution and future trends in mobile wallet technology

Output: future_wallet_timeline.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Mobile Wallet Evolution Timeline',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/future_wallet_timeline'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create mobile wallet evolution timeline"""
    fig, ax = plt.subplots(figsize=(13, 6))
    ax.set_xlim(2010, 2032)
    ax.set_ylim(0, 10)

    # Timeline base
    ax.axhline(y=5, color='#333333', lw=3, zorder=1)

    # Past milestones (above line)
    past_milestones = [
        (2011, 'Google Wallet\nlaunches', 6.5),
        (2014, 'Apple Pay\nlaunches', 7.5),
        (2016, 'WeChat Pay\n1B users', 6.5),
        (2017, 'India UPI\nlaunches', 7.5),
        (2020, 'Contactless\nsurges (COVID)', 6.5),
        (2022, 'Tap to Pay\non iPhone', 7.5),
    ]

    # Future milestones (below line)
    future_milestones = [
        (2024, 'CBDC wallet\npilots expand', 3.5),
        (2025, 'Biometric-only\nauthentication', 2.5),
        (2026, 'Cross-border\ninteroperability', 3.5),
        (2028, 'AI-powered\nfinancial advice', 2.5),
        (2030, 'Universal digital\nidentity wallets', 3.5),
    ]

    # Plot past milestones
    for year, label, y_pos in past_milestones:
        ax.plot(year, 5, 'o', color='#4A90E2', markersize=12, zorder=2)
        ax.plot([year, year], [5, y_pos - 0.3], 'k-', lw=1, zorder=1)
        ax.text(year, y_pos, label, ha='center', va='bottom', fontsize=8,
               fontweight='bold')

    # Plot future milestones
    for year, label, y_pos in future_milestones:
        ax.plot(year, 5, 'o', color='#44A044', markersize=12, zorder=2)
        ax.plot([year, year], [5, y_pos + 0.3], 'k-', lw=1, zorder=1)
        ax.text(year, y_pos, label, ha='center', va='top', fontsize=8,
               fontweight='bold')

    # Divider for past/future
    ax.axvline(x=2024, color='#D62728', linestyle='--', lw=2, alpha=0.5)
    ax.text(2023.8, 9, 'Today', fontsize=10, fontweight='bold', color='#D62728',
           ha='right', rotation=90, va='top')

    # Era labels
    ax.text(2014, 9.2, 'ADOPTION ERA', fontsize=11, fontweight='bold',
           color='#4A90E2', ha='center')
    ax.text(2027, 9.2, 'TRANSFORMATION ERA', fontsize=11, fontweight='bold',
           color='#44A044', ha='center')

    # Key trends box
    trends = """Key Future Trends:
    • Convergence with digital identity
    • CBDC integration
    • Cross-border interoperability
    • AI-driven personalization
    • Embedded finance everywhere"""

    ax.text(2031, 8, trends, fontsize=8, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Title
    ax.set_title('Mobile Wallet Evolution: Past to Future',
                fontsize=14, fontweight='bold', pad=15)

    # Clean up axes
    ax.set_xlabel('Year', fontsize=11)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#4A90E2',
                   markersize=10, label='Past milestones'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#44A044',
                   markersize=10, label='Future projections'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=9)

    # Synthetic label
    fig.text(0.98, 0.02, '[PROJECTIONS]', fontsize=7, color='#999999',
            ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'future_wallet_timeline.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
