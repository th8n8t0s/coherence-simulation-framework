"""Simple scalar field simulation runner."""

from __future__ import annotations

import numpy as np

from .metrics import entropy, curvature


def step(field: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Perform one diffusion-like step with convolution."""
    from scipy.signal import convolve2d

    return convolve2d(field, kernel, mode="same", boundary="wrap")


def run_simulation(initial: np.ndarray, steps: int = 10, dt: float = 0.1) -> list[np.ndarray]:
    """Run a simple simulation on the initial field."""
    kernel = np.array([[0, dt, 0], [dt, 1 - 4*dt, dt], [0, dt, 0]])
    field = initial.copy()
    history = [field]
    for _ in range(steps):
        field = step(field, kernel)
        history.append(field)
    return history


def analyze(history: list[np.ndarray]) -> dict[str, list[float]]:
    """Compute entropy and curvature over a simulation history."""
    ent = [entropy(f) for f in history]
    curv = [np.mean(np.abs(curvature(f))) for f in history]
    return {"entropy": ent, "curvature": curv}
