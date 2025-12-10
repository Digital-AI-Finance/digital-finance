"""
PDP and ICE Plots
Partial Dependence and Individual Conditional Expectation

Output: pdp_ice_plots.pdf
Module: module_03_ai_ml
Lesson: 35 - Explainability
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CHART_METADATA = {
    'title': 'PDP ICE Plots',
    'module': 'module_03_ai_ml',
    'lesson': 35,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_03_ai_ml/figures/pdp_ice_plots'
}

plt.rcParams.update({'font.size': 10, 'axes.labelsize': 10})

def create_chart():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    np.random.seed(42)

    # PDP: Debt-to-Income vs Default Probability
    ax1 = axes[0]

    dti = np.linspace(0.1, 0.8, 50)

    # ICE curves (individual)
    n_ice = 30
    for i in range(n_ice):
        offset = np.random.randn() * 0.05
        slope_var = np.random.uniform(0.8, 1.2)
        ice = 0.1 + slope_var * 0.5 * (1 / (1 + np.exp(-10 * (dti - 0.4)))) + offset
        ice = np.clip(ice, 0, 1)
        ax1.plot(dti * 100, ice, 'b-', alpha=0.15, linewidth=1)

    # PDP (average)
    pdp = 0.1 + 0.5 * (1 / (1 + np.exp(-10 * (dti - 0.4))))
    ax1.plot(dti * 100, pdp, 'r-', linewidth=3, label='PDP (Average)')

    ax1.set_xlabel('Debt-to-Income Ratio (%)', fontsize=11)
    ax1.set_ylabel('Default Probability', fontsize=11)
    ax1.set_title('PDP with ICE Curves: DTI Effect', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_xlim(10, 80)
    ax1.set_ylim(0, 0.8)
    ax1.grid(True, alpha=0.3)

    # Add interpretation
    ax1.annotate('Risk increases\nsteeply after 40%', xy=(45, 0.35),
                xytext=(55, 0.2), fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'))

    # 2D PDP: DTI x Credit Utilization
    ax2 = axes[1]

    dti_grid = np.linspace(0.1, 0.8, 30)
    util_grid = np.linspace(0.1, 0.9, 30)
    DTI, UTIL = np.meshgrid(dti_grid, util_grid)

    # Combined effect
    Z = 0.1 + 0.3 * (1 / (1 + np.exp(-8 * (DTI - 0.4)))) + 0.25 * (1 / (1 + np.exp(-8 * (UTIL - 0.6))))

    contour = ax2.contourf(DTI * 100, UTIL * 100, Z, levels=15, cmap='RdYlGn_r')
    cbar = plt.colorbar(contour, ax=ax2)
    cbar.set_label('Default Probability', fontsize=10)

    ax2.set_xlabel('Debt-to-Income Ratio (%)', fontsize=11)
    ax2.set_ylabel('Credit Utilization (%)', fontsize=11)
    ax2.set_title('2D PDP: DTI x Credit Utilization', fontsize=12, fontweight='bold')

    # Mark high-risk zone
    ax2.contour(DTI * 100, UTIL * 100, Z, levels=[0.5], colors='black', linewidths=2, linestyles='--')
    ax2.text(55, 75, 'High Risk\nZone', fontsize=10, fontweight='bold', color='white')
    ax2.text(25, 25, 'Low Risk\nZone', fontsize=10, fontweight='bold', color='black')

    fig.suptitle('Partial Dependence Plots: Understanding Feature Effects', fontsize=14, fontweight='bold', y=1.02)
    fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999', ha='right', style='italic')
    plt.tight_layout()

    output_path = Path(__file__).parent / 'pdp_ice_plots.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
