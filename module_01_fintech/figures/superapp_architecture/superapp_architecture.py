"""
Super App Architecture Diagram
Shows the layered architecture of financial super apps (WeChat, Alipay model)

Output: superapp_architecture.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Super App Architecture',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/superapp_architecture'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create super app architecture diagram"""
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Layer colors
    colors = {
        'user': '#4A90E2',
        'services': '#44A044',
        'mini': '#FF7F0E',
        'platform': '#6B5B95',
        'data': '#D62728',
    }

    # Layer 1: User Interface
    rect1 = mpatches.FancyBboxPatch((0.5, 7.5), 10, 1, boxstyle="round,pad=0.05",
                                     facecolor=colors['user'], alpha=0.8)
    ax.add_patch(rect1)
    ax.text(5.5, 8, 'USER INTERFACE LAYER', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')
    ax.text(5.5, 7.65, 'Single App Entry | Unified Experience | Personalization',
           ha='center', va='center', fontsize=8, color='white')

    # Layer 2: Core Services
    rect2 = mpatches.FancyBboxPatch((0.5, 5.8), 10, 1.5, boxstyle="round,pad=0.05",
                                     facecolor=colors['services'], alpha=0.8)
    ax.add_patch(rect2)
    ax.text(5.5, 6.9, 'CORE SERVICES', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    services = ['Payments', 'Messaging', 'Social', 'E-commerce', 'Finance']
    for i, svc in enumerate(services):
        x = 1.5 + i * 2
        ax.text(x, 6.2, svc, ha='center', va='center', fontsize=9,
               color='white', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='#2E7D32', edgecolor='white', lw=0.5))

    # Layer 3: Mini Programs
    rect3 = mpatches.FancyBboxPatch((0.5, 4), 10, 1.5, boxstyle="round,pad=0.05",
                                     facecolor=colors['mini'], alpha=0.8)
    ax.add_patch(rect3)
    ax.text(5.5, 5.1, 'MINI PROGRAMS ECOSYSTEM', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    minis = ['Food\nDelivery', 'Ride\nHailing', 'Travel', 'Gaming', 'Utilities',
             'Insurance', 'Investments']
    for i, mini in enumerate(minis):
        x = 1 + i * 1.4
        ax.text(x, 4.4, mini, ha='center', va='center', fontsize=7,
               color='#333333', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#CC6600', lw=0.5))

    # Layer 4: Platform Services
    rect4 = mpatches.FancyBboxPatch((0.5, 2.2), 10, 1.5, boxstyle="round,pad=0.05",
                                     facecolor=colors['platform'], alpha=0.8)
    ax.add_patch(rect4)
    ax.text(5.5, 3.3, 'PLATFORM SERVICES', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')

    platforms = ['Identity\nVerification', 'Payment\nProcessing', 'Credit\nScoring',
                'Merchant\nTools', 'API\nGateway']
    for i, plat in enumerate(platforms):
        x = 1.5 + i * 2
        ax.text(x, 2.6, plat, ha='center', va='center', fontsize=8,
               color='white')

    # Layer 5: Data & AI
    rect5 = mpatches.FancyBboxPatch((0.5, 0.7), 10, 1.3, boxstyle="round,pad=0.05",
                                     facecolor=colors['data'], alpha=0.8)
    ax.add_patch(rect5)
    ax.text(5.5, 1.6, 'DATA & AI LAYER', ha='center', va='center',
           fontsize=11, fontweight='bold', color='white')
    ax.text(5.5, 1.0, 'User Behavior | Transaction History | Risk Models | Recommendations',
           ha='center', va='center', fontsize=8, color='white')

    # Title
    ax.text(5.5, 8.8, 'Financial Super App Architecture',
           fontsize=14, fontweight='bold', ha='center')

    # Examples
    ax.text(0.3, 0.2, 'Examples: WeChat, Alipay, Grab, Gojek, PayTM',
           fontsize=8, color='#666666', style='italic')

    # Synthetic label
    ax.text(10.7, 0.2, '[ILLUSTRATIVE]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'superapp_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
