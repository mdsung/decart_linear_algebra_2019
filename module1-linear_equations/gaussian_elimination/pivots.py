import numpy as np

def find_pivot(c):
    m = c.shape[0]
    maxv = c[0]
    argmax = 0
    for i in range(1,m):
        if c[i] > maxv:
            maxv = c[i]
            argmax = i
        print("i=%d"%i)
        print("argmax=%f"%argmax)
    return argmax

def pivot_rows(a,k):
    # find pivot
    A = np.matrix.copy(a)
    pivot_row = find_pivot(A[k,k:])
    print(pivot_row)
    tmp = A[k,:]
    A[k,:] = A[pivot_row,:]
    A[pivot_row,:] = tmp
    return A

def pivot_rows(a,k):
    # find pivot
    A = np.matrix.copy(a)
    pivot_row = find_pivot(A[k:,k])
    print(pivot_row)
    tmp = A[k,:]
    A[k,:] = A[pivot_row,:]
    A[pivot_row,:] = tmp
    return A

def pivot_rows(a,_b,k):
    # find pivot
    A = np.matrix.copy(a)
    b = np.matrix.copy(_b)
    pivot_row = find_pivot(A[k:,k])
    print(pivot_row)
    tmp = A[k,:].copy()
    A[k,:] = A[pivot_row,:]
    A[pivot_row,:] = tmp
    return A

def pivot_rows(a,b,k):
    # find pivot
    pivot_row = find_pivot(A[k:,k])
    print(pivot_row)
    tmp = A[k,:].copy()
    A = swap_rows(a,k,pivot_row)
    b = swap_rows(b,k,pivot_row)
    return A,b
