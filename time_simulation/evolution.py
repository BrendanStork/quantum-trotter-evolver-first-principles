from .circuit import Quantum_Circuit
from scipy import linalg


def op_exact_evolve(H, t):
    return linalg.expm(-1j*H*t)

def exact_evolve(qc0, H, t):
    U = op_exact_evolve(H, t)
    new_state = qc0
    new_state.state = U @ qc0.state
    return new_state


######GENERAL N QUBIT TROTTER#########


def trotter_evolve(qc0, basis, time=1, trotter_steps=1):
    qc = qc0
    length_basis_term = len(next(iter(basis))) # Grabs the first basis state's length
    num_qubits = int(np.log2(len(qc.state))) # Gives number of qubits based on state coefficient length

    if num_qubits != length_basis_term:
        raise ValueError('Length of Pauli strings must equal number of qubits')
    
    dt = time / trotter_steps

    for _ in range(trotter_steps):

        for pauli_string, coeff in basis.items():
            active_qubits = []
            
            # Basis rotations
            
            for q in range(num_qubits):

                p = pauli_string[q]
                if p != 'I':
                    active_qubits.append(q)
                
                if p == 'X':
                    qc.h(q)

                elif p == 'Y':
                    qc.sdag(q)
                    qc.h(q)

            # Entangle parity (apply CNOT chain)

            for i in range(len(active_qubits) - 1):
                qc.cx(active_qubits[i],
                      active_qubits[i + 1])


            # Phase rotation
            
            if active_qubits:
                qc.rz(
                    active_qubits[-1],
                    2 * coeff * dt
                )

            # Uncompute parity (undo CNOT chain)
            
            for i in reversed(range(len(active_qubits) - 1)):
                qc.cx(active_qubits[i],
                      active_qubits[i + 1])

            # Undo basis rotations
            
            for q in range(num_qubits):

                p = pauli_string[q]

                if p == 'X':
                    qc.h(q)
                
                elif p == 'Y':
                    qc.h(q)
                    qc.s(q)

    return qc
