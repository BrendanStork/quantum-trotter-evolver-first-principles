# Quantum Trotter Evolution Simulator

A modular numpy and scipy-based framework for simulating quantum many-body dynamics using both **exact unitary evolution** and **Trotterized time evolution**. The project is designed for studying quantum Hamiltonians, benchmarking approximation error in Trotter decompositions, and exploring scalable simulation workflows.

---

## Key Features

- **Exact time evolution**
  - Matrix exponential-based unitary propagation
  - Arbitrary Hamiltonian construction from Pauli strings

- **Trotterized evolution**
  - First-order Trotter-Suzuki decomposition
  - Configurable time step and Trotter depth
  - Operator-level decomposition of Hamiltonians

- **Expectation value tracking**
  - Measurement of arbitrary Pauli observables
  - Time-dependent observable dynamics
  - Direct comparison: Trotter vs exact

- **Visualization tools**
  - Expectation value dynamics over time
  - Convergence analysis vs Trotter step count
  - Error analysis

---

## Project Structure
trotter-vs-exact-evolution/
│
├── time_simulation/
│   ├── __init__.py
│   ├── circuit.py          # Quantum state + gate application
│   ├── gates.py            # Single-qubit gate definitions
│   ├── hamiltonian.py      # Pauli Hamiltonian construction
│   ├── evolution.py        # Exact + Trotter evolution
│   ├── plotting.py         # Visualization utilities
│
├── examples/
│   └── run_time_simulation.py   # Main experiment entry point
│
├── figures/
└── README.md
