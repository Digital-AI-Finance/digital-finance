"""
Card Payment Flow Diagram
Visualizes the lifecycle of a card payment transaction
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Card Payment Flow Diagram',
    'url': 'https://github.com/Digital-AI-Finance/BSc-DigitalFinance/tree/main/charts/module_01_fintech/payment_flow'
}

def create_payment_flow_diagram():
    """Create a diagram showing card payment lifecycle"""

    fig, ax = plt.subplots(figsize=(11, 7))

    # Define actors and their positions
    actors = {
        'Cardholder': (0.5, 5.5),
        'Merchant': (2.5, 5.5),
        'Acquirer': (4.5, 5.5),
        'Card Network': (6.5, 5.5),
        'Issuer': (8.5, 5.5)
    }

    # Draw actor boxes
    box_width = 1.5
    box_height = 0.6
    for actor, (x, y) in actors.items():
        # Determine shading
        if actor == 'Cardholder':
            color = '0.85'
        elif actor == 'Merchant':
            color = '0.75'
        elif actor in ['Acquirer', 'Issuer']:
            color = '0.5'
        else:
            color = '0.35'

        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='black',
                             linewidth=1.5)
        ax.add_patch(box)

        text_color = 'white' if color in ['0.35', '0.5'] else 'black'
        ax.text(x, y, actor, ha='center', va='center',
                fontsize=8, fontweight='bold', color=text_color)

    # Define payment flow steps
    steps = [
        # Step 1: Authorization Request
        {'from': 'Cardholder', 'to': 'Merchant', 'y': 4.8, 'label': '1. Presents Card', 'style': '-'},
        {'from': 'Merchant', 'to': 'Acquirer', 'y': 4.3, 'label': '2. Auth Request', 'style': '-'},
        {'from': 'Acquirer', 'to': 'Card Network', 'y': 3.8, 'label': '3. Routes Request', 'style': '-'},
        {'from': 'Card Network', 'to': 'Issuer', 'y': 3.3, 'label': '4. Verifies', 'style': '-'},

        # Step 2: Authorization Response
        {'from': 'Issuer', 'to': 'Card Network', 'y': 2.8, 'label': '5. Approve/Decline', 'style': '--'},
        {'from': 'Card Network', 'to': 'Acquirer', 'y': 2.3, 'label': '6. Response', 'style': '--'},
        {'from': 'Acquirer', 'to': 'Merchant', 'y': 1.8, 'label': '7. Authorization', 'style': '--'},
        {'from': 'Merchant', 'to': 'Cardholder', 'y': 1.3, 'label': '8. Confirmation', 'style': '--'},

        # Step 3: Clearing & Settlement
        {'from': 'Merchant', 'to': 'Acquirer', 'y': 0.6, 'label': '9. Batch Clearing', 'style': ':'},
        {'from': 'Acquirer', 'to': 'Card Network', 'y': 0.3, 'label': '10. Settlement', 'style': ':'},
        {'from': 'Card Network', 'to': 'Issuer', 'y': 0.0, 'label': '11. Transfer Funds', 'style': ':'},
    ]

    # Draw flow arrows
    for step in steps:
        from_x = actors[step['from']][0]
        to_x = actors[step['to']][0]
        y = step['y']

        # Determine arrow direction
        if from_x < to_x:
            arrow_start = from_x + box_width/2 + 0.1
            arrow_end = to_x - box_width/2 - 0.1
        else:
            arrow_start = from_x - box_width/2 - 0.1
            arrow_end = to_x + box_width/2 + 0.1

        # Draw arrow
        arrow = FancyArrowPatch((arrow_start, y), (arrow_end, y),
                               arrowstyle='->', mutation_scale=15,
                               linestyle=step['style'], linewidth=1.2,
                               color='black', zorder=2)
        ax.add_patch(arrow)

        # Add label
        label_x = (arrow_start + arrow_end) / 2
        label_y = y + 0.15
        ax.text(label_x, label_y, step['label'], ha='center', va='bottom',
                fontsize=6, style='italic')

    # Add phase labels on the left
    ax.text(-0.3, 4.0, 'AUTHORIZATION', rotation=90, ha='center', va='center',
            fontsize=7, fontweight='bold', color='0.3')
    ax.text(-0.3, 1.5, 'RESPONSE', rotation=90, ha='center', va='center',
            fontsize=7, fontweight='bold', color='0.3')
    ax.text(-0.3, 0.3, 'SETTLEMENT', rotation=90, ha='center', va='center',
            fontsize=7, fontweight='bold', color='0.3')

    # Add horizontal dividers
    ax.axhline(y=1.0, xmin=0.05, xmax=0.95, color='0.6', linewidth=0.8, linestyle='-', alpha=0.5)
    ax.axhline(y=2.5, xmin=0.05, xmax=0.95, color='0.6', linewidth=0.8, linestyle='-', alpha=0.5)

    # Set axis properties
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 6.5)
    ax.axis('off')

    plt.title('Card Payment Transaction Lifecycle', fontsize=10, fontweight='bold', pad=15)

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'payment_flow_diagram.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_payment_flow_diagram()
