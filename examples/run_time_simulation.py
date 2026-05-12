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
    
    # Reference 2-qubit Hydrogen molecule Pauli basis reduced Hamiltonian:
    # (II = 0.4584, ZI = 0.3593, IZ = 0.48262, YY= .0896, ZZ = 0.5818)
	
	# 5 qubits example
    qc = Quantum_Circuit(5)
    
    # Example basis
    basis = create_hamiltonian(ZZZZZ = 0.4584, ZIYXX = 0.3593, XXYIZ = 0.48262, YYXXX= .0896, ZIIXZ = 0.5818) # Basis coeficients
    
    
    # Time-evolved expectation values
    exp_vals_YY_time = expectation_vals_vs_time(qc, basis, expectation_operator = 'YYYYY', trotter_steps = 50, time = 15)
    exp_vals_XX_time = expectation_vals_vs_time(qc, basis, expectation_operator = 'XXXXX', trotter_steps = 50, time = 15)
    
    # Expectation values at time "t" vs amount of trotter steps
    exp_vals_YY_trot_steps = expectation_vals_vs_trotter_steps(qc, basis, expectation_operator = 'YYYYY', trotter_steps = 50, time = 15)
    exp_vals_XX_trot_steps = expectation_vals_vs_trotter_steps(qc, basis, expectation_operator = 'XXXXX', trotter_steps = 50, time = 15)
    
	# Expectation values vs Trotter steps
    plt.figure()
    plot_expectation_value_vs_steps(exp_vals_YY_trot_steps)
    plot_expectation_value_vs_steps(exp_vals_XX_trot_steps)
    plt.legend()
    
    # Exact vs Trotter error plot
    plt.figure()
    plot_error_vs_time(exp_vals_XX_time)
    plt.legend()
    
	# Time-evolved expectation values plots
    plt.figure()
    plot_expectation_value_vs_time(exp_vals_YY_time)
    plot_expectation_value_vs_time(exp_vals_XX_time)
    plt.legend()
    
    plt.show()


if __name__ == '__main__':
    main()


