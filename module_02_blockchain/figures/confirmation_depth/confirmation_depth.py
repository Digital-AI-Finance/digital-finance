"""
Confirmation Depth
Shows probability of double-spend success vs number of confirmations

Output: confirmation_depth.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Confirmation Depth',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/confirmation_depth'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create confirmation depth security chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Data: confirmations vs attack success probability
    confirmations = np.arange(0, 13)

    # Different attacker hashpower scenarios
    scenarios = {
        '10% attacker': [1.0, 0.21, 0.04, 0.01, 0.002, 0.0004, 0.0001, 0, 0, 0, 0, 0, 0],
        '25% attacker': [1.0, 0.43, 0.18, 0.08, 0.03, 0.01, 0.005, 0.002, 0.001, 0, 0, 0, 0],
        '33% attacker': [1.0, 0.58, 0.34, 0.20, 0.12, 0.07, 0.04, 0.02, 0.01, 0.007, 0.004, 0.002, 0.001],
        '45% attacker': [1.0, 0.82, 0.67, 0.55, 0.45, 0.37, 0.30, 0.25, 0.20, 0.17, 0.14, 0.11, 0.09],
    }
    colors = ['#27AE60', '#F39C12', '#E67E22', '#E74C3C']

    for (label, probs), color in zip(scenarios.items(), colors):
        ax.semilogy(confirmations, [max(p, 1e-5) for p in probs],
                    marker='o', linewidth=2.5, markersize=8, label=label, color=color)

    ax.set_xlabel('Number of Confirmations', fontsize=14)
    ax.set_ylabel('Attack Success Probability', fontsize=14)
    ax.set_title('Double-Spend Attack Success vs Confirmations', fontsize=18, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=12)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(1e-5, 2)

    # Highlight 6 confirmation standard
    ax.axvline(x=6, color='#3498DB', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(6.2, 0.5, 'Bitcoin standard:\n6 confirmations', fontsize=11, color='#3498DB')

    # Add annotation for practical security
    ax.axhline(y=0.001, color='#95A5A6', linestyle=':', linewidth=1.5)
    ax.text(10, 0.002, '0.1% threshold', fontsize=10, color='#666')

    # Recommendation box
    ax.text(0.02, 0.02, 'Recommended: 6 confirmations (~1 hour) for large transactions\n'
                       'Exchanges typically require 3-6 confirmations',
           transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#27AE60'))

    # Source
    fig.text(0.5, 0.02, 'Source: Nakamoto, Bitcoin Whitepaper (2008), Section 11 - Calculations',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'confirmation_depth.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
