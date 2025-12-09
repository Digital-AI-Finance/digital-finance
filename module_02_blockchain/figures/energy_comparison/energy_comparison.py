"""
Energy Comparison
Compares energy consumption of PoW vs PoS

Output: energy_comparison.pdf
Module: module_02_blockchain
Lesson: 17 - Proof of Stake
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Energy Comparison',
    'module': 'module_02_blockchain',
    'lesson': 17,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/energy_comparison'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create energy comparison chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Left: Bar comparison
    systems = ['Bitcoin\n(PoW)', 'Ethereum\n(Pre-Merge PoW)', 'Ethereum\n(Post-Merge PoS)', 'Visa\n(Reference)']
    energy = [150, 85, 0.01, 0.002]  # TWh/year
    colors = ['#E74C3C', '#F39C12', '#27AE60', '#3498DB']

    # Use log scale
    bars = ax1.bar(systems, energy, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_yscale('log')
    ax1.set_ylabel('Energy Consumption (TWh/year)', fontsize=14)
    ax1.set_title('Blockchain Energy Consumption', fontsize=16, fontweight='bold')
    ax1.set_ylim(0.001, 200)

    # Add value labels
    for bar, e in zip(bars, energy):
        height = bar.get_height()
        label = f'{e:.2f}' if e < 1 else f'{e:.0f}'
        ax1.text(bar.get_x() + bar.get_width()/2, height * 1.3,
                f'{label} TWh', ha='center', fontsize=11, fontweight='bold')

    ax1.grid(axis='y', alpha=0.3, which='both')

    # Right: Percentage reduction
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('The Merge: Energy Impact', fontsize=16, fontweight='bold')

    # Before/After comparison
    ax2.text(5, 8.5, 'Ethereum Energy Reduction', ha='center', fontsize=14, fontweight='bold')

    # Before
    before_circle = plt.Circle((2.5, 5.5), 1.5, facecolor='#E74C3C', alpha=0.5, edgecolor='#C0392B', lw=2)
    ax2.add_patch(before_circle)
    ax2.text(2.5, 5.5, '85\nTWh', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax2.text(2.5, 3.5, 'Before\n(PoW)', ha='center', fontsize=12)

    # After
    after_circle = plt.Circle((7.5, 5.5), 0.1, facecolor='#27AE60', alpha=0.8, edgecolor='#1E8449', lw=2)
    ax2.add_patch(after_circle)
    ax2.text(7.5, 5.5, '', ha='center', va='center', fontsize=10, color='white')
    ax2.text(7.5, 4.2, '0.01 TWh', ha='center', fontsize=12, fontweight='bold', color='#27AE60')
    ax2.text(7.5, 3.5, 'After\n(PoS)', ha='center', fontsize=12)

    # Arrow
    ax2.annotate('', xy=(6, 5.5), xytext=(4.5, 5.5),
                arrowprops=dict(arrowstyle='->', lw=3, color='#333'))

    # Reduction percentage
    ax2.text(5, 2, '99.95%\nReduction', ha='center', fontsize=24, fontweight='bold', color='#27AE60',
            bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60', lw=2))

    # Context
    ax2.text(5, 0.5, 'Equivalent to: Removing a small country from global energy grid',
            ha='center', fontsize=11, style='italic')

    # Source
    fig.text(0.5, 0.02, 'Source: Cambridge Bitcoin Electricity Consumption Index, Ethereum Foundation (Sep 2022)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'energy_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
