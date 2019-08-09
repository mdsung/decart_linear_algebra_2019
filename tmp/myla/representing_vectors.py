
def vec_eq(v1, v2):
    """
    checks whether two vectors are equal
    
    v1: 
    v2:
    """
    assert len(v1) == len(v2)
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True

def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha
    """
    return [alpha*element for element in v]

def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2
    """
    assert len(v1) == len(v2)
    return [v1[i] + v2[i] for i in range(len(v1))]

def dot(v1,v2):
    assert len(v1) == len(v2)
    rslt = 0.0
    for i in range(len(v1)):
        rslt += v1[i]*v2[i]
    return rslt

