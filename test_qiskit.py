############ Testing a quibit circuit (1 qubit, 1 classical bit) with x-gate

from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

circuit = QuantumCircuit(1,1)
circuit.x(0)
circuit.barrier()
visualize_transition(circuit)
circuit.measure(0,0)
print(circuit)