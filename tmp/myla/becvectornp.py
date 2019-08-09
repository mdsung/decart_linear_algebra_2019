import math 
import numpy as np
from numpy.linalg import norm

def vec_eq(v1, v2):
    """
    checks whether two vectors are equal

    v1:
    v2:
    returns boolean
    """
    assert len(v1) == len(v2)
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True


def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha

    returns vector
    """
    return [alpha*r for r in v]

def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2

    returns vector
    """
    assert len(v1) == len(v2)
    return [v1[i]+v2[i] for i in range(len(v1))]


def dot(v1,v2):
    """
    computes the dot product between two vectors

    returns scalar
    """
    return np.inner(v1,v2)

def zero(n):
    """
    returns a zero vector of dimension n
    """
    return np.zeros(n)

def print_vector(v):
    for row in v:                     
        print("|",
              ("%5.2f"%row).ljust(7),
             "|")
        
#def norm(v):
#    return 

def cos_sim(v1, v2):
    return dot(v1,v2) / (norm(v1) * norm(v2))