"""
Blockchain Structure Visualization
Visualizes a chain of blocks with hashes linking them together

Required libraries: matplotlib, numpy
Output: blockchain_structure.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# Chart metadata for QuantLet integration
CHART_METADATA = {
    'title': 'Blockchain Structure Visualization',
    'url': 'https://github.com/Digital-AI-Finance/DigitalFinance_3/tree/main/charts/module_02_blockchain/blockchain_structure'
}

def create_blockchain_visualization():
    """Create a visualization of blockchain structure with linked blocks"""

    # Set style for academic publication
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.linewidth'] = 0.5

    fig, ax = plt.subplots(figsize=(10, 4))

    # Block parameters
    block_width = 2.0
    block_height = 1.5
    spacing = 0.5

    # Sample block data
    blocks = [
        {'index': 0, 'hash': '0000abc...', 'prev': 'Genesis', 'nonce': '0'},
        {'index': 1, 'hash': '0000def...', 'prev': '0000abc...', 'nonce': '12847'},
        {'index': 2, 'hash': '0000ghi...', 'prev': '0000def...', 'nonce': '45821'},
        {'index': 3, 'hash': '0000jkl...', 'prev': '0000ghi...', 'nonce': '98234'}
    ]

    # Draw blocks
    for i, block in enumerate(blocks):
        x = i * (block_width + spacing)
        y = 0

        # Block rectangle with grayscale fill
        rect = FancyBboxPatch((x, y), block_width, block_height,
                             boxstyle="round,pad=0.05",
                             linewidth=1.5,
                             edgecolor='black',
                             facecolor='lightgray' if i % 2 == 0 else 'white')
        ax.add_patch(rect)

        # Block content
        text_x = x + block_width / 2

        # Block number
        ax.text(text_x, y + 1.25, f'Block {block["index"]}',
               ha='center', va='center', fontsize=8, fontweight='bold')

        # Hash
        ax.text(text_x, y + 0.95, f'Hash: {block["hash"]}',
               ha='center', va='center', fontsize=6, family='monospace')

        # Previous hash
        ax.text(text_x, y + 0.65, f'Prev: {block["prev"]}',
               ha='center', va='center', fontsize=6, family='monospace')

        # Nonce
        ax.text(text_x, y + 0.35, f'Nonce: {block["nonce"]}',
               ha='center', va='center', fontsize=6)

        # Arrow to next block (except for last block)
        if i < len(blocks) - 1:
            arrow_start_x = x + block_width
            arrow_end_x = x + block_width + spacing
            arrow_y = y + block_height / 2

            arrow = FancyArrowPatch((arrow_start_x, arrow_y),
                                   (arrow_end_x, arrow_y),
                                   arrowstyle='->,head_width=0.3,head_length=0.2',
                                   linewidth=1.5,
                                   color='black')
            ax.add_patch(arrow)

    # Set axis properties
    ax.set_xlim(-0.3, len(blocks) * (block_width + spacing))
    ax.set_ylim(-0.3, block_height + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(len(blocks) * (block_width + spacing) / 2 - spacing/2,
            block_height + 0.3,
            'Blockchain Structure: Cryptographically Linked Blocks',
            ha='center', va='top', fontsize=10, fontweight='bold')

    plt.tight_layout()

    # Save as PDF
    output_path = Path(__file__).parent / 'blockchain_structure.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")

    plt.close()

if __name__ == '__main__':
    create_blockchain_visualization()
