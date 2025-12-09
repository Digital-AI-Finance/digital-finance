"""
Shared matplotlib styles for Digital Finance charts
Optimized for 8pt Beamer slides
"""

import matplotlib.pyplot as plt

# Standard rcParams for academic charts (8pt minimum)
CHART_RCPARAMS = {
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'legend.frameon': True,
    'legend.framealpha': 0.9,
    'axes.linewidth': 0.5,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
}

# Larger fonts for presentation (if needed)
PRESENTATION_RCPARAMS = {
    **CHART_RCPARAMS,
    'font.size': 12,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
}

# Smaller fonts for dense charts
COMPACT_RCPARAMS = {
    **CHART_RCPARAMS,
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
}


def apply_chart_style():
    """Apply standard chart style"""
    plt.rcParams.update(CHART_RCPARAMS)


def apply_presentation_style():
    """Apply larger presentation style"""
    plt.rcParams.update(PRESENTATION_RCPARAMS)


def apply_compact_style():
    """Apply compact style for dense charts"""
    plt.rcParams.update(COMPACT_RCPARAMS)


def setup_figure(figsize=(10, 6), style='standard'):
    """Create figure with appropriate style"""
    if style == 'presentation':
        apply_presentation_style()
    elif style == 'compact':
        apply_compact_style()
    else:
        apply_chart_style()

    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


def add_synthetic_label(ax, position='lower right'):
    """Add [SYNTHETIC] data label to chart"""
    positions = {
        'lower right': (0.98, 0.02),
        'lower left': (0.02, 0.02),
        'upper right': (0.98, 0.98),
        'upper left': (0.02, 0.98),
    }
    x, y = positions.get(position, (0.98, 0.02))
    ha = 'right' if 'right' in position else 'left'
    va = 'top' if 'upper' in position else 'bottom'

    ax.annotate(
        '[SYNTHETIC DATA]',
        xy=(x, y),
        xycoords='axes fraction',
        fontsize=7,
        color='#999999',
        ha=ha,
        va=va,
        style='italic'
    )
