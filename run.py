import src.state as state
import src.basis as basis
import numpy as np
import src.measurement as measure
def main():
    normalized, normalized_vector = state.normalized_complex_vector()
    if normalized == True:
        #state.measurement_probability(normalized_vector)
        basis_vectors = basis.ortho_basis(np.array([1,0]),np.array([0,1]))
        measure.measurement_trials(normalized_vector,basis_vectors,10)

       
    else:
        print("Vector is not normalized")
    


if __name__ == "__main__":
    main()