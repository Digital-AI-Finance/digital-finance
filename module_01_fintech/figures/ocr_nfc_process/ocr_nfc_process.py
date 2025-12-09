"""
OCR and NFC Data Extraction Process
Shows how data is extracted from ID documents via OCR and NFC

Output: ocr_nfc_process.pdf
Module: module_01_fintech
Lesson: 6 - Digital Identity
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'OCR and NFC Data Extraction',
    'module': 'module_01_fintech',
    'lesson': 6,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/ocr_nfc_process'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create OCR/NFC extraction process diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Document Data Extraction: OCR vs NFC', fontsize=14, fontweight='bold', ha='center')

    # OCR Section (left)
    ocr_box = mpatches.FancyBboxPatch((0.5, 3.5), 5.5, 5.5, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', alpha=0.15,
                                       edgecolor='#4A90E2', lw=2)
    ax.add_patch(ocr_box)
    ax.text(3.25, 8.5, 'OCR (Optical Character Recognition)', ha='center',
           fontsize=11, fontweight='bold', color='#4A90E2')

    # OCR flow
    ocr_steps = [
        ('1. Image Capture', 'Camera captures document'),
        ('2. Pre-processing', 'Deskew, noise reduction'),
        ('3. Text Detection', 'Locate text regions'),
        ('4. Character Recognition', 'ML-based text extraction'),
        ('5. MRZ Parsing', 'Machine Readable Zone decode'),
        ('6. Validation', 'Check digit verification'),
    ]
    for i, (step, desc) in enumerate(ocr_steps):
        ax.text(1, 7.8-i*0.7, step, fontsize=8, fontweight='bold')
        ax.text(3.2, 7.8-i*0.7, desc, fontsize=7)

    # NFC Section (right)
    nfc_box = mpatches.FancyBboxPatch((7, 3.5), 5.5, 5.5, boxstyle='round,pad=0.1',
                                       facecolor='#44A044', alpha=0.15,
                                       edgecolor='#44A044', lw=2)
    ax.add_patch(nfc_box)
    ax.text(9.75, 8.5, 'NFC (Near Field Communication)', ha='center',
           fontsize=11, fontweight='bold', color='#44A044')

    # NFC flow
    nfc_steps = [
        ('1. Chip Detection', 'Phone detects NFC chip'),
        ('2. BAC/PACE Auth', 'Authenticate with MRZ data'),
        ('3. Data Read', 'Extract chip data groups'),
        ('4. Active Auth', 'Verify chip authenticity'),
        ('5. Passive Auth', 'Validate digital signatures'),
        ('6. Clone Detection', 'Verify chip is original'),
    ]
    for i, (step, desc) in enumerate(nfc_steps):
        ax.text(7.5, 7.8-i*0.7, step, fontsize=8, fontweight='bold')
        ax.text(9.7, 7.8-i*0.7, desc, fontsize=7)

    # Comparison metrics
    metrics = [
        ['Metric', 'OCR', 'NFC'],
        ['Accuracy', '95-99%', '100%'],
        ['Security', 'Medium', 'Very High'],
        ['User effort', 'Take photo', 'Tap phone'],
        ['Device req.', 'Camera', 'NFC-enabled'],
        ['Tampering detect', 'Limited', 'Cryptographic'],
    ]

    table_y = 2.8
    for i, row in enumerate(metrics):
        color = '#E8E8E8' if i == 0 else 'white'
        weight = 'bold' if i == 0 else 'normal'
        ax.add_patch(mpatches.Rectangle((3, table_y-i*0.45), 7, 0.45,
                                         facecolor=color, edgecolor='#CCCCCC'))
        ax.text(4.5, table_y-i*0.45+0.22, row[0], ha='center', va='center', fontsize=7, fontweight=weight)
        ax.text(6.8, table_y-i*0.45+0.22, row[1], ha='center', va='center', fontsize=7)
        ax.text(9.2, table_y-i*0.45+0.22, row[2], ha='center', va='center', fontsize=7)

    # Best practice
    best = "Best Practice: Combine OCR + NFC for maximum security and accuracy"
    ax.text(6.5, 0.5, best, ha='center', fontsize=9, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: ICAO 9303 (Machine Readable Travel Documents), ePassport specifications',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'ocr_nfc_process.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
