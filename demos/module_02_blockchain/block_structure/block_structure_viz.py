"""
Blockchain Structure Visualization

This script visualizes how blocks are linked together in a blockchain
through cryptographic hashing.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import hashlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Set font size globally
plt.rcParams.update({'font.size': 8})

class Block:
    """Simple block structure for demonstration."""

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate block hash based on content."""
        block_string = f"{self.index}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()[:16]  # Shortened for display

def create_blockchain():
    """Create a simple blockchain with 4 blocks."""
    blockchain = []

    # Genesis block
    genesis = Block(0, "Genesis Block", "0" * 16)
    blockchain.append(genesis)

    # Add three more blocks
    blockchain.append(Block(1, "Alice -> Bob: 10 BTC", blockchain[-1].hash))
    blockchain.append(Block(2, "Bob -> Carol: 5 BTC", blockchain[-1].hash))
    blockchain.append(Block(3, "Carol -> Dave: 3 BTC", blockchain[-1].hash))

    return blockchain

def visualize_blockchain(blockchain):
    """Create visualization of blockchain structure."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Block dimensions
    block_width = 2.0
    block_height = 1.5
    spacing = 0.5
    start_x = 0.5
    y_position = 3.0

    # Draw each block
    for i, block in enumerate(blockchain):
        x = start_x + i * (block_width + spacing)

        # Main block rectangle
        rect = mpatches.FancyBboxPatch((x, y_position), block_width, block_height,
                                       boxstyle="round,pad=0.05",
                                       edgecolor='black', facecolor='lightgray',
                                       linewidth=1.5)
        ax.add_patch(rect)

        # Block content
        ax.text(x + block_width/2, y_position + block_height - 0.2,
               f'Block {block.index}', ha='center', va='top', fontsize=8, weight='bold')

        ax.text(x + 0.1, y_position + block_height - 0.5,
               f'Data:', ha='left', va='top', fontsize=7)
        ax.text(x + 0.1, y_position + block_height - 0.75,
               f'{block.data[:20]}...', ha='left', va='top', fontsize=6, style='italic')

        ax.text(x + 0.1, y_position + 0.6,
               f'Prev: {block.previous_hash[:12]}...', ha='left', va='top', fontsize=6,
               family='monospace')

        ax.text(x + 0.1, y_position + 0.3,
               f'Hash: {block.hash[:12]}...', ha='left', va='top', fontsize=6,
               family='monospace', weight='bold')

        # Draw arrow to next block
        if i < len(blockchain) - 1:
            arrow_start_x = x + block_width
            arrow_end_x = x + block_width + spacing
            arrow_y = y_position + block_height/2

            ax.annotate('', xy=(arrow_end_x, arrow_y), xytext=(arrow_start_x, arrow_y),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))

            # Label the link
            ax.text(arrow_start_x + spacing/2, arrow_y + 0.15,
                   'hash link', ha='center', va='bottom', fontsize=6, style='italic')

    # Add title and labels
    ax.set_title('Blockchain Structure: Cryptographic Linking of Blocks', fontsize=8, pad=20)

    # Add annotations
    ax.text(start_x, y_position - 0.5,
           'Genesis Block\n(no previous hash)', ha='left', va='top', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    # Add explanation text
    explanation = (
        "Each block contains:\n"
        "- Block index\n"
        "- Transaction data\n"
        "- Previous block hash\n"
        "- Current block hash\n\n"
        "Changing any block breaks\n"
        "the chain!"
    )
    ax.text(start_x + 4 * (block_width + spacing) - 0.3, y_position - 0.5,
           explanation, ha='left', va='top', fontsize=7,
           bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray'))

    # Set axis properties
    ax.set_xlim(0, start_x + 4 * (block_width + spacing))
    ax.set_ylim(0, y_position + block_height + 0.5)
    ax.axis('off')

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'block_structure_viz.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print block information
    print("\nBlockchain Details:")
    for block in blockchain:
        print(f"Block {block.index}:")
        print(f"  Data: {block.data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print()

def main():
    blockchain = create_blockchain()
    visualize_blockchain(blockchain)

if __name__ == '__main__':
    main()
