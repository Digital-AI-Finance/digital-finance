"""
CBDC vs Other Digital Money
Comparison of digital currency types

Output: cbdc_comparison.pdf
Module: module_04_trad_finance
Lesson: 48 - CBDC
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'CBDC Comparison',
    'module': 'module_04_trad_finance',
    'lesson': 48,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/cbdc_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Feature comparison
    ax1 = axes[0]

    features = ['Central Bank\nBacked', 'Digital\nNative', 'Programmable', 'Privacy', 'Decentralized', 'Stable\nValue']
    cbdc = [100, 100, 80, 50, 20, 100]
    stablecoins = [0, 100, 90, 40, 60, 95]
    crypto = [0, 100, 95, 70, 100, 10]
    bank_deposits = [50, 50, 30, 30, 0, 100]

    x = np.arange(len(features))
    width = 0.2

    ax1.bar(x - 1.5*width, cbdc, width, label='CBDC', color='#4A90E2', alpha=0.8)
    ax1.bar(x - 0.5*width, stablecoins, width, label='Stablecoins', color='#44A044', alpha=0.8)
    ax1.bar(x + 0.5*width, crypto, width, label='Crypto', color='#FF7F0E', alpha=0.8)
    ax1.bar(x + 1.5*width, bank_deposits, width, label='Bank Deposits', color='#9B59B6', alpha=0.8)

    ax1.set_ylabel('Score (0-100)', fontsize=11)
    ax1.set_title('Digital Money Feature Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(features, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 110)
    ax1.yaxis.grid(True, alpha=0.3)

    # Radar/Spider chart as alternative
    ax2 = axes[1]

    # Use cases comparison
    use_cases = ['Retail\nPayments', 'Cross-border', 'Wholesale\nSettlement', 'Financial\nInclusion', 'Policy\nImplementation', 'Privacy\nPreservation']
    cbdc_score = [85, 70, 90, 95, 100, 40]
    stablecoin_score = [80, 85, 60, 70, 20, 50]
    cash_score = [95, 20, 10, 60, 30, 100]

    x = np.arange(len(use_cases))
    width = 0.25

    ax2.bar(x - width, cbdc_score, width, label='CBDC', color='#4A90E2', alpha=0.8)
    ax2.bar(x, stablecoin_score, width, label='Stablecoins', color='#44A044', alpha=0.8)
    ax2.bar(x + width, cash_score, width, label='Cash', color='#FF7F0E', alpha=0.8)

    ax2.set_ylabel('Suitability Score', fontsize=11)
    ax2.set_title('Use Case Comparison', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(use_cases, fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    fig.suptitle('CBDC vs. Other Forms of Digital Money', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'cbdc_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
