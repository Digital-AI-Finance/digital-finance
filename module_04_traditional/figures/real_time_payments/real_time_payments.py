"""
Real-Time Payment Systems Adoption
Shows RTP adoption by country

Output: real_time_payments.pdf
Module: module_04_traditional
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    countries = ['India\n(UPI)', 'Brazil\n(PIX)', 'Thailand\n(PromptPay)', 'China', 'UK\n(FPS)', 'Australia\n(NPP)', 'USA\n(FedNow)']
    rtp_share = [70, 35, 45, 60, 20, 15, 5]  # % of person-to-person payments

    colors = [MLGREEN if x > 30 else MLORANGE if x > 10 else MLBLUE for x in rtp_share]

    bars = ax.bar(countries, rtp_share, color=colors, edgecolor='white', linewidth=2)

    for bar, val in zip(bars, rtp_share):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val}%', ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('RTP Share of P2P Payments (%)', fontsize=11)
    ax.set_title('Real-Time Payment Adoption by Country (2024)', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 85)

    # Add legend for colors
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=MLGREEN, label='High (>30%)'),
                       Patch(facecolor=MLORANGE, label='Medium (10-30%)'),
                       Patch(facecolor=MLBLUE, label='Low (<10%)')]
    ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: ACI Worldwide, FIS [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'real_time_payments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
