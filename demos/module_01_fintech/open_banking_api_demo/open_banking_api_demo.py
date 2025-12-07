"""
Open Banking API Structure Demonstration

Demonstrates the structure and data flow of Open Banking APIs using mock data.
Shows how account information and payment initiation services work.

Learning Objectives:
- Understand Open Banking API architecture
- Visualize data flow between banks, TPPs, and customers
- Explore typical API response structures
- Compare data richness: traditional vs open banking
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

# Chart metadata for QuantLet branding
CHART_METADATA = {
    'title': 'Open Banking API Architecture',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_BSc/tree/main/python_demos/module_01_fintech/open_banking_api_demo'
}


def generate_mock_account_data():
    """Generate mock account information API response."""
    return {
        "Data": {
            "Account": [
                {
                    "AccountId": "acc-001",
                    "Currency": "CHF",
                    "AccountType": "Current",
                    "AccountSubType": "CurrentAccount",
                    "Nickname": "Main Checking",
                    "Account": {
                        "SchemeName": "IBAN",
                        "Identification": "CH93 0076 2011 6238 5295 7",
                        "Name": "Max Mustermann"
                    },
                    "Balance": {
                        "Amount": 15234.56,
                        "CreditDebitIndicator": "Credit"
                    }
                },
                {
                    "AccountId": "acc-002",
                    "Currency": "CHF",
                    "AccountType": "Savings",
                    "AccountSubType": "Savings",
                    "Nickname": "Emergency Fund",
                    "Account": {
                        "SchemeName": "IBAN",
                        "Identification": "CH45 0076 2011 6238 5295 8",
                        "Name": "Max Mustermann"
                    },
                    "Balance": {
                        "Amount": 45000.00,
                        "CreditDebitIndicator": "Credit"
                    }
                }
            ]
        },
        "Links": {
            "Self": "https://api.bank.ch/open-banking/v3/accounts"
        },
        "Meta": {
            "TotalPages": 1
        }
    }


def generate_mock_transaction_data():
    """Generate mock transaction history API response."""
    base_date = datetime.now()
    transactions = []

    # Generate realistic transactions
    tx_data = [
        ("Migros Supermarket", -127.85, -5),
        ("Salary Deposit", 6500.00, -1),
        ("Netflix Subscription", -16.90, -8),
        ("SBB Mobile", -55.00, -10),
        ("Restaurant Löwen", -89.50, -3),
        ("Amazon.ch", -234.90, -12),
        ("Health Insurance", -387.50, -2),
        ("Rent Payment", -1850.00, -1),
        ("Electricity Bill", -145.00, -15),
        ("Coop Supermarket", -98.35, -7)
    ]

    for i, (merchant, amount, days_ago) in enumerate(tx_data):
        tx_date = base_date + timedelta(days=days_ago)
        transactions.append({
            "TransactionId": f"tx-{1000+i}",
            "BookingDateTime": tx_date.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "Amount": {
                "Amount": abs(amount),
                "Currency": "CHF"
            },
            "CreditDebitIndicator": "Credit" if amount > 0 else "Debit",
            "Status": "Booked",
            "MerchantDetails": {
                "MerchantName": merchant
            }
        })

    return {
        "Data": {
            "Transaction": sorted(transactions, key=lambda x: x["BookingDateTime"], reverse=True)
        },
        "Links": {
            "Self": "https://api.bank.ch/open-banking/v3/accounts/acc-001/transactions"
        }
    }


def create_api_architecture_diagram():
    """Create visual diagram of Open Banking API architecture."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'Open Banking API Architecture', ha='center', fontsize=10,
            fontweight='bold')

    # Define components with positions
    components = {
        'Customer': (1.5, 7, 1.5, 1, '0.9'),
        'TPP': (5, 7, 1.5, 1, '0.7'),
        'Bank API': (8.5, 7, 1.5, 1, '0.5'),
        'Bank Core': (8.5, 4, 1.5, 1, '0.3')
    }

    boxes = {}
    for name, (x, y, w, h, color) in components.items():
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                             boxstyle="round,pad=0.1",
                             edgecolor='black', facecolor=color,
                             linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, name, ha='center', va='center', fontsize=8, fontweight='bold')
        boxes[name] = (x, y)

    # Add arrows with labels
    arrows = [
        ('Customer', 'TPP', '1. Grant\nConsent'),
        ('TPP', 'Bank API', '2. Request\nData'),
        ('Bank API', 'Bank Core', '3. Fetch\nAccount Info'),
        ('Bank Core', 'Bank API', '4. Return\nData'),
        ('Bank API', 'TPP', '5. API\nResponse'),
        ('TPP', 'Customer', '6. Display\nInsights')
    ]

    for i, (from_comp, to_comp, label) in enumerate(arrows):
        x1, y1 = boxes[from_comp]
        x2, y2 = boxes[to_comp]

        # Calculate offset for bidirectional arrows
        if from_comp == 'Bank API' and to_comp == 'Bank Core':
            offset = -0.15
        elif from_comp == 'Bank Core' and to_comp == 'Bank API':
            offset = 0.15
        elif from_comp == 'Bank API' and to_comp == 'TPP':
            offset = 0.15
        elif from_comp == 'TPP' and to_comp == 'Bank API':
            offset = -0.15
        else:
            offset = 0

        arrow = FancyArrowPatch((x1+offset, y1-0.5), (x2+offset, y2+0.5 if y2 < y1 else y2-0.5),
                               arrowstyle='->', mutation_scale=20,
                               linewidth=1.5, color='0.2',
                               connectionstyle=f"arc3,rad=0")
        ax.add_patch(arrow)

        # Add label
        mid_x, mid_y = (x1+x2)/2 + offset, (y1+y2)/2
        ax.text(mid_x+0.3, mid_y, label, fontsize=7, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none'))

    # Add legend boxes
    legend_y = 2.5
    legend_items = [
        ('TPP', 'Third Party Provider\n(FinTech App)'),
        ('API', 'Standardized Interface\n(PSD2/Open Banking)'),
        ('Consent', 'Customer Authorization\n(OAuth 2.0)')
    ]

    for i, (title, desc) in enumerate(legend_items):
        y_pos = legend_y - i*0.8
        ax.text(1, y_pos, f'{title}:', fontsize=7, fontweight='bold')
        ax.text(1, y_pos-0.3, desc, fontsize=6, style='italic', color='0.3')

    # Add security note
    ax.text(5, 0.5, 'Secure communication via OAuth 2.0 + TLS encryption',
            ha='center', fontsize=7, style='italic',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='0.95', edgecolor='black', linewidth=1))

    plt.tight_layout()
    return fig


def create_data_richness_comparison():
    """Compare data available through traditional vs open banking."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Traditional banking data
    traditional_data = {
        'Account Balance': 5,
        'Transaction History': 3,
        'Spending Categories': 1,
        'Income Analysis': 1,
        'Merchant Details': 2,
        'Real-time Updates': 1,
        'Multi-account View': 2,
        'Export Options': 3
    }

    # Open banking data
    open_banking_data = {
        'Account Balance': 10,
        'Transaction History': 10,
        'Spending Categories': 9,
        'Income Analysis': 9,
        'Merchant Details': 10,
        'Real-time Updates': 10,
        'Multi-account View': 10,
        'Export Options': 10
    }

    categories = list(traditional_data.keys())
    trad_values = list(traditional_data.values())
    open_values = list(open_banking_data.values())

    # Plot 1: Traditional Banking
    y_pos = np.arange(len(categories))
    ax1.barh(y_pos, trad_values, color='0.6', edgecolor='black', linewidth=0.5)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(categories, fontsize=8)
    ax1.set_xlabel('Data Richness Score', fontsize=8)
    ax1.set_title('Traditional Banking\n(Limited Access)', fontsize=8, fontweight='bold')
    ax1.set_xlim(0, 10)
    ax1.tick_params(labelsize=8)
    ax1.grid(True, alpha=0.3, linestyle=':', axis='x')

    # Plot 2: Open Banking
    ax2.barh(y_pos, open_values, color='0.3', edgecolor='black', linewidth=0.5)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(categories, fontsize=8)
    ax2.set_xlabel('Data Richness Score', fontsize=8)
    ax2.set_title('Open Banking\n(Full API Access)', fontsize=8, fontweight='bold')
    ax2.set_xlim(0, 10)
    ax2.tick_params(labelsize=8)
    ax2.grid(True, alpha=0.3, linestyle=':', axis='x')

    plt.tight_layout()
    return fig


def create_api_response_visualization():
    """Visualize API response structure and data flow."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Open Banking API Data Examples', fontsize=10, fontweight='bold')

    # Get mock data
    account_data = generate_mock_account_data()
    transaction_data = generate_mock_transaction_data()

    # Plot 1: Account Overview
    ax1 = axes[0, 0]
    accounts = account_data['Data']['Account']
    account_types = [acc['AccountSubType'] for acc in accounts]
    balances = [acc['Balance']['Amount'] for acc in accounts]

    bars = ax1.bar(range(len(account_types)), balances, color=['0.4', '0.7'],
                   edgecolor='black', linewidth=0.5)
    ax1.set_xticks(range(len(account_types)))
    ax1.set_xticklabels(account_types, fontsize=8)
    ax1.set_ylabel('Balance (CHF)', fontsize=8)
    ax1.set_title('Account Balances via API', fontsize=8, fontweight='bold')
    ax1.tick_params(labelsize=8)
    ax1.grid(True, alpha=0.3, linestyle=':', axis='y')

    # Add value labels
    for bar, balance in zip(bars, balances):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'CHF {balance:,.2f}', ha='center', va='bottom', fontsize=7)

    # Plot 2: Transaction Flow
    ax2 = axes[0, 1]
    transactions = transaction_data['Data']['Transaction']
    credits = sum(tx['Amount']['Amount'] for tx in transactions
                  if tx['CreditDebitIndicator'] == 'Credit')
    debits = sum(tx['Amount']['Amount'] for tx in transactions
                 if tx['CreditDebitIndicator'] == 'Debit')

    flow_data = [credits, debits]
    flow_labels = ['Income', 'Expenses']
    colors_flow = ['0.7', '0.4']

    bars = ax2.bar(range(len(flow_labels)), flow_data, color=colors_flow,
                   edgecolor='black', linewidth=0.5)
    ax2.set_xticks(range(len(flow_labels)))
    ax2.set_xticklabels(flow_labels, fontsize=8)
    ax2.set_ylabel('Amount (CHF)', fontsize=8)
    ax2.set_title('Cash Flow Analysis', fontsize=8, fontweight='bold')
    ax2.tick_params(labelsize=8)
    ax2.grid(True, alpha=0.3, linestyle=':', axis='y')

    # Add value labels
    for bar, value in zip(bars, flow_data):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'CHF {value:,.2f}', ha='center', va='bottom', fontsize=7)

    # Plot 3: Merchant Breakdown
    ax3 = axes[1, 0]
    debit_transactions = [tx for tx in transactions if tx['CreditDebitIndicator'] == 'Debit']
    merchants = [tx['MerchantDetails']['MerchantName'] for tx in debit_transactions[:6]]
    amounts = [tx['Amount']['Amount'] for tx in debit_transactions[:6]]

    y_pos = np.arange(len(merchants))
    ax3.barh(y_pos, amounts, color='0.5', edgecolor='black', linewidth=0.5)
    ax3.set_yticks(y_pos)
    ax3.set_yticklabels(merchants, fontsize=7)
    ax3.set_xlabel('Amount (CHF)', fontsize=8)
    ax3.set_title('Top Merchants (Transaction Detail)', fontsize=8, fontweight='bold')
    ax3.tick_params(labelsize=8)
    ax3.grid(True, alpha=0.3, linestyle=':', axis='x')

    # Plot 4: API Response Time Simulation
    ax4 = axes[1, 1]
    api_endpoints = ['Account\nInfo', 'Transaction\nHistory', 'Balance\nCheck',
                     'Payment\nInitiation', 'Consent\nManagement']
    response_times = [120, 350, 80, 200, 150]  # milliseconds

    bars = ax4.bar(range(len(api_endpoints)), response_times,
                   color=['0.3', '0.4', '0.5', '0.6', '0.7'],
                   edgecolor='black', linewidth=0.5)
    ax4.set_xticks(range(len(api_endpoints)))
    ax4.set_xticklabels(api_endpoints, fontsize=7)
    ax4.set_ylabel('Response Time (ms)', fontsize=8)
    ax4.set_title('API Performance (Mock Data)', fontsize=8, fontweight='bold')
    ax4.tick_params(labelsize=8)
    ax4.grid(True, alpha=0.3, linestyle=':', axis='y')
    ax4.axhline(y=200, color='0.2', linestyle='--', linewidth=1, label='Target SLA')
    ax4.legend(fontsize=7, frameon=True, fancybox=False, edgecolor='black')

    plt.tight_layout()
    return fig


def print_api_examples():
    """Print example API request and response structures."""
    print("\n" + "="*80)
    print("OPEN BANKING API EXAMPLES")
    print("="*80)

    print("\n1. ACCOUNT INFORMATION REQUEST")
    print("-" * 80)
    request_example = {
        "method": "GET",
        "endpoint": "/open-banking/v3/accounts",
        "headers": {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "x-fapi-financial-id": "bank-id-12345",
            "Accept": "application/json"
        }
    }
    print(json.dumps(request_example, indent=2))

    print("\n2. ACCOUNT INFORMATION RESPONSE")
    print("-" * 80)
    account_data = generate_mock_account_data()
    print(json.dumps(account_data, indent=2))

    print("\n3. TRANSACTION HISTORY REQUEST")
    print("-" * 80)
    tx_request = {
        "method": "GET",
        "endpoint": "/open-banking/v3/accounts/acc-001/transactions",
        "query_parameters": {
            "fromBookingDateTime": "2024-01-01T00:00:00Z",
            "toBookingDateTime": "2024-12-31T23:59:59Z"
        },
        "headers": {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "Accept": "application/json"
        }
    }
    print(json.dumps(tx_request, indent=2))

    print("\n" + "="*80)
    print("\nKey API Features:")
    print("1. RESTful architecture (GET, POST, DELETE methods)")
    print("2. OAuth 2.0 authentication with bearer tokens")
    print("3. Standardized response format (Data, Links, Meta)")
    print("4. Rich transaction metadata (merchant, categories, timestamps)")
    print("5. Real-time balance updates")
    print("6. Secure consent management")
    print("="*80 + "\n")


if __name__ == "__main__":
    print("Open Banking API Demonstration")
    print("=" * 80)
    print("\nThis demo illustrates:")
    print("1. Open Banking API architecture and data flow")
    print("2. Example API requests and responses")
    print("3. Data richness comparison: Traditional vs Open Banking")
    print("4. Practical use cases (account aggregation, spending analysis)")
    print("\n")

    # Print API examples
    print_api_examples()

    # Create visualizations
    print("\nGenerating visualizations...")

    print("1. Creating API architecture diagram...")
    fig1 = create_api_architecture_diagram()
    output_path1 = Path(__file__).parent / 'api_architecture.pdf'
    fig1.savefig(output_path1, dpi=300, bbox_inches='tight')
    print(f"   Saved to: {output_path1}")

    print("2. Creating data richness comparison...")
    fig2 = create_data_richness_comparison()
    output_path2 = Path(__file__).parent / 'data_richness.pdf'
    fig2.savefig(output_path2, dpi=300, bbox_inches='tight')
    print(f"   Saved to: {output_path2}")

    print("3. Creating API response visualization...")
    fig3 = create_api_response_visualization()
    output_path3 = Path(__file__).parent / 'api_response.pdf'
    fig3.savefig(output_path3, dpi=300, bbox_inches='tight')
    print(f"   Saved to: {output_path3}")

    # Save PNG for QR code
    png_path = Path(__file__).parent / 'open_banking_api_demo.png'
    fig1.savefig(png_path, dpi=150, bbox_inches='tight')

    plt.show()

    print("\nDemo complete!")
