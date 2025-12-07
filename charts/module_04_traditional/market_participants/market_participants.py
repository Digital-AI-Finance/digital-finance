"""
Market Participants Diagram
Buy-side vs Sell-side visualization in financial markets

Required libraries: matplotlib, numpy
Output: market_participants.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Market Participants Diagram',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_04_traditional/market_participants'
}

def create_market_participants():
    """Create a diagram showing buy-side and sell-side market participants"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, ax = plt.subplots(figsize=(10, 8))

    # Define buy-side participants
    buy_side = {
        'title': 'BUY-SIDE',
        'subtitle': 'Asset Owners & Managers',
        'y_start': 5,
        'participants': [
            {'name': 'Institutional Investors', 'examples': 'Pension Funds, Insurance Companies'},
            {'name': 'Asset Managers', 'examples': 'Mutual Funds, ETFs'},
            {'name': 'Hedge Funds', 'examples': 'Alternative Investment Strategies'},
            {'name': 'Private Equity', 'examples': 'Buyout Funds, Venture Capital'},
            {'name': 'Retail Investors', 'examples': 'Individual Investors'}
        ]
    }

    # Define sell-side participants
    sell_side = {
        'title': 'SELL-SIDE',
        'subtitle': 'Intermediaries & Service Providers',
        'y_start': 5,
        'participants': [
            {'name': 'Investment Banks', 'examples': 'Capital Raising, M&A Advisory'},
            {'name': 'Broker-Dealers', 'examples': 'Trade Execution, Market Making'},
            {'name': 'Prime Brokers', 'examples': 'Clearing, Financing, Custody'},
            {'name': 'Trading Venues', 'examples': 'Stock Exchanges, ECNs, MTFs'},
            {'name': 'Research Providers', 'examples': 'Equity Research, Analytics'}
        ]
    }

    # Draw buy-side (left)
    x_buy = 1
    y = buy_side['y_start']

    # Buy-side header
    header_box = FancyBboxPatch((x_buy - 0.4, y + 0.2), 3, 0.6,
                               boxstyle="round,pad=0.05",
                               linewidth=2,
                               edgecolor='black',
                               facecolor='darkgray')
    ax.add_patch(header_box)

    ax.text(x_buy + 1.1, y + 0.5, buy_side['title'],
           ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(x_buy + 1.1, y + 0.3, buy_side['subtitle'],
           ha='center', va='center',
           fontsize=7, style='italic')

    # Buy-side participants
    y_offset = y - 0.3
    for i, participant in enumerate(buy_side['participants']):
        y_pos = y_offset - i * 0.8

        # Participant box
        part_box = Rectangle((x_buy - 0.3, y_pos - 0.3), 2.8, 0.5,
                            linewidth=1,
                            edgecolor='black',
                            facecolor='lightgray' if i % 2 == 0 else 'white')
        ax.add_patch(part_box)

        # Participant name
        ax.text(x_buy, y_pos, participant['name'],
               ha='left', va='center',
               fontsize=8, fontweight='bold')

        # Examples
        ax.text(x_buy, y_pos - 0.15, participant['examples'],
               ha='left', va='center',
               fontsize=6, style='italic', color='gray')

    # Draw sell-side (right)
    x_sell = 6.5
    y = sell_side['y_start']

    # Sell-side header
    header_box = FancyBboxPatch((x_sell - 0.4, y + 0.2), 3, 0.6,
                               boxstyle="round,pad=0.05",
                               linewidth=2,
                               edgecolor='black',
                               facecolor='darkgray')
    ax.add_patch(header_box)

    ax.text(x_sell + 1.1, y + 0.5, sell_side['title'],
           ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(x_sell + 1.1, y + 0.3, sell_side['subtitle'],
           ha='center', va='center',
           fontsize=7, style='italic')

    # Sell-side participants
    y_offset = y - 0.3
    for i, participant in enumerate(sell_side['participants']):
        y_pos = y_offset - i * 0.8

        # Participant box
        part_box = Rectangle((x_sell - 0.3, y_pos - 0.3), 2.8, 0.5,
                            linewidth=1,
                            edgecolor='black',
                            facecolor='lightgray' if i % 2 == 0 else 'white')
        ax.add_patch(part_box)

        # Participant name
        ax.text(x_sell, y_pos, participant['name'],
               ha='left', va='center',
               fontsize=8, fontweight='bold')

        # Examples
        ax.text(x_sell, y_pos - 0.15, participant['examples'],
               ha='left', va='center',
               fontsize=6, style='italic', color='gray')

    # Draw interaction arrows in the middle
    arrow_y_positions = [4.2, 3.0, 1.8]

    for i, y_arrow in enumerate(arrow_y_positions):
        # Buy-side to Sell-side
        arrow1 = FancyArrowPatch((x_buy + 2.5, y_arrow + 0.1),
                                (x_sell - 0.5, y_arrow + 0.1),
                                arrowstyle='->,head_width=0.3,head_length=0.3',
                                linewidth=1.5,
                                color='black')
        ax.add_patch(arrow1)

        # Sell-side to Buy-side
        arrow2 = FancyArrowPatch((x_sell - 0.5, y_arrow - 0.1),
                                (x_buy + 2.5, y_arrow - 0.1),
                                arrowstyle='->,head_width=0.3,head_length=0.3',
                                linewidth=1.5,
                                color='gray')
        ax.add_patch(arrow2)

    # Add interaction labels
    interactions = [
        (4.75, 4.4, 'Orders'),
        (4.75, 4.0, 'Execution\n& Services'),
        (4.75, 3.2, 'Research'),
        (4.75, 2.8, 'Analysis'),
        (4.75, 2.0, 'Liquidity'),
        (4.75, 1.6, 'Market Access')
    ]

    for x, y, label in interactions:
        ax.text(x, y, label,
               ha='center', va='center',
               fontsize=6,
               bbox=dict(boxstyle='round,pad=0.2',
                        facecolor='white',
                        edgecolor='gray',
                        linewidth=0.5))

    # Add key characteristics boxes
    buy_char = "• Capital allocation\n• Investment decisions\n• Risk management\n• Portfolio optimization"
    sell_char = "• Facilitate trading\n• Provide liquidity\n• Advisory services\n• Price discovery"

    ax.text(x_buy + 1.1, 0.3, buy_char,
           ha='center', va='top',
           fontsize=6,
           bbox=dict(boxstyle='round,pad=0.3',
                    facecolor='white',
                    edgecolor='black',
                    linewidth=0.5))

    ax.text(x_sell + 1.1, 0.3, sell_char,
           ha='center', va='top',
           fontsize=6,
           bbox=dict(boxstyle='round,pad=0.3',
                    facecolor='white',
                    edgecolor='black',
                    linewidth=0.5))

    # Title
    ax.text(5.0, 6.5, 'Financial Market Participants: Buy-Side vs Sell-Side',
           ha='center', va='center',
           fontsize=12, fontweight='bold')

    # Set axis properties
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'market_participants.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_market_participants()
