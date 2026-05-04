import matplotlib.pyplot as plt
import numpy as np
from .circuit import Quantum_Circuit
from .evolution import trotter_evolve, exact_evolve

def plot_trotter_expectation_value_vs_time(basis, trotter_steps = 1, time = 1):
    t = np.linspace(0, time, num=100)
    
    exp_arrayZ0_time = np.zeros((len(t)), dtype = 'complex')
    exp_arrayY0_time = np.zeros((len(t)), dtype = 'complex')
    exp_arrayX0_time = np.zeros((len(t)), dtype = 'complex')
    exp_arrayZ1_time = np.zeros((len(t)), dtype = 'complex')
    exp_arrayY1_time = np.zeros((len(t)), dtype = 'complex')
    exp_arrayX1_time = np.zeros((len(t)), dtype = 'complex')

    for i in range(len(t)):
        qc = Quantum_Circuit()
        psi = trotter_evolve(qc, basis, time = t[i], trotter_steps=trotter_steps)
        #print(psi.expectation_value('Z'))
        exp_arrayZ0_time[i] = psi.expectation_value('Z')
        exp_arrayY0_time[i] = psi.expectation_value('Y')
        exp_arrayX0_time[i] = psi.expectation_value('X')
    
        exp_arrayZ1_time[i] = psi.expectation_value('I', 'Z')
        exp_arrayY1_time[i] = psi.expectation_value('I', 'Y')
        exp_arrayX1_time[i] = psi.expectation_value('I', 'X')

    plt.plot(t, exp_arrayZ0_time.real, label = '<Z0>')
    plt.plot(t, exp_arrayY0_time.real, label = '<Y0>')
    plt.plot(t, exp_arrayX0_time.real, label = '<X0>')
    
    #plt.plot(time, exp_arrayZ1_time.real, label = '<Z1>')
    #plt.plot(time, exp_arrayY1_time.real, label = '<Y1>')
    #plt.plot(time, exp_arrayX1_time.real, label = '<X1>')
    plt.title('Trotterize <Z> vs t', fontsize = 15)
    plt.xlabel('Time', fontsize = 15)
    plt.ylabel(r'$<O>$', fontsize = 15)
    plt.legend()
    plt.show()
    
def plot_expectation_value_vs_trotter_steps(basis, time = 1, trotter_steps = 10):
    r_array = np.arange(1, trotter_steps+1, 1)
    
    exp_arrayZ0_r = np.zeros((len(r_array)), dtype = 'complex')
    exp_arrayY0_r = np.zeros((len(r_array)), dtype = 'complex')
    exp_arrayX0_r = np.zeros((len(r_array)), dtype = 'complex')
    
    exp_arrayZ1_r = np.zeros((len(r_array)), dtype = 'complex')
    exp_arrayY1_r = np.zeros((len(r_array)), dtype = 'complex')
    exp_arrayX1_r = np.zeros((len(r_array)), dtype = 'complex')

    for i in range(len(r_array)):
        qc = Quantum_Circuit()
        psi = trotter_evolve(qc, basis, time = 1, trotter_steps=r_array[i])
        #print(psi.expectation_value('Z'))
        exp_arrayZ0_r[i] = psi.expectation_value('Z')
        exp_arrayY0_r[i] = psi.expectation_value('Y')
        exp_arrayX0_r[i] = psi.expectation_value('X')
    
        exp_arrayZ1_r[i] = psi.expectation_value('I', 'Z')
        exp_arrayY1_r[i] = psi.expectation_value('I', 'Y')
        exp_arrayX1_r[i] = psi.expectation_value('I', 'X')

    plt.plot(r_array, exp_arrayZ0_r.real, label = '<Z0>')#, title = '<Z> vs t')
    #plt.plot(r_array, exp_arrayY0_r, label = '<Y0>')#, title = '<Z> vs t')
    #plt.plot(r_array, exp_arrayX0_r, label = '<X0>')#, title = '<Z> vs t')
    
    #plt.plot(r_array, exp_arrayZ1_r, label = '<Z1>')#, title = '<Z> vs t')
    #plt.plot(r_array, exp_arrayY1_r, label = '<Y1>')#, title = '<Z> vs t')
    #plt.plot(r_array, exp_arrayX1_r, label = '<X1>')#, title = '<Z> vs t')
    plt.title('<O> vs r', fontsize = 15)
    plt.xlabel('r', fontsize = 15)
    plt.ylabel(r'$<O>$', fontsize = 15)
    plt.legend()
    plt.show()
    
##For EXACT evolution
def plot_exact_expectation_value_vs_time(H, time = 1):
    #psi0 = Quantum_Circuit()
    #H = exact_hamiltonian(ZZ = -1.0, IX = -0.5, XI = -0.5)
    t = np.linspace(0, time, num=100)
    #exact_psi = exact_evolve(psi0, H, 1.1)
    #exact_psi.state
    #exact_psi.state, psi0.state
    
    
    
    exact_exp_arrayZ0_time = np.zeros((len(t)), dtype = 'complex')
    exact_exp_arrayY0_time = np.zeros((len(t)), dtype = 'complex')
    exact_exp_arrayX0_time = np.zeros((len(t)), dtype = 'complex')
    
    exact_exp_arrayZZ_time = np.zeros((len(t)), dtype = 'complex')
    
    exact_exp_arrayZ1_time = np.zeros((len(t)), dtype = 'complex')
    exact_exp_arrayY1_time = np.zeros((len(t)), dtype = 'complex')
    exact_exp_arrayX1_time = np.zeros((len(t)), dtype = 'complex')
    #print(np.size(exact_exp_arrayX1_time), np.size(time))
    for i in range(len(t)):
        psi0 = Quantum_Circuit()
        exact_psi = exact_evolve(psi0, H, t[i])
        #print(i)
        #print(exact_psi.state)
        #print(psi.expectation_value('Z'))
        exact_exp_arrayZ0_time[i] = exact_psi.expectation_value('Z')
        exact_exp_arrayY0_time[i] = exact_psi.expectation_value('Y')
        #print(exact_exp_arrayY0_time[i])
        exact_exp_arrayX0_time[i] = exact_psi.expectation_value('X')
    
        #exact_exp_arrayZ1_time[i] = exact_psi.expectation_value('I', 'Z')
        #exact_exp_arrayY1_time[i] = exact_psi.expectation_value('I', 'Y')
        #exact_exp_arrayX1_time[i] = exact_psi.expectation_value('I', 'X')
    
        #exact_exp_arrayZZ_time[i] = exact_psi.expectation_value('Z', 'Z')
    
    plt.plot(t, exact_exp_arrayZ0_time.real, label = '<Z0>')#, title = '<Z> vs t')
    plt.plot(t, exact_exp_arrayY0_time.real, label = '<Y0>')#, title = '<Z> vs t')
    plt.plot(t, exact_exp_arrayX0_time.real, label = '<X0>')#, title = '<Z> vs t')
    
    #plt.plot(time, exp_arrayZ1_time.real, label = '<Z1>', marker = '.'), ls = 'dashdot')#, title = '<Z> vs t')
    #plt.plot(time, exp_arrayY1_time.real, label = '<Y1>', marker = '.'), ls = 'dashdot')#, title = '<Z> vs t')
    #plt.plot(time, exp_arrayX1_time.real, label = '<X1>', marker = '.') #, ls = 'dashdot')#, title = '<Z> vs t')
    
    #plt.plot(t, exact_exp_arrayZZ_time.real, label = '<ZZ>')#, title = '<Z> vs t')
    plt.title('Exact <O> vs t', fontsize = 15)
    plt.xlabel('Time', fontsize = 15)
    plt.ylabel(r'$<O>$', fontsize = 15)
    plt.legend()
    plt.show()
#print(time)
