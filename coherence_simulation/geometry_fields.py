"""Geometry field generators for the coherence simulation framework."""

import numpy as np

def spiral_mask(size: int, turns: int = 3) -> np.ndarray:
    """Return a spiral mask as a 2D numpy array."""
    y, x = np.ogrid[-1:1:complex(size), -1:1:complex(size)]
    theta = np.arctan2(y, x)
    radius = np.hypot(x, y)
    spiral = np.sin(turns * theta + radius * np.pi)
    return spiral

def arc_mask(size: int, angle: float = np.pi/2) -> np.ndarray:
    """Return an arc mask covering the given angle."""
    y, x = np.ogrid[-1:1:complex(size), -1:1:complex(size)]
    theta = np.arctan2(y, x)
    mask = (np.abs(theta) < angle/2).astype(float)
    return mask

def dual_core_mask(size: int, separation: float = 0.5) -> np.ndarray:
    """Return a dual-core mask composed of two Gaussian spots."""
    y, x = np.ogrid[-1:1:complex(size), -1:1:complex(size)]
    core1 = np.exp(-((x-separation)**2 + y**2)/0.1)
    core2 = np.exp(-((x+separation)**2 + y**2)/0.1)
    return core1 + core2
