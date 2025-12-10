"""
Order Types in Algorithmic Trading
Market, Limit, Stop orders explained

Output: order_types.pdf
Module: module_03_ai_ml
Lesson: 29 - Algorithmic Trading Concepts
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'Order Types',
    'module': 'module_03_ai_ml',
    'lesson': 29,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/order_types'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    np.random.seed(42)
    time = np.arange(100)
    price = 100 + np.cumsum(np.random.randn(100) * 0.5)

    # Market Order
    ax1 = axes[0]
    ax1.plot(time, price, 'b-', linewidth=2, alpha=0.7)
    exec_time, exec_price = 50, price[50]
    ax1.axhline(y=exec_price, color='#D62728', linestyle='--', linewidth=1.5, alpha=0.7)
    ax1.scatter([exec_time], [exec_price], color='#D62728', s=150, zorder=5, marker='*')
    ax1.annotate('Immediate\nExecution', xy=(exec_time, exec_price),
                xytext=(exec_time+15, exec_price+2), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='#D62728'))
    ax1.set_title('Market Order\n(Execute at Current Price)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Price ($)')
    ax1.grid(True, alpha=0.3)

    # Limit Order
    ax2 = axes[1]
    ax2.plot(time, price, 'b-', linewidth=2, alpha=0.7)
    limit_price = 98
    ax2.axhline(y=limit_price, color='#44A044', linestyle='--', linewidth=2, label='Limit Price')
    # Find where price crosses limit
    cross_idx = np.where(price < limit_price)[0]
    if len(cross_idx) > 0:
        ax2.scatter([cross_idx[0]], [limit_price], color='#44A044', s=150, zorder=5, marker='*')
        ax2.annotate('Triggered\nwhen price\nreaches limit', xy=(cross_idx[0], limit_price),
                    xytext=(cross_idx[0]+15, limit_price+2), fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='#44A044'))
    ax2.fill_between(time, limit_price, min(price)-1, alpha=0.1, color='#44A044')
    ax2.set_title('Limit Order\n(Execute at Specified Price or Better)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Price ($)')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', fontsize=9)

    # Stop Loss Order
    ax3 = axes[2]
    ax3.plot(time, price, 'b-', linewidth=2, alpha=0.7)
    stop_price = 97
    ax3.axhline(y=stop_price, color='#D62728', linestyle='--', linewidth=2, label='Stop Price')
    cross_idx = np.where(price < stop_price)[0]
    if len(cross_idx) > 0:
        ax3.scatter([cross_idx[0]], [stop_price], color='#D62728', s=150, zorder=5, marker='*')
        ax3.annotate('Stop triggered\n(Becomes market order)', xy=(cross_idx[0], stop_price),
                    xytext=(cross_idx[0]+10, stop_price+3), fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='#D62728'))
    ax3.fill_between(time, stop_price, min(price)-1, alpha=0.1, color='#D62728')
    ax3.set_title('Stop-Loss Order\n(Trigger Sale Below Price)', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Price ($)')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper right', fontsize=9)

    fig.suptitle('Order Types in Algorithmic Trading', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'order_types.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
