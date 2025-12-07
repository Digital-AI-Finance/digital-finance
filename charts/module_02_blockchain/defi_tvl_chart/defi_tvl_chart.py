"""
DeFi Total Value Locked (TVL) Over Time
Historical visualization of DeFi TVL growth by major protocols

Required libraries: matplotlib, numpy
Output: defi_tvl_chart.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'DeFi Total Value Locked (TVL) Over Time',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_02_blockchain/defi_tvl_chart'
}

def create_defi_tvl_chart():
    """Create visualization of DeFi TVL growth over time"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    # Set random seed for reproducibility
    np.random.seed(42)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

    # Generate synthetic time series data (monthly from 2019 to 2024)
    start_date = datetime(2019, 1, 1)
    months = 72  # 6 years
    dates = [start_date + timedelta(days=30*i) for i in range(months)]

    # Synthetic TVL data showing realistic DeFi growth pattern
    # Exponential growth with some volatility
    base_growth = np.linspace(0.5, 150, months)
    noise = np.random.normal(0, 5, months)

    # Add market events (crashes and recoveries)
    tvl_total = base_growth.copy()
    tvl_total[20:25] *= 0.7  # COVID crash 2020
    tvl_total[25:35] *= 1.8  # DeFi summer 2020-2021
    tvl_total[45:50] *= 0.5  # 2022 crypto winter
    tvl_total[50:] *= 1.3    # Recovery
    tvl_total += np.abs(noise)

    # Individual protocol data (stacked)
    protocols = {
        'Uniswap': tvl_total * 0.20,
        'Aave': tvl_total * 0.18,
        'MakerDAO': tvl_total * 0.15,
        'Curve': tvl_total * 0.12,
        'Lido': tvl_total * 0.10,
        'Others': tvl_total * 0.25
    }

    # Top panel: Stacked area chart
    colors = ['black', 'darkgray', 'gray', 'lightgray', 'whitesmoke', 'white']

    ax1.stackplot(dates, protocols.values(),
                 labels=protocols.keys(),
                 colors=colors,
                 edgecolor='black',
                 linewidth=0.3,
                 alpha=0.8)

    ax1.set_ylabel('Total Value Locked (Billion USD)', fontsize=8)
    ax1.set_title('DeFi Total Value Locked by Protocol [SYNTHETIC DATA]',
                 fontsize=10, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=7, ncol=2)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Add event annotations
    events = [
        (datetime(2020, 3, 1), 30, 'COVID-19\nCrash'),
        (datetime(2020, 9, 1), 85, 'DeFi Summer'),
        (datetime(2022, 5, 1), 65, 'Crypto Winter')
    ]

    for event_date, y_pos, label in events:
        ax1.annotate(label, xy=(event_date, y_pos),
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=6, ha='left',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                            edgecolor='black', linewidth=0.5),
                    arrowprops=dict(arrowstyle='->', lw=0.5))

    # Bottom panel: Growth rate
    growth_rate = np.zeros(months)
    growth_rate[1:] = (tvl_total[1:] - tvl_total[:-1]) / tvl_total[:-1] * 100

    ax2.bar(dates, growth_rate, width=25, color='gray',
           edgecolor='black', linewidth=0.5, alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)

    ax2.set_xlabel('Date', fontsize=8)
    ax2.set_ylabel('Month-over-Month Growth (%)', fontsize=8)
    ax2.set_title('DeFi TVL Growth Rate', fontsize=10, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, axis='y')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'defi_tvl_chart.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_defi_tvl_chart()
