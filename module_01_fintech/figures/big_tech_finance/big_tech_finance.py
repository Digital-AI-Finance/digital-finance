"""
Big Tech in Finance
Shows Big Tech companies' financial services

Output: big_tech_finance.pdf
Module: module_01_fintech
Lesson: 12 - FinTech Trends
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CHART_METADATA = {
    'title': 'Big Tech in Finance',
    'module': 'module_01_fintech',
    'lesson': 12,
    'url': 'https://github.com/Digital-AI-Finance/digital-finance/tree/main/module_01_fintech/figures/big_tech_finance'
}

plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 14,
})

def create_chart():
    """Create Big Tech in finance diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.3, 'Big Tech in Financial Services', fontsize=20, fontweight='bold', ha='center')

    # Companies
    companies = [
        {
            'name': 'Apple',
            'x': 2.2, 'y': 6.5,
            'color': '#333333',
            'services': ['Apple Pay', 'Apple Card', 'Apple Savings', 'BNPL'],
        },
        {
            'name': 'Google',
            'x': 5.5, 'y': 6.5,
            'color': '#4A90E2',
            'services': ['Google Pay', 'Plex (cancelled)', 'Google Wallet', 'Cloud banking'],
        },
        {
            'name': 'Amazon',
            'x': 8.5, 'y': 6.5,
            'color': '#FF7F0E',
            'services': ['Amazon Pay', 'SMB Lending', 'Insurance', 'Amazon One'],
        },
        {
            'name': 'Meta',
            'x': 11.8, 'y': 6.5,
            'color': '#4A90E2',
            'services': ['Meta Pay', 'Diem (cancelled)', 'WhatsApp Pay', 'Novi (ended)'],
        },
        {
            'name': 'Alibaba/Ant',
            'x': 4.75, 'y': 2.5,
            'color': '#D62728',
            'services': ['Alipay (1B+ users)', 'Yu\'e Bao MMF', 'Ant Credit', 'MYbank'],
        },
        {
            'name': 'Tencent',
            'x': 9.25, 'y': 2.5,
            'color': '#44A044',
            'services': ['WeChat Pay (900M+)', 'LiCaiTong', 'WeBank', 'Insurance'],
        },
    ]

    for comp in companies:
        box = mpatches.FancyBboxPatch((comp['x']-1.5, comp['y']-1.4), 3, 2.9,
                                       boxstyle='round,pad=0.1',
                                       facecolor=comp['color'], alpha=0.15,
                                       edgecolor=comp['color'], lw=2)
        ax.add_patch(box)
        ax.text(comp['x'], comp['y']+1.1, comp['name'], ha='center',
               fontsize=14, fontweight='bold', color=comp['color'])

        for i, svc in enumerate(comp['services']):
            ax.text(comp['x'], comp['y']+0.3-i*0.45, f'* {svc}', ha='center', fontsize=10)

    # Key insight
    insight = "Regulatory concern: Data advantages, systemic risk, competition with banks"
    ax.text(7, 0.8, insight, ha='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='#FFF9E6', edgecolor='#FFD700'))

    # Source
    fig.text(0.5, 0.02, 'Source: Company reports, BIS Big Tech in Finance papers (2024)',
            fontsize=10, ha='center', style='italic', color='#666666')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'big_tech_finance.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
