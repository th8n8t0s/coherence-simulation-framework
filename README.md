# 🌐 Coherence Simulation Framework

This project explores how static geometric fields—such as spirals, arcs, and dual-core shapes—can influence entropy and curvature in scalar signal propagation. The framework simulates energy-like signals diffusing through these geometries and tracks how coherence, structure, and information density evolve over time.

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

├── coherence_simulation/ │ ├── geometry_fields.py # Spiral, Arc, Dual-Core masks │ ├── simulation_runner.py # Main evolution logic │ ├── metrics.py # Entropy and curvature functions │ └── visualization.py # Plotting and animation tools ├── outputs/ │ └── figures, animations ├── r_go2.ipynb # Main notebook with documentation └── README.md

yaml
Copy
Edit

---

## 🧠 Concept

The central idea is to test whether *geometry alone*—without dynamic feedback—can meaningfully shape signal coherence and information flow. The simulation measures:

- **Entropy**: Information dispersion across the signal field
- **Curvature**: Structural sharpness of spatial gradients

These quantities help describe how “focused” or “diffuse” energy becomes within a given field shape.

---

## ▶️ How to Run

1. Install required packages:
   ```bash
   pip install numpy matplotlib
Run the notebook:

bash
Copy
Edit
jupyter notebook r_go2.ipynb
Or, run the Python script directly once modularized:

bash
Copy
Edit
python simulation_runner.py
📈 Example Outputs
Geometry Type	Final Distribution	Entropy Curve
Spiral	
Arc	
Dual-Core	
🧪 Experimental Inspiration
This framework could inspire physical experiments using thermal waveguides:

Etch spiral or arc shapes onto thin conductive films (e.g., copper or graphite)

Inject energy via laser or IR pulse

Record thermal diffusion using IR camera

Compare patterned vs flat substrate for energy shaping behavior

📜 License
This project is licensed under the MIT License — feel free to build, remix, or contribute.

🤝 Acknowledgments
This project was developed as a personal exploration of wave-based geometry and information flow. Special thanks to the open-source community and theoretical physics inspiration.
