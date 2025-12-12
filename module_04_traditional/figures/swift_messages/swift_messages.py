"""
SWIFT Message Volume Growth
Shows the growth in cross-border payment messages

Output: swift_messages.pdf
Module: module_04_traditional
Lesson: 39 - Payment Rails
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (10, 6),
    'figure.dpi': 150
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'

def create_chart():
    fig, ax = plt.subplots(figsize=(10, 6))

    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

    # SWIFT message volumes (billions per year)
    messages = [6.1, 6.5, 7.0, 7.8, 8.4, 8.9, 10.6, 11.2, 11.8, 12.5]

    ax.bar(years, messages, color=MLBLUE, edgecolor='white', linewidth=2)
    ax.plot(years, messages, 'o-', color=MLORANGE, linewidth=2, markersize=8)

    for year, msg in zip(years, messages):
        ax.text(year, msg + 0.2, f'{msg}B', ha='center', fontsize=9, fontweight='bold')

    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Messages (Billions)', fontsize=11)
    ax.set_title('SWIFT Annual Message Volume', fontsize=14,
                 fontweight='bold', color=MLPURPLE, pad=10)

    ax.set_ylim(0, 15)

    # Add growth rate
    cagr = ((messages[-1]/messages[0])**(1/len(years)) - 1) * 100
    ax.text(0.02, 0.95, f'CAGR: {cagr:.1f}%',
            transform=ax.transAxes, ha='left', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.text(0.98, 0.02, 'Source: SWIFT Annual Reports [SYNTHETIC ESTIMATES]',
             fontsize=7, color='#999999', ha='right', style='italic')

    plt.tight_layout()

    output_path = Path(__file__).parent / 'swift_messages.pdf'
    plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chart saved to: {output_path}")
    return output_path

if __name__ == '__main__':
    create_chart()
