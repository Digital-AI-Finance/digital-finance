"""
Biometric Modalities Comparison
Compares different biometric authentication methods

Output: biometric_modalities.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Biometric Modalities Comparison',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/biometric_modalities'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create biometric modalities comparison chart"""
    fig, ax = plt.subplots(figsize=(13, 7))

    # Modalities data
    modalities = ['Face\nRecognition', 'Fingerprint', 'Voice', 'Iris', 'Behavioral']

    # Metrics (1-5 scale)
    accuracy = [4.2, 4.5, 3.5, 4.8, 3.0]
    ease_of_use = [4.5, 4.0, 4.0, 3.0, 5.0]
    spoofing_resistance = [3.5, 3.0, 2.5, 4.5, 4.0]
    device_availability = [5.0, 4.5, 5.0, 2.0, 5.0]
    cost = [4.0, 4.5, 5.0, 2.5, 4.5]  # Higher = lower cost

    x = np.arange(len(modalities))
    width = 0.15

    bars1 = ax.bar(x - 2*width, accuracy, width, label='Accuracy', color='#4A90E2')
    bars2 = ax.bar(x - width, ease_of_use, width, label='Ease of Use', color='#44A044')
    bars3 = ax.bar(x, spoofing_resistance, width, label='Spoof Resistance', color='#FF7F0E')
    bars4 = ax.bar(x + width, device_availability, width, label='Device Availability', color='#6B5B95')
    bars5 = ax.bar(x + 2*width, cost, width, label='Cost Efficiency', color='#333333')

    ax.set_ylabel('Score (1-5 scale)', fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(modalities, fontsize=9)
    ax.set_ylim(0, 5.5)
    ax.legend(loc='upper right', fontsize=8, ncol=2)
    ax.set_title('Biometric Modalities Comparison', fontsize=14, fontweight='bold', pad=15)

    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    # Add adoption rates text below
    adoption_text = """Market Adoption (2024):
    Face: 65% of smartphones | Fingerprint: 80% of smartphones | Voice: 25% of devices | Iris: <5% | Behavioral: Growing in fraud detection"""

    fig.text(0.5, 0.02, adoption_text, fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Key considerations
    considerations = """Key Considerations:
    - Liveness detection essential
    - Privacy regulations (GDPR, BIPA)
    - Fallback mechanisms needed
    - Multi-modal approach best"""

    ax.text(12.5, 4.5, considerations, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.98, 0.02, '[ILLUSTRATIVE COMPARISON]', fontsize=7, ha='right',
            style='italic', color='#999999')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.12)

    output_path = Path(__file__).parent / 'biometric_modalities.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
