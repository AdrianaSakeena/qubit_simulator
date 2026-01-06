# Qubit Simulator
- Integrates the project’s mathematical and computational ideas into a single qubit simulator.
- Defines physical states as normalized equivalence classes in a complex vector space.
- Uses superposition and the Bloch sphere to represent and interpret single-qubit states.
- Applies unitary evolution to preserve probabilities and control state transformations.
- Demonstrates interference and entanglement as the mechanisms of quantum computation.

## Quantum State As a Normalizes Equivalence Class of Vectors in a Complex Vector Space (code in state.py and run.py)
- A qubit is represented as a quantum state in a two-dimensional complex vector space. 
- Physical states must be normalized to produce valid measurement probabilities. 
- In quantum mechanics, physical states correspond to equivalence classes of vectors that differ only by a global phase, rather than individual vectors. 
- Vectors related by a complex scalar of magnitude one yield identical measurement probabilities and represent the same physical state, known as a ray in Hilbert space, or a quantum state. 
- This project generates code to create a normalized complex vector and demonstrates computationally that multiplying a normalized state by different global phases does not change measurement outcomes. 
- This contrasts with classical state representations, where each state corresponds to a single definite outcome rather than a probability distribution. 
## Superposition as Linear Algebra
- Superposition is the representation of a quantum state as a linear combination of basis vectors in a chosen basis. 
- The coefficients of this expansion, called amplitudes, may be complex or negative and therefore cannot be interpreted directly as probabilities. 
- Probabilities are obtained using the Born rule, which assigns probabilities as the squared magnitudes of amplitudes. 
- Measurement corresponds to projecting the state vector onto a measurement basis, with outcomes occurring randomly according to these probabilities. 
- This simulation demonstrates that measurement statistics arise from the projection of a state vector onto basis vectors, and that repeated measurements produce frequencies that converge to the theoretical probabilities.
- 10,000 Measurement trials:
-  <img width="443" height="140" alt="image" src="https://github.com/user-attachments/assets/61c5b41f-730c-4f5b-b533-bd6af93aafb6" />






