from .gates import GATES
import numpy as np

def pauliOpGenerator():
    pauliops = ['I', 'X', 'Y', 'Z']
    paulilist = []
    for i in range(4):
        for j in range(4):
            paulilist.append(pauliops[i] + pauliops[j])
    return paulilist
    
def hamil(**Pauli):
    paulilist = pauliOpGenerator()
    for op in Pauli:
        if op not in paulilist:
            raise TypeError(f'Unknown Operator: "{op}"')
    #pauli_basis = list(Pauli)
    return Pauli
    
def exact_hamiltonian(basis):
    H = 0*1j
    for op, coeff in basis.items():
        H += coeff * np.kron(GATES[op[0]],  GATES[op[1]])
    return H
