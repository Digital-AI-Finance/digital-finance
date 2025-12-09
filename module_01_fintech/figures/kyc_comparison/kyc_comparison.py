"""
KYC Comparison: Traditional vs Digital
Compares traditional and digital KYC approaches

Output: kyc_comparison.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'KYC Comparison: Traditional vs Digital',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/kyc_comparison'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create KYC comparison chart"""
    fig, ax = plt.subplots(figsize=(13, 8))

    # Comparison metrics
    metrics = ['Time to\nComplete', 'Cost per\nVerification', 'User\nExperience', 'Fraud\nDetection', 'Scalability',
               'Document\nCoverage', 'Regulatory\nCompliance', 'Error\nRate']

    traditional = [2, 2.5, 2, 2.5, 1.5, 3, 4, 2.5]  # 1-5 scale
    digital = [4.5, 4, 4.5, 4, 5, 4, 4, 4.5]

    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax.bar(x - width/2, traditional, width, label='Traditional KYC', color='#FF7F0E', alpha=0.8)
    bars2 = ax.bar(x + width/2, digital, width, label='Digital/eKYC', color='#4A90E2', alpha=0.8)

    ax.set_ylabel('Score (1=Poor, 5=Excellent)', fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=8)
    ax.set_ylim(0, 5.5)
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title('KYC Comparison: Traditional vs Digital', fontsize=14, fontweight='bold', pad=15)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3), textcoords="offset points",
                   ha='center', va='bottom', fontsize=7)

    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3), textcoords="offset points",
                   ha='center', va='bottom', fontsize=7)

    # Specific metrics text
    comparison_text = """Key Metrics:
    Traditional: 3-5 days, $20-50/check, manual review
    Digital: 2-5 minutes, $2-10/check, automated AI"""

    fig.text(0.5, 0.02, comparison_text, fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.98, 0.02, '[ILLUSTRATIVE COMPARISON]', fontsize=7, ha='right',
            style='italic', color='#999999')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)

    output_path = Path(__file__).parent / 'kyc_comparison.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
