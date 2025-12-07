"""
CBDC Landscape Visualization
Global CBDC status comparison and characteristics

Required libraries: matplotlib, numpy
Output: cbdc_landscape.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'CBDC Landscape Visualization',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_04_traditional/cbdc_landscape'
}

def create_cbdc_landscape():
    """Create visualization of global CBDC development status"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig = plt.figure(figsize=(10, 9))
    gs = fig.add_gridspec(3, 2, hspace=0.4, wspace=0.3,
                         height_ratios=[1, 1, 1])

    # CBDC status data (as of 2024)
    status_categories = {
        'Research': 45,
        'Proof of Concept': 28,
        'Pilot': 18,
        'Launched': 4,
        'Cancelled': 5
    }

    # Top left: CBDC Status Distribution
    ax1 = fig.add_subplot(gs[0, 0])

    categories = list(status_categories.keys())
    counts = list(status_categories.values())
    colors = ['white', 'lightgray', 'gray', 'darkgray', 'black']

    bars = ax1.barh(categories, counts, color=colors,
                   edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (bar, count) in enumerate(zip(bars, counts)):
        ax1.text(count + 1, i, f'{count}',
                va='center', fontsize=7)

    ax1.set_xlabel('Number of Countries', fontsize=8)
    ax1.set_title('Global CBDC Development Status (2024)', fontsize=10, fontweight='bold')
    ax1.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Top right: Notable CBDC Projects
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis('off')

    cbdc_projects = [
        ['Country', 'Name', 'Status', 'Type'],
        ['China', 'e-CNY', 'Pilot', 'Retail'],
        ['Bahamas', 'Sand Dollar', 'Launched', 'Retail'],
        ['Nigeria', 'eNaira', 'Launched', 'Retail'],
        ['Jamaica', 'JAM-DEX', 'Launched', 'Retail'],
        ['Sweden', 'e-Krona', 'Pilot', 'Retail'],
        ['Euro Area', 'Digital Euro', 'Research', 'Retail'],
        ['USA', 'Digital Dollar', 'Research', 'Retail/Wholesale'],
        ['UK', 'Digital Pound', 'Research', 'Retail']
    ]

    table = ax2.table(cellText=cbdc_projects,
                     cellLoc='left',
                     loc='center',
                     bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(6)

    # Style header
    for i in range(4):
        cell = table[(0, i)]
        cell.set_facecolor('darkgray')
        cell.set_text_props(weight='bold', color='black')

    # Style rows
    for i in range(1, len(cbdc_projects)):
        for j in range(4):
            cell = table[(i, j)]
            # Color by status
            if cbdc_projects[i][2] == 'Launched':
                cell.set_facecolor('darkgray')
            elif cbdc_projects[i][2] == 'Pilot':
                cell.set_facecolor('gray')
            else:
                cell.set_facecolor('lightgray')
            cell.set_edgecolor('black')
            cell.set_linewidth(0.5)

    ax2.set_title('Notable CBDC Projects', fontsize=10, fontweight='bold', pad=20)

    # Middle row: CBDC Architecture Types
    ax3 = fig.add_subplot(gs[1, :])

    # Create comparison diagram
    architectures = [
        {
            'name': 'Direct CBDC\n(Single-Tier)',
            'desc': 'Central bank manages\nall accounts',
            'pros': 'Full control\nSimple design',
            'cons': 'High operational burden\nPrivacy concerns',
            'x': 1.5
        },
        {
            'name': 'Indirect CBDC\n(Two-Tier)',
            'desc': 'Banks manage accounts\nCB manages reserves',
            'pros': 'Leverages existing infrastructure\nBanks handle KYC/AML',
            'cons': 'More complex\nBank dependency',
            'x': 5.0
        },
        {
            'name': 'Hybrid CBDC',
            'desc': 'Banks operate\nCB has direct access',
            'pros': 'Balance of control\nResilience',
            'cons': 'Most complex\nHigher costs',
            'x': 8.5
        }
    ]

    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 5)
    ax3.axis('off')

    for arch in architectures:
        # Architecture box
        from matplotlib.patches import FancyBboxPatch

        box = FancyBboxPatch((arch['x'] - 0.8, 3), 1.6, 0.6,
                            boxstyle="round,pad=0.05",
                            linewidth=1.5,
                            edgecolor='black',
                            facecolor='darkgray')
        ax3.add_patch(box)

        ax3.text(arch['x'], 3.3, arch['name'],
                ha='center', va='center',
                fontsize=7, fontweight='bold')

        # Description
        ax3.text(arch['x'], 2.3, arch['desc'],
                ha='center', va='center',
                fontsize=6,
                bbox=dict(boxstyle='round,pad=0.3',
                         facecolor='white',
                         edgecolor='black',
                         linewidth=0.5))

        # Pros
        ax3.text(arch['x'], 1.3, f"Pros:\n{arch['pros']}",
                ha='center', va='center',
                fontsize=5, color='darkgreen',
                bbox=dict(boxstyle='round,pad=0.2',
                         facecolor='white',
                         edgecolor='gray',
                         linewidth=0.5))

        # Cons
        ax3.text(arch['x'], 0.3, f"Cons:\n{arch['cons']}",
                ha='center', va='center',
                fontsize=5, color='darkred',
                bbox=dict(boxstyle='round,pad=0.2',
                         facecolor='white',
                         edgecolor='gray',
                         linewidth=0.5))

    ax3.text(5, 4.5, 'CBDC Architecture Models',
            ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Bottom left: Key Motivations
    ax4 = fig.add_subplot(gs[2, 0])

    motivations = [
        'Financial Inclusion',
        'Payment Efficiency',
        'Monetary Policy',
        'Reduce Cash Costs',
        'Counter Crypto',
        'Cross-Border Payments'
    ]

    # Synthetic importance scores
    importance = [85, 78, 72, 65, 58, 70]

    bars = ax4.barh(motivations, importance,
                   color=['darkgray', 'gray', 'lightgray', 'white',
                         'lightgray', 'gray'],
                   edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, importance)):
        ax4.text(val + 2, i, f'{val}%',
                va='center', fontsize=6)

    ax4.set_xlabel('Importance Score (%)', fontsize=8)
    ax4.set_title('Key Motivations for CBDC Development', fontsize=10, fontweight='bold')
    ax4.set_xlim(0, 100)
    ax4.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)

    # Bottom right: Key Challenges
    ax5 = fig.add_subplot(gs[2, 1])

    challenges = [
        'Privacy Concerns',
        'Cyber Security',
        'Technology Risk',
        'Bank Disintermediation',
        'Financial Stability',
        'Legal Framework'
    ]

    # Synthetic concern scores
    concern = [88, 85, 75, 72, 68, 80]

    bars = ax5.barh(challenges, concern,
                   color=['black', 'darkgray', 'gray', 'lightgray',
                         'white', 'gray'],
                   edgecolor='black', linewidth=0.8)

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, concern)):
        ax5.text(val + 2, i, f'{val}%',
                va='center', fontsize=6)

    ax5.set_xlabel('Concern Level (%)', fontsize=8)
    ax5.set_title('Key Challenges and Concerns', fontsize=10, fontweight='bold')
    ax5.set_xlim(0, 100)
    ax5.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)

    # Main title
    fig.suptitle('Central Bank Digital Currency (CBDC) Landscape',
                fontsize=12, fontweight='bold', y=0.98)

    # Add note
    note_text = 'Note: Status data represents 100 central banks surveyed. Scores are illustrative based on policy reports.'
    fig.text(0.5, 0.01, note_text,
            ha='center', fontsize=6, style='italic')

    # Save as PDF
    output_path = Path(__file__).parent / 'cbdc_landscape.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_cbdc_landscape()
