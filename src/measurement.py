import src.state as state
import src.basis as basis
import numpy as np
import random as random

#create a normalized state and measurement basis
def amplitudes(vector,basis):
    #getting coeffcients for each basis vector by taking inner product
    a = state.inner_product(basis[0],vector)
    b = state.inner_product(basis[1],vector)
    amplitudes = [a,b]
    return amplitudes

def measurement_trials(vector,basis,trials):
    #generate amplitudes and use them to compute theoretical probabilites
    a = (amplitudes(vector,basis))[0]
    b = (amplitudes(vector,basis))[1]
    #Finding theoretical probabilities from amplitudes
    theo_prob0 = ((np.abs(a))**2)
    theo_prob1 = ((np.abs(b))**2)
 

    outcome0 = 0
    outcome1 = 0
    for i in range(trials):
        choice = np.random.choice([0,1],p= [theo_prob0,theo_prob1])
        if choice == 1:
            outcome1 += 1
        elif choice == 0:
            outcome0 +=1
    

    #print(f"Basis: {basis}")
    #print(f"Amplitude |0>: {a}")
    #print(f"Amplitude |1>: {b}")
    print(f"Superposition: {a:.4f}|0> + {b:.4f}|1>")
    print(f"Outcome frequency |0>: {outcome0/trials}")
    print(f"Outcome frequency |1>: {outcome1/trials}")
    if outcome0>outcome1:
        outcome_statement = "|0>"
    elif outcome1>outcome0:
        outcome_statement = "|1>"
    elif outcome1 == outcome0:
        outcome_statement = "both |1> and |0>"
    print(f"The most likely measurement outcome is {outcome_statement}")

 


