"""
Shared color palette for Digital Finance charts
Grayscale-friendly colors suitable for B&W printing
"""

# Primary grayscale palette
COLORS = {
    'primary': '#333333',      # Dark gray (main elements)
    'secondary': '#666666',    # Medium gray
    'tertiary': '#999999',     # Light gray
    'background': '#CCCCCC',   # Very light gray
    'white': '#FFFFFF',
    'black': '#000000',
}

# Accent colors (used sparingly)
ACCENTS = {
    'blue': '#4A90E2',         # Highlight/positive
    'purple': '#6B5B95',       # Alternative accent
    'green': '#44A044',        # Success/positive
    'red': '#D62728',          # Error/negative
    'orange': '#FF7F0E',       # Warning/attention
    'teal': '#17BECF',         # Data series
}

# Sequential palette for data series
SERIES_COLORS = [
    '#333333',  # Series 1
    '#666666',  # Series 2
    '#999999',  # Series 3
    '#4A90E2',  # Series 4 (blue accent)
    '#6B5B95',  # Series 5 (purple accent)
    '#44A044',  # Series 6 (green accent)
]

# Categorical palette
CATEGORICAL = [
    '#333333',
    '#4A90E2',
    '#44A044',
    '#FF7F0E',
    '#D62728',
    '#6B5B95',
    '#17BECF',
    '#666666',
]

# Diverging palette (for positive/negative)
DIVERGING = {
    'negative': '#D62728',
    'neutral': '#999999',
    'positive': '#44A044',
}

def get_color(name):
    """Get color by name from any palette"""
    all_colors = {**COLORS, **ACCENTS}
    return all_colors.get(name, '#333333')
