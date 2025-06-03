"""Metrics for evaluating scalar fields in the coherence simulation framework."""

import numpy as np
from scipy.ndimage import gaussian_laplace


def entropy(field: np.ndarray) -> float:
    """Compute Shannon entropy of a normalized field."""
    flat = field.ravel()
    prob = np.abs(flat) / np.sum(np.abs(flat))
    prob = prob[prob > 0]
    return -np.sum(prob * np.log(prob))


def curvature(field: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    """Compute curvature using a Laplacian operator."""
    return gaussian_laplace(field, sigma=sigma)
