"""
Document Verification Process
Shows how ID documents are verified in digital onboarding

Output: document_verification.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Document Verification Process',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/document_verification'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create document verification process diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Document Verification Process', fontsize=14, fontweight='bold', ha='center')

    # Verification stages
    stages = [
        {'name': 'Document\nCapture', 'x': 2, 'y': 7, 'color': '#4A90E2',
         'checks': ['Image quality', 'Glare detection', 'Corner detection', 'Blur check']},
        {'name': 'Document\nClassification', 'x': 5.5, 'y': 7, 'color': '#44A044',
         'checks': ['ID type (passport, DL)', 'Country of origin', 'Version/format', 'Front/back detection']},
        {'name': 'Data\nExtraction', 'x': 9, 'y': 7, 'color': '#FF7F0E',
         'checks': ['OCR text extraction', 'MRZ parsing', 'Barcode reading', 'NFC chip data']},
    ]

    for stage in stages:
        # Main box
        box = mpatches.FancyBboxPatch((stage['x']-1.3, stage['y']-0.5), 2.6, 1.5,
                                       boxstyle='round,pad=0.1',
                                       facecolor=stage['color'], edgecolor='#333333', lw=2)
        ax.add_patch(box)
        ax.text(stage['x'], stage['y']+0.25, stage['name'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

        # Checks list
        checks_box = mpatches.FancyBboxPatch((stage['x']-1.3, stage['y']-2.8), 2.6, 2,
                                              boxstyle='round,pad=0.1',
                                              facecolor='white', edgecolor=stage['color'], lw=1.5)
        ax.add_patch(checks_box)
        for i, check in enumerate(stage['checks']):
            ax.text(stage['x'], stage['y']-1.2-i*0.45, f'* {check}', ha='center', fontsize=7)

    # Arrows between stages
    ax.annotate('', xy=(4, 7), xytext=(3.5, 7),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
    ax.annotate('', xy=(7.5, 7), xytext=(7, 7),
               arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

    # Second row - verification checks
    checks = [
        {'name': 'Security\nFeatures', 'x': 2, 'y': 2.5, 'color': '#6B5B95',
         'items': ['Holograms', 'UV patterns', 'Microprint', 'Watermarks']},
        {'name': 'Fraud\nDetection', 'x': 5.5, 'y': 2.5, 'color': '#D62728',
         'items': ['Template matching', 'Font consistency', 'Photo tampering', 'Data consistency']},
        {'name': 'Database\nChecks', 'x': 9, 'y': 2.5, 'color': '#333333',
         'items': ['PEP/Sanctions', 'Document blacklists', 'Identity registries', 'Cross-reference']},
    ]

    for check in checks:
        box = mpatches.FancyBboxPatch((check['x']-1.3, check['y']-0.3), 2.6, 1.3,
                                       boxstyle='round,pad=0.1',
                                       facecolor=check['color'], alpha=0.15,
                                       edgecolor=check['color'], lw=2)
        ax.add_patch(box)
        ax.text(check['x'], check['y']+0.5, check['name'], ha='center',
               fontsize=9, fontweight='bold', color=check['color'])
        items_text = ' | '.join(check['items'])
        ax.text(check['x'], check['y']-0.1, items_text, ha='center', fontsize=6, wrap=True)

    # Accuracy stats
    stats = """Industry Accuracy (2024):
    - OCR accuracy: 95-99%
    - Document classification: 98%+
    - Fraud detection: 94-97%
    Source: IDV provider benchmarks"""

    ax.text(12.5, 9, stats, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, '[CONCEPTUAL PROCESS FLOW]',
            fontsize=7, ha='center', style='italic', color='#999999')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'document_verification.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
