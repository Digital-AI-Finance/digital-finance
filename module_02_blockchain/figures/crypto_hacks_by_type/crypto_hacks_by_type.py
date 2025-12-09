"""
Crypto Hacks by Type
Bar chart showing losses by attack vector

Output: crypto_hacks_by_type.pdf
Module: module_02_blockchain
Lesson: 23 - Security
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Crypto Hacks by Type',
    'module': 'module_02_blockchain',
    'lesson': 23,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/crypto_hacks_by_type'
}

plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 14,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create crypto hacks by type bar chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    attack_types = ['Bridge\nExploits', 'Smart Contract\nBugs', 'Private Key\nCompromise',
                   'Flash Loan\nAttacks', 'Oracle\nManipulation', 'Rug Pulls']
    losses = [2800, 1500, 1200, 800, 500, 400]  # Millions USD cumulative
    colors = ['#E74C3C', '#3498DB', '#F39C12', '#9B59B6', '#27AE60', '#95A5A6']

    bars = ax.bar(attack_types, losses, color=colors, alpha=0.85, edgecolor='black', linewidth=2)

    ax.set_ylabel('Total Losses ($ Millions)', fontsize=20)
    ax.set_title('Cumulative Crypto Losses by Attack Type (2020-2024)', fontsize=26, fontweight='bold', pad=20)

    # Add value labels
    for bar, val in zip(bars, losses):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
               f'${val/1000:.1f}B' if val >= 1000 else f'${val}M',
               ha='center', fontsize=16, fontweight='bold')

    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, 3500)

    # Total losses annotation
    total = sum(losses)
    ax.text(0.98, 0.95, f'Total: ${total/1000:.1f}B', transform=ax.transAxes,
           fontsize=18, ha='right', va='top', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#E74C3C'))

    fig.text(0.5, 0.02, 'Source: Chainalysis, Rekt.news, DeFiLlama Hacks (Dec 2024) [ILLUSTRATIVE]',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'crypto_hacks_by_type.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
