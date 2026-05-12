from .evolution import trotter_evolve, exact_evolve
from .circuit import Quantum_Circuit
from .hamiltonian import exact_hamiltonian


def expectation_vals_vs_time(qc0, basis, *, expectation_operator, trotter_steps = 10, time = 10, timesteps = 100): # method,
    t = np.linspace(0, time, num = timesteps)
    H = exact_hamiltonian(basis)
    valsTrot = np.zeros((len(t)))
    valsExact = np.zeros((len(t)))

    for i in range(len(t)):
        psi_trotter0 = qc0.copy()
        psi_exact0 = qc0.copy()
        psi_trotter = trotter_evolve(psi_trotter0, basis, time = t[i], trotter_steps=trotter_steps)
        valsTrot[i] = psi_trotter.expectation_value(expectation_operator)
        psi_exact = exact_evolve(psi_exact0, H, t[i])
        valsExact[i] = psi_exact.expectation_value(expectation_operator)

    return t, valsExact, valsTrot, expectation_operator, trotter_steps
    
def expectation_vals_vs_trotter_steps(qc0, basis, *, expectation_operator, trotter_steps = 10, time = 10):
    steps_array = np.arange(1, trotter_steps+1, 1)
    vals_steps = np.zeros((len(steps_array)))

    for i in range(len(steps_array)):
        qc = qc0.copy()
        psi = trotter_evolve(qc, basis, time = time, trotter_steps=steps_array[i])
        vals_steps[i] = psi.expectation_value(expectation_operator)


    return steps_array, vals_steps, expectation_operator
