"""
ECC Point Addition
Illustrates elliptic curve point addition operation

Output: ecc_point_addition.pdf
Module: module_02_blockchain
Lesson: 15 - Public Key Cryptography
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'ECC Point Addition',
    'module': 'module_02_blockchain',
    'lesson': 15,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_02_blockchain/figures/ecc_point_addition'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create ECC point addition diagram"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Left plot: Point addition P + Q = R
    # Elliptic curve y^2 = x^3 - x + 1
    x = np.linspace(-1.5, 2, 400)
    y_pos = np.sqrt(np.clip(x**3 - x + 1, 0, None))
    y_neg = -y_pos

    ax1.plot(x, y_pos, 'b-', linewidth=2, label='y² = x³ - x + 1')
    ax1.plot(x, y_neg, 'b-', linewidth=2)

    # Points P, Q, R
    P = (-1, 1)
    Q = (0, 1)
    R_neg = (1, -1)  # -R (intersection)
    R = (1, 1)  # R (reflection)

    ax1.plot(*P, 'ro', markersize=12, label='P')
    ax1.plot(*Q, 'go', markersize=12, label='Q')
    ax1.plot(*R_neg, 'mo', markersize=10, alpha=0.5)
    ax1.plot(*R, 'ko', markersize=12, label='R = P + Q')

    # Line through P and Q
    ax1.plot([P[0], Q[0], R_neg[0], 2], [P[1], Q[1], R_neg[1], 2], 'r--', linewidth=1.5, alpha=0.7)

    # Vertical line from -R to R
    ax1.plot([R_neg[0], R[0]], [R_neg[1], R[1]], 'g--', linewidth=1.5, alpha=0.7)

    # Annotations
    ax1.annotate('P', P, xytext=(P[0]-0.3, P[1]+0.2), fontsize=14, fontweight='bold')
    ax1.annotate('Q', Q, xytext=(Q[0]+0.1, Q[1]+0.2), fontsize=14, fontweight='bold')
    ax1.annotate('-R', R_neg, xytext=(R_neg[0]+0.1, R_neg[1]-0.3), fontsize=12, color='purple')
    ax1.annotate('R', R, xytext=(R[0]+0.1, R[1]+0.2), fontsize=14, fontweight='bold')

    ax1.set_xlim(-2, 2.5)
    ax1.set_ylim(-2, 2.5)
    ax1.set_xlabel('x', fontsize=14)
    ax1.set_ylabel('y', fontsize=14)
    ax1.set_title('Point Addition: P + Q = R', fontsize=16, fontweight='bold')
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='lower right', fontsize=10)

    # Right plot: Point doubling 2P = R
    ax2.plot(x, y_pos, 'b-', linewidth=2, label='y² = x³ - x + 1')
    ax2.plot(x, y_neg, 'b-', linewidth=2)

    # Point P and 2P
    P2 = (-0.5, np.sqrt((-0.5)**3 - (-0.5) + 1))
    R2 = (1.5, -np.sqrt(1.5**3 - 1.5 + 1))  # Approximate

    ax2.plot(*P2, 'ro', markersize=12, label='P')
    ax2.plot(1.5, 0.9, 'ko', markersize=12, label='2P')

    # Tangent line at P
    ax2.plot([-1.5, 2], [1.8, -0.3], 'r--', linewidth=1.5, alpha=0.7, label='Tangent at P')

    ax2.annotate('P', P2, xytext=(P2[0]-0.3, P2[1]+0.2), fontsize=14, fontweight='bold')
    ax2.annotate('2P', (1.5, 0.9), xytext=(1.6, 1.1), fontsize=14, fontweight='bold')

    ax2.set_xlim(-2, 2.5)
    ax2.set_ylim(-2, 2.5)
    ax2.set_xlabel('x', fontsize=14)
    ax2.set_ylabel('y', fontsize=14)
    ax2.set_title('Point Doubling: 2P = P + P', fontsize=16, fontweight='bold')
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='lower right', fontsize=10)

    # Add formula box
    fig.text(0.5, 0.02, 'Source: SEC 1: Elliptic Curve Cryptography, Standards for Efficient Cryptography Group',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ecc_point_addition.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
