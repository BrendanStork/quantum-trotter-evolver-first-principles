from time_simulation.hamiltonian import hamil, exact_hamiltonian
from time_simulation.plotting import (
    plot_exact_expectation_value_vs_time,
    plot_trotter_expectation_value_vs_time
)
  
def main():
    
    #basis = hamil(II = -0.4584, ZI = 0.3593, IZ = -0.48262, ZZ = 0.5818, XX = 0.0896, YY = 0.0896 )
    basis = hamil(ZZ = -1.0, IX = -0.5, XI = -0.5, YY = 0.4)
    H = exact_hamiltonian(basis)
    
    plot_exact_expectation_value_vs_time(H, time = 10)
    plot_trotter_expectation_value_vs_time(basis, trotter_steps=100, time = 10)


if __name__ == '__main__':
    main()


