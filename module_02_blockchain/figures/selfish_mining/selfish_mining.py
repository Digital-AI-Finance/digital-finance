"""
Selfish Mining
Illustrates the selfish mining attack strategy

Output: selfish_mining.pdf
Module: module_02_blockchain
Lesson: 14 - Hashing
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Selfish Mining',
    'module': 'module_02_blockchain',
    'lesson': 14,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/selfish_mining'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create selfish mining attack diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(7, 10.3, 'Selfish Mining Attack Strategy', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 9.6, 'Withholding blocks to gain unfair advantage', fontsize=14, ha='center', color='#666')

    # Step 1: Normal mining
    ax.text(1, 8.5, 'Step 1: Selfish miner finds block but keeps it private', fontsize=12, fontweight='bold')

    # Public chain
    for i, x in enumerate([2, 4, 6]):
        block = mpatches.FancyBboxPatch((x-0.6, 7.2), 1.2, 0.8,
                                         boxstyle='round,pad=0.05',
                                         facecolor='#27AE60', alpha=0.8,
                                         edgecolor='black', lw=1.5)
        ax.add_patch(block)
        ax.text(x, 7.6, f'B{i+1}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    ax.text(8, 7.6, 'Public Chain', fontsize=11, color='#27AE60', fontweight='bold')

    # Secret block
    secret = mpatches.FancyBboxPatch((7.4, 7.2), 1.2, 0.8,
                                      boxstyle='round,pad=0.05',
                                      facecolor='#E74C3C', alpha=0.8,
                                      edgecolor='black', lw=2)
    ax.add_patch(secret)
    ax.text(8, 7.6, 'B4', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    ax.text(8, 6.6, '(SECRET)', ha='center', fontsize=9, color='#E74C3C', fontweight='bold')

    # Arrows
    ax.annotate('', xy=(3.4, 7.6), xytext=(2.6, 7.6), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(5.4, 7.6), xytext=(4.6, 7.6), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(7.4, 7.6), xytext=(6.6, 7.6), arrowprops=dict(arrowstyle='->', lw=1.5, color='#E74C3C', linestyle='dashed'))

    # Step 2: Race condition
    ax.text(1, 5.8, 'Step 2: If honest miner finds B4, selfish miner releases their B4', fontsize=12, fontweight='bold')

    # Two competing blocks
    honest_b4 = mpatches.FancyBboxPatch((4.4, 4.5), 1.2, 0.8,
                                         boxstyle='round,pad=0.05',
                                         facecolor='#27AE60', alpha=0.8,
                                         edgecolor='black', lw=1.5)
    ax.add_patch(honest_b4)
    ax.text(5, 4.9, "B4'", ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    ax.text(5, 4.1, 'Honest', fontsize=9, color='#27AE60')

    selfish_b4 = mpatches.FancyBboxPatch((7.4, 4.5), 1.2, 0.8,
                                          boxstyle='round,pad=0.05',
                                          facecolor='#E74C3C', alpha=0.8,
                                          edgecolor='black', lw=1.5)
    ax.add_patch(selfish_b4)
    ax.text(8, 4.9, 'B4', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    ax.text(8, 4.1, 'Selfish', fontsize=9, color='#E74C3C')

    ax.text(6.5, 4.9, 'vs', fontsize=14, ha='center', fontweight='bold')

    # Step 3: Advantage
    ax.text(1, 3.2, 'Step 3: With >25% hashpower, selfish miner gains disproportionate rewards', fontsize=12, fontweight='bold')

    # Profit visualization
    categories = ['Hashpower', 'Expected\nReward']
    honest_vals = [75, 68]
    selfish_vals = [25, 32]

    bar_width = 0.35
    x_pos = [2.5, 5]

    for i, (cat, h, s) in enumerate(zip(categories, honest_vals, selfish_vals)):
        # Stacked bars
        ax.barh(x_pos[i], h, bar_width, color='#27AE60', alpha=0.8, label='Honest' if i == 0 else '')
        ax.barh(x_pos[i], s, bar_width, left=h, color='#E74C3C', alpha=0.8, label='Selfish' if i == 0 else '')
        ax.text(1.5, x_pos[i], cat, ha='right', va='center', fontsize=11)
        ax.text(h/2, x_pos[i], f'{h}%', ha='center', va='center', fontsize=11, color='white', fontweight='bold')
        ax.text(h + s/2, x_pos[i], f'{s}%', ha='center', va='center', fontsize=11, color='white', fontweight='bold')

    # Defense box
    defense_box = mpatches.FancyBboxPatch((0.5, 0.3), 13, 1.2,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#3498DB', alpha=0.2,
                                           edgecolor='#3498DB', lw=2)
    ax.add_patch(defense_box)
    ax.text(7, 1.1, 'Defenses: Uniform tie-breaking, timestamp verification, difficulty adjustment', ha='center', fontsize=12, fontweight='bold', color='#2980B9')
    ax.text(7, 0.6, 'Research shows attack profitable with >25% hashpower (not 51%)', ha='center', fontsize=11)

    # Source
    fig.text(0.5, 0.02, 'Source: Eyal & Sirer, "Majority is not Enough" (2014), Cornell University',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'selfish_mining.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
