"""Hashrate Evolution - Bitcoin network computing power 2009-2024"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10, 'axes.labelsize': 10, 'axes.titlesize': 11,
    'xtick.labelsize': 9, 'ytick.labelsize': 9, 'legend.fontsize': 9,
    'figure.dpi': 150, 'font.family': 'serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'

fig, ax = plt.subplots(figsize=(11, 6))

# Synthetic but realistic hashrate data (EH/s - Exahashes per second)
years = np.array([2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
# Log scale data (approximate historical progression)
hashrate = np.array([
    0.000001,    # 2009 - CPU mining, ~1 MH/s
    0.00001,     # 2010 - GPU mining begins
    0.001,       # 2011 - GPUs dominant
    0.01,        # 2012 - First ASICs
    1,           # 2013 - ASIC revolution
    100,         # 2014 - Industrial mining
    400,         # 2015
    2000,        # 2016
    15000,       # 2017 - Bull run
    40000,       # 2018
    100000,      # 2019
    150000,      # 2020
    180000,      # 2021 - China ban dip then recovery
    250000,      # 2022
    450000,      # 2023
    700000,      # 2024
]) / 1000  # Convert to EH/s

ax.semilogy(years, hashrate, color=MLPURPLE, linewidth=2.5, marker='o', markersize=6)
ax.fill_between(years, hashrate, alpha=0.2, color=MLPURPLE)

# Annotations for key events
annotations = [
    (2010, 0.00001/1000, 'GPU era'),
    (2013, 1/1000, 'ASIC\nrevolution'),
    (2017, 15000/1000, 'First\nbull run'),
    (2021, 180000/1000, 'China\nban'),
    (2024, 700000/1000, '700 EH/s'),
]

for year, rate, label in annotations:
    ax.annotate(label, xy=(year, rate), xytext=(year, rate * 3),
                fontsize=8, ha='center', color='#666666',
                arrowprops=dict(arrowstyle='-', color='#999999', lw=0.5))

ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('Network Hashrate (EH/s, log scale)', fontsize=10)
ax.set_title('Bitcoin Network Hashrate: Exponential Growth', fontsize=12, fontweight='bold', color=MLPURPLE)

ax.set_xlim(2009, 2024)
ax.grid(True, alpha=0.3, which='both')
ax.set_xticks([2009, 2012, 2015, 2018, 2021, 2024])

# Add annotation for scale
ax.text(2015, 0.0000001, '1 EH/s = 1 quintillion hashes/second', fontsize=8,
        style='italic', color='#666666')

fig.text(0.98, 0.02, '[SYNTHETIC DATA]', fontsize=7, color='#999999',
         ha='right', style='italic')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'hashrate_evolution.pdf',
            format='pdf', dpi=300, bbox_inches='tight')
plt.close()
