"""Visualization utilities for coherence simulation."""

import matplotlib.pyplot as plt
import numpy as np


def plot_field(field: np.ndarray, title: str = "") -> None:
    """Plot a 2D scalar field."""
    plt.imshow(field, cmap="viridis")
    plt.colorbar()
    plt.title(title)
    plt.show()
