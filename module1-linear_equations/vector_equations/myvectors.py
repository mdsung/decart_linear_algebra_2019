import math

def vec_eq(v1, v2):
    """
    checks whether two vectors are equal
    
    v1: 
    v2:
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors are of unequal length")
    for i in range(len(v1)):
        if v1[i] != v1[2]:
            return False
    return True


def alpha_x_v(alpha, v):
    """
    
    """
    newv = []
    for e in v:
        newv.append(alpha*e)
    return tuple(newv)

def alpha_x_v_2(alpha, v):
    """
    
    """
    return tuple(alpha*v for e in v)


def v_plus_v(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("vectors are not of equal length")
    newv = []
    for i in range(len(v1)):
        newv.append((v1[i]+v2[i]))
    return tuple(newv)


def l2_norm(v):
    s = 0
    for e in v:
        s += e**2
    return math.sqrt(s)
def l2_norm_v2(vt):
    s = 0
    for e in v:
        s += e*e
    return math.sqrt(s)


def inner(v1,v2):
    if len(v1) != len(v2):
        raise ValueError('vectors are not the same length')
    s = 0
    for i in range(len(v1)):
        s += v1[i]*v2[i]
    return s
def inner_v2(v1,v2):
    if len(v1) != len(v2):
        raise ValueError('vectors are not the same length')
    return sum(map(lambda x:x[0]*x[1], zip(v1,v2)))
