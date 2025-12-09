"""
Open Banking Security Framework
Shows security layers and requirements for open banking

Output: open_banking_security.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking Security Framework',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/open_banking_security'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open banking security framework chart"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6, 9.5, 'Open Banking Security Framework', fontsize=14, fontweight='bold', ha='center')

    # Security layers (stacked)
    layers = [
        ('Transport Security', 8.2, '#D62728',
         ['TLS 1.2+ required', 'Certificate pinning', 'mTLS for API calls']),
        ('Identity & Auth', 6.8, '#FF7F0E',
         ['eIDAS certificates', 'SCA (2-factor auth)', 'OAuth 2.0 + OIDC']),
        ('Authorization', 5.4, '#4A90E2',
         ['Consent management', 'Scope-based access', 'Token lifecycle']),
        ('Data Protection', 4.0, '#44A044',
         ['Encryption at rest', 'Data minimization', 'GDPR compliance']),
        ('Monitoring & Audit', 2.6, '#6B5B95',
         ['API logging', 'Fraud detection', 'Incident response']),
    ]

    for name, y, color, items in layers:
        # Main layer bar
        bar = mpatches.FancyBboxPatch((1, y-0.5), 7, 1, boxstyle='round,pad=0.05',
                                       facecolor=color, edgecolor='#333333', lw=1.5)
        ax.add_patch(bar)
        ax.text(1.3, y, name, ha='left', va='center', fontsize=10, fontweight='bold', color='white')

        # Items
        for i, item in enumerate(items):
            ax.text(8.5, y + 0.25 - i*0.3, f'* {item}', fontsize=8, va='top')

    # eIDAS certificates box
    eidas_box = """eIDAS Certificates:
    - QWAC: Website authentication
    - QSEAL: Message signing
    - Issued by qualified TSPs
    - Required for PSD2 API access"""

    ax.text(11.5, 8, eidas_box, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Threat vectors
    threats = """Common Threats:
    - Man-in-the-middle attacks
    - Token theft/replay
    - Phishing for consent
    - Screen scraping fallback
    - API abuse/DoS"""

    ax.text(11.5, 4.5, threats, fontsize=7, ha='right', va='top',
           bbox=dict(boxstyle='round', facecolor='#FEECEC', edgecolor='#D62728'))

    # Compliance requirements
    compliance = """Compliance Requirements:
    - PSD2/RTS Technical Standards
    - eIDAS Regulation
    - GDPR (data protection)
    - National cybersecurity laws"""

    ax.text(0.5, 1.5, compliance, fontsize=7, va='top',
           bbox=dict(boxstyle='round', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

    # Source
    fig.text(0.5, 0.02, 'Source: PSD2 RTS, EBA Guidelines on ICT and Security Risk Management',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'open_banking_security.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
