"""
DeFi Impermanent Loss Calculator and Visualization

This script demonstrates the concept of impermanent loss in automated market makers (AMMs)
used in decentralized finance protocols.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set font size globally
plt.rcParams.update({'font.size': 8})

def calculate_impermanent_loss(price_ratio):
    """
    Calculate impermanent loss for a given price ratio.

    Parameters:
    -----------
    price_ratio : float
        Ratio of final price to initial price (P1/P0)

    Returns:
    --------
    float
        Impermanent loss as a percentage
    """
    # AMM formula: k = x * y (constant product)
    # IL = (2 * sqrt(price_ratio)) / (1 + price_ratio) - 1
    il = (2 * np.sqrt(price_ratio)) / (1 + price_ratio) - 1
    return il * 100

def calculate_hodl_return(price_ratio):
    """Calculate simple HODL return."""
    return ((price_ratio - 1) / 2) * 100  # Average of 50/50 portfolio

def main():
    # Generate price ratio range (0.1x to 10x)
    price_ratios = np.linspace(0.1, 10, 500)

    # Calculate impermanent loss for each ratio
    il_values = [calculate_impermanent_loss(pr) for pr in price_ratios]

    # Calculate HODL returns
    hodl_values = [calculate_hodl_return(pr) for pr in price_ratios]

    # Calculate LP returns (HODL - IL)
    lp_values = [hodl - il for hodl, il in zip(hodl_values, il_values)]

    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Plot 1: Impermanent Loss vs Price Change
    ax1.plot(price_ratios, il_values, 'k-', linewidth=1.5, label='Impermanent Loss')
    ax1.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    ax1.axvline(x=1, color='gray', linestyle='--', linewidth=0.5)

    # Highlight key points
    key_points = [0.5, 1.0, 2.0, 4.0]
    for point in key_points:
        il_at_point = calculate_impermanent_loss(point)
        ax1.plot(point, il_at_point, 'o', color='black', markersize=5)
        ax1.annotate(f'{il_at_point:.1f}%',
                    xy=(point, il_at_point),
                    xytext=(10, -10), textcoords='offset points',
                    fontsize=7, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    ax1.set_xlabel('Price Ratio (Final/Initial)', fontsize=8)
    ax1.set_ylabel('Impermanent Loss (%)', fontsize=8)
    ax1.set_title('Impermanent Loss vs Price Change', fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 10)
    ax1.legend(fontsize=7)

    # Plot 2: LP vs HODL comparison
    ax2.plot(price_ratios, hodl_values, 'k--', linewidth=1.5, label='HODL (50/50)', alpha=0.7)
    ax2.plot(price_ratios, lp_values, 'k-', linewidth=1.5, label='LP Position')
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
    ax2.axvline(x=1, color='gray', linestyle='--', linewidth=0.5)

    # Fill area between HODL and LP (impermanent loss)
    ax2.fill_between(price_ratios, hodl_values, lp_values,
                     where=(np.array(hodl_values) >= np.array(lp_values)),
                     alpha=0.3, color='gray', label='Impermanent Loss')

    ax2.set_xlabel('Price Ratio (Final/Initial)', fontsize=8)
    ax2.set_ylabel('Return (%)', fontsize=8)
    ax2.set_title('Liquidity Provider vs HODL Returns', fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 10)
    ax2.legend(fontsize=7, loc='upper left')

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'defi_impermanent_loss.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print example calculations
    print("\nImpermanent Loss Examples:")
    print("-" * 50)
    examples = [
        ("No change (1x)", 1.0),
        ("2x increase", 2.0),
        ("5x increase", 5.0),
        ("50% decrease (0.5x)", 0.5),
        ("80% decrease (0.2x)", 0.2)
    ]

    for description, ratio in examples:
        il = calculate_impermanent_loss(ratio)
        print(f"{description:25s}: {il:6.2f}% loss")

    print("\nNote: IL is always negative (a loss), but can be offset by trading fees")

if __name__ == '__main__':
    main()
