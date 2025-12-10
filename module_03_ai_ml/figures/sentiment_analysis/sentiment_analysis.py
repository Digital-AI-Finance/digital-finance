"""
Sentiment Analysis Results
Financial news sentiment scoring

Output: sentiment_analysis.pdf
Module: module_03_ai_ml
Lesson: 32 - NLP in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Sentiment Analysis',
    'module': 'module_03_ai_ml',
    'lesson': 32,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/sentiment_analysis'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Sentiment distribution
    ax1 = axes[0]

    categories = ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
    counts = [85, 220, 450, 280, 65]
    colors = ['#D62728', '#FF7F0E', '#888888', '#90EE90', '#44A044']

    bars = ax1.bar(categories, counts, color=colors, edgecolor='black', alpha=0.8)

    for bar, count in zip(bars, counts):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                str(count), ha='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Sentiment Category', fontsize=11)
    ax1.set_ylabel('Number of Articles', fontsize=11)
    ax1.set_title('News Sentiment Distribution (Sample)', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 550)
    ax1.yaxis.grid(True, alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=20, ha='right')

    # Sentiment over time with price
    ax2 = axes[1]

    days = np.arange(60)
    # Generate sentiment scores
    sentiment = np.random.randn(60) * 0.2
    sentiment[20:30] += 0.4  # Positive news period
    sentiment[40:50] -= 0.3  # Negative news period
    sentiment = np.convolve(sentiment, np.ones(5)/5, mode='same')

    # Correlated price movement
    price = 100 + np.cumsum(sentiment * 2 + np.random.randn(60) * 0.3)

    ax2_twin = ax2.twinx()

    ln1 = ax2.bar(days, sentiment, color=['#44A044' if s > 0 else '#D62728' for s in sentiment],
                  alpha=0.6, width=0.8, label='Sentiment')
    ln2 = ax2_twin.plot(days, price, 'b-', linewidth=2, label='Stock Price')

    ax2.axhline(y=0, color='black', linewidth=1)
    ax2.set_xlabel('Days', fontsize=11)
    ax2.set_ylabel('Sentiment Score', fontsize=11)
    ax2_twin.set_ylabel('Stock Price ($)', fontsize=11, color='#4A90E2')
    ax2_twin.tick_params(axis='y', labelcolor='#4A90E2')
    ax2.set_title('Sentiment vs. Price Movement', fontsize=12, fontweight='bold')

    # Annotate correlation
    ax2.annotate('Positive News\nImpact', xy=(25, 0.3), xytext=(30, 0.5),
                fontsize=9, fontweight='bold', color='#44A044',
                arrowprops=dict(arrowstyle='->', color='#44A044'))

    ax2.set_ylim(-0.8, 0.8)
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)

    fig.suptitle('Financial Sentiment Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'sentiment_analysis.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
