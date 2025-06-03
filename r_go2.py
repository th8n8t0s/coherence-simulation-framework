"""Example usage of the coherence_simulation package."""

import numpy as np

from coherence_simulation import geometry_fields, simulation_runner, visualization


def main():
    size = 50
    field = geometry_fields.spiral_mask(size)
    history = simulation_runner.run_simulation(field, steps=20)
    analysis = simulation_runner.analyze(history)

    visualization.plot_field(history[-1], title="Final Field")
    print("Final entropy:", analysis["entropy"][-1])


if __name__ == "__main__":
    main()
