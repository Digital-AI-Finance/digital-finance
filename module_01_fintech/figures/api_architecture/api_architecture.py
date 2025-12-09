"""
Open Banking API Architecture
Shows typical REST API structure for open banking

Output: api_architecture.pdf
Module: module_01_fintech
Lesson: 5 - Open Banking
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Open Banking API Architecture',
    'module': 'module_01_fintech',
    'lesson': 5,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/api_architecture'
}

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
})

def create_chart():
    """Create open banking API architecture diagram"""
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6.5, 9.5, 'Open Banking API Architecture', fontsize=14, fontweight='bold', ha='center')

    # TPP Application layer
    tpp_box = mpatches.FancyBboxPatch((0.5, 6.5), 3, 2.5, boxstyle='round,pad=0.1',
                                       facecolor='#4A90E2', edgecolor='#333333', lw=2)
    ax.add_patch(tpp_box)
    ax.text(2, 8.5, 'TPP Application', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(2, 7.8, 'FinTech App', ha='center', fontsize=9, color='white')
    ax.text(2, 7.3, 'OAuth Client', ha='center', fontsize=8, color='#CCE5FF')

    # API Gateway layer
    gateway_box = mpatches.FancyBboxPatch((4.5, 6.5), 4, 2.5, boxstyle='round,pad=0.1',
                                           facecolor='#FF7F0E', edgecolor='#333333', lw=2)
    ax.add_patch(gateway_box)
    ax.text(6.5, 8.5, 'API Gateway', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(6.5, 7.8, 'Rate limiting | Throttling', ha='center', fontsize=8, color='white')
    ax.text(6.5, 7.3, 'Certificate validation (eIDAS)', ha='center', fontsize=8, color='white')
    ax.text(6.5, 6.8, 'Request logging', ha='center', fontsize=8, color='white')

    # Bank Backend
    bank_box = mpatches.FancyBboxPatch((9.5, 6.5), 3, 2.5, boxstyle='round,pad=0.1',
                                        facecolor='#333333', edgecolor='#333333', lw=2)
    ax.add_patch(bank_box)
    ax.text(11, 8.5, 'Bank Core', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(11, 7.8, 'Account Systems', ha='center', fontsize=9, color='white')
    ax.text(11, 7.3, 'Payment Rails', ha='center', fontsize=8, color='#CCCCCC')

    # OAuth/Auth layer
    auth_box = mpatches.FancyBboxPatch((4.5, 3.5), 4, 2.5, boxstyle='round,pad=0.1',
                                        facecolor='#44A044', edgecolor='#333333', lw=2)
    ax.add_patch(auth_box)
    ax.text(6.5, 5.5, 'Authorization Server', ha='center', fontsize=11, fontweight='bold', color='white')
    ax.text(6.5, 4.8, 'OAuth 2.0 + OIDC', ha='center', fontsize=9, color='white')
    ax.text(6.5, 4.3, 'Consent Management', ha='center', fontsize=8, color='white')
    ax.text(6.5, 3.8, 'Token Issuance', ha='center', fontsize=8, color='white')

    # API endpoints listing
    endpoints_box = mpatches.FancyBboxPatch((0.5, 0.5), 5.5, 2.5, boxstyle='round,pad=0.1',
                                             facecolor='#F5F5F5', edgecolor='#CCCCCC', lw=1)
    ax.add_patch(endpoints_box)
    ax.text(3.25, 2.7, 'Key API Endpoints (RESTful)', ha='center', fontsize=10, fontweight='bold')

    endpoints = [
        'GET  /accounts',
        'GET  /accounts/{id}/balances',
        'GET  /accounts/{id}/transactions',
        'POST /payments',
        'GET  /payments/{id}/status'
    ]
    for i, ep in enumerate(endpoints):
        ax.text(1, 2.2 - i*0.35, ep, fontsize=8, family='monospace')

    # Security requirements
    security_box = mpatches.FancyBboxPatch((7, 0.5), 5.5, 2.5, boxstyle='round,pad=0.1',
                                            facecolor='#FFF9E6', edgecolor='#FFD700', lw=1)
    ax.add_patch(security_box)
    ax.text(9.75, 2.7, 'Security Requirements', ha='center', fontsize=10, fontweight='bold')

    security = [
        '* mTLS (mutual TLS)',
        '* eIDAS QWAC/QSEAL certificates',
        '* OAuth 2.0 + PKCE',
        '* Request signing (JWS)',
        '* Token binding'
    ]
    for i, sec in enumerate(security):
        ax.text(7.3, 2.2 - i*0.35, sec, fontsize=8)

    # Connection arrows
    ax.annotate('', xy=(4.5, 7.75), xytext=(3.5, 7.75),
               arrowprops=dict(arrowstyle='<->', color='#333333', lw=2))
    ax.text(4, 8.2, 'HTTPS', fontsize=8, ha='center')

    ax.annotate('', xy=(9.5, 7.75), xytext=(8.5, 7.75),
               arrowprops=dict(arrowstyle='<->', color='#333333', lw=2))
    ax.text(9, 8.2, 'Internal', fontsize=8, ha='center')

    ax.annotate('', xy=(6.5, 6.5), xytext=(6.5, 6),
               arrowprops=dict(arrowstyle='<->', color='#44A044', lw=2))
    ax.text(7, 6.25, 'Auth', fontsize=8, color='#44A044')

    ax.annotate('', xy=(3.5, 4.75), xytext=(4.5, 4.75),
               arrowprops=dict(arrowstyle='<->', color='#44A044', lw=2))
    ax.text(4, 5.1, 'Token\nRequest', fontsize=7, ha='center', color='#44A044')

    # Source
    fig.text(0.5, 0.02, 'Source: Open Banking API specifications (Berlin Group, UK OBIE, STET)',
            fontsize=7, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'api_architecture.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
