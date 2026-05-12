from .gates import GATES
import numpy as np

def string_to_operator(pauli_string):
    operator = GATES[pauli_string[0]] # Builds operator
    for p in pauli_string[1:]:
        operator = np.kron(operator, GATES[p])
    return operator


def create_hamiltonian(**pauli_terms):
    if not pauli_terms:
        raise ValueError('Hamiltonian cannot be empty')`
        
    pauli_ops = ['I', 'X', 'Y', 'Z']
    lengths = {len(term) for term in pauli_terms} # If all the terms have the same length, set length = 1
    
    if len(lengths) != 1:
        raise ValueError('All Pauli strings must have the same length')

    for term, coeff in pauli_terms.items():
        if not isinstance(term, str):
            raise TypeError(f'{term} is not a string')
            
        if not isinstance(coeff, (int, float, complex)):
            raise TypeError(f'Coefficient for "{term}" must be a real number')
    return pauli_terms


def exact_hamiltonian(basis):
    H = 0*1j
    for op, coeff in basis.items():
        H += coeff * string_to_operator(op)
    return H
