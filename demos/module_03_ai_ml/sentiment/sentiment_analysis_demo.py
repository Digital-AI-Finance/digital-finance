"""
Financial News Sentiment Analysis Demonstration

This script demonstrates sentiment analysis on financial news headlines
using a simple rule-based approach with visualization of sentiment scores.

Author: BSc Digital Finance Course
Date: 2025-12-07
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime, timedelta

# Set font size globally and random seed
plt.rcParams.update({'font.size': 8})
np.random.seed(42)

# Simple sentiment lexicon for financial news
POSITIVE_WORDS = [
    'profit', 'gains', 'surge', 'rally', 'growth', 'beat', 'strong', 'soar',
    'positive', 'upgrade', 'bullish', 'recovery', 'expansion', 'breakthrough'
]

NEGATIVE_WORDS = [
    'loss', 'decline', 'crash', 'fall', 'weak', 'miss', 'slump', 'plunge',
    'negative', 'downgrade', 'bearish', 'recession', 'contraction', 'crisis'
]

# Sample financial headlines
HEADLINES = [
    "Tech stocks surge on strong earnings reports",
    "Market crash fears grow amid inflation concerns",
    "Company beats profit expectations in Q3",
    "Oil prices plunge on oversupply worries",
    "Federal Reserve signals positive economic outlook",
    "Banking sector faces major crisis",
    "Stock rally continues for third consecutive day",
    "Weak consumer spending data disappoints investors",
    "Breakthrough in renewable energy boosts green stocks",
    "Economic recession fears trigger market selloff",
    "Strong job growth signals healthy economy",
    "Corporate earnings miss analyst expectations",
    "Bullish sentiment drives market to new highs",
    "Trade tensions lead to market uncertainty",
    "Innovation in fintech attracts investor interest"
]

def calculate_sentiment_score(text):
    """
    Calculate sentiment score for a text using simple word counting.

    Returns:
    --------
    float
        Sentiment score between -1 (very negative) and +1 (very positive)
    """
    text_lower = text.lower()
    words = text_lower.split()

    positive_count = sum(1 for word in words if word in POSITIVE_WORDS)
    negative_count = sum(1 for word in words if word in NEGATIVE_WORDS)

    total_sentiment_words = positive_count + negative_count

    if total_sentiment_words == 0:
        return 0.0

    score = (positive_count - negative_count) / total_sentiment_words
    return score

def classify_sentiment(score):
    """Classify sentiment score into categories."""
    if score > 0.3:
        return 'Positive'
    elif score < -0.3:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    # Calculate sentiment scores
    scores = [calculate_sentiment_score(headline) for headline in HEADLINES]
    sentiments = [classify_sentiment(score) for score in scores]

    # Generate timestamps (last 15 days)
    end_date = datetime.now()
    dates = [end_date - timedelta(days=i) for i in range(len(HEADLINES)-1, -1, -1)]

    # Create visualization
    fig = plt.figure(figsize=(10, 7))
    gs = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])

    # Plot 1: Sentiment scores over time
    colors = ['black' if s > 0.3 else 'gray' if s > -0.3 else 'darkgray' for s in scores]
    markers = ['^' if s > 0.3 else 'o' if s > -0.3 else 'v' for s in scores]

    for i, (date, score, color, marker) in enumerate(zip(dates, scores, colors, markers)):
        ax1.plot(date, score, marker=marker, color=color, markersize=8,
                markeredgecolor='black', markeredgewidth=0.5)

    # Connect points with line
    ax1.plot(dates, scores, 'k-', alpha=0.3, linewidth=0.5)

    # Add sentiment zones
    ax1.axhspan(0.3, 1.0, alpha=0.1, color='black', label='Positive zone')
    ax1.axhspan(-0.3, 0.3, alpha=0.05, color='gray', label='Neutral zone')
    ax1.axhspan(-1.0, -0.3, alpha=0.15, color='gray', label='Negative zone')
    ax1.axhline(y=0, color='black', linestyle='--', linewidth=0.5)

    ax1.set_ylabel('Sentiment Score', fontsize=8)
    ax1.set_title('Financial News Sentiment Analysis Over Time', fontsize=8)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.legend(fontsize=6, loc='upper left')
    ax1.set_ylim(-1.1, 1.1)

    # Plot 2: Distribution of sentiment scores
    ax2.hist(scores, bins=15, color='gray', edgecolor='black', alpha=0.7)
    ax2.axvline(x=0, color='black', linestyle='--', linewidth=1)
    ax2.axvline(x=np.mean(scores), color='black', linestyle='-', linewidth=1.5,
               label=f'Mean: {np.mean(scores):.2f}')
    ax2.set_xlabel('Sentiment Score', fontsize=8)
    ax2.set_ylabel('Frequency', fontsize=8)
    ax2.set_title('Distribution of Sentiment Scores', fontsize=8)
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.3, axis='y')

    # Plot 3: Sentiment category breakdown
    sentiment_counts = {
        'Positive': sentiments.count('Positive'),
        'Neutral': sentiments.count('Neutral'),
        'Negative': sentiments.count('Negative')
    }

    categories = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())
    colors_bar = ['black', 'gray', 'darkgray']

    bars = ax3.bar(categories, counts, color=colors_bar, edgecolor='black', alpha=0.7)

    # Add count labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({count/len(HEADLINES)*100:.0f}%)',
                ha='center', va='bottom', fontsize=7)

    ax3.set_ylabel('Count', fontsize=8)
    ax3.set_title('Sentiment Category Distribution', fontsize=8)
    ax3.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    # Save output
    output_path = Path(__file__).parent / 'sentiment_analysis_demo.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Output saved to: {output_path}")

    # Print detailed results
    print("\nSentiment Analysis Results:")
    print("-" * 70)
    print(f"{'Headline':<50} {'Score':>8} {'Sentiment':>12}")
    print("-" * 70)

    for headline, score, sentiment in zip(HEADLINES, scores, sentiments):
        headline_short = headline[:47] + '...' if len(headline) > 50 else headline
        print(f"{headline_short:<50} {score:>8.2f} {sentiment:>12}")

    print("-" * 70)
    print(f"Average sentiment score: {np.mean(scores):.3f}")
    print(f"Sentiment volatility (std): {np.std(scores):.3f}")
    print(f"\nPositive headlines: {sentiment_counts['Positive']} ({sentiment_counts['Positive']/len(HEADLINES)*100:.1f}%)")
    print(f"Neutral headlines:  {sentiment_counts['Neutral']} ({sentiment_counts['Neutral']/len(HEADLINES)*100:.1f}%)")
    print(f"Negative headlines: {sentiment_counts['Negative']} ({sentiment_counts['Negative']/len(HEADLINES)*100:.1f}%)")

if __name__ == '__main__':
    main()
