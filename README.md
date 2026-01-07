# Qubit Simulator
- Integrates the project’s mathematical and computational ideas into a single qubit simulator.
- Defines physical states as normalized equivalence classes in a complex vector space.
- Uses superposition and the Bloch sphere to represent and interpret single-qubit states.
- Applies unitary evolution to preserve probabilities and control state transformations.
- Demonstrates interference and entanglement as the mechanisms of quantum computation.

## Quantum State As a Normalizes Equivalence Class of Vectors in a Complex Vector Space 
Program files: state.py, run.py
  
- A qubit is represented as a quantum state in a two-dimensional complex vector space. 
- Physical states must be normalized to produce valid measurement probabilities. 
- In quantum mechanics, physical states correspond to equivalence classes of vectors that differ only by a global phase, rather than individual vectors. 
- Vectors related by a complex scalar of magnitude one yield identical measurement probabilities and represent the same physical state, known as a ray in Hilbert space, or a quantum state. 
- This project generates code to create a normalized complex vector and demonstrates computationally that multiplying a normalized state by different global phases does not change measurement outcomes. 
- This contrasts with classical state representations, where each state corresponds to a single definite outcome rather than a probability distribution.
- Within the source code folder in the python file state.py, the function physical_state creates a state vector from a given vector by removing global phase and therefore creating an equivalence class of vectors repersented by the outputted state vector
## Superposition as Linear Algebra
Program files: state.py, run.py, measurememt.py, basis.py
  
- Superposition is the representation of a quantum state as a linear combination of basis vectors in a chosen basis. 
- The coefficients of this expansion, called amplitudes, may be complex or negative and therefore cannot be interpreted directly as probabilities. 
- Probabilities are obtained using the Born rule, which assigns probabilities as the squared magnitudes of amplitudes. 
- Measurement corresponds to projecting the state vector onto a measurement basis, with outcomes occurring randomly according to these probabilities. 
- This simulation demonstrates that measurement statistics arise from the projection of a state vector onto basis vectors, and that repeated measurements produce frequencies that converge to the theoretical probabilities.
- 10 Measurement trials:
- <img width="400" height="139" alt="image" src="https://github.com/user-attachments/assets/9e77cb42-7ed7-4a74-ba98-3182cc405e73" />

- 10,000 Measurement trials:
-  <img width="443" height="140" alt="image" src="https://github.com/user-attachments/assets/61c5b41f-730c-4f5b-b533-bd6af93aafb6" />

## The Bloch Sphere 
Program files: state.py, run.py, bloch.py, basis.py, measurement.py
  
- A qubit can be written as
|ψ⟩ = α|0⟩ + β|1⟩,
where |α|² + |β|² = 1.
- Although qubit amplitudes are complex, the physical state depends only on relative amplitudes and phases.
- The Bloch sphere provides a geometric representation of pure qubit states as points on the unit sphere.
- The angle θ determines the position of the state along the z-axis:
θ = 0 corresponds to |0⟩.
θ = π corresponds to |1⟩.
- The angle φ represents the relative phase between amplitudes and determines rotation around the equator.
- A normalized state is mapped to Bloch sphere coordinates by computing:
x = ⟨ψ|σx|ψ⟩
y = ⟨ψ|σy|ψ⟩
z = ⟨ψ|σz|ψ⟩
- This mapping is implemented in bloch.py using Pauli matrices and inner products.
Program Output:
![Screenshot 2026-01-06 220522](https://github.com/user-attachments/assets/a29d6d4a-406a-4475-a454-1093e19c3eca)
![Screenshot 2026-01-06 220546](https://github.com/user-attachments/assets/a8f2f35e-67ad-42a3-9992-c5c7bf73375d)
![Screenshot 2026-01-06 220642](https://github.com/user-attachments/assets/8265d8cf-dcb2-4244-b6a4-6e2ae5ec1d1e)














