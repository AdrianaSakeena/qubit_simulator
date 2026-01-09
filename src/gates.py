import numpy as np
import src.state as state
# checking if a given matrices is unitary
def is_unitary(A):
    #Given a matrix A, the function will check that it is unitary by checking the the conjugate transpose applied to the original matrix is the identity matrix

    #taking the conjugate transpose of the matrix
    conj_transposeA = np.conjugate(A).T
    #creating two row identity matrix
    shape = np.shape(A)
    identity = np.identity(shape[0])
    
    if np.allclose(conj_transposeA@A,identity):
        unitary = True
    else:
        unitary = False
    
    return unitary

def apply_unitary(vector,type,theta = None):
    # these do not include all unitary operators
    if type == 'Identity':
        #changes nothing
        unitary = np.array([[1,0],[0,1]])
    elif type == 'Pauli X':
        # Applying the Pauli X operator which swaps the amplitudes of |0> and |1>
        #rotation by pi along the x axis
        unitary = np.array([[0,1],[1,0]])
    elif type == "Pauli Y":
        #Applying the Pauli Y operator which flips amplitude and introduces phase 
        #Rotation by pi along the y axis
        unitary = np.array([[0,-1j],[1j,0]])
    elif type == 'Pauli Z':
        #Applying the Pauli Z operator which leaves probabilities unchanged and changes relative phase
        #Rotation by pi about the z axis
        unitary = np.array([[1,0],[0,-1]])
    elif type == 'Hadmard Operator':
        #Creates superposition 
        #Maps basis states to equal super positions 
        #Crucial for interference and quantum algorithms  
        #Maps z axis to x axis 
    
        unitary = np.array([[1,1],[1,-1]])*(1/(np.sqrt(2)))
    # rotation operators
    elif type == 'Rotation about x':
        #rotation about the x axis
        unitary = np.array([[np.cos(theta/2),-1j*(np.sin(theta/2))],[-1j*(np.sin(theta/2)),np.cos(theta/2)]])
    elif type == 'Rotation about y':
        #rotation about y axis
        unitary = np.array([[np.cos(theta/2),np.sin(theta/2)],[-1*(np.sin(theta/2)),np.cos(theta/2)]])

    elif type == 'Rotation about z':
        #rotation about z axis
        unitary = np.array([[np.exp(-1j*(theta/2)),0],[0,np.exp(1j*(theta/2))]])

    elif type == None:
        print("Unitary transformation type never provided")
        return None
    else:
        print("No such unitary transformation")
        return None

    # checks if matrix is truly a unitary matrix
    if is_unitary(unitary) == True:
        new_vector = unitary@vector
    else:
        print("Operator choice is not unitary.")
        print("Unable to return transformed vector.")
    # checks if the norm of the vector is still one after the transformation
    if np.isclose(state.norm(new_vector),1):
        return new_vector
    else:
        print("State vector is no longer normalized.")
        print("Unable to return transformed vector.")
    
