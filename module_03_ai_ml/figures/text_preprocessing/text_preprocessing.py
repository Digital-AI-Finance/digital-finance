"""
Text Preprocessing Steps
NLP preprocessing pipeline example

Output: text_preprocessing.pdf
Module: module_03_ai_ml
Lesson: 32 - NLP in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CHART_METADATA = {
    'title': 'Text Preprocessing',
    'module': 'module_03_ai_ml',
    'lesson': 32,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/text_preprocessing'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)

    # Processing steps with examples
    steps = [
        ('Raw Text', '"Apple Inc. reported Q4 earnings of $1.24 per share, BEATING analysts\' expectations!!!"',
         '#E8E8E8', 9),
        ('Lowercase', '"apple inc. reported q4 earnings of $1.24 per share, beating analysts\' expectations!!!"',
         '#E3F2FD', 7.5),
        ('Remove Punctuation', '"apple inc reported q4 earnings of 1 24 per share beating analysts expectations"',
         '#E8F5E9', 6),
        ('Tokenization', '["apple", "inc", "reported", "q4", "earnings", "of", "1", "24", "per", "share", ...]',
         '#FFF3E0', 4.5),
        ('Remove Stop Words', '["apple", "inc", "reported", "q4", "earnings", "1", "24", "share", "beating", ...]',
         '#F3E5F5', 3),
        ('Lemmatization', '["apple", "inc", "report", "q4", "earning", "1", "24", "share", "beat", ...]',
         '#FFEBEE', 1.5),
    ]

    for step_name, example, color, y_pos in steps:
        # Step box
        rect = mpatches.FancyBboxPatch((0.5, y_pos-0.5), 2.5, 0.9,
                                        boxstyle="round,pad=0.05",
                                        facecolor='#4A90E2', alpha=0.8,
                                        edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(1.75, y_pos, step_name, ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        # Example box
        rect2 = mpatches.FancyBboxPatch((3.5, y_pos-0.5), 10, 0.9,
                                         boxstyle="round,pad=0.05",
                                         facecolor=color, alpha=0.8,
                                         edgecolor='#999999', linewidth=1)
        ax.add_patch(rect2)
        ax.text(8.5, y_pos, example, ha='center', va='center',
               fontsize=8, family='monospace')

        # Arrow to next step
        if y_pos > 2:
            ax.annotate('', xy=(1.75, y_pos-0.6), xytext=(1.75, y_pos-1.1),
                       arrowprops=dict(arrowstyle='->', color='#4A90E2', lw=2))

    ax.set_title('Text Preprocessing Pipeline for Financial NLP', fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')

    output_path = Path(__file__).parent / 'text_preprocessing.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
