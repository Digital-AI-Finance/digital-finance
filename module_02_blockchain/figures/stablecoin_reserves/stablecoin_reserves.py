"""
Stablecoin Reserves Composition
Pie chart showing USDC reserve breakdown

Output: stablecoin_reserves.pdf
Module: module_02_blockchain
Lesson: 22 - Stablecoins
"""

from pathlib import Path
import matplotlib.pyplot as plt

CHART_METADATA = {
    'title': 'Stablecoin Reserves Composition',
    'module': 'module_02_blockchain',
    'lesson': 22,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/stablecoin_reserves'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create stablecoin reserves pie chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # USDC reserves
    usdc_reserves = ['US Treasuries', 'Cash', 'Repo']
    usdc_pct = [75, 20, 5]
    colors1 = ['#3498DB', '#27AE60', '#F39C12']

    wedges1, texts1, autotexts1 = ax1.pie(usdc_pct, labels=usdc_reserves, autopct='%1.0f%%',
                                          colors=colors1, startangle=90, explode=[0.02, 0, 0])
    ax1.set_title('USDC Reserves\n($25B)', fontsize=22, fontweight='bold')
    for autotext in autotexts1:
        autotext.set_fontsize(18)
        autotext.set_fontweight('bold')
    for text in texts1:
        text.set_fontsize(14)

    # USDT reserves (more complex)
    usdt_reserves = ['T-Bills', 'Cash', 'Corp Bonds', 'Other']
    usdt_pct = [80, 10, 5, 5]
    colors2 = ['#3498DB', '#27AE60', '#E74C3C', '#95A5A6']

    wedges2, texts2, autotexts2 = ax2.pie(usdt_pct, labels=usdt_reserves, autopct='%1.0f%%',
                                          colors=colors2, startangle=90, explode=[0.02, 0, 0, 0])
    ax2.set_title('USDT Reserves\n($120B)', fontsize=22, fontweight='bold')
    for autotext in autotexts2:
        autotext.set_fontsize(18)
        autotext.set_fontweight('bold')
    for text in texts2:
        text.set_fontsize(14)

    fig.text(0.5, 0.02, 'Source: Circle Attestation Reports, Tether Transparency Page (Q3 2024)',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'stablecoin_reserves.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
