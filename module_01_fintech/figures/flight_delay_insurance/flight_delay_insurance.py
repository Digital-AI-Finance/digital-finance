"""
Flight Delay Insurance
Shows automated flight delay insurance flow

Output: flight_delay_insurance.pdf
Module: module_01_fintech
Lesson: 9 - InsurTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Flight Delay Insurance',
    'module': 'module_01_fintech',
    'lesson': 9,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/flight_delay_insurance'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create flight delay insurance flow diagram"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Automated Flight Delay Insurance', fontsize=20, fontweight='bold', ha='center')
    ax.text(7, 8.7, 'Example: Revolut Travel Insurance', fontsize=13, ha='center', color='#666666')

    # Process flow
    steps = [
        {'name': '1. Book\nFlight', 'x': 1.5, 'y': 6, 'color': '#4A90E2',
         'desc': 'Via app with\ninsurance add-on'},
        {'name': '2. Auto\nMonitor', 'x': 4.3, 'y': 6, 'color': '#44A044',
         'desc': 'Real-time\nflight tracking'},
        {'name': '3. Delay\nDetected', 'x': 7.1, 'y': 6, 'color': '#FF7F0E',
         'desc': '2+ hour delay\nauto-triggered'},
        {'name': '4. Instant\nPayout', 'x': 9.9, 'y': 6, 'color': '#6B5B95',
         'desc': 'Money to\naccount instantly'},
        {'name': '5. Spend at\nAirport', 'x': 12.7, 'y': 6, 'color': '#D62728',
         'desc': 'Use card\nimmediately'},
    ]

    # Draw flow arrows
    for i in range(len(steps)-1):
        ax.annotate('', xy=(steps[i+1]['x']-0.9, 6), xytext=(steps[i]['x']+0.9, 6),
                   arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    for step in steps:
        # Step box
        box = mpatches.FancyBboxPatch((step['x']-1, step['y']-1.5), 2, 3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=step['color'], alpha=0.2,
                                       edgecolor=step['color'], lw=2)
        ax.add_patch(box)
        ax.text(step['x'], step['y']+1, step['name'], ha='center', va='center',
               fontsize=12, fontweight='bold', color=step['color'])
        ax.text(step['x'], step['y']-0.5, step['desc'], ha='center', va='center', fontsize=10)

    # Key features
    features = """Key Features:
    - No claim filing required
    - Payout within minutes of delay
    - Tiered payouts: 2hr=$50, 4hr=$100, 6hr+=$200
    - Data from FlightAware/Cirium APIs
    - Blockchain smart contracts (some providers)"""

    ax.text(4, 2.2, features, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Providers
    providers = """Providers:
    - Revolut
    - Blink Parametric
    - AXA (Fizzy - discontinued)
    - Etherisc (blockchain)
    - Kolibri (API)"""

    ax.text(10, 2.2, providers, ha='center', fontsize=11, va='top',
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Revolut, Blink Parametric product documentation (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'flight_delay_insurance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
