import numpy as np
import src.state as state

#creating an orthonormal basis
def ortho_basis(b0,b1):

    #checking to make sure vectors are normalized and orthogonal
    try:
        if state.norm(b0) == 1 and state.norm(b1)==1:
            if state.inner_product(b0,(b1.conjugate())) == 0:
                basis = np.array([b0,b1])
                return basis
        else:
            raise ValueError
    except ValueError:
        print("Vectors are not an orthonormal basis")
        return None
    


    

