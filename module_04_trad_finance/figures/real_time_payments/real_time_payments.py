"""
Real-Time Payment Systems
Global RTP adoption

Output: real_time_payments.pdf
Module: module_04_trad_finance
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Real Time Payments',
    'module': 'module_04_trad_finance',
    'lesson': 39,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/real_time_payments'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # RTP Systems by Country
    ax1 = axes[0]

    countries = ['India\n(UPI)', 'China\n(CNAPS)', 'Brazil\n(PIX)', 'UK\n(FPS)',
                'Thailand\n(PromptPay)', 'USA\n(RTP/FedNow)']
    transactions = [12.0, 8.5, 4.2, 3.8, 2.5, 0.8]  # Billions per year

    colors = ['#FF7F0E', '#D62728', '#44A044', '#4A90E2', '#9B59B6', '#17BECF']

    bars = ax1.barh(countries, transactions, color=colors, alpha=0.8, edgecolor='black')

    for bar, txn in zip(bars, transactions):
        ax1.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{txn}B', va='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Annual Transactions (Billions)', fontsize=11)
    ax1.set_title('Real-Time Payment Volume by Country', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 15)
    ax1.xaxis.grid(True, alpha=0.3)

    # RTP Adoption Growth
    ax2 = axes[1]

    years = ['2020', '2021', '2022', '2023', '2024', '2025E']
    global_rtp = [70, 120, 195, 266, 350, 450]  # Billions

    ax2.plot(years, global_rtp, 'g-', linewidth=2.5, marker='o', markersize=8)
    ax2.fill_between(years, global_rtp, alpha=0.2, color='green')

    for i, (year, vol) in enumerate(zip(years, global_rtp)):
        ax2.text(i, vol + 15, f'{vol}B', ha='center', fontsize=9, fontweight='bold')

    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Global RTP Transactions (Billions)', fontsize=11)
    ax2.set_title('Global Real-Time Payment Growth', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 500)
    ax2.grid(True, alpha=0.3)

    # CAGR annotation
    ax2.text(2.5, 400, 'CAGR: ~45%', fontsize=11, fontweight='bold',
            color='#44A044', ha='center')

    fig.suptitle('Real-Time Payment Systems: Global Landscape', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'real_time_payments.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
