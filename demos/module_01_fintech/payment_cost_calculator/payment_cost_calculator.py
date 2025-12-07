"""
Cross-Border Payment Cost Calculator

Demonstrates the cost structure of different payment methods for cross-border transactions.
Shows how FinTech solutions (e.g., Wise, Revolut) compare to traditional banks.

Learning Objectives:
- Understand payment cost components (FX markup, transfer fees, intermediary fees)
- Compare traditional vs FinTech payment solutions
- Visualize total cost of ownership for different transaction sizes
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Cross-Border Payment Cost Comparison',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_BSc/tree/main/python_demos/module_01_fintech/payment_cost_calculator'
}


def calculate_traditional_bank_cost(amount, fx_markup=0.03, fixed_fee=25, swift_fee=15):
    """
    Calculate traditional bank transfer cost.

    Args:
        amount: Transfer amount in USD
        fx_markup: FX markup percentage (default 3%)
        fixed_fee: Fixed transfer fee
        swift_fee: SWIFT intermediary fee

    Returns:
        Total cost in USD
    """
    fx_cost = amount * fx_markup
    total_cost = fx_cost + fixed_fee + swift_fee
    return total_cost


def calculate_fintech_cost(amount, fx_markup=0.005, fixed_fee=3):
    """
    Calculate FinTech provider cost (e.g., Wise).

    Args:
        amount: Transfer amount in USD
        fx_markup: FX markup percentage (default 0.5%)
        fixed_fee: Fixed transfer fee

    Returns:
        Total cost in USD
    """
    fx_cost = amount * fx_markup
    total_cost = fx_cost + fixed_fee
    return total_cost


def calculate_crypto_cost(amount, network_fee=2, exchange_fee_pct=0.01):
    """
    Calculate cryptocurrency transfer cost.

    Args:
        amount: Transfer amount in USD
        network_fee: Blockchain network fee
        exchange_fee_pct: Exchange fee percentage (both ends)

    Returns:
        Total cost in USD
    """
    exchange_fees = amount * exchange_fee_pct * 2  # Buy and sell
    total_cost = exchange_fees + network_fee
    return total_cost


def create_comparison_chart():
    """Create comprehensive payment cost comparison visualization."""

    # Transaction amounts to compare
    amounts = np.array([100, 250, 500, 1000, 2500, 5000, 10000])

    # Calculate costs for each method
    trad_costs = np.array([calculate_traditional_bank_cost(amt) for amt in amounts])
    fintech_costs = np.array([calculate_fintech_cost(amt) for amt in amounts])
    crypto_costs = np.array([calculate_crypto_cost(amt) for amt in amounts])

    # Calculate cost as percentage of amount
    trad_pct = (trad_costs / amounts) * 100
    fintech_pct = (fintech_costs / amounts) * 100
    crypto_pct = (crypto_costs / amounts) * 100

    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Cross-Border Payment Cost Analysis', fontsize=10, fontweight='bold')

    # Grayscale colors
    colors = {'Traditional Bank': '0.2', 'FinTech': '0.5', 'Crypto': '0.7'}
    linestyles = {'Traditional Bank': '-', 'FinTech': '--', 'Crypto': ':'}

    # Plot 1: Absolute costs
    ax1 = axes[0, 0]
    ax1.plot(amounts, trad_costs, label='Traditional Bank',
             color=colors['Traditional Bank'], linestyle=linestyles['Traditional Bank'],
             linewidth=2, marker='o', markersize=4)
    ax1.plot(amounts, fintech_costs, label='FinTech',
             color=colors['FinTech'], linestyle=linestyles['FinTech'],
             linewidth=2, marker='s', markersize=4)
    ax1.plot(amounts, crypto_costs, label='Crypto',
             color=colors['Crypto'], linestyle=linestyles['Crypto'],
             linewidth=2, marker='^', markersize=4)
    ax1.set_xlabel('Transaction Amount (USD)', fontsize=8)
    ax1.set_ylabel('Total Cost (USD)', fontsize=8)
    ax1.set_title('Absolute Transaction Costs', fontsize=8, fontweight='bold')
    ax1.legend(fontsize=8, frameon=True, fancybox=False, edgecolor='black')
    ax1.grid(True, alpha=0.3, linestyle=':')
    ax1.tick_params(labelsize=8)

    # Plot 2: Percentage costs
    ax2 = axes[0, 1]
    ax2.plot(amounts, trad_pct, label='Traditional Bank',
             color=colors['Traditional Bank'], linestyle=linestyles['Traditional Bank'],
             linewidth=2, marker='o', markersize=4)
    ax2.plot(amounts, fintech_pct, label='FinTech',
             color=colors['FinTech'], linestyle=linestyles['FinTech'],
             linewidth=2, marker='s', markersize=4)
    ax2.plot(amounts, crypto_pct, label='Crypto',
             color=colors['Crypto'], linestyle=linestyles['Crypto'],
             linewidth=2, marker='^', markersize=4)
    ax2.set_xlabel('Transaction Amount (USD)', fontsize=8)
    ax2.set_ylabel('Cost as % of Amount', fontsize=8)
    ax2.set_title('Relative Transaction Costs', fontsize=8, fontweight='bold')
    ax2.legend(fontsize=8, frameon=True, fancybox=False, edgecolor='black')
    ax2.grid(True, alpha=0.3, linestyle=':')
    ax2.tick_params(labelsize=8)

    # Plot 3: Cost breakdown for $1000 transfer
    ax3 = axes[1, 0]
    transfer_amount = 1000

    # Traditional bank breakdown
    trad_fx = transfer_amount * 0.03
    trad_fixed = 25
    trad_swift = 15

    # FinTech breakdown
    fintech_fx = transfer_amount * 0.005
    fintech_fixed = 3

    # Crypto breakdown
    crypto_exchange = transfer_amount * 0.01 * 2
    crypto_network = 2

    categories = ['Traditional\nBank', 'FinTech', 'Crypto']
    fx_costs = [trad_fx, fintech_fx, crypto_exchange]
    fixed_costs = [trad_fixed + trad_swift, fintech_fixed, crypto_network]

    x_pos = np.arange(len(categories))
    width = 0.6

    bars1 = ax3.bar(x_pos, fx_costs, width, label='FX Markup/Exchange',
                    color='0.4', edgecolor='black', linewidth=0.5)
    bars2 = ax3.bar(x_pos, fixed_costs, width, bottom=fx_costs,
                    label='Fixed/Network Fees', color='0.7', edgecolor='black', linewidth=0.5)

    ax3.set_ylabel('Cost (USD)', fontsize=8)
    ax3.set_title('Cost Breakdown for $1,000 Transfer', fontsize=8, fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(categories, fontsize=8)
    ax3.legend(fontsize=8, frameon=True, fancybox=False, edgecolor='black')
    ax3.tick_params(labelsize=8)
    ax3.grid(True, alpha=0.3, linestyle=':', axis='y')

    # Add value labels on bars
    for i, (fx, fixed) in enumerate(zip(fx_costs, fixed_costs)):
        total = fx + fixed
        ax3.text(i, total + 1, f'${total:.2f}', ha='center', va='bottom', fontsize=7, fontweight='bold')

    # Plot 4: Savings comparison
    ax4 = axes[1, 1]
    savings_fintech = trad_costs - fintech_costs
    savings_crypto = trad_costs - crypto_costs

    x_pos = np.arange(len(amounts))
    width = 0.35

    bars1 = ax4.bar(x_pos - width/2, savings_fintech, width, label='FinTech vs Bank',
                    color='0.4', edgecolor='black', linewidth=0.5)
    bars2 = ax4.bar(x_pos + width/2, savings_crypto, width, label='Crypto vs Bank',
                    color='0.7', edgecolor='black', linewidth=0.5)

    ax4.set_xlabel('Transaction Amount (USD)', fontsize=8)
    ax4.set_ylabel('Savings (USD)', fontsize=8)
    ax4.set_title('Cost Savings vs Traditional Bank', fontsize=8, fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels([f'${amt}' for amt in amounts], fontsize=7, rotation=45, ha='right')
    ax4.legend(fontsize=8, frameon=True, fancybox=False, edgecolor='black')
    ax4.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax4.tick_params(labelsize=8)

    plt.tight_layout()

    # Save figure
    output_path = Path(__file__).parent / 'payment_cost.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    # Also save as PNG for QR code generation
    png_path = Path(__file__).parent / 'payment_cost.png'
    plt.savefig(png_path, dpi=150, bbox_inches='tight')

    plt.show()


def print_cost_table():
    """Print detailed cost comparison table."""
    amounts = [100, 500, 1000, 5000, 10000]

    print("\n" + "="*80)
    print("CROSS-BORDER PAYMENT COST COMPARISON TABLE")
    print("="*80)
    print(f"{'Amount':<12} {'Traditional Bank':<20} {'FinTech':<20} {'Crypto':<20}")
    print(f"{'(USD)':<12} {'Cost (% of amt)':<20} {'Cost (% of amt)':<20} {'Cost (% of amt)':<20}")
    print("-"*80)

    for amt in amounts:
        trad = calculate_traditional_bank_cost(amt)
        fintech = calculate_fintech_cost(amt)
        crypto = calculate_crypto_cost(amt)

        trad_pct = (trad / amt) * 100
        fintech_pct = (fintech / amt) * 100
        crypto_pct = (crypto / amt) * 100

        print(f"${amt:<11} ${trad:>6.2f} ({trad_pct:>5.2f}%)    "
              f"${fintech:>6.2f} ({fintech_pct:>5.2f}%)    "
              f"${crypto:>6.2f} ({crypto_pct:>5.2f}%)")

    print("="*80)
    print("\nKey Insights:")
    print("1. Traditional banks charge high fixed fees (SWIFT + transfer)")
    print("2. FinTech providers offer lower FX markups and minimal fixed fees")
    print("3. Crypto has flat network fees but exchange costs on both ends")
    print("4. For small amounts (<$500), FinTech is most cost-effective")
    print("5. For large amounts (>$5000), cost differences become less significant in %")
    print("="*80 + "\n")


if __name__ == "__main__":
    print("Cross-Border Payment Cost Calculator")
    print("=" * 50)
    print("\nThis demo compares costs across three payment methods:")
    print("1. Traditional Bank (high FX markup + SWIFT fees)")
    print("2. FinTech Provider (low FX markup + minimal fees)")
    print("3. Cryptocurrency (exchange fees + network fees)")
    print("\n")

    # Print cost table
    print_cost_table()

    # Create visualization
    print("\nGenerating cost comparison charts...")
    create_comparison_chart()

    print("\nDemo complete!")
