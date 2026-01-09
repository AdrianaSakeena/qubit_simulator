import src.state as state
import numpy as np
import matplotlib.pyplot as plt
#takes a normalized vector and finds components
def bloch_coordinates(vector):
    #find coordinates by applying pauli matricies
    #finding x coordinate by applying Pauli x operator
    psix = vector
    #the Pauli X operator
    Pauli_operatorX = np.array([[0,1],[1,0]],dtype= complex)
    #Applying the Pauli X operator to the vector
    Ax = Pauli_operatorX@psix
    #take inner product with original vector
    x = state.inner_product(psix,Ax)

    #finding the y coordinate by applying the Pauli Y operator
    psiy = vector
    #The Pauli Y operator
    Pauli_operatorY = np.array([[0,-1j],[1j, 0]],dtype = complex)
    #Applying the Pauli Y operator to the vector
    Ay = Pauli_operatorY@psiy
    #take inner product with original vector
    y = state.inner_product(psiy,Ay)

    #finding the z coordinate by applying the Pauli Y operator
    psiz = vector
    # The Pauli z operator
    Pauli_operatorZ = np.array([[1,0],[0,-1]],dtype = complex)
    # Applying the Pauli Z operator ro the vector
    Az = Pauli_operatorZ@psiz
    #take inner product with original vector
    z = state.inner_product(psiz,Az)
    #returns x y and z coordinates
    r2 = ((x**2)+(y**2)+(z**2))
    if np.isclose(r2,1.0,atol = 1e-8):#check to see if they are close to 1 (normalized)
        valid = True
        print()
        print("Coordinates of Bloch Sphere:")
        print(f"X: {x}")
        print(f"Y: {y}")
        print(f"Z: {z}")

    
    else:
        print("Invalid Bloch vector: |r|^2 = {r2}")
        valid = False
    
    return valid,x,y,z
    
def angle_converter(x,y,z):
    #take coordinates and converts them to angles on the bloch sphere
    theta = np.arccos(z)
    phi = np.arctan2(y,x)

    return theta,phi

    

def build_sphere(valid,x,y,z,label):
    #creating the figure
    if valid == True:
        fig = plt.figure()
        sub = fig.add_subplot(111,projection = '3d')
        # creating array for 0 to pi values
        pi = np.pi
        theta = np.linspace(0,pi,num= 75)
        phi = np.linspace(0,2*pi,num = 75)
        #creating a meshgrid containing possible coordinates
        theta,phi = np.meshgrid(theta,phi,indexing = "xy")
        #creating the surface coordinates
        x_surf = (np.sin(theta))*(np.cos(phi))
        y_surf = (np.sin(theta))*(np.sin(phi))
        z_surf = (np.cos(theta))

        #plotting the sphere such that it skips no rows or columns, sets the surface color, and makes it semitransparent
        sub.plot_surface(x_surf,y_surf,z_surf,rstride = 
        1,cstride = 1,color = 'lightblue',alpha = 0.3,linewidth =0)
        #setting axis limits
        sub.set_xlim((-1,1))
        sub.set_ylim((-1,1))
        sub.set_zlim((-1,1)) 
        #labelling axes
        sub.set_xlabel('X')
        sub.set_ylabel('Y')
        sub.set_zlabel('Z')
        #keep the box round
        sub.set_box_aspect([1,1,1])
        #set ticks so that they do not get bunched up on the screen
        sub.set_xticks([-1,-.5,0,.5,1])
        sub.set_yticks([-1,-.5,0,.5,1])
        sub.set_zticks([-1,-.5,0,.5,1])
        # creating the arrow
        sub.quiver(0,0,0,x,y,z,color= 'red',linewidth = 2)
        sub.set_title(label)
        plt.show()
        plt.clf()
    else:
        print("Unable to plot Bloch Sphere")
