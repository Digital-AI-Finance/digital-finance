"""
Trading Algorithm Comparison
Performance of different algo trading strategies

Output: algorithm_comparison.pdf
Module: module_03_ai_ml
Lesson: 29 - Algorithmic Trading Concepts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Algorithm Comparison',
    'module': 'module_03_ai_ml',
    'lesson': 29,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/algorithm_comparison'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Algorithm Performance Metrics
    ax1 = axes[0]
    algorithms = ['TWAP', 'VWAP', 'Arrival\nPrice', 'Market\nMaking', 'Momentum', 'Mean\nReversion']

    # Performance metrics (normalized 0-100)
    execution_quality = [75, 82, 88, 70, 65, 72]
    risk_adjusted = [80, 78, 85, 60, 55, 68]
    market_impact = [20, 25, 15, 40, 45, 35]  # Lower is better

    x = np.arange(len(algorithms))
    width = 0.25

    bars1 = ax1.bar(x - width, execution_quality, width, label='Execution Quality', color='#4A90E2', alpha=0.8)
    bars2 = ax1.bar(x, risk_adjusted, width, label='Risk-Adjusted Return', color='#44A044', alpha=0.8)
    bars3 = ax1.bar(x + width, market_impact, width, label='Market Impact', color='#D62728', alpha=0.8)

    ax1.set_xlabel('Algorithm Type', fontsize=11)
    ax1.set_ylabel('Score (0-100)', fontsize=11)
    ax1.set_title('Algorithm Performance Comparison', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(algorithms, fontsize=9)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 100)
    ax1.yaxis.grid(True, alpha=0.3)

    # Use Case Heatmap
    ax2 = axes[1]
    use_cases = ['Large Orders', 'Volatile Markets', 'High Liquidity', 'Low Latency', 'Passive Income']

    suitability = np.array([
        [90, 85, 70, 40, 20],   # TWAP
        [85, 75, 80, 50, 25],   # VWAP
        [80, 60, 85, 70, 30],   # Arrival Price
        [40, 50, 90, 95, 85],   # Market Making
        [50, 80, 60, 80, 40],   # Momentum
        [55, 85, 70, 70, 50]    # Mean Reversion
    ])

    im = ax2.imshow(suitability, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)

    ax2.set_xticks(np.arange(len(use_cases)))
    ax2.set_yticks(np.arange(len(algorithms)))
    ax2.set_xticklabels(use_cases, fontsize=9, rotation=30, ha='right')
    ax2.set_yticklabels([a.replace('\n', ' ') for a in algorithms], fontsize=9)

    # Add text annotations
    for i in range(len(algorithms)):
        for j in range(len(use_cases)):
            text_color = 'white' if suitability[i, j] < 50 or suitability[i, j] > 80 else 'black'
            ax2.text(j, i, f'{suitability[i, j]}', ha='center', va='center',
                    color=text_color, fontsize=9, fontweight='bold')

    ax2.set_title('Algorithm Suitability by Use Case', fontsize=12, fontweight='bold')

    cbar = plt.colorbar(im, ax=ax2, shrink=0.8)
    cbar.set_label('Suitability Score', fontsize=10)

    fig.suptitle('Algorithmic Trading Strategy Analysis', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'algorithm_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
