import numpy as np
import random as r
import src.measurement as measure

# create a function which take an arbitray complex vector has input and normalizes it
def complex_vector():
    #create a complex number
    real_num1 = r.randint(0,100)
    complex_num1 = r.randint(0,100)
    complex_num = complex(real_num1, complex_num1)

    #create another complex number
    real_num2 = r.randint(0,100)
    complex_num2 = r.randint(0,100)
    complex_num2 = complex(real_num2, complex_num2)

    #create a vector using both complex numbers
    complex_vector = np.array([complex_num1, complex_num2])

    return(complex_vector)
def inner_product(conj_vector,vector):
    inner_num = 0
    index = 0
    for i in vector:
        num = (conj_vector[index].conjugate()*i)
        inner_num += num
        index +=1
    
    return inner_num


def norm(vector):
    #the function norm(takes a complex vector and normalizes it)

    #find the inner product by multiplying each vector entry by its conjugate and the adding the results

    inner = inner_product(vector,vector)
    #finding the norm by taking the square root of the inner_product

    norm = inner**(1/2)
  
    return norm



def normalized_complex_vector():
    #creating a complecx vector
    vector = complex_vector()
    #finding the norm of the complex vector
    norm_num = norm(vector)
    new_vector = []

    for i in vector:
        num = i/norm_num
        new_vector.append(num)
    normalized_vector = np.array(new_vector)
    length = norm(normalized_vector)
    #print(f"length: {length}")

    if 0.9<=length<=1.0 :
        normalize = True
    else:
        print(f"Invalid length: {length}")
        print("false")
        normalize = False

    return normalize, normalized_vector

#checks to see if a change in global phase changes the final measurement probability

def phase_choice():
    pi = np.pi
    phase1 = np.exp(1j*(2*pi))
    phase2 = np.exp(1j*pi/2)
    phase3 = np.exp(1j*pi)
    phase4 = np.exp(1j*((3*pi)/2))

    phase_list = [phase1,phase2,phase3,phase4]

    return phase_list

def measurement_probability(input_vector):
    loop_index = 0
    difference_basis0 = 0 
    difference_basis1 = 0
    m0= 0
    m1 =0
    #iterating through each phase choice
    phases = phase_choice()
    for phase in phases:
        
        #creating new vector with phase
        vector = []
        for i in input_vector:
            num = phase*i
            vector.append(num)
        vector = np.array(vector) 

        #basis states
        basis0 = np.array([1,0])
        basis1 = np.array([0,1])
        #Finding the inner product of 0
        inner_product0 = inner_product(basis0,vector)
        #finding the inner product <1|
        inner_product1 = inner_product(basis1,vector)
      
        #finding the measurement probabilty of both basis given the inner product
        measurement_probability0 = (np.abs(inner_product0))**2
        measurement_probability1 = (np.abs(inner_product1))**2
        print(f"Phase: {phase}")
        print(f"<0|: {measurement_probability0}")
        print(f"<1|: {measurement_probability1}")
        print()
        if loop_index == 0:
            m0 = measurement_probability0
            m1= measurement_probability1
        elif loop_index > 0:
            difference0 = m0 - measurement_probability0
            difference1 = m1 - measurement_probability1

        
            difference_basis0 +=  difference0
            difference_basis1 += difference1
        
        loop_index+= 1

        
    print(f"Difference of probabilites between phases for basis vector |0> = {difference_basis0}")
    print(f"Difference of probabilites between phases for basis vector |1> = {difference_basis1}")


def physical_state(vector,basis,zero = 1e-12,):
    #taking a vector and creating anchor ro repersent a quantum state
    amps = measure.amplitudes(vector,basis)
    for i, a in enumerate(amps): #for each index i in amps pull out the amplitude a
        if abs(a)>zero:
            k = i
            break
    
    if k == None:
        print("Cannot create physical state: all amplitudes are approximately 0")
        raise ValueError
    
    else:
        #remove phase
        phase = np.angle(amps[k]) #this repersents the phase of the anchor amplitude (the angle phi arctan2(y,x))
        phase_factor = np.exp(-1j*phase)
        #multiplying the whole state by the phase_factor in order to cancel out the global phase
        state_vector = vector*phase_factor
        return state_vector







