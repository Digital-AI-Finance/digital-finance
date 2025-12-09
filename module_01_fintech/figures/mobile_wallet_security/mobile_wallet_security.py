"""
Mobile Wallet Security Layers Diagram
Shows the multi-layer security architecture of mobile wallets

Output: mobile_wallet_security.pdf
Module: module_01_fintech
Lesson: 3 - Mobile Wallets
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Mobile Wallet Security Architecture',
    'module': 'module_01_fintech',
    'lesson': 3,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/mobile_wallet_security'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create mobile wallet security layers diagram"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Security layers (concentric)
    layers = [
        (5, 5, 4.2, 'Device Security', '#D62728', 'white'),
        (5, 5, 3.4, 'App Security', '#FF7F0E', 'white'),
        (5, 5, 2.6, 'Authentication', '#4A90E2', 'white'),
        (5, 5, 1.8, 'Tokenization', '#44A044', 'white'),
        (5, 5, 1.0, 'Encryption', '#6B5B95', 'white'),
    ]

    for x, y, r, label, color, text_color in layers:
        circle = mpatches.Circle((x, y), r, facecolor=color, edgecolor='white',
                                  lw=2, alpha=0.85)
        ax.add_patch(circle)
        # Position labels
        ax.text(x, y + r - 0.3, label, ha='center', va='center',
               fontsize=10, fontweight='bold', color=text_color)

    # Center label
    ax.text(5, 5, 'User\nData', ha='center', va='center',
           fontsize=10, fontweight='bold', color='white')

    # Side annotations with security measures
    left_measures = [
        (0.3, 8, 'Device Layer:', ['• Secure Element (SE)', '• TEE (Trusted Execution)',
                                   '• Device binding', '• Remote wipe']),
        (0.3, 5.5, 'App Layer:', ['• Code obfuscation', '• Jailbreak detection',
                                   '• Certificate pinning', '• Runtime protection']),
        (0.3, 3, 'Auth Layer:', ['• Biometrics', '• PIN/Password',
                                 '• 2FA/MFA', '• Behavioral analysis']),
    ]

    right_measures = [
        (9.7, 7, 'Token Layer:', ['• Card tokenization', '• One-time tokens',
                                  '• Device-specific tokens', '• Token lifecycle']),
        (9.7, 4, 'Encryption:', ['• End-to-end encryption', '• TLS 1.3',
                                 '• AES-256', '• Key management']),
    ]

    for x, y, title, measures in left_measures:
        ax.text(x, y, title, fontsize=9, fontweight='bold', va='top')
        for i, m in enumerate(measures):
            ax.text(x, y - 0.4 - i*0.35, m, fontsize=7, va='top')

    for x, y, title, measures in right_measures:
        ax.text(x, y, title, fontsize=9, fontweight='bold', va='top', ha='right')
        for i, m in enumerate(measures):
            ax.text(x, y - 0.4 - i*0.35, m, fontsize=7, va='top', ha='right')

    # Title
    ax.text(5, 9.7, 'Mobile Wallet Security Architecture',
           fontsize=14, fontweight='bold', ha='center')
    ax.text(5, 9.3, 'Defense in Depth Approach',
           fontsize=10, ha='center', style='italic', color='#666666')

    # Synthetic label
    ax.text(9.8, 0.3, '[ILLUSTRATIVE]', fontsize=7, color='#999999',
           ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'mobile_wallet_security.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
