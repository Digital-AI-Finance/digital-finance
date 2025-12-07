"""
Batch Chart Generation for Module 2 Blockchain Lessons 15-24
Creates all visualizations referenced in the Beamer slides
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import pandas as pd

# Set style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Create charts directory structure
base_dir = Path(__file__).parent / "charts"
for lesson_num in range(15, 25):
    (base_dir / f"lesson_{lesson_num}").mkdir(parents=True, exist_ok=True)

# Color scheme
COLOR_PRIMARY = '#6B5B95'  # mlpurple
COLOR_SECONDARY = '#9B7EBD'  # lighter purple
COLOR_ACCENT = '#4A90E2'  # mlblue
COLOR_GREEN = '#44A044'
COLOR_RED = '#D62728'
COLOR_ORANGE = '#FF7F0E'

print("Starting chart generation for Lessons 15-24...")

# ============================================================================
# LESSON 15: Public Key Cryptography
# ============================================================================
print("\nGenerating Lesson 15 charts (Public Key Crypto)...")

# Chart 1: Symmetric vs Asymmetric
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Symmetric
ax = axes[0]
ax.text(0.5, 0.8, 'Alice', ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.5))
ax.text(0.5, 0.2, 'Bob', ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.5))
ax.annotate('', xy=(0.5, 0.25), xytext=(0.5, 0.75), arrowprops=dict(arrowstyle='<->', lw=2, color=COLOR_PRIMARY))
ax.text(0.7, 0.5, 'Shared\nSecret Key', fontsize=10, bbox=dict(boxstyle='round', facecolor=COLOR_ORANGE, alpha=0.7))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Symmetric Encryption', fontsize=12, fontweight='bold')
# Asymmetric
ax = axes[1]
ax.text(0.2, 0.8, 'Alice', ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.5))
ax.text(0.2, 0.6, 'Public Key', ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor=COLOR_GREEN, alpha=0.7))
ax.text(0.2, 0.4, 'Private Key', ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor=COLOR_RED, alpha=0.7))
ax.text(0.8, 0.8, 'Bob', ha='center', fontsize=14, bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.5))
ax.annotate('', xy=(0.75, 0.75), xytext=(0.25, 0.6), arrowprops=dict(arrowstyle='->', lw=2, color=COLOR_GREEN))
ax.text(0.5, 0.9, 'Public key shared', fontsize=8)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Asymmetric Encryption', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_15' / 'symmetric_vs_asymmetric.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Elliptic Curve
fig, ax = plt.subplots(figsize=(10, 6))
y_vals = np.linspace(-5, 5, 1000)
x_vals = y_vals**2 - y_vals**4/16 + 7  # Simplified visualization
ax.plot(x_vals, y_vals, color=COLOR_PRIMARY, lw=2, label='$y^2 = x^3 + 7$ (secp256k1)')
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.scatter([3, 4, 2.5], [2, -1.5, 3], s=100, c=COLOR_ACCENT, zorder=5, label='Points on curve')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Elliptic Curve: secp256k1 (used by Bitcoin)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_15' / 'elliptic_curve.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Bitcoin Address Generation Flow
fig, ax = plt.subplots(figsize=(12, 6))
steps = ['Private Key\n(256 bits)', 'Public Key\n(ECDSA)', 'SHA256', 'RIPEMD160', 'Add version\n+ checksum', 'Base58\nEncode', 'Bitcoin Address']
y_pos = 0.5
for i, step in enumerate(steps):
    x_pos = i / (len(steps) - 1)
    color = COLOR_PRIMARY if i % 2 == 0 else COLOR_ACCENT
    ax.text(x_pos, y_pos, step, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.6, edgecolor='black'))
    if i < len(steps) - 1:
        ax.annotate('', xy=((i+1)/(len(steps)-1) - 0.05, y_pos), xytext=(x_pos + 0.05, y_pos),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Bitcoin Address Generation Pipeline', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_15' / 'bitcoin_address_generation.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 4: HD Wallet Tree
fig, ax = plt.subplots(figsize=(12, 7))
ax.text(0.5, 0.9, 'Master Seed\n(BIP-39)', ha='center', fontsize=11,
        bbox=dict(boxstyle='round', facecolor=COLOR_PRIMARY, alpha=0.7))
# Derivation paths
paths = [
    (0.25, 0.6, "m/44'/0'/0'", 'Bitcoin'),
    (0.5, 0.6, "m/44'/60'/0'", 'Ethereum'),
    (0.75, 0.6, "m/44'/2'/0'", 'Litecoin')
]
for x, y, path, name in paths:
    ax.text(x, y, f'{path}\n{name}', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.6))
    ax.plot([0.5, x], [0.85, y+0.05], 'k-', lw=1.5)
    # Child addresses
    for i, child_y in enumerate([y-0.15, y-0.25, y-0.35]):
        ax.text(x, child_y, f'Address {i}', ha='center', fontsize=8,
                bbox=dict(boxstyle='round', facecolor=COLOR_SECONDARY, alpha=0.5))
        ax.plot([x, x], [y-0.05, child_y+0.02], 'k-', lw=1, alpha=0.5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Hierarchical Deterministic (HD) Wallet Structure', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_15' / 'hd_wallet_tree.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 15 charts complete (4 charts)")

# ============================================================================
# LESSON 16: Proof of Work
# ============================================================================
print("\nGenerating Lesson 16 charts (Proof of Work)...")

# Chart 1: Mining Process
fig, ax = plt.subplots(figsize=(12, 6))
steps = ['Collect\nTransactions', 'Build Merkle\nTree', 'Create Block\nHeader', 'Try Nonce\n(Hash)', 'Hash < Target?', 'Broadcast\nBlock']
colors = [COLOR_ACCENT, COLOR_ACCENT, COLOR_PRIMARY, COLOR_ORANGE, COLOR_RED, COLOR_GREEN]
for i, (step, color) in enumerate(zip(steps, colors)):
    x_pos = i / (len(steps) - 1)
    ax.text(x_pos, 0.5, step, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.6, edgecolor='black'))
    if i < len(steps) - 1:
        if i == 4:
            # Decision branch
            ax.annotate('No', xy=(x_pos + 0.05, 0.3), xytext=(x_pos - 0.15, 0.3),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='red'))
            ax.annotate('Yes', xy=((i+1)/(len(steps)-1) - 0.05, 0.5), xytext=(x_pos + 0.05, 0.5),
                        arrowprops=dict(arrowstyle='->', lw=2, color='green'))
        else:
            ax.annotate('', xy=((i+1)/(len(steps)-1) - 0.05, 0.5), xytext=(x_pos + 0.05, 0.5),
                        arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Bitcoin Mining Process', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_16' / 'mining_process.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Bitcoin Difficulty History (Exponential Growth)
years = np.arange(2009, 2025)
difficulty = 1 * (1.8 ** (years - 2009))  # Exponential approximation
fig, ax = plt.subplots(figsize=(12, 6))
ax.semilogy(years, difficulty, marker='o', color=COLOR_PRIMARY, lw=2, markersize=6)
ax.fill_between(years, difficulty, alpha=0.3, color=COLOR_SECONDARY)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Difficulty (log scale)', fontsize=12)
ax.set_title('Bitcoin Mining Difficulty: 2009-2024', fontsize=14, fontweight='bold')
ax.grid(alpha=0.3)
ax.annotate('CPU Era', xy=(2010, difficulty[1]), xytext=(2011, difficulty[2]*10),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)
ax.annotate('ASIC Era', xy=(2014, difficulty[5]), xytext=(2015, difficulty[6]*0.5),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_16' / 'bitcoin_difficulty_history.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Energy Consumption
categories = ['Bitcoin\n(PoW)', 'Ethereum\n(Pre-Merge)', 'Ethereum\n(Post-Merge)', 'Visa\nNetwork']
energy_twh = [150, 78, 0.01, 0.002]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, energy_twh, color=[COLOR_PRIMARY, COLOR_ORANGE, COLOR_GREEN, COLOR_ACCENT], alpha=0.7, edgecolor='black')
ax.set_ylabel('Energy Consumption (TWh/year)', fontsize=12)
ax.set_title('Annual Energy Consumption Comparison', fontsize=14, fontweight='bold')
ax.set_yscale('log')
for bar, val in zip(bars, energy_twh):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height*1.5, f'{val:.2f}', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_16' / 'energy_consumption.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 16 charts complete (3 core charts)")

# ============================================================================
# LESSON 17: Proof of Stake
# ============================================================================
print("\nGenerating Lesson 17 charts (Proof of Stake)...")

# Chart 1: PoW vs PoS Comparison
fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Energy\nUsage', 'Hardware\nCost', 'Centralization\nRisk', 'Finality\nSpeed']
pow_scores = [10, 9, 7, 3]  # Higher = worse
pos_scores = [1, 2, 6, 9]   # Higher = better for finality
x = np.arange(len(categories))
width = 0.35
ax.bar(x - width/2, pow_scores, width, label='Proof of Work', color=COLOR_PRIMARY, alpha=0.7)
ax.bar(x + width/2, pos_scores, width, label='Proof of Stake', color=COLOR_GREEN, alpha=0.7)
ax.set_ylabel('Score (Higher = More Concern/Better)', fontsize=12)
ax.set_title('Proof of Work vs Proof of Stake Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_17' / 'pow_vs_pos_comparison.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: The Merge Impact
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Energy reduction
categories = ['Before\n(PoW)', 'After\n(PoS)']
energy = [78, 0.01]
axes[0].bar(categories, energy, color=[COLOR_RED, COLOR_GREEN], alpha=0.7, edgecolor='black')
axes[0].set_ylabel('Energy (TWh/year)', fontsize=12)
axes[0].set_title('Energy Reduction: 99.95%', fontsize=12, fontweight='bold')
axes[0].set_yscale('log')
# Issuance reduction
issuance = [13000, 1600]
axes[1].bar(categories, issuance, color=[COLOR_ORANGE, COLOR_ACCENT], alpha=0.7, edgecolor='black')
axes[1].set_ylabel('Daily Issuance (ETH)', fontsize=12)
axes[1].set_title('Issuance Reduction: 88%', fontsize=12, fontweight='bold')
plt.suptitle('The Merge Impact (Sept 2022)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_17' / 'the_merge_impact.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Staking Pool Distribution (Lido dominance)
pools = ['Lido', 'Coinbase', 'Rocket Pool', 'Binance', 'Kraken', 'Others']
market_share = [32, 10, 2.5, 6, 4, 45.5]
fig, ax = plt.subplots(figsize=(10, 7))
colors_pie = [COLOR_RED if pool == 'Lido' else COLOR_ACCENT for pool in pools]
wedges, texts, autotexts = ax.pie(market_share, labels=pools, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('Ethereum Staking Pool Distribution (2024)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_17' / 'staking_pool_distribution.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 17 charts complete (3 core charts)")

# ============================================================================
# LESSON 18: Bitcoin Architecture
# ============================================================================
print("\nGenerating Lesson 18 charts (Bitcoin Architecture)...")

# Chart 1: UTXO vs Account Model
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# UTXO
ax = axes[0]
ax.text(0.5, 0.8, 'Alice owns:', ha='center', fontsize=11, fontweight='bold')
ax.text(0.5, 0.65, 'UTXO1: 0.5 BTC', ha='center', bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.6))
ax.text(0.5, 0.5, 'UTXO2: 0.3 BTC', ha='center', bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.6))
ax.text(0.5, 0.35, 'UTXO3: 0.1 BTC', ha='center', bbox=dict(boxstyle='round', facecolor=COLOR_ACCENT, alpha=0.6))
ax.text(0.5, 0.15, 'Total: 0.9 BTC', ha='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor=COLOR_GREEN, alpha=0.5))
ax.set_title('UTXO Model (Bitcoin)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
# Account
ax = axes[1]
ax.text(0.5, 0.7, 'Alice Account:', ha='center', fontsize=11, fontweight='bold')
ax.text(0.5, 0.5, 'Balance: 0.9 BTC', ha='center', fontsize=14,
        bbox=dict(boxstyle='round', facecolor=COLOR_PRIMARY, alpha=0.6))
ax.text(0.5, 0.3, 'Nonce: 42', ha='center', fontsize=10)
ax.set_title('Account Model (Ethereum)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.suptitle('UTXO vs Account Model', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_18' / 'utxo_vs_account.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Transaction Lifecycle
fig, ax = plt.subplots(figsize=(12, 6))
stages = ['Creation\n(User signs)', 'Broadcast\n(P2P network)', 'Mempool\n(Unconfirmed)', 'Mining\n(Block inclusion)', 'Confirmation\n(Block added)', 'Finality\n(6+ blocks)']
colors_stages = [COLOR_ACCENT, COLOR_ACCENT, COLOR_ORANGE, COLOR_PRIMARY, COLOR_GREEN, COLOR_GREEN]
for i, (stage, color) in enumerate(zip(stages, colors_stages)):
    x_pos = i / (len(stages) - 1)
    ax.text(x_pos, 0.5, stage, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.6, edgecolor='black'))
    if i < len(stages) - 1:
        ax.annotate('', xy=((i+1)/(len(stages)-1) - 0.05, 0.5), xytext=(x_pos + 0.05, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Bitcoin Transaction Lifecycle', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_18' / 'transaction_lifecycle.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Lightning Network Concept
fig, ax = plt.subplots(figsize=(10, 6))
# Nodes
nodes = {'Alice': (0.1, 0.5), 'Bob': (0.4, 0.7), 'Carol': (0.7, 0.6), 'Dave': (0.9, 0.4)}
for name, (x, y) in nodes.items():
    ax.scatter(x, y, s=1000, c=COLOR_ACCENT, alpha=0.6, edgecolors='black', linewidths=2, zorder=3)
    ax.text(x, y, name, ha='center', va='center', fontsize=12, fontweight='bold')
# Channels
channels = [('Alice', 'Bob'), ('Bob', 'Carol'), ('Carol', 'Dave')]
for node1, node2 in channels:
    x1, y1 = nodes[node1]
    x2, y2 = nodes[node2]
    ax.plot([x1, x2], [y1, y2], 'k-', lw=3, alpha=0.5)
    mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
    ax.text(mid_x, mid_y+0.05, 'Channel', fontsize=9, ha='center',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
# Payment route
ax.annotate('Payment Route', xy=(0.5, 0.3), xytext=(0.5, 0.1),
            fontsize=11, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=COLOR_GREEN, alpha=0.5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Lightning Network: Off-Chain Payment Channels', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_18' / 'lightning_network_concept.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 18 charts complete (3 core charts)")

# ============================================================================
# LESSON 19: Ethereum and Smart Contracts
# ============================================================================
print("\nGenerating Lesson 19 charts (Ethereum & Smart Contracts)...")

# Chart 1: EVM Architecture
fig, ax = plt.subplots(figsize=(10, 7))
layers = [
    ('Application Layer', 0.9, COLOR_ACCENT),
    ('Smart Contract Code (Solidity)', 0.75, COLOR_PRIMARY),
    ('EVM Bytecode', 0.6, COLOR_SECONDARY),
    ('EVM Execution', 0.45, COLOR_ORANGE),
    ('State Database', 0.3, COLOR_GREEN)
]
for name, y_pos, color in layers:
    ax.add_patch(Rectangle((0.1, y_pos-0.05), 0.8, 0.1, facecolor=color, alpha=0.6, edgecolor='black', linewidth=2))
    ax.text(0.5, y_pos, name, ha='center', va='center', fontsize=11, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Ethereum Virtual Machine (EVM) Architecture', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_19' / 'evm_architecture.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: EIP-1559 Fee Structure
fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Legacy\n(Pre-EIP-1559)', 'EIP-1559']
base_fee = [0, 30]
priority_fee = [50, 10]
x = np.arange(len(categories))
width = 0.5
p1 = ax.bar(x, base_fee, width, label='Base Fee (Burned)', color=COLOR_RED, alpha=0.7)
p2 = ax.bar(x, priority_fee, width, bottom=base_fee, label='Priority Fee (To Validator)', color=COLOR_GREEN, alpha=0.7)
ax.set_ylabel('Fee (Gwei)', fontsize=12)
ax.set_title('Transaction Fee Structure: Legacy vs EIP-1559', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis='y', alpha=0.3)
for i, (b, p) in enumerate(zip(base_fee, priority_fee)):
    total = b + p
    ax.text(i, total + 2, f'{total} gwei', ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_19' / 'eip1559_structure.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: ETH Issuance vs Burn (Post-Merge)
fig, ax = plt.subplots(figsize=(10, 6))
days = np.arange(0, 365)
issuance = np.ones(365) * 1600  # Daily issuance
burn = 1000 + 500 * np.sin(days / 30)  # Variable burn
net = issuance - burn
ax.fill_between(days, 0, issuance, alpha=0.3, color=COLOR_GREEN, label='Daily Issuance (1600 ETH)')
ax.fill_between(days, 0, burn, alpha=0.3, color=COLOR_RED, label='Daily Burn (Variable)')
ax.plot(days, net, color=COLOR_PRIMARY, lw=2, label='Net Issuance')
ax.axhline(0, color='black', lw=1, linestyle='--', alpha=0.5)
ax.set_xlabel('Days Since Merge', fontsize=12)
ax.set_ylabel('ETH per Day', fontsize=12)
ax.set_title('Ethereum Issuance vs Burn (Post-Merge)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_19' / 'eth_issuance_burn.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 19 charts complete (3 core charts)")

# ============================================================================
# LESSON 20: Tokens
# ============================================================================
print("\nGenerating Lesson 20 charts (Tokens)...")

# Chart 1: ERC-20 Transfer Flow
fig, ax = plt.subplots(figsize=(12, 6))
steps = ['User calls\ntransfer()', 'Check balance', 'Update\nbalances', 'Emit Transfer\nevent', 'Transaction\ncomplete']
for i, step in enumerate(steps):
    x_pos = i / (len(steps) - 1)
    color = COLOR_PRIMARY if i % 2 == 0 else COLOR_ACCENT
    ax.text(x_pos, 0.5, step, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.6, edgecolor='black'))
    if i < len(steps) - 1:
        ax.annotate('', xy=((i+1)/(len(steps)-1) - 0.05, 0.5), xytext=(x_pos + 0.05, 0.5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('ERC-20 Token Transfer Flow', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_20' / 'erc20_transfer_flow.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: NFT Market Volume (2021-2024)
months = pd.date_range('2021-01', '2024-12', freq='M')
volume = 0.1 + 5 * np.exp(-((np.arange(len(months)) - 12) / 8) ** 2)  # Gaussian peak at Aug 2021
fig, ax = plt.subplots(figsize=(12, 6))
ax.fill_between(range(len(months)), volume, alpha=0.4, color=COLOR_PRIMARY)
ax.plot(range(len(months)), volume, color=COLOR_PRIMARY, lw=2)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Monthly Volume (Billions USD)', fontsize=12)
ax.set_title('NFT Market Volume: Boom and Bust (2021-2024)', fontsize=14, fontweight='bold')
ax.set_xticks(range(0, len(months), 6))
ax.set_xticklabels([months[i].strftime('%Y-%m') for i in range(0, len(months), 6)], rotation=45)
ax.grid(alpha=0.3)
ax.annotate('Peak\n(Aug 2021)', xy=(12, volume[12]), xytext=(18, volume[12]+1),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_20' / 'nft_market_volume.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Tokenomics Distribution
labels = ['Team\n(20%)', 'Investors\n(15%)', 'Community\nRewards\n(40%)', 'Treasury\n(15%)', 'Liquidity\n(10%)']
sizes = [20, 15, 40, 15, 10]
colors_tok = [COLOR_PRIMARY, COLOR_ACCENT, COLOR_GREEN, COLOR_ORANGE, COLOR_SECONDARY]
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%',
                                     colors=colors_tok, startangle=90)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('Typical Token Distribution (Tokenomics)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_20' / 'tokenomics_distribution.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 20 charts complete (3 core charts)")

# ============================================================================
# LESSON 21: DeFi
# ============================================================================
print("\nGenerating Lesson 21 charts (DeFi)...")

# Chart 1: AMM Bonding Curve (x*y=k)
fig, ax = plt.subplots(figsize=(10, 7))
k = 10000
x = np.linspace(50, 250, 500)
y = k / x
ax.plot(x, y, color=COLOR_PRIMARY, lw=3, label='$x \\times y = k$ (constant product)')
# Mark a trade
x_before, y_before = 100, 100
x_after, y_after = 90, k/90
ax.scatter([x_before], [y_before], s=200, c=COLOR_GREEN, zorder=5, label='Before Trade', edgecolors='black', linewidths=2)
ax.scatter([x_after], [y_after], s=200, c=COLOR_RED, zorder=5, label='After Trade (10 ETH bought)', edgecolors='black', linewidths=2)
ax.annotate('', xy=(x_after, y_after), xytext=(x_before, y_before),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlabel('Token A Reserve (e.g., ETH)', fontsize=12)
ax.set_ylabel('Token B Reserve (e.g., USDC)', fontsize=12)
ax.set_title('Automated Market Maker: Constant Product Curve', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_21' / 'bonding_curve.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Impermanent Loss
price_ratios = np.linspace(0.5, 5, 100)
il = 2 * np.sqrt(price_ratios) / (1 + price_ratios) - 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(price_ratios, il * 100, color=COLOR_RED, lw=3)
ax.fill_between(price_ratios, il * 100, alpha=0.3, color=COLOR_RED)
ax.axhline(0, color='black', lw=1, linestyle='--')
ax.axvline(1, color='black', lw=1, linestyle='--', alpha=0.5)
ax.set_xlabel('Price Ratio (Final / Initial)', fontsize=12)
ax.set_ylabel('Impermanent Loss (%)', fontsize=12)
ax.set_title('Impermanent Loss vs Price Change', fontsize=14, fontweight='bold')
ax.grid(alpha=0.3)
ax.annotate('2x price: -5.7%', xy=(2, il[50]*100), xytext=(3, -10),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_21' / 'impermanent_loss.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: DeFi TVL History (2020-2024)
months_defi = pd.date_range('2020-01', '2024-12', freq='M')
tvl = 1 + 99 * (1 / (1 + np.exp(-0.3 * (np.arange(len(months_defi)) - 20))))  # Sigmoid growth
tvl = tvl * (1 + 0.2 * np.sin(np.arange(len(months_defi)) / 3))  # Add volatility
fig, ax = plt.subplots(figsize=(12, 6))
ax.fill_between(range(len(months_defi)), tvl, alpha=0.4, color=COLOR_GREEN)
ax.plot(range(len(months_defi)), tvl, color=COLOR_GREEN, lw=2)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Total Value Locked (Billions USD)', fontsize=12)
ax.set_title('DeFi Total Value Locked (TVL): 2020-2024', fontsize=14, fontweight='bold')
ax.set_xticks(range(0, len(months_defi), 12))
ax.set_xticklabels([months_defi[i].year for i in range(0, len(months_defi), 12)])
ax.grid(alpha=0.3)
ax.annotate('DeFi Summer\n2020', xy=(6, tvl[6]), xytext=(10, tvl[6]+20),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_21' / 'defi_tvl_history.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 21 charts complete (3 core charts)")

# ============================================================================
# LESSON 22: Stablecoins
# ============================================================================
print("\nGenerating Lesson 22 charts (Stablecoins)...")

# Chart 1: Crypto Volatility vs Stablecoin
days_vol = np.arange(0, 365)
btc_price = 40000 + 20000 * np.sin(days_vol / 50) + 5000 * np.random.randn(len(days_vol))
usdc_price = 1 + 0.01 * np.random.randn(len(days_vol))
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
axes[0].plot(days_vol, btc_price, color=COLOR_ORANGE, lw=1.5, alpha=0.7)
axes[0].set_ylabel('BTC Price (USD)', fontsize=12)
axes[0].set_title('Bitcoin: High Volatility', fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)
axes[1].plot(days_vol, usdc_price, color=COLOR_GREEN, lw=1.5, alpha=0.7)
axes[1].axhline(1, color='black', lw=1, linestyle='--', label='$1 Peg')
axes[1].set_ylabel('USDC Price (USD)', fontsize=12)
axes[1].set_xlabel('Days', fontsize=12)
axes[1].set_title('USDC Stablecoin: Stable Value', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(alpha=0.3)
plt.suptitle('Volatility Problem: Why Stablecoins?', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_22' / 'crypto_volatility.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Terra Death Spiral
days_terra = np.arange(0, 15)
ust_price = np.array([1.0, 0.98, 0.95, 0.85, 0.60, 0.30, 0.15, 0.08, 0.05, 0.03, 0.02, 0.01, 0.008, 0.005, 0.003])
luna_price = np.array([80, 70, 50, 30, 10, 2, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001])
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
axes[0].plot(days_terra, ust_price, color=COLOR_RED, lw=3, marker='o', markersize=6)
axes[0].axhline(1, color='black', lw=1, linestyle='--', alpha=0.5)
axes[0].set_ylabel('UST Price (USD)', fontsize=12)
axes[0].set_title('UST Depeg', fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)
axes[1].semilogy(days_terra, luna_price, color=COLOR_ORANGE, lw=3, marker='o', markersize=6)
axes[1].set_ylabel('LUNA Price (USD, log scale)', fontsize=12)
axes[1].set_xlabel('Days (May 2022)', fontsize=12)
axes[1].set_title('LUNA Collapse', fontsize=12, fontweight='bold')
axes[1].grid(alpha=0.3)
plt.suptitle('Terra/Luna Death Spiral (May 7-20, 2022)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_22' / 'terra_death_spiral.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Stablecoin Market Share
labels_stable = ['USDT\n(Tether)', 'USDC\n(Circle)', 'DAI\n(MakerDAO)', 'Others']
sizes_stable = [65, 20, 3, 12]
colors_stable = [COLOR_PRIMARY, COLOR_ACCENT, COLOR_GREEN, COLOR_SECONDARY]
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sizes_stable, labels=labels_stable, autopct='%1.0f%%',
                                     colors=colors_stable, startangle=90)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
ax.set_title('Stablecoin Market Share (2024)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_22' / 'stablecoin_market_share.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 22 charts complete (3 core charts)")

# ============================================================================
# LESSON 23: Security
# ============================================================================
print("\nGenerating Lesson 23 charts (Security)...")

# Chart 1: Crypto Hacks Timeline
years_hacks = ['2016\nThe DAO', '2018\nCoincheck', '2021\nPoly', '2022\nRonin', '2022\nWormhole', '2022\nFTX']
amounts_hacks = [60, 530, 611, 625, 325, 8000]  # Millions USD
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(len(years_hacks)), amounts_hacks, color=[COLOR_RED if amt > 500 else COLOR_ORANGE for amt in amounts_hacks],
                alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Amount Stolen (Million USD)', fontsize=12)
ax.set_title('Major Crypto Hacks Timeline', fontsize=14, fontweight='bold')
ax.set_xticks(range(len(years_hacks)))
ax.set_xticklabels(years_hacks, rotation=45, ha='right')
ax.grid(axis='y', alpha=0.3)
for i, (bar, amt) in enumerate(zip(bars, amounts_hacks)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 100, f'${amt}M', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_23' / 'crypto_hacks_timeline.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Reentrancy Flow
fig, ax = plt.subplots(figsize=(10, 7))
steps_re = [
    (0.5, 0.9, 'User calls withdraw()', COLOR_ACCENT),
    (0.5, 0.75, 'Contract sends ETH', COLOR_PRIMARY),
    (0.5, 0.6, 'Malicious contract receives', COLOR_RED),
    (0.5, 0.45, 'Calls withdraw() again!', COLOR_RED),
    (0.5, 0.3, 'Contract sends ETH again', COLOR_ORANGE),
    (0.5, 0.15, 'Repeat until drained', COLOR_RED)
]
for i, (x, y, text, color) in enumerate(steps_re):
    ax.text(x, y, text, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.6, edgecolor='black', linewidth=2))
    if i < len(steps_re) - 1:
        ax.annotate('', xy=(x, steps_re[i+1][1] + 0.04), xytext=(x, y - 0.04),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Reentrancy Attack Flow', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_23' / 'reentrancy_flow.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: Bridge Hacks Chart
bridge_names = ['Ronin', 'Poly\nNetwork', 'Wormhole', 'Nomad', 'Harmony']
bridge_amounts = [625, 611, 325, 190, 100]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(bridge_names, bridge_amounts, color=COLOR_RED, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Amount Stolen (Million USD)', fontsize=12)
ax.set_title('Major Bridge Hacks (2021-2022)', fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
for bar, amt in zip(bars, bridge_amounts):
    width = bar.get_width()
    ax.text(width + 20, bar.get_y() + bar.get_height()/2, f'${amt}M', va='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_23' / 'bridge_hacks_chart.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 23 charts complete (3 core charts)")

# ============================================================================
# LESSON 24: Regulation and Future
# ============================================================================
print("\nGenerating Lesson 24 charts (Regulation & Future)...")

# Chart 1: Global Regulatory Map (simplified)
fig, ax = plt.subplots(figsize=(12, 6))
regions = ['Switzerland\n(Permissive)', 'Singapore\n(Permissive)', 'EU\n(Moderate)', 'US\n(Restrictive)', 'China\n(Banned)']
scores = [9, 8, 6, 4, 1]  # Higher = more permissive
colors_reg = [COLOR_GREEN, COLOR_GREEN, COLOR_ACCENT, COLOR_ORANGE, COLOR_RED]
bars = ax.barh(regions, scores, color=colors_reg, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Regulatory Favorability Score (1-10)', fontsize=12)
ax.set_title('Global Crypto Regulatory Landscape (2024)', fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_24' / 'global_regulatory_map.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 2: Bitcoin ETF Inflows
months_etf = np.arange(0, 12)
inflows = np.cumsum([2, 4, 6, 8, 5, 7, 6, 4, 3, 5, 4, 6])  # Cumulative billions
fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(months_etf, inflows, alpha=0.4, color=COLOR_PRIMARY)
ax.plot(months_etf, inflows, color=COLOR_PRIMARY, lw=3, marker='o', markersize=8)
ax.set_xlabel('Months Since Approval (Jan 2024)', fontsize=12)
ax.set_ylabel('Cumulative Inflows (Billions USD)', fontsize=12)
ax.set_title('Bitcoin Spot ETF Inflows: First Year', fontsize=14, fontweight='bold')
ax.grid(alpha=0.3)
ax.annotate(f'Total: ${inflows[-1]}B', xy=(11, inflows[-1]), xytext=(9, inflows[-1]+5),
            arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(base_dir / 'lesson_24' / 'btc_etf_inflows.pdf', dpi=300, bbox_inches='tight')
plt.close()

# Chart 3: RWA Market Size Projection
years_rwa = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
market_size = [0.5, 1.5, 3, 5, 8, 12, 16]  # Trillions USD
fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(years_rwa, market_size, alpha=0.4, color=COLOR_GREEN)
ax.plot(years_rwa, market_size, color=COLOR_GREEN, lw=3, marker='s', markersize=8)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Size (Trillions USD)', fontsize=12)
ax.set_title('Real-World Asset (RWA) Tokenization: Projected Growth', fontsize=14, fontweight='bold')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(base_dir / 'lesson_24' / 'rwa_market_size.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Lesson 24 charts complete (3 core charts)")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("CHART GENERATION COMPLETE!")
print("="*70)
print(f"\nTotal charts generated: ~30+ charts across 10 lessons")
print(f"Output directory: {base_dir}")
print("\nChart breakdown:")
for lesson_num in range(15, 25):
    lesson_dir = base_dir / f"lesson_{lesson_num}"
    num_charts = len(list(lesson_dir.glob("*.pdf")))
    print(f"  Lesson {lesson_num}: {num_charts} charts")
print("\nAll charts saved as PDF files (300 DPI, publication quality)")
print("Ready for LaTeX Beamer compilation!")
