# Quantum Hamiltonian Simulation Framework

A modular numpy and scipy-based Python framework for simulating quantum many-body dynamics using exact and Trotterized evolution of generalized Pauli-string Hamiltonians.

The framework supports arbitrary \(N\)-qubit systems, configurable Hamiltonian construction, expectation-value analysis, fidelity benchmarking, and Trotter error characterization.

---

# Features

## Generalized Pauli-String Hamiltonians

Construct arbitrary Hamiltonians in the Pauli basis:

H = Σᵢ cᵢPᵢ

Example:

```python
basis = create_basis(
    XX = 1.0,
    YY = 1.0,
    ZZ = 0.5,
    IX = -0.2
)
```

Supports:
- Arbitrary qubit count
- Arbitrary Pauli strings
- Validation/error checking
- Dense Hamiltonian generation

---

# Time Evolution

## Exact Evolution

Implements exact unitary evolution:

|ψ(t)⟩ = e^(-iHt)|ψ(0)⟩

using matrix exponentiation.

---

## Trotterized Evolution

Implements generalized product-formula decomposition for arbitrary Pauli-string Hamiltonians.

Features include:
- Automatic basis rotations
- Generalized CNOT ladder construction
- Arbitrary \(N\)-qubit support
- Configurable Trotter step count

---

# Observables & Diagnostics

## Expectation Values

Compute expectation values of arbitrary Pauli operators:

```python
qc.expectation_value('ZZXI')
```

Supports:
- Local observables
- Multi-qubit correlators
- General Pauli-string operators

---

## Fidelity Analysis

Compute state fidelity between:
- Exact evolution
- Trotterized evolution

for benchmarking Trotter accuracy.

---

## Error Characterization

Includes utilities for:
- Absolute error analysis
- Log-scale error visualization
- Trotter convergence analysis
- Fidelity evolution over time

---

# Example

## Construct Hamiltonian

```python
basis = create_basis(
    XX = 1,
    YY = 1,
    ZZ = 1
)
```

---

## Compute Time Evolution

```python
results = expectation_vals_vs_time(
    qc,
    basis,
    expectation_operator = 'ZZ',
    trotter_steps = 30,
    time = 20
)
```

---

## Plot Observables

```python
plt.figure()

plot_expectation(
    results,
    label = '<ZZ>'
)

plt.legend()
plt.show()
```

---

# Project Structure

```text
project/
│
├── circuit.py
├── evolution.py
├── hamiltonian.py
├── expectation_values.py
├── plotting.py
│
├── examples/
│   └──run_time_simulation.py
├── figures/
└── README.md
```

---

# Core Components

## Hamiltonian Construction
Generation of dense Hamiltonians from arbitrary Pauli-string expansions.

## Quantum Circuit Simulation
Gate-based statevector simulation for arbitrary qubit counts.

## Product-Formula Dynamics
Generalized Trotter evolution for noncommuting Hamiltonian terms.

## Observable Analysis
Expectation-value and fidelity computation utilities.

---

# Dependencies

- NumPy
- SciPy
- Matplotlib

---

# Future Extensions

Planned extensions include:
- Higher-order Suzuki-Trotter formulas
- Sparse-operator support
- Jordan-Wigner transformations
- Fermionic Hamiltonians
- Hubbard-model simulation
- Tensor-network integration
- GPU acceleration

---

# Author

Brendan Stork

BS & MS Physics — Quantum Engineering  
San Jose State University

Research areas include:
- Quantum simulation
- Quantum many-body systems
- Condensed matter physics
- Hamiltonian dynamics
- Numerical quantum methods
