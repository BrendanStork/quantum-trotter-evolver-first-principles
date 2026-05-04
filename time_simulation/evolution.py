from .circuit import Quantum_Circuit
from scipy import linalg

def op_exact_evolve(H, t):
    return linalg.expm(-1j*H*t)

def exact_evolve(psi0, H, t):
    U = op_exact_evolve(H, t)
    new_state = Quantum_Circuit()
    new_state.state = U @ psi0.state
    return new_state

def trotter_evolve(qc, basis, time = 1, trotter_steps = 1):
    for r in range(trotter_steps):
        for base, coeff in basis.items():
            #print(transform[base[0]])
            #print(transform[base[1]])
            #if 'II' in base:
            #    continue
            #print(' (', end='')
            for i in range(2):
                #print(base[i])
                if base[i] == 'X':
                    #op_order.extend([f'H{i}'] )
                    qc.h(i)
                    #print(f'H{i}', end=' ')
                    #print('X' )
                    #transform['X']
                elif base[i] == 'Y':
                    #op_order.extend([f'S{i}', f'H{i}']) #The list is reversed order
                    qc.sdag(i)
                    qc.h(i)
                    #print(f'Sdag{i}', end=' ')
                    #print(f'H{i}', end=' ')
                    #print('Y')
                    #transform['Y'](0)
                    #transform['Y'](1)
                if ('I' in base and base[i] != 'I'):
                    #print(f'{base}: Not CNOT coeff:{coeff}')
                    qc.rz(i, 2*coeff*time/trotter_steps)
                    #print(f'Rz(2*c={coeff}*t={t}/r={r})', end=' ')
                    #print(f'Rz(2*theta_{base})', end=' ')
                    #op_order.extend([f'Rz{i}'] )
        
            if 'I' not in base:
                #print(f'{base}: CNOT coeff:{coeff}')
                qc.cx(0,1)
                #print(f'CNOT_0,1', end=' ')
                qc.rz(1, 2*coeff*time/trotter_steps)
                #print(f'Rz(2*c={coeff}*t={t}/r={r})', end=' ')
                #print(f'Rz(2*theta_{base})', end=' ')
                qc.cx(0,1)
                #print(f'CNOT_0,1', end=' ')
                #op_order.extend(['CNOT', 'Rz1', 'CNOT'])
                #print('true')
                
            for i in range(2):
                if base[i] == 'X':
                    #op_order.extend([f'H{i}'] )
                    qc.h(i)
                    #print(f'H{i}', end=' ')
                    #print('X' )
                    #transform['X']
                elif base[i] == 'Y':
                    #op_order.extend([f'H{i}', f'Sdag{i}'])
                    qc.h(i)
                    qc.s(i)
                    #print(f'H{i}', end=' ')
                    #print(f'S{i}', end=' ')
                    #print('Y')
                    #transform['Y'](0)
                    #transform['Y'](1)
            #print(') ', end='')
        #print(qc.state)
    return qc
    
