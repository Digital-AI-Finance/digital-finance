"""
Double Spending Scenario
Illustrates the double spending problem in digital currencies

Output: double_spending_scenario.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Double Spending Scenario',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/double_spending_scenario'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create double spending scenario diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'The Double Spending Problem', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 9.6, 'Why digital cash needs blockchain consensus', fontsize=14, ha='center', color='#666')

    # Attacker (Alice)
    attacker_box = mpatches.FancyBboxPatch((5.5, 7), 3, 1.5,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#E74C3C', alpha=0.3,
                                            edgecolor='#E74C3C', lw=2)
    ax.add_patch(attacker_box)
    ax.text(7, 8, 'Alice (Attacker)', ha='center', fontsize=14, fontweight='bold')
    ax.text(7, 7.4, 'Has 1 BTC', ha='center', fontsize=12)

    # Two transactions
    tx1_box = mpatches.FancyBboxPatch((1, 4), 4, 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#3498DB', alpha=0.3,
                                       edgecolor='#3498DB', lw=2)
    ax.add_patch(tx1_box)
    ax.text(3, 5.5, 'Transaction 1', ha='center', fontsize=12, fontweight='bold')
    ax.text(3, 4.9, 'Send 1 BTC to Bob', ha='center', fontsize=11)
    ax.text(3, 4.4, '(Buy goods)', ha='center', fontsize=10, style='italic')

    tx2_box = mpatches.FancyBboxPatch((9, 4), 4, 2,
                                       boxstyle='round,pad=0.1',
                                       facecolor='#F39C12', alpha=0.3,
                                       edgecolor='#F39C12', lw=2)
    ax.add_patch(tx2_box)
    ax.text(11, 5.5, 'Transaction 2', ha='center', fontsize=12, fontweight='bold')
    ax.text(11, 4.9, 'Send 1 BTC to Carol', ha='center', fontsize=11)
    ax.text(11, 4.4, '(Buy services)', ha='center', fontsize=10, style='italic')

    # Arrows from Alice to transactions
    ax.annotate('', xy=(3, 6), xytext=(5.5, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#E74C3C'))
    ax.annotate('', xy=(11, 6), xytext=(8.5, 7),
               arrowprops=dict(arrowstyle='->', lw=2, color='#E74C3C'))

    # Problem statement
    problem_box = mpatches.FancyBboxPatch((3, 2), 8, 1.5,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#9B59B6', alpha=0.2,
                                           edgecolor='#9B59B6', lw=2)
    ax.add_patch(problem_box)
    ax.text(7, 3, 'PROBLEM: Which transaction is valid?', ha='center', fontsize=14, fontweight='bold', color='#9B59B6')
    ax.text(7, 2.4, 'Without consensus, both recipients think they were paid', ha='center', fontsize=11)

    # Solution
    solution_box = mpatches.FancyBboxPatch((2, 0.3), 10, 1.2,
                                            boxstyle='round,pad=0.1',
                                            facecolor='#27AE60', alpha=0.2,
                                            edgecolor='#27AE60', lw=2)
    ax.add_patch(solution_box)
    ax.text(7, 1.1, 'SOLUTION: Blockchain consensus determines which Tx is confirmed first', ha='center', fontsize=12, fontweight='bold', color='#27AE60')
    ax.text(7, 0.6, 'PoW/PoS ensures network agrees on transaction order', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, 'Source: Nakamoto, Bitcoin Whitepaper (2008), "Commerce on the Internet"',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'double_spending_scenario.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
