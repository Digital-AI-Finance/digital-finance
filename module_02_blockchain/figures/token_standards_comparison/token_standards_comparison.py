"""
Token Standards Comparison
Bar chart comparing ERC token standards

Output: token_standards_comparison.pdf
Module: module_02_blockchain
Lesson: 20 - Tokens
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Token Standards Comparison',
    'module': 'module_02_blockchain',
    'lesson': 20,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/token_standards_comparison'
}

# 40% larger fonts
plt.rcParams.update({
    'font.size': 20,
    'axes.labelsize': 20,
    'axes.titlesize': 28,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
})

def create_chart():
    """Create token standards comparison bar chart"""
    fig, ax = plt.subplots(figsize=(14, 8))

    standards = ['ERC-20', 'ERC-721', 'ERC-1155', 'ERC-4626']
    deployed_contracts = [500000, 150000, 25000, 5000]  # Approximate numbers
    colors = ['#3498DB', '#27AE60', '#F39C12', '#9B59B6']

    bars = ax.bar(standards, deployed_contracts, color=colors, alpha=0.85, edgecolor='black', linewidth=2)

    ax.set_ylabel('Deployed Contracts (approx.)', fontsize=20)
    ax.set_title('Ethereum Token Standards by Adoption', fontsize=28, fontweight='bold', pad=20)
    ax.set_ylim(0, 600000)

    # Add value labels
    for bar, val in zip(bars, deployed_contracts):
        height = bar.get_height()
        label = f'{val/1000:.0f}K' if val >= 1000 else str(val)
        ax.text(bar.get_x() + bar.get_width()/2, height + 15000,
               label, ha='center', fontsize=18, fontweight='bold')

    # Add use case labels
    use_cases = ['Fungible tokens', 'NFTs (unique)', 'Multi-token', 'Yield vaults']
    for bar, use in zip(bars, use_cases):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
               use, ha='center', va='center', fontsize=14, color='white', fontweight='bold', rotation=90)

    ax.grid(axis='y', alpha=0.3)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

    fig.text(0.5, 0.02, 'Source: Etherscan, Dune Analytics (Dec 2024) [ILLUSTRATIVE]',
            fontsize=14, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'token_standards_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
