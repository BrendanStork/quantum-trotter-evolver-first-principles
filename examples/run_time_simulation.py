import matplotlib.pyplot as plt
from time_simulation.circuit import Quantum_Circuit
from time_simulation.hamiltonian import create_hamiltonian
from time_simulation.expectation_values import expectation_vals_vs_time, expectation_vals_vs_trotter_steps
from time_simulation.plotting import (
    plot_expectation_value_vs_time,
    plot_expectation_value_vs_steps,
    plot_error_vs_time
)

  
def main():
    
    # Hydrogen molecule Pauli basis Hamiltonian values: II = 0.4584, ZI = 0.3593, IZ = 0.48262, YY= .0896, ZZ = 0.5818)

    qc = Quantum_Circuit(2)
    basis = create_hamiltonian(II = 0.4584, ZI = 0.3593, IZ = 0.48262, YY= .0896, ZZ = 0.5818)
    
    exp_vals_YY_time = expectation_vals_vs_time(qc, basis, expectation_operator = 'YY', trotter_steps = 10, time = 10)
    exp_vals_XX_time = expectation_vals_vs_time(qc, basis, expectation_operator = 'XX', trotter_steps = 10, time = 10)
    exp_vals_YY_trot_steps = expectation_vals_vs_trotter_steps(qc, basis, expectation_operator = 'YY', trotter_steps = 40, time = 20)
    exp_vals_XX_trot_steps = expectation_vals_vs_trotter_steps(qc, basis, expectation_operator = 'XX', trotter_steps = 40, time = 20)
    
    plt.figure()
    plot_expectation_value_vs_steps(exp_vals_YY_trot_steps)
    plot_expectation_value_vs_steps(exp_vals_XX_trot_steps)
    plt.legend()
    
    plt.figure()
    plot_error_vs_time(exp_vals_XX_time)
    plt.legend()
    
    plt.figure()
    plot_expectation_value_vs_time(exp_vals_YY_time)
    plot_expectation_value_vs_time(exp_vals_XX_time)
    plt.legend()
    
    plt.show()


if __name__ == '__main__':
    main()


