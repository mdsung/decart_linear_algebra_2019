from .becvector import *
import math

def print_matrix(m, width=7):
    for row in range(len(m[0])):                     
        print("|"," ".join([("%5.2f"%m[col][row]).ljust(width) for col in range(len(m))]), "|")

def m_x_v(m,v):
    assert len(v) == len(m)
    rslt = zero(len(m[0]))
    for i in range(len(m)):
        col = m[i]
        col2 = alpha_x_v(v[i], col)
        rslt = v_plus_v(rslt, col2)
    return rslt

def m_x_v2(m,v):
    assert len(v) == len(m)
    rslt = zero(len(m[0]))
    for col, alpha in zip(m,v):
        print(col)
        print(alpha)
        print("*"*20)
        col2 = alpha_x_v(alpha, col)
        rslt = v_plus_v(rslt,col2)
    return rslt

def m_x_m(A, B):
    return [m_x_v2(A, b) for b in B]

def m_x_m2(A, B):
    assert len(A) == len(B[0])
    rslt = []
    for b in B:
        rslt.append(m_x_v2(A,b))
    return rslt

def get_rot(phi, units="degrees"):
    if units.lower()[0] == "d":
        phi = math.pi * phi / 180
    rot_mat = [[math.cos(phi), math.sin(phi)], [-math.sin(phi), math.cos(phi)]]
    return rot_mat

def rotate_vec(v,phi, units="degrees"):
    return m_x_v2(get_rot(phi, units), v)

def transpose(a):
    new_a = []
    for n in range(len(a[0])):
        new_r = []
        for m in range(len(a)):
            new_r.append(a[m][n])
        new_a.append(new_r)
    return new_a