"""
SWIFT Network Overview
Global interbank messaging

Output: swift_network.pdf
Module: module_04_trad_finance
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'SWIFT Network',
    'module': 'module_04_trad_finance',
    'lesson': 39,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/swift_network'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # SWIFT Message Types
    ax1 = axes[0]

    msg_types = ['MT103\n(Customer)', 'MT202\n(Bank-Bank)', 'MT700\n(L/C)',
                'MT900/910\n(Confirm)', 'MT940/950\n(Statement)', 'Others']
    volume = [45, 25, 8, 10, 7, 5]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#888888']

    wedges, texts, autotexts = ax1.pie(volume, labels=msg_types, autopct='%1.0f%%',
                                        colors=colors, startangle=90)

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)

    ax1.set_title('SWIFT Message Types by Volume', fontsize=12, fontweight='bold')

    # Daily SWIFT Traffic
    ax2 = axes[1]

    years = ['2018', '2019', '2020', '2021', '2022', '2023']
    messages = [33.0, 35.5, 37.0, 42.0, 44.5, 46.0]  # Millions per day

    ax2.bar(years, messages, color='#4A90E2', alpha=0.8, edgecolor='black')

    for i, (year, msg) in enumerate(zip(years, messages)):
        ax2.text(i, msg + 0.5, f'{msg}M', ha='center', fontsize=10, fontweight='bold')

    ax2.set_xlabel('Year', fontsize=11)
    ax2.set_ylabel('Daily Messages (Millions)', fontsize=11)
    ax2.set_title('SWIFT Daily Message Volume', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 55)
    ax2.yaxis.grid(True, alpha=0.3)

    # Key stats
    ax2.text(2.5, 50, '11,000+ Banks | 200+ Countries', fontsize=10, ha='center',
            fontweight='bold', color='#4A90E2')

    fig.suptitle('SWIFT: Global Financial Messaging Network', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'swift_network.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
