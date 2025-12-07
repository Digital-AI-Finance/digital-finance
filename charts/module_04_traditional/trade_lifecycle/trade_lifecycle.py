"""
Trade Lifecycle Flowchart
Order to settlement workflow visualization

Required libraries: matplotlib, numpy
Output: trade_lifecycle.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Trade Lifecycle Flowchart',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_04_traditional/trade_lifecycle'
}

def create_trade_lifecycle():
    """Create a flowchart showing the trade lifecycle from order to settlement"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, ax = plt.subplots(figsize=(10, 9))

    # Define trade lifecycle stages
    stages = [
        {
            'name': 'Pre-Trade',
            'y': 8,
            'steps': [
                {'title': 'Order Creation', 'desc': 'Client/Portfolio Manager decides to trade'},
                {'title': 'Compliance Check', 'desc': 'Risk limits, regulatory compliance'},
                {'title': 'Order Routing', 'desc': 'Select execution venue and strategy'}
            ],
            'color': 'lightgray'
        },
        {
            'name': 'Trade Execution',
            'y': 5.5,
            'steps': [
                {'title': 'Order Matching', 'desc': 'Order book matching engine'},
                {'title': 'Trade Confirmation', 'desc': 'Both parties confirm trade details'},
                {'title': 'Trade Reporting', 'desc': 'Report to regulatory authorities'}
            ],
            'color': 'gray'
        },
        {
            'name': 'Post-Trade',
            'y': 3,
            'steps': [
                {'title': 'Clearing', 'desc': 'Central counterparty (CCP) novation'},
                {'title': 'Settlement', 'desc': 'Securities vs cash exchange (T+2)'},
                {'title': 'Reconciliation', 'desc': 'Confirm all records match'}
            ],
            'color': 'darkgray'
        }
    ]

    # Draw stages
    for stage_idx, stage in enumerate(stages):
        y_base = stage['y']

        # Stage header
        header_box = FancyBboxPatch((0.5, y_base + 0.8), 9, 0.5,
                                   boxstyle="round,pad=0.05",
                                   linewidth=2,
                                   edgecolor='black',
                                   facecolor=stage['color'])
        ax.add_patch(header_box)

        ax.text(5, y_base + 1.05, stage['name'],
               ha='center', va='center',
               fontsize=11, fontweight='bold')

        # Draw steps horizontally
        step_width = 2.8
        step_height = 1.0
        x_start = 0.8

        for step_idx, step in enumerate(stage['steps']):
            x = x_start + step_idx * (step_width + 0.2)
            y = y_base

            # Step box
            step_box = FancyBboxPatch((x, y - step_height), step_width, step_height,
                                     boxstyle="round,pad=0.05",
                                     linewidth=1.5,
                                     edgecolor='black',
                                     facecolor='white')
            ax.add_patch(step_box)

            # Step title
            ax.text(x + step_width/2, y - 0.25, step['title'],
                   ha='center', va='center',
                   fontsize=8, fontweight='bold')

            # Step description
            ax.text(x + step_width/2, y - 0.65, step['desc'],
                   ha='center', va='center',
                   fontsize=6, style='italic',
                   wrap=True)

            # Arrow to next step (within same stage)
            if step_idx < len(stage['steps']) - 1:
                arrow = FancyArrowPatch((x + step_width, y - step_height/2),
                                       (x + step_width + 0.2, y - step_height/2),
                                       arrowstyle='->,head_width=0.3,head_length=0.2',
                                       linewidth=1.5,
                                       color='black')
                ax.add_patch(arrow)

        # Arrow to next stage
        if stage_idx < len(stages) - 1:
            next_y = stages[stage_idx + 1]['y']
            arrow = FancyArrowPatch((5, y_base - step_height - 0.1),
                                   (5, next_y + 0.8),
                                   arrowstyle='->,head_width=0.4,head_length=0.3',
                                   linewidth=2,
                                   color='black')
            ax.add_patch(arrow)

            # Add timing label
            if stage_idx == 0:
                timing_text = 'Milliseconds to seconds'
            elif stage_idx == 1:
                timing_text = 'Minutes to hours'
            else:
                timing_text = ''

            if timing_text:
                ax.text(5.5, (y_base - step_height + next_y + 0.8) / 2,
                       timing_text,
                       ha='left', va='center',
                       fontsize=6, style='italic',
                       bbox=dict(boxstyle='round,pad=0.2',
                                facecolor='white',
                                edgecolor='gray',
                                linewidth=0.5))

    # Add side annotations for participants
    participants = [
        (0.2, 8.5, 'Participants:\n• Investor\n• Broker\n• Compliance'),
        (0.2, 6, 'Participants:\n• Exchange\n• Market Maker\n• Regulators'),
        (0.2, 3.5, 'Participants:\n• CCP\n• Custodian\n• Back Office')
    ]

    for x, y, text in participants:
        ax.text(x, y, text,
               ha='left', va='top',
               fontsize=6,
               bbox=dict(boxstyle='round,pad=0.3',
                        facecolor='white',
                        edgecolor='black',
                        linewidth=0.5))

    # Add timeline on the right
    timeline_data = [
        (9.5, 8.5, 'T-0\n(Order Time)', 'Pre-trade checks\nand routing'),
        (9.5, 6, 'T+0\n(Execution)', 'Trade occurs\non exchange'),
        (9.5, 3.5, 'T+2\n(Settlement)', 'Cash and securities\nexchange')
    ]

    for x, y, time, desc in timeline_data:
        ax.text(x, y, f'{time}\n\n{desc}',
               ha='left', va='top',
               fontsize=6,
               bbox=dict(boxstyle='round,pad=0.3',
                        facecolor='lightyellow',
                        edgecolor='black',
                        linewidth=0.5))

    # Key risks box
    risks_text = """
    Key Risks at Each Stage:
    • Pre-Trade: Compliance violations, market impact
    • Execution: Price slippage, partial fills, information leakage
    • Post-Trade: Settlement failures, operational errors, counterparty risk
    """

    ax.text(5, 0.5, risks_text,
           ha='center', va='center',
           fontsize=6,
           bbox=dict(boxstyle='round,pad=0.4',
                    facecolor='white',
                    edgecolor='red',
                    linewidth=1))

    # Title
    ax.text(5, 9.5, 'Trade Lifecycle: From Order to Settlement',
           ha='center', va='center',
           fontsize=12, fontweight='bold')

    # Set axis properties
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'trade_lifecycle.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_trade_lifecycle()
