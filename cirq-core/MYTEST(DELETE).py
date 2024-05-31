from cirq.ops import PauliString
import cirq

a, b = cirq.LineQubit.range(2)
Xa = cirq.X(a)
Zb = cirq.Z(b)
print(PauliString([Xa]) * PauliString([Zb]) ** 3)
print(Zb ** 3)