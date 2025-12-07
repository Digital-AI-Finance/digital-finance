"""
Fintech Ecosystem Map
Visualizes the major categories and subcategories of fintech services
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
import numpy as np

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Fintech Ecosystem Map',
    'url': 'https://github.com/Digital-AI-Finance/BSc-DigitalFinance/tree/main/charts/module_01_fintech/fintech_ecosystem'
}

def create_fintech_ecosystem_map():
    """Create a visual map of fintech categories"""

    fig, ax = plt.subplots(figsize=(10, 8))

    # Define fintech categories with subcategories
    categories = {
        'Payments': ['Digital Wallets', 'P2P Transfers', 'Remittances', 'Cryptocurrencies'],
        'Lending': ['P2P Lending', 'Crowdfunding', 'Invoice Financing', 'Student Loans'],
        'Banking': ['Neobanks', 'Challenger Banks', 'BaaS', 'Open Banking'],
        'Investment': ['Robo-Advisors', 'Social Trading', 'Micro-Investing', 'ETF Platforms'],
        'Insurance': ['Insurtech', 'P2P Insurance', 'Usage-Based', 'Claims Automation'],
        'RegTech': ['KYC/AML', 'Compliance', 'Risk Management', 'Reporting']
    }

    # Layout parameters
    n_categories = len(categories)
    angles = np.linspace(0, 2*np.pi, n_categories, endpoint=False)

    # Position for central hub
    center_x, center_y = 0.5, 0.5
    hub_radius = 0.08
    spoke_length = 0.28

    # Colors (grayscale-friendly)
    colors = ['0.2', '0.35', '0.5', '0.65', '0.75', '0.85']

    # Draw central hub
    central_circle = mpatches.Circle((center_x, center_y), hub_radius,
                                     facecolor='0.3', edgecolor='black',
                                     linewidth=2, zorder=10)
    ax.add_patch(central_circle)
    ax.text(center_x, center_y, 'FINTECH\nECOSYSTEM',
            ha='center', va='center', fontsize=8, fontweight='bold',
            color='white', zorder=11)

    # Draw categories as nodes around the center
    for idx, (category, subcats) in enumerate(categories.items()):
        angle = angles[idx]

        # Calculate position
        node_x = center_x + (hub_radius + spoke_length) * np.cos(angle)
        node_y = center_y + (hub_radius + spoke_length) * np.sin(angle)

        # Draw spoke line
        spoke_start_x = center_x + hub_radius * np.cos(angle)
        spoke_start_y = center_y + hub_radius * np.sin(angle)
        ax.plot([spoke_start_x, node_x], [spoke_start_y, node_y],
                'k-', linewidth=1.5, zorder=1)

        # Draw category node
        node_radius = 0.065
        category_circle = mpatches.Circle((node_x, node_y), node_radius,
                                         facecolor=colors[idx],
                                         edgecolor='black', linewidth=1.5, zorder=5)
        ax.add_patch(category_circle)
        ax.text(node_x, node_y, category, ha='center', va='center',
                fontsize=7, fontweight='bold', zorder=6)

        # Draw subcategories
        n_subcats = len(subcats)
        subcat_angles = np.linspace(angle - np.pi/6, angle + np.pi/6, n_subcats)

        for sub_idx, (subcat, sub_angle) in enumerate(zip(subcats, subcat_angles)):
            # Position subcategory further out
            subcat_dist = spoke_length + 0.15
            subcat_x = center_x + subcat_dist * np.cos(sub_angle)
            subcat_y = center_y + subcat_dist * np.sin(sub_angle)

            # Draw connecting line
            ax.plot([node_x, subcat_x], [node_y, subcat_y],
                    'k-', linewidth=0.5, alpha=0.5, zorder=1)

            # Draw subcategory box
            box_width = 0.08
            box_height = 0.04
            rect = mpatches.Rectangle((subcat_x - box_width/2, subcat_y - box_height/2),
                                     box_width, box_height,
                                     facecolor='white', edgecolor='0.4',
                                     linewidth=0.8, zorder=3)
            ax.add_patch(rect)
            ax.text(subcat_x, subcat_y, subcat, ha='center', va='center',
                    fontsize=6, zorder=4)

    # Set axis properties
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.title('Fintech Ecosystem Map', fontsize=10, fontweight='bold', pad=15)

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'fintech_ecosystem_map.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_fintech_ecosystem_map()
