"""
Feature Engineering in Finance
Common technical and fundamental features

Output: feature_engineering_finance.pdf
Module: module_03_ai_ml
Lesson: 26 - Financial Data
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Feature Engineering in Finance',
    'module': 'module_03_ai_ml',
    'lesson': 26,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/feature_engineering_finance'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Technical Features
    ax1 = axes[0]
    features_tech = ['Moving Averages', 'RSI', 'MACD', 'Bollinger Bands',
                     'Volume Indicators', 'Momentum', 'Volatility']
    importance_tech = [0.85, 0.78, 0.72, 0.68, 0.65, 0.62, 0.58]

    colors = ['#4A90E2' if i > 0.7 else '#6BB0E2' if i > 0.6 else '#999999' for i in importance_tech]
    ax1.barh(features_tech, importance_tech, color=colors, height=0.6)
    ax1.set_xlabel('Feature Importance', fontsize=11)
    ax1.set_title('Technical Features', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.xaxis.grid(True, alpha=0.3)

    # Fundamental Features
    ax2 = axes[1]
    features_fund = ['P/E Ratio', 'Debt/Equity', 'ROE', 'Revenue Growth',
                     'EPS Growth', 'Market Cap', 'Dividend Yield']
    importance_fund = [0.82, 0.75, 0.73, 0.70, 0.68, 0.55, 0.52]

    colors = ['#44A044' if i > 0.7 else '#6BD06B' if i > 0.6 else '#999999' for i in importance_fund]
    ax2.barh(features_fund, importance_fund, color=colors, height=0.6)
    ax2.set_xlabel('Feature Importance', fontsize=11)
    ax2.set_title('Fundamental Features', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.xaxis.grid(True, alpha=0.3)

    fig.suptitle('Feature Engineering for Financial ML Models', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'feature_engineering_finance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
