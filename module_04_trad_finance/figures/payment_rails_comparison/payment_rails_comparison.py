"""
Payment Rails Comparison
Different payment network characteristics

Output: payment_rails_comparison.pdf
Module: module_04_trad_finance
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Payment Rails Comparison',
    'module': 'module_04_trad_finance',
    'lesson': 39,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/payment_rails_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 8))

    rails = ['Wire\n(Fedwire)', 'ACH', 'SWIFT', 'RTP', 'Card\nNetworks', 'Crypto']
    attributes = ['Speed', 'Cost', 'Volume Limit', 'Global Reach', 'Finality', 'Availability']

    scores = np.array([
        [95, 30, 100, 60, 100, 70],   # Wire
        [40, 90, 70, 40, 60, 60],     # ACH
        [60, 50, 95, 100, 80, 80],    # SWIFT
        [100, 75, 50, 30, 95, 95],    # RTP
        [85, 60, 60, 90, 70, 95],     # Card
        [80, 70, 80, 95, 100, 100]    # Crypto
    ])

    im = ax.imshow(scores, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

    ax.set_xticks(np.arange(len(attributes)))
    ax.set_yticks(np.arange(len(rails)))
    ax.set_xticklabels(attributes, fontsize=10)
    ax.set_yticklabels(rails, fontsize=10)

    for i in range(len(rails)):
        for j in range(len(attributes)):
            text_color = 'white' if scores[i, j] < 40 or scores[i, j] > 70 else 'black'
            ax.text(j, i, f'{scores[i, j]}', ha='center', va='center',
                   color=text_color, fontsize=10, fontweight='bold')

    ax.set_title('Payment Rails: Attribute Comparison', fontsize=14, fontweight='bold', pad=15)

    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('Score (0-100)', fontsize=10)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'payment_rails_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
