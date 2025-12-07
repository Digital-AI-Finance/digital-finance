"""
SHA-256 Avalanche Effect Demonstration

This script demonstrates the avalanche effect in cryptographic hash functions.
Shows how small input changes produce drastically different hash outputs.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import hashlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set font size globally
plt.rcParams.update({'font.size': 8})

def sha256_hash(text):
    """Calculate SHA-256 hash of input text."""
    return hashlib.sha256(text.encode()).hexdigest()

def hash_to_binary(hash_hex):
    """Convert hexadecimal hash to binary string."""
    return bin(int(hash_hex, 16))[2:].zfill(256)

def hamming_distance(bin1, bin2):
    """Calculate Hamming distance between two binary strings."""
    return sum(c1 != c2 for c1, c2 in zip(bin1, bin2))

def main():
    # Original message and variations
    messages = [
        "Bitcoin",
        "bitcoin",  # Changed case
        "Bitcoin ",  # Added space
        "Bitcoin!",  # Added character
        "Bitcoim",  # Changed letter
    ]

    # Calculate hashes
    hashes = [sha256_hash(msg) for msg in messages]
    binary_hashes = [hash_to_binary(h) for h in hashes]

    # Calculate Hamming distances from original
    distances = [hamming_distance(binary_hashes[0], bh) for bh in binary_hashes]

    # Create visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    # Plot 1: Hamming distances
    bars = ax1.bar(range(len(messages)), distances, color='gray', edgecolor='black')
    bars[0].set_color('lightgray')  # Highlight original
    ax1.set_ylabel('Hamming Distance (bits changed)', fontsize=8)
    ax1.set_xlabel('Input Variation', fontsize=8)
    ax1.set_title('SHA-256 Avalanche Effect: Bit Changes per Input Modification', fontsize=8)
    ax1.set_xticks(range(len(messages)))
    ax1.set_xticklabels([f'"{msg}"' for msg in messages], rotation=15, ha='right', fontsize=7)
    ax1.axhline(y=128, color='black', linestyle='--', linewidth=0.5, label='Expected (50%)')
    ax1.legend(fontsize=7)
    ax1.grid(axis='y', alpha=0.3)

    # Add percentage labels on bars
    for i, (bar, dist) in enumerate(zip(bars, distances)):
        percentage = (dist / 256) * 100
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{dist}\n({percentage:.1f}%)', ha='center', va='bottom', fontsize=7)

    # Plot 2: Binary hash visualization (first 128 bits for clarity)
    binary_matrix = np.array([[int(bit) for bit in bh[:128]] for bh in binary_hashes])

    im = ax2.imshow(binary_matrix, cmap='gray', aspect='auto', interpolation='nearest')
    ax2.set_ylabel('Input Variation', fontsize=8)
    ax2.set_xlabel('Hash Bit Position (first 128 of 256 bits)', fontsize=8)
    ax2.set_title('Binary Hash Patterns (0=black, 1=white)', fontsize=8)
    ax2.set_yticks(range(len(messages)))
    ax2.set_yticklabels([f'"{msg}"' for msg in messages], fontsize=7)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax2, orientation='vertical', pad=0.02)
    cbar.set_label('Bit Value', fontsize=7)
    cbar.ax.tick_params(labelsize=7)

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'hash_demonstration.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print hash values for reference
    print("\nHash Values:")
    for msg, hash_val in zip(messages, hashes):
        print(f'"{msg}": {hash_val}')

if __name__ == '__main__':
    main()
