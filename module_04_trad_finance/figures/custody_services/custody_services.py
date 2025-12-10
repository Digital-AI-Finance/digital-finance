"""
Custody Services Overview
Asset safekeeping and services

Output: custody_services.pdf
Module: module_04_trad_finance
Lesson: 44 - Capital Markets Tech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Custody Services',
    'module': 'module_04_trad_finance',
    'lesson': 44,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/custody_services'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Global custodians market share
    ax1 = axes[0]

    custodians = ['BNY Mellon', 'State Street', 'JPMorgan', 'Citi', 'BNP Paribas', 'Others']
    auc = [47.8, 43.3, 32.6, 26.3, 13.8, 40.2]  # Assets Under Custody in $T
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#9B59B6', '#D62728', '#888888']

    wedges, texts, autotexts = ax1.pie(auc, labels=custodians, autopct='%1.1f%%',
                                        colors=colors, startangle=90,
                                        explode=[0.02, 0.02, 0, 0, 0, 0])

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    for text in texts:
        text.set_fontsize(9)

    ax1.set_title('Global Custodians by AUC', fontsize=12, fontweight='bold')

    # Add center text
    centre_circle = plt.Circle((0, 0), 0.4, fc='white')
    ax1.add_patch(centre_circle)
    ax1.text(0, 0, 'Total:\n$204T', ha='center', va='center', fontsize=10, fontweight='bold')

    # Custody services breakdown
    ax2 = axes[1]

    services = ['Asset\nSafekeeping', 'Settlement', 'Corporate\nActions', 'Income\nCollection', 'Tax\nReclaim', 'Reporting']
    importance = [95, 90, 85, 80, 70, 88]
    automation = [98, 95, 75, 90, 60, 85]

    x = np.arange(len(services))
    width = 0.35

    bars1 = ax2.bar(x - width/2, importance, width, label='Client Importance',
                    color='#4A90E2', alpha=0.8, edgecolor='black')
    bars2 = ax2.bar(x + width/2, automation, width, label='Automation Level',
                    color='#44A044', alpha=0.8, edgecolor='black')

    ax2.set_ylabel('Score (%)', fontsize=11)
    ax2.set_title('Custody Services: Importance vs. Automation', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(services, fontsize=9)
    ax2.legend(loc='lower right', fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.yaxis.grid(True, alpha=0.3)

    # Highlight automation gap
    for i, (imp, auto) in enumerate(zip(importance, automation)):
        if imp > auto:
            ax2.annotate('', xy=(i+width/2, auto+2), xytext=(i-width/2, imp-2),
                        arrowprops=dict(arrowstyle='<->', color='#D62728', lw=1.5))

    fig.suptitle('Custody Services Landscape', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'custody_services.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
