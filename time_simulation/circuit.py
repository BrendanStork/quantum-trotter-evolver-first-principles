import numpy as np
from .gates import GATES

def operator_tensor_product(Operator1, Operator2):
    return np.kron(GATES[Operator1], GATES[Operator2])

class Quantum_Circuit:
    def __init__(self, numqubits = 2):
        #self.state = np.array([1, 0, 0, 0])
        self.state = np.zeros(2**numqubits, dtype=complex)
        self.state[0] = 1
        self.numqubits = numqubits

    '''
    def build_n_qubit_operator(self, single_qubit_gate, target_qubit):
        ops = []
    
        for i in range(self.numqubits):
            if i == target_qubit:
                ops.append(single_qubit_gate)
            else:
                ops.append(GATES['I'])
        return ops
    '''
        
    def gate_op_no_params(self, Gate, qubitIndex):
        if qubitIndex == 0:
            self.state = operator_tensor_product(Gate, 'I') @ self.state
        elif qubitIndex == 1:
            self.state = operator_tensor_product('I', Gate) @ self.state
        else:
            raise ValueError('Invalid qubit index')
        return self.state
        
    def gate_op_with_params(self, Gate, qubitIndex, theta):
        if qubitIndex == 0:
            self.state = np.kron(GATES[Gate](theta), GATES['I']) @ self.state
        elif qubitIndex == 1:
            self.state = np.kron(GATES['I'], GATES[Gate](theta)) @ self.state
        else:
            raise ValueError('Invalid qubit index')
        return self.state
    
    def x(self, qubitIndex):
        return self.gate_op_no_params('X', qubitIndex)
        
        
    def y(self, qubitIndex):
        return self.gate_op_no_params('Y', qubitIndex)
        
    def z(self, qubitIndex):
        return self.gate_op_no_params('Z', qubitIndex)
        
    def h(self, qubitIndex):
        return self.gate_op_no_params('H', qubitIndex)

    def s(self, qubitIndex):
        return self.gate_op_no_params('S', qubitIndex)

    def sdag(self, qubitIndex):
        return self.gate_op_no_params('Sdag', qubitIndex)
        
    def rz(self, qubitIndex, theta):
        return self.gate_op_with_params('RZ', qubitIndex, theta)

    def P(self, theta):
        P = np.array([[1, 0],[0, np.e**(1j*theta)]])
        return P

    def cx(self, control, target):
        if control == target:
            raise ValueError('Target qubit must be different from control qubit')
        elif control == 0:
            CX = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                            [0, 0, 0, 1], [0, 0, 1, 0]])
            self.state = CX @ self.state
        elif control == 1:
            CX = np.array([[1, 0, 0, 0], [0, 0, 0, 1],
                            [0, 0, 1, 0], [0, 1, 0, 0]])
            self.state = CX @ self.state
        else:
            raise ValueError('Invalid qubit index')
        return self.state
        
    def expectation_value(self, operator1, operator2 = 'I'):
        return np.vdot(self.state, np.kron(GATES[operator1], GATES[operator2]) @ self.state)

def initialize_state(*operations):
    qc = Quantum_Circuit()
    for gate, qubit in operations:
        if gate not in GATES:
            raise ValueError(f"Unknown gate: {gate}")

        if gate == 'X':
            qc.x(qubit)
        elif gate == 'Y':
            qc.y(qubit)
        elif gate == 'Z':
            qc.z(qubit)
        elif gate == 'H':
            qc.h(qubit)
        elif gate == 'S':
            qc.s(qubit)
        elif gate == 'Sdag':
            qc.sdag(qubit)
        #elif gate == 'Rz':
        #    qc.sdag(qubit)

        return qc
        
def initialize_state(*operations):
    qc = Quantum_Circuit()
    for gate, qubit in operations:
        if gate not in GATES:
            raise ValueError(f"Unknown gate: {gate}")

        if gate == 'X':
            qc.x(qubit)
        elif gate == 'Y':
            qc.y(qubit)
        elif gate == 'Z':
            qc.z(qubit)
        elif gate == 'H':
            qc.h(qubit)
        elif gate == 'S':
            qc.s(qubit)
        elif gate == 'Sdag':
            qc.sdag(qubit)
        #elif gate == 'Rz':
        #    qc.sdag(qubit)

        return qc
        
