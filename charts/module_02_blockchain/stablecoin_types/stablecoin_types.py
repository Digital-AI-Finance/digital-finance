"""
Stablecoin Classification Diagram
Visual taxonomy of different stablecoin types and mechanisms

Required libraries: matplotlib, numpy
Output: stablecoin_types.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Stablecoin Classification Diagram',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_02_blockchain/stablecoin_types'
}

def create_stablecoin_classification():
    """Create a classification diagram of stablecoin types"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, ax = plt.subplots(figsize=(10, 8))

    # Stablecoin categories
    categories = {
        'Fiat-Collateralized': {
            'y': 6.5,
            'examples': ['USDT (Tether)', 'USDC (Circle)', 'BUSD (Binance)'],
            'mechanism': 'Backed 1:1 by fiat currency reserves',
            'advantages': 'Simple, stable, liquid',
            'risks': 'Centralized, requires trust, regulatory'
        },
        'Crypto-Collateralized': {
            'y': 4.5,
            'examples': ['DAI (MakerDAO)', 'sUSD (Synthetix)'],
            'mechanism': 'Over-collateralized by crypto assets',
            'advantages': 'Decentralized, transparent',
            'risks': 'Capital inefficient, liquidation risk'
        },
        'Algorithmic': {
            'y': 2.5,
            'examples': ['FRAX (Fractional)', 'UST (Terra) - Failed'],
            'mechanism': 'Algorithm adjusts supply/demand',
            'advantages': 'Capital efficient, decentralized',
            'risks': 'Death spiral risk, complex'
        },
        'Commodity-Backed': {
            'y': 0.5,
            'examples': ['PAXG (Gold)', 'DGX (Gold)'],
            'mechanism': 'Backed by physical commodities',
            'advantages': 'Real asset backing, hedge',
            'risks': 'Storage costs, centralized custody'
        }
    }

    # Draw category boxes
    for category, data in categories.items():
        y = data['y']

        # Main category box
        main_box = FancyBboxPatch((0.5, y), 2.5, 0.6,
                                 boxstyle="round,pad=0.05",
                                 linewidth=1.5,
                                 edgecolor='black',
                                 facecolor='darkgray')
        ax.add_patch(main_box)

        # Category name
        ax.text(1.75, y + 0.3, category,
               ha='center', va='center',
               fontsize=9, fontweight='bold')

        # Mechanism box
        mech_box = Rectangle((3.5, y), 3.0, 0.6,
                            linewidth=1,
                            edgecolor='black',
                            facecolor='lightgray')
        ax.add_patch(mech_box)

        ax.text(5.0, y + 0.3, data['mechanism'],
               ha='center', va='center',
               fontsize=7)

        # Examples box
        examples_box = Rectangle((7.0, y), 2.5, 0.6,
                                linewidth=1,
                                edgecolor='black',
                                facecolor='white')
        ax.add_patch(examples_box)

        examples_text = '\n'.join(data['examples'])
        ax.text(8.25, y + 0.3, examples_text,
               ha='center', va='center',
               fontsize=6)

        # Advantages/Risks boxes
        adv_box = Rectangle((0.5, y - 0.5), 4.0, 0.4,
                           linewidth=0.5,
                           edgecolor='gray',
                           facecolor='white',
                           linestyle='--')
        ax.add_patch(adv_box)

        ax.text(0.7, y - 0.3, f"+ {data['advantages']}",
               ha='left', va='center',
               fontsize=6, color='darkgreen')

        risk_box = Rectangle((5.0, y - 0.5), 4.5, 0.4,
                            linewidth=0.5,
                            edgecolor='gray',
                            facecolor='white',
                            linestyle='--')
        ax.add_patch(risk_box)

        ax.text(5.2, y - 0.3, f"- {data['risks']}",
               ha='left', va='center',
               fontsize=6, color='darkred')

    # Column headers
    headers = [
        (1.75, 7.5, 'Type'),
        (5.0, 7.5, 'Mechanism'),
        (8.25, 7.5, 'Examples')
    ]

    for x, y, text in headers:
        ax.text(x, y, text,
               ha='center', va='center',
               fontsize=9, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3',
                        facecolor='white',
                        edgecolor='black',
                        linewidth=1))

    # Title
    ax.text(5.0, 8.2, 'Stablecoin Classification and Characteristics',
           ha='center', va='center',
           fontsize=12, fontweight='bold')

    # Legend for advantages/risks
    ax.text(0.5, -0.8, '+ Advantages',
           ha='left', va='center',
           fontsize=7, color='darkgreen', fontweight='bold')

    ax.text(5.0, -0.8, '- Risks',
           ha='left', va='center',
           fontsize=7, color='darkred', fontweight='bold')

    # Set axis limits and properties
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.2, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'stablecoin_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_stablecoin_classification()
