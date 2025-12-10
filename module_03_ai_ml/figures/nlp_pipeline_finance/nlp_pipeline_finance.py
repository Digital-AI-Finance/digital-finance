"""
NLP Pipeline for Finance
Natural Language Processing workflow

Output: nlp_pipeline_finance.pdf
Module: module_03_ai_ml
Lesson: 32 - NLP in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'NLP Pipeline Finance',
    'module': 'module_03_ai_ml',
    'lesson': 32,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/nlp_pipeline_finance'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)

    # Pipeline stages
    stages = [
        (2, 5, 'Raw Text\nSources', '#4A90E2',
         ['News Articles', 'SEC Filings', 'Earnings Calls', 'Social Media']),
        (5, 5, 'Preprocessing', '#44A044',
         ['Tokenization', 'Stop Words', 'Lemmatization', 'NER']),
        (8, 5, 'Feature\nExtraction', '#FF7F0E',
         ['TF-IDF', 'Word2Vec', 'BERT Embed', 'N-grams']),
        (11, 5, 'Analysis', '#9B59B6',
         ['Sentiment', 'Topic Model', 'Entity Link', 'QA']),
        (14, 5, 'Application', '#D62728',
         ['Trading Signal', 'Risk Alert', 'Report Gen', 'Chatbot'])
    ]

    for x, y, label, color, items in stages:
        # Main box
        rect = mpatches.FancyBboxPatch((x-1.2, y-0.7), 2.4, 1.4,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')

        # Items below
        for i, item in enumerate(items):
            ax.text(x, y - 1.3 - i*0.35, f'{item}', ha='center', va='top',
                   fontsize=8, color='#333333')

        # Arrows
        if x < 14:
            ax.annotate('', xy=(x+1.8, y), xytext=(x+1.3, y),
                       arrowprops=dict(arrowstyle='->', color='black', lw=2))

    # Add example text flow
    ax.text(8, 7.3, 'Example: "Apple reports record Q4 revenue, beating analyst expectations"',
           ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

    ax.set_title('NLP Pipeline for Financial Text Analysis', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'nlp_pipeline_finance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
