# 🌐 Coherence Simulation Framework

This project explores how static geometric fields—such as spirals, arcs, and dual-core shapes—affect entropy and curvature during scalar signal propagation. The framework simulates energy-like signals diffusing through these geometries and tracks how coherence, structure, and information density evolve over time.

---

## 🧪 Features

- Modular scalar field simulation in 2D
- Predefined waveguide geometries (spiral, arc, dual-core)
- Entropy and curvature metrics computed per timestep
- Animated signal propagation
- Visual outputs for spatial structure and entropy gradients
- Easily extendable for new field configurations

---

## 📂 Project Structure

```
coherence_simulation/
├── geometry_fields.py   # Spiral, Arc, Dual-Core masks
├── simulation_runner.py # Main evolution logic
├── metrics.py           # Entropy and curvature functions
└── visualization.py     # Plotting helpers
outputs/
└── figures, animations
r_go2.py                 # Example script
README.md
```

---

## 🧠 Concept

The central idea is to test whether *geometry alone*—without dynamic feedback—can meaningfully shape signal coherence and information flow. The simulation measures:

- **Entropy**: Information dispersion across the signal field
- **Curvature**: Structural sharpness of spatial gradients

These quantities help describe how "focused" or "diffuse" energy becomes within a given field shape.

---

## ▶️ How to Run

1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the example script:
   ```bash
   python r_go2.py
   ```

Unit tests can be executed with:
```bash
pytest
```

---

📜 **License**

This project is licensed under the MIT License — feel free to build, remix, or contribute.

🤝 **Acknowledgments**

This project was developed as a personal exploration of wave-based geometry and information flow. Special thanks to the open-source community and theoretical physics inspiration.
