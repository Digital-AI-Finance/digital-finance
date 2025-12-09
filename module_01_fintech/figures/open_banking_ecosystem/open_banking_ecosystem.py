"""
Open Banking Ecosystem Players
Shows the key participants in the open banking ecosystem

Output: open_banking_ecosystem.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking Ecosystem',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/open_banking_ecosystem'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open banking ecosystem chart"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Open Banking Ecosystem Players', fontsize=14, fontweight='bold', ha='center')

    # Central - APIs
    api_circle = mpatches.Circle((6.5, 5), 1.2, facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(api_circle)
    ax.text(6.5, 5.2, 'Open', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(6.5, 4.7, 'APIs', ha='center', fontsize=11, fontweight='bold', color='white')

    # Surrounding players
    players = [
        {'name': 'Banks\n(ASPSPs)', 'x': 2, 'y': 7.5, 'color': '#333333',
         'details': 'Provide APIs\nHold accounts'},
        {'name': 'FinTechs\n(TPPs)', 'x': 11, 'y': 7.5, 'color': '#44A044',
         'details': 'Build apps\nUse APIs'},
        {'name': 'Regulators', 'x': 2, 'y': 2.5, 'color': '#D62728',
         'details': 'Set rules\nEnforce compliance'},
        {'name': 'Consumers', 'x': 11, 'y': 2.5, 'color': '#6B5B95',
         'details': 'Control data\nBenefit from services'},
        {'name': 'Technology\nProviders', 'x': 6.5, 'y': 8.5, 'color': '#FF7F0E',
         'details': 'API platforms\nInfrastructure'},
        {'name': 'Standards\nBodies', 'x': 6.5, 'y': 1.5, 'color': '#999999',
         'details': 'Define specs\nEnsure interop'},
    ]

    for p in players:
        box = mpatches.FancyBboxPatch((p['x']-1.2, p['y']-0.8), 2.4, 1.6,
                                       boxstyle='round,pad=0.1',
                                       facecolor=p['color'], edgecolor='#333333', lw=2)
        ax.add_patch(box)
        ax.text(p['x'], p['y']+0.3, p['name'], ha='center', va='center',
               fontsize=9, fontweight='bold', color='white')
        ax.text(p['x'], p['y']-0.4, p['details'], ha='center', va='center',
               fontsize=7, color='white')

        # Connection to center
        ax.annotate('', xy=(6.5 + 1.2*(p['x']-6.5)/abs(p['x']-6.5+0.01) if abs(p['x']-6.5)>2 else p['x']/6.5,
                           5 + 1.2*(p['y']-5)/abs(p['y']-5+0.01) if abs(p['y']-5)>2 else 5),
                   xytext=(p['x'], p['y']),
                   arrowprops=dict(arrowstyle='-', color='#CCCCCC', lw=1.5, linestyle='--'))

    # Connect with lines to center
    ax.plot([6.5, 2], [6.2, 6.7], 'k--', lw=1, alpha=0.3)
    ax.plot([6.5, 11], [6.2, 6.7], 'k--', lw=1, alpha=0.3)
    ax.plot([6.5, 2], [3.8, 3.3], 'k--', lw=1, alpha=0.3)
    ax.plot([6.5, 11], [3.8, 3.3], 'k--', lw=1, alpha=0.3)
    ax.plot([6.5, 6.5], [6.2, 7.7], 'k--', lw=1, alpha=0.3)
    ax.plot([6.5, 6.5], [3.8, 2.3], 'k--', lw=1, alpha=0.3)

    # Key players examples
    examples = """Key Players by Category:
    Banks: JPMorgan, HSBC, Lloyds, BNP
    FinTechs: Plaid, TrueLayer, Tink, Yapily
    Tech: AWS, Google Cloud, MuleSoft
    Regulators: FCA (UK), EBA (EU), CFPB (US)
    Standards: Berlin Group, STET, OBIE"""

    ax.text(0.5, 0.3, examples, fontsize=7, va='bottom',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.98, 0.02, '[ECOSYSTEM MAP]',
            fontsize=7, ha='right', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'open_banking_ecosystem.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
