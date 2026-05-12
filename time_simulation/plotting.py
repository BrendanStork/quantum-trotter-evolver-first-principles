import matplotlib.pyplot as plt
import numpy as np
from .circuit import Quantum_Circuit
from .evolution import trotter_evolve, exact_evolve
from .expectation_values import expectation_vals_vs_time, expectation_vals_vs_trotter_steps
    

def plot_expectation_value_vs_time(expectation_vals, exclusive = None, **plot_kwargs):
    
    t = expectation_vals[0]
    valsExact = expectation_vals[1]
    valsTrot = expectation_vals[2]
    expectation_operator = expectation_vals[3]
    trotter_steps = expectation_vals[4]
    
    if exclusive == 'trotter':
        plt.plot(t, valsTrot, marker = '.', label = rf'Trotter $\langle {expectation_operator} \rangle$', **plot_kwargs)
    elif exclusive == 'exact':
        plt.plot(t, valsExact, **plot_kwargs, label = rf'Exact $\langle {expectation_operator} \rangle$')
    elif exclusive == None:
        plt.plot(t, valsTrot, marker = '.', label = rf'Trotter $\langle {expectation_operator} \rangle$', **plot_kwargs)
        plt.plot(t, valsExact, **plot_kwargs, label = rf'Exact $\langle {expectation_operator} \rangle$')
    else:
        raise ValueError("Exclusive must be 'trotter' or 'exact'")
        
    plt.xlabel('Time', size = 15, **plot_kwargs)
    plt.ylabel('Expectation Value', size = 15, **plot_kwargs)
    plt.title(fr'Exact vs Trotterized Time Evolution (n={trotter_steps})', size = 15, **plot_kwargs)
    plt.xlim(0, t[-1])
    #plt.legend()


def plot_expectation_value_vs_steps(steps_expectation_vals, **plot_kwargs):
    steps_array = steps_expectation_vals[0]
    vals_steps = steps_expectation_vals[1]
    expectation_operator = steps_expectation_vals[2]
    
    plt.plot(steps_array, vals_steps, label = rf'Trotter $\langle {expectation_operator} \rangle$', **plot_kwargs)
    plt.xlabel('Trotter Steps', size = 15, **plot_kwargs)
    plt.ylabel('Expectation Value', size = 15, **plot_kwargs)
    plt.title(fr'Expectation Value vs Trotter Steps', size = 15, **plot_kwargs)
    plt.xlim(1, steps_array[-1])
    #plt.legend()


def plot_error_vs_time(expectation_vals, method = 'absolute', **plot_kwargs):
    t = expectation_vals[0]
    error_array = np.abs(expectation_vals[2] - expectation_vals[1])
    expectation_operator = expectation_vals[3]
    trotter_steps = expectation_vals[4]

    plt.plot(t, error_array, label = rf'Error $\langle {expectation_operator} \rangle$', **plot_kwargs)
    plt.xlabel('Time', size = 15, **plot_kwargs)
    plt.ylabel('Expectation Value Error', size = 15, **plot_kwargs)
    plt.title(fr'Absolute Trotter Error vs Time', size = 15, **plot_kwargs)
    plt.xlim(1, t[-1])
    #plt.legend()
