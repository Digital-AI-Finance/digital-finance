"""
Consensus Mechanism Comparison: PoW vs PoS
Comparative visualization of Proof of Work vs Proof of Stake characteristics

Required libraries: matplotlib, numpy
Output: consensus_comparison.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Consensus Mechanism Comparison (PoW vs PoS)',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_02_blockchain/consensus_comparison'
}

def create_consensus_comparison():
    """Create a comparison chart of PoW vs PoS consensus mechanisms"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Metrics for comparison
    metrics = ['Energy\nEfficiency', 'Security\n(51% Attack)', 'Decentralization',
               'Transaction\nSpeed', 'Environmental\nImpact']

    # Scores (0-10 scale)
    pow_scores = [2, 9, 8, 4, 2]  # PoW characteristics
    pos_scores = [9, 7, 6, 8, 9]  # PoS characteristics

    x = np.arange(len(metrics))
    width = 0.35

    # Left panel: Bar chart comparison
    bars1 = ax1.bar(x - width/2, pow_scores, width, label='Proof of Work',
                    color='darkgray', edgecolor='black', linewidth=0.5)
    bars2 = ax1.bar(x + width/2, pos_scores, width, label='Proof of Stake',
                    color='lightgray', edgecolor='black', linewidth=0.5)

    ax1.set_ylabel('Score (0-10)', fontsize=8)
    ax1.set_title('Consensus Mechanism Comparison', fontsize=10, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, fontsize=7)
    ax1.legend(loc='upper right', fontsize=7)
    ax1.set_ylim(0, 10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Right panel: Key characteristics table
    ax2.axis('off')

    # Table data
    characteristics = [
        ['Characteristic', 'Proof of Work', 'Proof of Stake'],
        ['Selection Basis', 'Computational Power', 'Token Ownership'],
        ['Hardware Required', 'Specialized ASICs', 'Standard Computer'],
        ['Energy Consumption', 'Very High', 'Very Low'],
        ['Examples', 'Bitcoin, Ethereum 1.0', 'Ethereum 2.0, Cardano'],
        ['Barrier to Entry', 'High (equipment)', 'Medium (stake)'],
        ['Finality', 'Probabilistic', 'Faster/Deterministic']
    ]

    # Create table
    table = ax2.table(cellText=characteristics,
                     cellLoc='left',
                     loc='center',
                     bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(7)

    # Style header row
    for i in range(3):
        cell = table[(0, i)]
        cell.set_facecolor('darkgray')
        cell.set_text_props(weight='bold', color='black')

    # Alternate row colors
    for i in range(1, len(characteristics)):
        for j in range(3):
            cell = table[(i, j)]
            if i % 2 == 0:
                cell.set_facecolor('lightgray')
            else:
                cell.set_facecolor('white')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

    ax2.set_title('Key Characteristics', fontsize=10, fontweight='bold', pad=20)

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'consensus_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_consensus_comparison()
