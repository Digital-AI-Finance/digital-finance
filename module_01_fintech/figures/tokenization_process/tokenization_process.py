"""
Tokenization Process Flow Diagram
Shows how payment card tokenization works for mobile wallets

Output: tokenization_process.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Payment Card Tokenization Process',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/tokenization_process'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
})

def create_chart():
    """Create tokenization process flow diagram"""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Colors
    box_color = '#E8E8E8'
    arrow_color = '#333333'
    highlight = '#4A90E2'

    # Define box positions and labels
    boxes = [
        (1, 6, 'User adds card\nto wallet'),
        (4, 6, 'Card network\nreceives request'),
        (7, 6, 'Token Service\nProvider (TSP)'),
        (10, 6, 'Token generated\n& stored'),
        (1, 3, 'User makes\npayment'),
        (4, 3, 'Token sent\nto merchant'),
        (7, 3, 'Network\nde-tokenizes'),
        (10, 3, 'Issuer\nauthorizes'),
    ]

    # Draw boxes
    for x, y, text in boxes:
        rect = mpatches.FancyBboxPatch(
            (x - 1.2, y - 0.8), 2.4, 1.6,
            boxstyle="round,pad=0.1",
            facecolor=box_color,
            edgecolor='#666666',
            linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold')

    # Draw arrows (horizontal)
    arrow_style = dict(arrowstyle='->', color=arrow_color, lw=2)

    # Top row arrows
    for i in range(3):
        x_start = boxes[i][0] + 1.2
        x_end = boxes[i+1][0] - 1.2
        ax.annotate('', xy=(x_end, 6), xytext=(x_start, 6),
                   arrowprops=arrow_style)

    # Bottom row arrows
    for i in range(4, 7):
        x_start = boxes[i][0] + 1.2
        x_end = boxes[i+1][0] - 1.2
        ax.annotate('', xy=(x_end, 3), xytext=(x_start, 3),
                   arrowprops=arrow_style)

    # Vertical arrows (connecting rows)
    ax.annotate('', xy=(1, 3.8), xytext=(1, 5.2),
               arrowprops=dict(arrowstyle='->', color=highlight, lw=2, linestyle='--'))
    ax.annotate('', xy=(10, 5.2), xytext=(10, 3.8),
               arrowprops=dict(arrowstyle='->', color=highlight, lw=2, linestyle='--'))

    # Labels for rows
    ax.text(0.2, 6, 'ENROLLMENT', fontsize=11, fontweight='bold',
            color='#333333', rotation=90, va='center')
    ax.text(0.2, 3, 'TRANSACTION', fontsize=11, fontweight='bold',
            color='#333333', rotation=90, va='center')

    # Key information box
    key_text = """Key Points:
- Original PAN never stored on device
- Token is device-specific
- Cryptogram adds transaction security
- Real PAN only known to network/issuer"""

    ax.text(6, 0.8, key_text, fontsize=8, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#999999'))

    # Title
    ax.text(6, 7.5, 'Payment Card Tokenization Process',
           fontsize=14, fontweight='bold', ha='center')

    # Synthetic data label
    ax.text(11.8, 0.2, '[ILLUSTRATIVE]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'tokenization_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
