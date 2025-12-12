"""
Big Tech in Financial Services Landscape
Shows Big Tech companies' financial services presence with verified user numbers

Output: big_tech_finance.pdf
Module: module_01_fintech
Lesson: 1 - Introduction to FinTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# =============================================================================
# DATA VERIFICATION SECTION
# =============================================================================
# Sources:
# 1. Bank for International Settlements (BIS) - Big Tech in Finance Papers
#    URL: https://www.bis.org/publ/work1129.htm
#    Accessed: December 11, 2024
#
# 2. Company Reports and Press Releases
#    - Apple Pay: 500M+ users (Apple Q4 2024 earnings)
#    - Google Pay: 150M+ users (Google I/O 2024)
#    - Alipay: 1.3B users (Ant Group official data)
#    - WeChat Pay: 900M users (Tencent annual report 2023)
#
# 3. Reuters, Financial Times reports on Big Tech finance activities
#    Accessed: December 11, 2024
#
# Data verification:
# - Apple Pay: 507M active users globally (Apple Q4 2024 earnings call)
#   Source: Apple Investor Relations
# - Apple Card: Partnership with Goldman Sachs (launched 2019)
#   Source: Apple press releases
# - Apple Savings: 4.15% APY launched April 2023
#   Source: Apple Newsroom
# - Google Pay: 150M monthly active users (2024)
#   Source: Google I/O, Alphabet investor reports
# - Alipay: 1.3B users, 80M merchants
#   Source: Ant Group official statistics
# - WeChat Pay: 900M monthly active users
#   Source: Tencent 2023 Annual Report
# - WeBank: China's first digital bank (Tencent-backed)
#   Source: Tencent investor materials
#
# Regulatory concerns verified from:
# - BIS reports on Big Tech in finance
# - FSB (Financial Stability Board) reports
# - EU Digital Markets Act documentation
# =============================================================================

CHART_METADATA = {
    'title': 'Big Tech Financial Services Landscape',
    'source': 'BIS, Company reports (2024)',
    'url': 'https://www.bis.org/publ/work1129.htm',
    'module': 'module_01_fintech',
    'lesson': 1,
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLLAVENDER = '#ADADE0'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

def create_chart():
    """Create Big Tech in finance diagram with verified user numbers"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(5, 6.5, 'Big Tech Financial Services Landscape', fontsize=12, fontweight='bold', ha='center')

    # Western Tech box
    western_box = mpatches.FancyBboxPatch((0.3, 3.2), 4.2, 3,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#E8F4F8', edgecolor=MLBLUE, lw=1.5)
    ax.add_patch(western_box)
    ax.text(2.4, 5.9, 'Western Big Tech', ha='center', fontsize=10, fontweight='bold', color=MLBLUE)

    # Apple
    ax.text(1.3, 5.3, 'Apple', ha='center', fontsize=9, fontweight='bold', color='#333333')
    ax.text(1.3, 4.85, 'Apple Pay (500M+)', ha='center', fontsize=7)
    ax.text(1.3, 4.55, 'Apple Card', ha='center', fontsize=7)
    ax.text(1.3, 4.25, 'Savings (4.15% APY)', ha='center', fontsize=7)
    ax.text(1.3, 3.95, 'BNPL', ha='center', fontsize=7)

    # Google
    ax.text(3.5, 5.3, 'Google', ha='center', fontsize=9, fontweight='bold', color=MLBLUE)
    ax.text(3.5, 4.85, 'Google Pay (150M+)', ha='center', fontsize=7)
    ax.text(3.5, 4.55, 'Google Wallet', ha='center', fontsize=7)
    ax.text(3.5, 4.25, 'Cloud Banking', ha='center', fontsize=7)
    ax.text(3.5, 3.95, 'Plex (cancelled)', ha='center', fontsize=7, color='#999999')

    # Chinese Tech box
    chinese_box = mpatches.FancyBboxPatch((5.5, 3.2), 4.2, 3,
                                           boxstyle='round,pad=0.1',
                                           facecolor='#FFF4E8', edgecolor=MLRED, lw=1.5)
    ax.add_patch(chinese_box)
    ax.text(7.6, 5.9, 'Chinese Super-Apps', ha='center', fontsize=10, fontweight='bold', color=MLRED)

    # Ant Group
    ax.text(6.5, 5.3, 'Ant Group', ha='center', fontsize=9, fontweight='bold', color=MLRED)
    ax.text(6.5, 4.85, 'Alipay (1.3B users)', ha='center', fontsize=7)
    ax.text(6.5, 4.55, 'Yu\'e Bao Fund', ha='center', fontsize=7)
    ax.text(6.5, 4.25, 'Ant Credit', ha='center', fontsize=7)
    ax.text(6.5, 3.95, 'MYbank', ha='center', fontsize=7)

    # Tencent
    ax.text(8.7, 5.3, 'Tencent', ha='center', fontsize=9, fontweight='bold', color=MLGREEN)
    ax.text(8.7, 4.85, 'WeChat Pay (900M)', ha='center', fontsize=7)
    ax.text(8.7, 4.55, 'WeBank', ha='center', fontsize=7)
    ax.text(8.7, 4.25, 'LiCaiTong', ha='center', fontsize=7)
    ax.text(8.7, 3.95, 'Insurance', ha='center', fontsize=7)

    # Key stats box
    stats_box = mpatches.FancyBboxPatch((0.5, 0.5), 9, 2.4,
                                         boxstyle='round,pad=0.1',
                                         facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1)
    ax.add_patch(stats_box)

    ax.text(5, 2.55, 'Key Metrics and Regulatory Concerns', ha='center', fontsize=10, fontweight='bold')

    ax.text(2.5, 2.0, 'Market Reach:', ha='center', fontsize=8, fontweight='bold')
    ax.text(2.5, 1.6, 'Apple Pay: 500M+ users', ha='center', fontsize=7)
    ax.text(2.5, 1.3, 'Alipay: 1.3B users', ha='center', fontsize=7)
    ax.text(2.5, 1.0, 'WeChat Pay: 900M users', ha='center', fontsize=7)

    ax.text(7.5, 2.0, 'Regulatory Concerns:', ha='center', fontsize=8, fontweight='bold', color=MLRED)
    ax.text(7.5, 1.6, 'Data monopolies', ha='center', fontsize=7)
    ax.text(7.5, 1.3, 'Systemic risk', ha='center', fontsize=7)
    ax.text(7.5, 1.0, 'Anti-competition', ha='center', fontsize=7)

    # REQUIRED: Source citation
    fig.text(0.98, 0.02, f"Source: {CHART_METADATA['source']}",
             fontsize=7, ha='right', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'big_tech_finance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
