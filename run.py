import src.state as state
import src.basis as basis
import numpy as np
import src.measurement as measure
import src.bloch as bloch
import src.gates as gate
def main():
    normalized, normalized_vector = state.normalized_complex_vector()
    if normalized == True:
        #show meausrement probability for differenr global phases
        #state.measurement_probability(normalized_vector)
        #create basis vectors
        basis_vectors = basis.ortho_basis(np.array([1,0]),np.array([0,1]))
        #create equivalence class of vectors (state vector)
        state_vector = state.physical_state(normalized_vector,basis_vectors)
        

        print(f"State vector: {state_vector} ")
        #run n number measurement trials of measurement trails for a vector and observe measurement outcome frequencies
        measure.measurement_trials(normalized_vector,basis_vectors,10000)
        #find the coordinates on the bloch for the vectors
        valid,x,y,z = bloch.bloch_coordinates(normalized_vector)
        #plot bloch sphere
        bloch.build_sphere(valid,x,y,z,"Bloch Sphere of State Vector")


        new_vector = gate.apply_unitary(state_vector,'Pauli Y')
        print()
        print(f"Transformed vector: {new_vector} ")
        #run n number measurement trials of measurement trails for a vector and observe measurement outcome frequencies
        measure.measurement_trials(new_vector,basis_vectors,10000)
        #find the coordinates on the bloch for the vectors
        valid,x,y,z = bloch.bloch_coordinates(new_vector)
        #plot bloch sphere
        bloch.build_sphere(valid,x,y,z,"Bloch Sphere of Transformed Vector")
        


      
       
    else:
        print("Vector is not normalized")
    


if __name__ == "__main__":
    main()