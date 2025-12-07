"""
Open Banking Architecture Diagram
Visualizes PSD2 actors and data flows in open banking
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Open Banking Architecture (PSD2)',
    'url': 'https://github.com/Digital-AI-Finance/BSc-DigitalFinance/tree/main/charts/module_01_fintech/open_banking_architecture'
}

def create_open_banking_architecture():
    """Create diagram of open banking architecture under PSD2"""

    fig, ax = plt.subplots(figsize=(11, 8))

    # Define main components with positions
    components = {
        # Top: User layer
        'Customer': {'pos': (5.5, 7), 'size': (1.8, 0.7), 'color': '0.75', 'text_color': 'black'},

        # Middle: TPPs
        'AISP\n(Account Info)': {'pos': (2, 5), 'size': (1.6, 0.7), 'color': '0.4', 'text_color': 'white'},
        'PISP\n(Payment Init.)': {'pos': (5.5, 5), 'size': (1.6, 0.7), 'color': '0.4', 'text_color': 'white'},
        'CBPII\n(Card Check)': {'pos': (9, 5), 'size': (1.6, 0.7), 'color': '0.4', 'text_color': 'white'},

        # Bottom left: API & Bank
        'Open Banking\nAPI': {'pos': (2, 2.5), 'size': (1.8, 0.7), 'color': '0.25', 'text_color': 'white'},
        'ASPSP\n(Bank)': {'pos': (2, 0.5), 'size': (1.8, 0.9), 'color': '0.5', 'text_color': 'white'},

        # Bottom right: Regulator
        'Regulator\n(Authority)': {'pos': (9, 2.5), 'size': (1.6, 0.7), 'color': '0.6', 'text_color': 'white'},
    }

    # Draw component boxes
    for component, props in components.items():
        x, y = props['pos']
        width, height = props['size']

        box = FancyBboxPatch((x - width/2, y - height/2),
                            width, height,
                            boxstyle="round,pad=0.08",
                            facecolor=props['color'],
                            edgecolor='black',
                            linewidth=1.5)
        ax.add_patch(box)

        ax.text(x, y, component, ha='center', va='center',
                fontsize=7, fontweight='bold',
                color=props['text_color'])

    # Define data flows
    flows = [
        # Customer to TPPs
        {'from': (5.5, 6.65), 'to': (2, 5.35), 'label': '1. Consent', 'style': '-', 'bend': 0.3},
        {'from': (5.5, 6.65), 'to': (5.5, 5.35), 'label': '1. Consent', 'style': '-', 'bend': 0},
        {'from': (5.5, 6.65), 'to': (9, 5.35), 'label': '1. Consent', 'style': '-', 'bend': -0.3},

        # TPPs to API
        {'from': (2, 4.65), 'to': (2, 2.85), 'label': '2. Request\nData', 'style': '-', 'bend': 0},
        {'from': (5.5, 4.65), 'to': (2.6, 2.8), 'label': '2. Payment\nInstruction', 'style': '-', 'bend': -0.2},
        {'from': (9, 4.65), 'to': (2.8, 2.75), 'label': '2. Check\nFunds', 'style': '-', 'bend': -0.4},

        # API to Bank
        {'from': (2, 2.15), 'to': (2, 0.95), 'label': '3. Query', 'style': '-', 'bend': 0},

        # Bank to API (response)
        {'from': (2.3, 0.95), 'to': (2.3, 2.15), 'label': '4. Response', 'style': '--', 'bend': 0},

        # API to TPPs (response)
        {'from': (2, 2.85), 'to': (2, 4.5), 'label': '5. Data', 'style': '--', 'bend': 0.15},
        {'from': (2.4, 2.75), 'to': (5.3, 4.55), 'label': '5. Confirm', 'style': '--', 'bend': 0.2},
        {'from': (2.6, 2.7), 'to': (8.7, 4.6), 'label': '5. Result', 'style': '--', 'bend': 0.35},

        # Regulator connections
        {'from': (9, 3.15), 'to': (3.5, 2.7), 'label': 'Register\n& Monitor', 'style': ':', 'bend': 0.15},
        {'from': (9, 3.15), 'to': (3.2, 5.2), 'label': 'License', 'style': ':', 'bend': 0.3},
    ]

    # Draw arrows
    for flow in flows:
        from_pos = flow['from']
        to_pos = flow['to']
        bend = flow['bend']

        if bend == 0:
            # Straight arrow
            arrow = FancyArrowPatch(from_pos, to_pos,
                                   arrowstyle='->', mutation_scale=12,
                                   linestyle=flow['style'], linewidth=1.2,
                                   color='black', zorder=2)
        else:
            # Curved arrow
            mid_x = (from_pos[0] + to_pos[0]) / 2 + bend
            mid_y = (from_pos[1] + to_pos[1]) / 2

            arrow = FancyArrowPatch(from_pos, to_pos,
                                   arrowstyle='->', mutation_scale=12,
                                   connectionstyle=f"arc3,rad={bend}",
                                   linestyle=flow['style'], linewidth=1.2,
                                   color='black', zorder=2)

        ax.add_patch(arrow)

        # Add label
        label_x = (from_pos[0] + to_pos[0]) / 2 + bend * 0.5
        label_y = (from_pos[1] + to_pos[1]) / 2
        ax.text(label_x, label_y, flow['label'], ha='center', va='center',
                fontsize=5.5, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor='none', alpha=0.8))

    # Add legend
    legend_elements = [
        mpatches.Patch(facecolor='0.75', edgecolor='black', label='Customer'),
        mpatches.Patch(facecolor='0.4', edgecolor='black', label='TPP (Third Party Provider)'),
        mpatches.Patch(facecolor='0.25', edgecolor='black', label='API Gateway'),
        mpatches.Patch(facecolor='0.5', edgecolor='black', label='ASPSP (Bank)'),
        mpatches.Patch(facecolor='0.6', edgecolor='black', label='Regulator'),
    ]
    ax.legend(handles=legend_elements, loc='lower center', ncol=3,
              fontsize=6, framealpha=0.95, edgecolor='0.5',
              bbox_to_anchor=(0.5, -0.05))

    # Annotations for acronyms
    ax.text(10.8, 7.5, 'AISP: Account Information Service Provider\nPISP: Payment Initiation Service Provider\nCBPII: Card-Based Payment Instrument Issuer\nASPSP: Account Servicing Payment Service Provider',
            fontsize=5.5, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='0.95', edgecolor='0.5', linewidth=0.8))

    # Set axis properties
    ax.set_xlim(0, 13)
    ax.set_ylim(-0.3, 8)
    ax.axis('off')

    plt.title('Open Banking Architecture (PSD2)', fontsize=10, fontweight='bold', pad=15)

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'open_banking_architecture.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_open_banking_architecture()
