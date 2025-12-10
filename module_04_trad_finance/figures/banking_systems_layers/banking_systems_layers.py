"""
Banking Systems Layers
System stack in banking

Output: banking_systems_layers.pdf
Module: module_04_trad_finance
Lesson: 38 - Core Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Banking Systems Layers',
    'module': 'module_04_trad_finance',
    'lesson': 38,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_04_trad_finance/figures/banking_systems_layers'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # System Categories
    ax1 = axes[0]

    categories = ['Core Banking', 'Risk Systems', 'Treasury', 'CRM', 'Compliance',
                 'Data Analytics', 'Digital Channels']
    investment = [35, 18, 12, 10, 12, 8, 5]  # IT spend percentage
    age = [25, 15, 18, 8, 10, 5, 3]  # Average system age

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax1.bar(x - width/2, investment, width, label='IT Spend (%)', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x + width/2, age, width, label='Avg System Age (yrs)', color='#D62728', alpha=0.8)

    ax1.set_xlabel('System Category', fontsize=11)
    ax1.set_ylabel('Value', fontsize=11)
    ax1.set_title('Bank IT Landscape: Spend and Age', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, rotation=30, ha='right', fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 40)
    ax1.yaxis.grid(True, alpha=0.3)

    # Vendor Market Share
    ax2 = axes[1]

    vendors = ['Temenos', 'Finastra', 'FIS', 'Infosys\nFinacle', 'Oracle', 'SAP', 'Others']
    share = [18, 15, 14, 12, 10, 8, 23]
    colors = ['#4A90E2', '#44A044', '#FF7F0E', '#D62728', '#9B59B6', '#17BECF', '#888888']

    wedges, texts, autotexts = ax2.pie(share, labels=vendors, autopct='%1.0f%%',
                                        colors=colors, startangle=90)

    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)

    ax2.set_title('Core Banking Vendor Market Share', fontsize=12, fontweight='bold')

    fig.suptitle('Banking Technology Systems Overview', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'banking_systems_layers.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
