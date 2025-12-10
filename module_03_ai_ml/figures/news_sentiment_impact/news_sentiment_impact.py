"""
News Sentiment Impact on Markets
Event study of news impact

Output: news_sentiment_impact.pdf
Module: module_03_ai_ml
Lesson: 32 - NLP in Finance
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'News Sentiment Impact',
    'module': 'module_03_ai_ml',
    'lesson': 32,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/news_sentiment_impact'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # Event study: CAR around news
    ax1 = axes[0]

    days = np.arange(-10, 11)

    # Positive news event
    car_positive = np.zeros(21)
    car_positive[10:] = np.cumsum([0.015, 0.012, 0.005, 0.003, 0.002, 0.001, 0.001, 0, 0, 0, 0])
    car_positive += np.random.randn(21) * 0.002

    # Negative news event
    car_negative = np.zeros(21)
    car_negative[10:] = np.cumsum([-0.02, -0.015, -0.008, -0.004, -0.002, -0.001, 0, 0.001, 0.001, 0, 0])
    car_negative += np.random.randn(21) * 0.002

    ax1.plot(days, car_positive * 100, 'g-', linewidth=2.5, label='Positive News', marker='o', markersize=4)
    ax1.plot(days, car_negative * 100, 'r-', linewidth=2.5, label='Negative News', marker='s', markersize=4)
    ax1.axvline(x=0, color='black', linestyle='--', linewidth=2, label='News Release')
    ax1.axhline(y=0, color='gray', linewidth=1)

    ax1.fill_between(days, 0, car_positive * 100, alpha=0.2, color='green')
    ax1.fill_between(days, 0, car_negative * 100, alpha=0.2, color='red')

    ax1.set_xlabel('Days Relative to News Event', fontsize=11)
    ax1.set_ylabel('Cumulative Abnormal Return (%)', fontsize=11)
    ax1.set_title('Event Study: News Impact on Stock Returns', fontsize=12, fontweight='bold')
    ax1.legend(loc='best', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-10, 10)

    # Sentiment-Return Correlation by Source
    ax2 = axes[1]

    sources = ['Earnings\nCalls', 'SEC\nFilings', 'News\nWires', 'Social\nMedia', 'Analyst\nReports']
    correlations = [0.42, 0.38, 0.28, 0.15, 0.35]
    signal_lag = [0, 1, 0.5, 0.2, 2]  # Days until market reaction

    colors = plt.cm.RdYlGn(np.array(correlations) / max(correlations))

    bars = ax2.bar(sources, correlations, color=colors, edgecolor='black', alpha=0.8)

    for bar, corr, lag in zip(bars, correlations, signal_lag):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'r={corr:.2f}', ha='center', fontsize=9, fontweight='bold')

    # Add signal quality line
    ax2_twin = ax2.twinx()
    ax2_twin.plot(sources, signal_lag, 'ro-', linewidth=2, markersize=8, label='Signal Lag (days)')
    ax2_twin.set_ylabel('Signal Lag (Days)', fontsize=10, color='#D62728')
    ax2_twin.tick_params(axis='y', labelcolor='#D62728')
    ax2_twin.set_ylim(0, 3)

    ax2.set_xlabel('Text Source', fontsize=11)
    ax2.set_ylabel('Sentiment-Return Correlation', fontsize=11)
    ax2.set_title('Predictive Power by Text Source', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 0.55)
    ax2.yaxis.grid(True, alpha=0.3)
    ax2_twin.legend(loc='upper right', fontsize=9)

    fig.suptitle('News Sentiment Impact Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'news_sentiment_impact.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
