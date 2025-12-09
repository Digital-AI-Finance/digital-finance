"""
RegTech Cost Savings
Shows ROI and cost savings from RegTech implementation

Output: regtech_cost_savings.pdf
Module: module_01_fintech
Lesson: 10 - RegTech
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'RegTech Cost Savings',
    'module': 'module_01_fintech',
    'lesson': 10,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/regtech_cost_savings'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create RegTech cost savings comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    categories = ['KYC/Onboarding', 'AML\nMonitoring', 'Regulatory\nReporting', 'Compliance\nTraining', 'Audit\nPreparation']
    traditional = [100, 100, 100, 100, 100]  # Baseline
    regtech = [35, 45, 30, 50, 40]  # Cost with RegTech (as % of traditional)

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, traditional, width, label='Traditional', color='#D62728',
                   edgecolor='#333333', lw=1.5)
    bars2 = ax.bar(x + width/2, regtech, width, label='With RegTech', color='#44A044',
                   edgecolor='#333333', lw=1.5)

    ax.set_ylabel('Relative Cost (Traditional = 100)', fontsize=14)
    ax.set_title('RegTech Cost Reduction by Function', fontsize=20, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=12)
    ax.legend(fontsize=12)
    ax.set_ylim(0, 120)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add savings labels
    for i, (trad, reg) in enumerate(zip(traditional, regtech)):
        savings = trad - reg
        ax.annotate(f'-{savings}%',
                   xy=(x[i] + width/2, reg),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=12, fontweight='bold', color='#44A044')

    # Average savings
    avg_savings = 100 - np.mean(regtech)
    ax.text(0.98, 0.95, f'Average Savings:\n{avg_savings:.0f}%',
           transform=ax.transAxes, fontsize=14, fontweight='bold',
           ha='right', va='top', color='#44A044',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#44A044'))

    # ROI note
    ax.text(0.02, 0.02, 'Typical ROI: 3-5x within 2 years | Payback period: 6-18 months',
           transform=ax.transAxes, fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#E8F4EA', edgecolor='#44A044'))

    # Source
    fig.text(0.5, 0.02, 'Source: Deloitte RegTech study, McKinsey analysis (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    output_path = Path(__file__).parent / 'regtech_cost_savings.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
