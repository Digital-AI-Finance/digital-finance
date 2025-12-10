"""
Word Embeddings Visualization
Financial word vectors in 2D

Output: word_embeddings.pdf
Module: module_03_ai_ml
Lesson: 32 - NLP in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Word Embeddings',
    'module': 'module_03_ai_ml',
    'lesson': 32,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/word_embeddings'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(12, 10))

    np.random.seed(42)

    # Word clusters (simulated 2D projections)
    clusters = {
        'Financial Terms': {
            'words': ['stock', 'equity', 'shares', 'market', 'trading'],
            'center': (2, 3),
            'color': '#4A90E2'
        },
        'Positive Sentiment': {
            'words': ['growth', 'profit', 'gain', 'surge', 'bullish'],
            'center': (6, 7),
            'color': '#44A044'
        },
        'Negative Sentiment': {
            'words': ['loss', 'decline', 'crash', 'bearish', 'risk'],
            'center': (-2, -3),
            'color': '#D62728'
        },
        'Companies': {
            'words': ['Apple', 'Google', 'Amazon', 'Tesla', 'Microsoft'],
            'center': (-4, 5),
            'color': '#9B59B6'
        },
        'Metrics': {
            'words': ['revenue', 'earnings', 'PE ratio', 'dividend', 'EPS'],
            'center': (5, -2),
            'color': '#FF7F0E'
        }
    }

    for cluster_name, data in clusters.items():
        center = data['center']
        words = data['words']
        color = data['color']

        # Scatter words around cluster center
        x_coords = [center[0] + np.random.randn() * 0.8 for _ in words]
        y_coords = [center[1] + np.random.randn() * 0.8 for _ in words]

        ax.scatter(x_coords, y_coords, s=100, c=color, alpha=0.7, edgecolors='black')

        for word, x, y in zip(words, x_coords, y_coords):
            ax.annotate(word, (x, y), xytext=(5, 5), textcoords='offset points',
                       fontsize=9, fontweight='bold')

        # Cluster label
        ax.annotate(cluster_name, center, fontsize=11, fontweight='bold',
                   color=color, ha='center',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # Draw relationship arrows
    ax.annotate('', xy=(5.5, 6.5), xytext=(2.5, 3.5),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5, ls='--'))
    ax.text(4, 5.2, 'Semantic\nSimilarity', fontsize=8, ha='center', color='gray')

    ax.set_xlabel('Embedding Dimension 1 (t-SNE)', fontsize=11)
    ax.set_ylabel('Embedding Dimension 2 (t-SNE)', fontsize=11)
    ax.set_title('Word Embeddings: Financial Vocabulary Clusters', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(-7, 9)
    ax.set_ylim(-6, 10)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'word_embeddings.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
