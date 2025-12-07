"""
Neobank Fee Structure Comparison

Compares fee structures across traditional banks and neobanks (digital-only banks).
Demonstrates how neobanks leverage technology to offer lower fees.

Learning Objectives:
- Understand different banking fee models
- Compare cost structures: traditional vs digital banks
- Visualize total cost of banking for different user profiles
- Analyze the business model of neobanks
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Neobank vs Traditional Bank Fee Comparison',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_BSc/tree/main/python_demos/module_01_fintech/neobank_fee_comparison'
}


class BankFeeStructure:
    """Represents fee structure for a bank."""

    def __init__(self, name, monthly_fee, atm_fee_domestic, atm_fee_international,
                 fx_markup, overdraft_fee, card_replacement_fee, account_statement_fee):
        self.name = name
        self.monthly_fee = monthly_fee
        self.atm_fee_domestic = atm_fee_domestic
        self.atm_fee_international = atm_fee_international
        self.fx_markup = fx_markup  # percentage
        self.overdraft_fee = overdraft_fee  # per transaction
        self.card_replacement_fee = card_replacement_fee
        self.account_statement_fee = account_statement_fee  # per statement

    def calculate_annual_cost(self, usage_profile):
        """
        Calculate annual cost based on usage profile.

        Args:
            usage_profile: dict with keys:
                - atm_domestic: number of domestic ATM withdrawals per year
                - atm_international: number of international ATM withdrawals per year
                - fx_transactions: number of foreign currency transactions per year
                - fx_amount: average amount per FX transaction
                - overdrafts: number of overdraft transactions per year
                - card_replacements: number of card replacements per year
                - statements: number of paper statements per year

        Returns:
            Total annual cost in CHF
        """
        cost = 0

        # Monthly account fee
        cost += self.monthly_fee * 12

        # ATM fees
        cost += usage_profile['atm_domestic'] * self.atm_fee_domestic
        cost += usage_profile['atm_international'] * self.atm_fee_international

        # FX transaction costs
        fx_total = usage_profile['fx_transactions'] * usage_profile['fx_amount']
        cost += fx_total * (self.fx_markup / 100)

        # Overdraft fees
        cost += usage_profile['overdrafts'] * self.overdraft_fee

        # Card replacement
        cost += usage_profile['card_replacements'] * self.card_replacement_fee

        # Account statements
        cost += usage_profile['statements'] * self.account_statement_fee

        return cost


def define_banks():
    """Define fee structures for different banks."""
    banks = []

    # Traditional Swiss Bank
    banks.append(BankFeeStructure(
        name="Traditional Bank",
        monthly_fee=15.0,
        atm_fee_domestic=0.0,  # Free at own ATMs
        atm_fee_international=5.0,
        fx_markup=2.5,
        overdraft_fee=25.0,
        card_replacement_fee=50.0,
        account_statement_fee=3.50
    ))

    # Neobank (e.g., Neon, Revolut style)
    banks.append(BankFeeStructure(
        name="Neobank Free",
        monthly_fee=0.0,
        atm_fee_domestic=0.0,
        atm_fee_international=2.0,
        fx_markup=1.0,
        overdraft_fee=0.0,  # Not offered
        card_replacement_fee=10.0,
        account_statement_fee=0.0  # Digital only
    ))

    # Neobank Premium
    banks.append(BankFeeStructure(
        name="Neobank Premium",
        monthly_fee=7.90,
        atm_fee_domestic=0.0,
        atm_fee_international=0.0,
        fx_markup=0.5,
        overdraft_fee=0.0,
        card_replacement_fee=0.0,  # Free express delivery
        account_statement_fee=0.0
    ))

    # Online-only traditional bank
    banks.append(BankFeeStructure(
        name="Online Bank",
        monthly_fee=5.0,
        atm_fee_domestic=2.0,  # Partner network
        atm_fee_international=3.0,
        fx_markup=1.5,
        overdraft_fee=15.0,
        card_replacement_fee=25.0,
        account_statement_fee=0.0
    ))

    return banks


def define_user_profiles():
    """Define typical user profiles with different banking behaviors."""
    profiles = {}

    # Student: minimal usage, occasional travel
    profiles['Student'] = {
        'atm_domestic': 24,  # 2 per month
        'atm_international': 4,  # Summer travel
        'fx_transactions': 10,
        'fx_amount': 100,
        'overdrafts': 2,
        'card_replacements': 0,
        'statements': 0  # Digital native
    }

    # Professional: moderate usage, regular travel
    profiles['Professional'] = {
        'atm_domestic': 12,  # 1 per month
        'atm_international': 20,  # Business travel
        'fx_transactions': 50,
        'fx_amount': 300,
        'overdrafts': 0,
        'card_replacements': 0,
        'statements': 0
    }

    # Frequent Traveler: high international usage
    profiles['Frequent Traveler'] = {
        'atm_domestic': 6,
        'atm_international': 48,  # 4 per month abroad
        'fx_transactions': 100,
        'fx_amount': 500,
        'overdrafts': 0,
        'card_replacements': 1,  # Lost during travel
        'statements': 0
    }

    # Traditional User: prefers physical banking
    profiles['Traditional User'] = {
        'atm_domestic': 48,  # 4 per month
        'atm_international': 8,  # Occasional travel
        'fx_transactions': 20,
        'fx_amount': 200,
        'overdrafts': 4,
        'card_replacements': 0,
        'statements': 12  # Monthly paper statements
    }

    return profiles


def create_fee_comparison_chart():
    """Create comprehensive fee comparison visualization."""
    banks = define_banks()
    profiles = define_user_profiles()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Neobank vs Traditional Bank Fee Comparison', fontsize=10, fontweight='bold')

    # Plot 1: Annual cost by user profile
    ax1 = axes[0, 0]
    profile_names = list(profiles.keys())
    x_pos = np.arange(len(profile_names))
    width = 0.2

    for i, bank in enumerate(banks):
        costs = [bank.calculate_annual_cost(profiles[p]) for p in profile_names]
        offset = (i - 1.5) * width
        color = ['0.2', '0.4', '0.6', '0.8'][i]
        ax1.bar(x_pos + offset, costs, width, label=bank.name,
                color=color, edgecolor='black', linewidth=0.5)

    ax1.set_ylabel('Annual Cost (CHF)', fontsize=8)
    ax1.set_title('Total Annual Cost by User Profile', fontsize=8, fontweight='bold')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(profile_names, fontsize=7, rotation=15, ha='right')
    ax1.legend(fontsize=7, frameon=True, fancybox=False, edgecolor='black')
    ax1.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax1.tick_params(labelsize=8)

    # Plot 2: Fee structure breakdown for Professional
    ax2 = axes[0, 1]
    professional_profile = profiles['Professional']

    fee_categories = ['Monthly\nFees', 'ATM\nFees', 'FX\nCosts', 'Other\nFees']
    bottom = np.zeros(len(banks))

    # Calculate breakdown for each bank
    breakdowns = []
    for bank in banks:
        monthly = bank.monthly_fee * 12
        atm = (professional_profile['atm_domestic'] * bank.atm_fee_domestic +
               professional_profile['atm_international'] * bank.atm_fee_international)
        fx_total = professional_profile['fx_transactions'] * professional_profile['fx_amount']
        fx = fx_total * (bank.fx_markup / 100)
        other = (professional_profile['overdrafts'] * bank.overdraft_fee +
                professional_profile['card_replacements'] * bank.card_replacement_fee +
                professional_profile['statements'] * bank.account_statement_fee)
        breakdowns.append([monthly, atm, fx, other])

    breakdowns = np.array(breakdowns).T
    x_pos = np.arange(len(banks))
    colors = ['0.3', '0.5', '0.7', '0.9']

    for i, (category, color) in enumerate(zip(fee_categories, colors)):
        ax2.bar(x_pos, breakdowns[i], label=category, bottom=bottom,
                color=color, edgecolor='black', linewidth=0.5)
        bottom += breakdowns[i]

    ax2.set_ylabel('Annual Cost (CHF)', fontsize=8)
    ax2.set_title('Cost Breakdown: Professional Profile', fontsize=8, fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels([b.name for b in banks], fontsize=7, rotation=15, ha='right')
    ax2.legend(fontsize=7, frameon=True, fancybox=False, edgecolor='black', loc='upper left')
    ax2.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax2.tick_params(labelsize=8)

    # Plot 3: Individual fee comparison
    ax3 = axes[1, 0]
    fee_types = ['Monthly\nFee', 'ATM\nDomestic', 'ATM\nIntl', 'FX\nMarkup\n(%)',
                 'Overdraft\nFee', 'Card\nReplace']
    fee_values = []
    for bank in banks:
        fee_values.append([
            bank.monthly_fee,
            bank.atm_fee_domestic,
            bank.atm_fee_international,
            bank.fx_markup,
            bank.overdraft_fee,
            bank.card_replacement_fee
        ])

    x_pos = np.arange(len(fee_types))
    width = 0.2

    for i, (bank, fees) in enumerate(zip(banks, fee_values)):
        offset = (i - 1.5) * width
        color = ['0.2', '0.4', '0.6', '0.8'][i]
        ax3.bar(x_pos + offset, fees, width, label=bank.name,
                color=color, edgecolor='black', linewidth=0.5)

    ax3.set_ylabel('Fee Amount (CHF or %)', fontsize=8)
    ax3.set_title('Individual Fee Comparison', fontsize=8, fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(fee_types, fontsize=7)
    ax3.legend(fontsize=7, frameon=True, fancybox=False, edgecolor='black')
    ax3.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax3.tick_params(labelsize=8)

    # Plot 4: Savings vs Traditional Bank
    ax4 = axes[1, 1]
    traditional_bank = banks[0]
    profile_names = list(profiles.keys())

    savings = []
    for i, bank in enumerate(banks[1:]):  # Exclude traditional bank
        profile_savings = []
        for profile_name in profile_names:
            trad_cost = traditional_bank.calculate_annual_cost(profiles[profile_name])
            bank_cost = bank.calculate_annual_cost(profiles[profile_name])
            saving = trad_cost - bank_cost
            profile_savings.append(saving)
        savings.append(profile_savings)

    x_pos = np.arange(len(profile_names))
    width = 0.25

    for i, (bank, bank_savings) in enumerate(zip(banks[1:], savings)):
        offset = (i - 1) * width
        color = ['0.4', '0.6', '0.8'][i]
        ax4.bar(x_pos + offset, bank_savings, width, label=bank.name,
                color=color, edgecolor='black', linewidth=0.5)

    ax4.set_ylabel('Annual Savings (CHF)', fontsize=8)
    ax4.set_title('Savings vs Traditional Bank', fontsize=8, fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(profile_names, fontsize=7, rotation=15, ha='right')
    ax4.legend(fontsize=7, frameon=True, fancybox=False, edgecolor='black')
    ax4.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax4.tick_params(labelsize=8)

    plt.tight_layout()

    # Save figure
    output_path = Path(__file__).parent / 'neobank_fee_comparison.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    # Save PNG for QR code
    png_path = Path(__file__).parent / 'neobank_fee_comparison.png'
    plt.savefig(png_path, dpi=150, bbox_inches='tight')

    plt.show()


def print_cost_analysis():
    """Print detailed cost analysis table."""
    banks = define_banks()
    profiles = define_user_profiles()

    print("\n" + "="*100)
    print("ANNUAL BANKING COST COMPARISON (CHF)")
    print("="*100)

    # Create results table
    results = []
    for profile_name, profile in profiles.items():
        row = {'Profile': profile_name}
        for bank in banks:
            cost = bank.calculate_annual_cost(profile)
            row[bank.name] = f'{cost:.2f}'
        results.append(row)

    # Print table
    headers = ['Profile'] + [bank.name for bank in banks]
    print(f"{'Profile':<20}", end='')
    for bank in banks:
        print(f"{bank.name:>18}", end='')
    print()
    print("-"*100)

    for row in results:
        print(f"{row['Profile']:<20}", end='')
        for bank in banks:
            print(f"{row[bank.name]:>18}", end='')
        print()

    print("="*100)

    # Print key insights
    print("\nKEY INSIGHTS:")
    print("-" * 100)

    # Find best bank for each profile
    for profile_name, profile in profiles.items():
        costs = [(bank.name, bank.calculate_annual_cost(profile)) for bank in banks]
        costs.sort(key=lambda x: x[1])
        best_bank, best_cost = costs[0]
        worst_bank, worst_cost = costs[-1]
        savings = worst_cost - best_cost

        print(f"\n{profile_name}:")
        print(f"  Best option: {best_bank} (CHF {best_cost:.2f}/year)")
        print(f"  Most expensive: {worst_bank} (CHF {worst_cost:.2f}/year)")
        print(f"  Potential savings: CHF {savings:.2f}/year ({(savings/worst_cost)*100:.1f}%)")

    # Business model analysis
    print("\n" + "-" * 100)
    print("NEOBANK BUSINESS MODEL ADVANTAGES:")
    print("-" * 100)
    print("1. No physical branches → Lower operational costs")
    print("2. Digital-first → Automated processes, reduced staff")
    print("3. Modern technology → Lower IT maintenance costs")
    print("4. Freemium model → Free tier attracts users, premium for power users")
    print("5. Real-time FX → Interbank rates, minimal markup")
    print("6. Partnership networks → ATM fee rebates, revenue sharing")
    print("="*100 + "\n")


def create_feature_comparison():
    """Create feature comparison matrix."""
    banks = define_banks()

    features = {
        'Mobile App': [7, 10, 10, 9],
        'Physical Branches': [10, 0, 0, 2],
        'ATM Network': [10, 7, 8, 6],
        'FX Rates': [4, 8, 10, 7],
        'Digital Experience': [5, 10, 10, 9],
        'Customer Support': [9, 7, 8, 7],
        'Investment Options': [9, 5, 7, 6],
        'Multi-currency': [5, 9, 10, 7]
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    feature_names = list(features.keys())
    bank_names = [bank.name for bank in banks]

    # Create heatmap data
    data = np.array(list(features.values()))

    # Plot heatmap
    im = ax.imshow(data, cmap='Greys', aspect='auto', vmin=0, vmax=10)

    # Set ticks
    ax.set_xticks(np.arange(len(bank_names)))
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_xticklabels(bank_names, fontsize=8, rotation=15, ha='right')
    ax.set_yticklabels(feature_names, fontsize=8)

    # Add values to cells
    for i in range(len(feature_names)):
        for j in range(len(bank_names)):
            text = ax.text(j, i, f'{data[i, j]:.0f}',
                          ha="center", va="center", color="white" if data[i, j] < 5 else "black",
                          fontsize=8, fontweight='bold')

    ax.set_title('Feature Comparison Matrix (0-10 scale)', fontsize=10, fontweight='bold')
    plt.colorbar(im, ax=ax, label='Score')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'feature_comparison.pdf'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Feature comparison saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    print("Neobank Fee Structure Comparison")
    print("=" * 100)
    print("\nThis demo compares fee structures across:")
    print("1. Traditional Swiss Bank (branch-based)")
    print("2. Neobank Free Tier (digital-only, no fees)")
    print("3. Neobank Premium (subscription model)")
    print("4. Online Bank (digital with limited branches)")
    print("\nAnalyzing costs for different user profiles:")
    print("- Student, Professional, Frequent Traveler, Traditional User")
    print("\n")

    # Print detailed cost analysis
    print_cost_analysis()

    # Create visualizations
    print("\nGenerating fee comparison charts...")
    create_fee_comparison_chart()

    print("\nGenerating feature comparison matrix...")
    create_feature_comparison()

    print("\nDemo complete!")
