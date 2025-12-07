"""
Generate all charts for Module 1 FinTech lessons 3-12
Creates ~170 professional charts using matplotlib/seaborn
Grayscale-friendly design, saved as PDF
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Color scheme (grayscale-friendly)
COLORS = {
    'primary': '#333333',
    'secondary': '#666666',
    'accent1': '#999999',
    'accent2': '#CCCCCC',
    'highlight': '#6B5B95',  # mlpurple
}

# Create figures directory
FIGURES_DIR = Path(__file__).parent / 'figures'
FIGURES_DIR.mkdir(exist_ok=True)

def save_chart(filename):
    """Save chart as PDF with consistent formatting"""
    filepath = FIGURES_DIR / f"{filename}.pdf"
    plt.savefig(filepath, dpi=300, bbox_inches='tight', format='pdf')
    plt.close()
    print(f"Created: {filename}.pdf")


# ============================================================================
# LESSON 3: MOBILE WALLETS
# ============================================================================

def lesson03_mobile_wallet_adoption():
    """Mobile wallet adoption growth 2014-2023"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = np.arange(2014, 2024)
    volume = np.array([0.5, 1.2, 2.5, 4.8, 7.2, 9.8, 11.5, 13.2, 14.8, 16.0])

    ax.plot(years, volume, marker='o', linewidth=3, markersize=8,
            color=COLORS['highlight'], label='Global Transaction Volume')
    ax.fill_between(years, volume, alpha=0.3, color=COLORS['highlight'])

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Transaction Volume (\$T)', fontsize=12, fontweight='bold')
    ax.set_title('Mobile Wallet Global Adoption Growth', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    save_chart('mobile_wallet_adoption')

def lesson03_nfc_technology_diagram():
    """NFC technology diagram"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simple architecture representation
    components = ['Phone NFC\nChip', 'Secure\nElement', 'Payment\nTerminal', 'Bank\nServer']
    y_positions = [2, 2, 2, 2]
    x_positions = [1, 2.5, 5, 7]

    for x, y, comp in zip(x_positions, y_positions, components):
        ax.add_patch(plt.Rectangle((x-0.4, y-0.3), 0.8, 0.6,
                                   fill=True, facecolor=COLORS['accent2'],
                                   edgecolor=COLORS['primary'], linewidth=2))
        ax.text(x, y, comp, ha='center', va='center', fontsize=10, fontweight='bold')

    # Arrows
    ax.annotate('', xy=(2.1, 2), xytext=(1.4, 2),
                arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['primary']))
    ax.annotate('', xy=(4.6, 2), xytext=(2.9, 2),
                arrowprops=dict(arrowstyle='<->', lw=2, color=COLORS['highlight']))
    ax.annotate('', xy=(6.6, 2), xytext=(5.4, 2),
                arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['primary']))

    ax.text(3.75, 2.35, '13.56 MHz\n4-10 cm', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['highlight']))

    ax.set_xlim(0, 8)
    ax.set_ylim(1, 3)
    ax.axis('off')
    ax.set_title('NFC Technology Architecture', fontsize=14, fontweight='bold', y=0.95)

    save_chart('nfc_technology_diagram')

def lesson03_apple_pay_flow():
    """Apple Pay transaction flow"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Flow diagram
    steps = [
        'User taps phone',
        'Biometric auth',
        'Token requested',
        'Token generated',
        'Cryptogram created',
        'Payment authorized'
    ]

    for i, step in enumerate(steps):
        y = 5 - i*0.8
        ax.add_patch(plt.Rectangle((1, y-0.3), 3, 0.6,
                                   fill=True, facecolor=COLORS['accent2'],
                                   edgecolor=COLORS['primary'], linewidth=2))
        ax.text(2.5, y, f"{i+1}. {step}", ha='center', va='center',
                fontsize=11, fontweight='bold')

        if i < len(steps) - 1:
            ax.annotate('', xy=(2.5, y-0.5), xytext=(2.5, y-0.3),
                       arrowprops=dict(arrowstyle='->', lw=2, color=COLORS['highlight']))

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('Apple Pay Transaction Flow', fontsize=14, fontweight='bold')

    save_chart('apple_pay_flow')

def lesson03_mpesa_growth():
    """M-Pesa user growth"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = np.arange(2007, 2024)
    users = np.array([0.5, 2, 5, 8, 12, 15, 17, 19, 21, 24, 28, 32, 38, 43, 48, 51, 51])

    ax.bar(years, users, color=COLORS['highlight'], alpha=0.7, edgecolor=COLORS['primary'])

    # Add 96% penetration annotation
    ax.axhline(y=51, color='red', linestyle='--', linewidth=2, alpha=0.5)
    ax.text(2015, 53, '96% adult penetration', fontsize=10, fontweight='bold', color='red')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Users (Millions)', fontsize=12, fontweight='bold')
    ax.set_title('M-Pesa User Growth in Kenya', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    save_chart('mpesa_growth')

def lesson03_china_wallet_comparison():
    """Alipay vs WeChat Pay comparison"""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Users\n(Billions)', 'Market Share\n(%)', 'Transaction\nVolume\n(\$T)', 'QR Code\nAdoption\n(%)']
    alipay = [1.3, 54, 18, 98]
    wechat = [1.0, 38, 14, 96]

    x = np.arange(len(categories))
    width = 0.35

    ax.bar(x - width/2, alipay, width, label='Alipay',
           color=COLORS['primary'], alpha=0.7)
    ax.bar(x + width/2, wechat, width, label='WeChat Pay',
           color=COLORS['highlight'], alpha=0.7)

    ax.set_ylabel('Value', fontsize=12, fontweight='bold')
    ax.set_title('Alipay vs WeChat Pay Comparison (2023)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')

    save_chart('china_wallet_comparison')

def lesson03_qr_vs_nfc_comparison():
    """QR Code vs NFC comparison matrix"""
    fig, ax = plt.subplots(figsize=(10, 8))

    features = ['Cost', 'Speed', 'Security', 'Adoption', 'Infrastructure']
    qr_scores = [9, 6, 6, 9, 10]
    nfc_scores = [5, 9, 9, 6, 4]

    x = np.arange(len(features))
    width = 0.35

    ax.barh(x - width/2, qr_scores, width, label='QR Code',
            color=COLORS['primary'], alpha=0.7)
    ax.barh(x + width/2, nfc_scores, width, label='NFC',
            color=COLORS['highlight'], alpha=0.7)

    ax.set_xlabel('Score (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('QR Code vs NFC Technology Comparison', fontsize=14, fontweight='bold')
    ax.set_yticks(x)
    ax.set_yticklabels(features, fontsize=11)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(0, 10)

    save_chart('qr_vs_nfc_comparison')

def lesson03_global_wallet_share():
    """Global wallet market share"""
    fig, ax = plt.subplots(figsize=(10, 8))

    wallets = ['Alipay', 'WeChat Pay', 'Apple Pay', 'Google Pay', 'PayPal', 'Others']
    shares = [28, 20, 12, 8, 6, 26]
    colors_list = [COLORS['primary'], COLORS['highlight'], COLORS['secondary'],
                   COLORS['accent1'], COLORS['accent2'], '#DDDDDD']

    wedges, texts, autotexts = ax.pie(shares, labels=wallets, autopct='%1.1f%%',
                                       colors=colors_list, startangle=90,
                                       textprops={'fontsize': 11, 'fontweight': 'bold'})

    ax.set_title('Global Mobile Wallet Market Share (2023)', fontsize=14, fontweight='bold')

    save_chart('global_wallet_share')


# ============================================================================
# LESSON 4: NEOBANKS
# ============================================================================

def lesson04_neobank_vs_traditional():
    """Neobank vs traditional bank comparison"""
    fig, ax = plt.subplots(figsize=(10, 8))

    metrics = ['CAC\n(\$)', 'Operating\nCost\n(%)', 'Branches', 'Digital\nFirst\n(%)', 'Speed to\nMarket\n(months)']
    traditional = [300, 65, 100, 40, 24]
    neobank = [50, 25, 0, 100, 6]

    x = np.arange(len(metrics))
    width = 0.35

    # Normalize for better visualization
    traditional_norm = [300/10, 65, 100, 40, 24]
    neobank_norm = [50/10, 25, 0, 100, 6]

    ax.bar(x - width/2, traditional_norm, width, label='Traditional Bank',
           color=COLORS['secondary'], alpha=0.7)
    ax.bar(x + width/2, neobank_norm, width, label='Neobank',
           color=COLORS['highlight'], alpha=0.7)

    ax.set_ylabel('Normalized Value', fontsize=12, fontweight='bold')
    ax.set_title('Neobank vs Traditional Bank Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=10)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')

    save_chart('neobank_vs_traditional')

def lesson04_neobank_market_leaders():
    """Neobank market leaders by customers"""
    fig, ax = plt.subplots(figsize=(10, 6))

    banks = ['Revolut', 'Nubank', 'Chime', 'N26', 'Monzo', 'Starling']
    customers = [35, 89, 13, 8, 7, 4]  # millions

    bars = ax.barh(banks, customers, color=COLORS['highlight'], alpha=0.7,
                   edgecolor=COLORS['primary'], linewidth=1.5)

    # Add value labels
    for i, v in enumerate(customers):
        ax.text(v + 1, i, f'{v}M', va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Customers (Millions)', fontsize=12, fontweight='bold')
    ax.set_title('Leading Neobanks by Customer Base (2023)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')

    save_chart('neobank_market_leaders')

def lesson04_revolut_growth():
    """Revolut growth trajectory"""
    fig, ax = plt.subplots(figsize=(10, 6))

    years = np.arange(2015, 2024)
    customers = np.array([0.1, 0.5, 1.5, 3.0, 8.0, 12.0, 16.0, 25.0, 35.0])

    ax.plot(years, customers, marker='o', linewidth=3, markersize=10,
            color=COLORS['highlight'], label='Total Customers')
    ax.fill_between(years, customers, alpha=0.3, color=COLORS['highlight'])

    # Add milestone annotations
    ax.annotate('1M users', xy=(2017, 1.5), xytext=(2016, 5),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=9, fontweight='bold', color='red')
    ax.annotate('\$33B valuation', xy=(2021, 16.0), xytext=(2019, 20),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=9, fontweight='bold', color='red')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Customers (Millions)', fontsize=12, fontweight='bold')
    ax.set_title('Revolut Growth Trajectory 2015-2023', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    save_chart('revolut_growth')

def lesson04_unit_economics():
    """Neobank unit economics waterfall"""
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Revenue\nper User', 'Operating\nCost', 'CAC\n(amortized)', 'Regulatory\nCost', 'Net\nProfit']
    values = [125, -40, -25, -15, 45]
    colors_list = [COLORS['highlight'] if v > 0 else COLORS['secondary'] for v in values]

    cumulative = np.cumsum([0] + values[:-1])

    for i, (cat, val, cum) in enumerate(zip(categories, values, cumulative)):
        ax.bar(i, abs(val), bottom=cum if val > 0 else cum + val,
               color=colors_list[i], alpha=0.7, edgecolor=COLORS['primary'], linewidth=1.5)
        ax.text(i, cum + val/2, f'\${abs(val)}', ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

    ax.axhline(y=0, color='black', linewidth=1)
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylabel('Value (\$ per customer/year)', fontsize=12, fontweight='bold')
    ax.set_title('Neobank Unit Economics Breakdown', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    save_chart('neobank_unit_economics')

def lesson04_cac_comparison():
    """CAC comparison traditional vs neobank"""
    fig, ax = plt.subplots(figsize=(10, 6))

    bank_types = ['Traditional\nBank', 'Neobank\n(Digital)', 'Neobank\n(Referral)']
    cac = [300, 80, 20]

    bars = ax.bar(bank_types, cac, color=[COLORS['secondary'], COLORS['highlight'], COLORS['primary']],
                  alpha=0.7, edgecolor='black', linewidth=1.5)

    for bar, val in zip(bars, cac):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'\${val}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_ylabel('Customer Acquisition Cost (\$)', fontsize=12, fontweight='bold')
    ax.set_title('Customer Acquisition Cost Comparison', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    save_chart('cac_comparison')


# ============================================================================
# Continue with remaining lessons (5-12) using similar pattern
# ============================================================================

def generate_all_charts():
    """Generate all charts for lessons 3-12"""
    print("Generating charts for Module 1 FinTech Lessons 3-12...")
    print(f"Output directory: {FIGURES_DIR}")
    print("-" * 60)

    # Lesson 3: Mobile Wallets
    print("\nLesson 3: Mobile Wallets")
    lesson03_mobile_wallet_adoption()
    lesson03_nfc_technology_diagram()
    lesson03_apple_pay_flow()
    lesson03_mpesa_growth()
    lesson03_china_wallet_comparison()
    lesson03_qr_vs_nfc_comparison()
    lesson03_global_wallet_share()

    # Lesson 4: Neobanks
    print("\nLesson 4: Neobanks")
    lesson04_neobank_vs_traditional()
    lesson04_neobank_market_leaders()
    lesson04_revolut_growth()
    lesson04_unit_economics()
    lesson04_cac_comparison()

    # TODO: Continue with lessons 5-12
    # For now, creating placeholder message
    print("\nLessons 5-12: Chart generation functions to be implemented")
    print("Total charts created so far: 12")
    print("\nNext steps:")
    print("1. Implement chart functions for lessons 5-12 (~158 more charts)")
    print("2. Follow same pattern: market data, architecture, flows, comparisons")
    print("3. Test LaTeX compilation with generated charts")

    print("-" * 60)
    print(f"Charts saved to: {FIGURES_DIR}")


if __name__ == "__main__":
    generate_all_charts()
