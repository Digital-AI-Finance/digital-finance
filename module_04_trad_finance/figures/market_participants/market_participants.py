"""
Market Participants
Key players in financial markets

Output: market_participants.pdf
Module: module_04_trad_finance
Lesson: 37 - Financial Markets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Market Participants',
    'module': 'module_04_trad_finance',
    'lesson': 37,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/market_participants'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Participant types and market share
    ax1 = axes[0]

    participants = ['Institutional\nInvestors', 'Retail\nInvestors', 'Market\nMakers',
                   'Hedge\nFunds', 'Banks', 'Corporations']
    volume_share = [45, 15, 18, 12, 7, 3]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#888888']

    wedges, texts, autotexts = ax1.pie(volume_share, labels=participants, autopct='%1.0f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.05, 0, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax1.set_title('Trading Volume by Participant Type', fontsize=12, fontweight='bold')

    # Participant characteristics
    ax2 = axes[1]

    characteristics = ['Trade\nFrequency', 'Position\nSize', 'Time\nHorizon',
                      'Information\nAdvantage', 'Market\nImpact']
    institutional = [70, 90, 80, 75, 85]
    retail = [40, 20, 50, 25, 15]
    hft = [100, 30, 10, 60, 40]

    x = np.arange(len(characteristics))
    width = 0.25

    ax2.bar(x - width, institutional, width, label='Institutional', color='#4A90E2', alpha=0.8)
    ax2.bar(x, retail, width, label='Retail', color='#44A044', alpha=0.8)
    ax2.bar(x + width, hft, width, label='HFT/Market Makers', color='#FF7F0E', alpha=0.8)

    ax2.set_xlabel('Characteristic', fontsize=11)
    ax2.set_ylabel('Relative Score', fontsize=11)
    ax2.set_title('Participant Characteristics Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(characteristics, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('Financial Market Participants', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'market_participants.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
