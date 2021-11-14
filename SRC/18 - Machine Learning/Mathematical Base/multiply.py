import numpy as np

# Variables.

vx = np.array([1,2,3,4,5])
vy = np.array([1,2,3,4,5])
mx = np.array([[1,2,3,4,5],[6,7,8,9,10]])
my = np.array([[1,2,3,4,5],[6,7,8,9,10]])
tx = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[-1,-2,-3,-4,-5],[-6,-7,-8,-9,-10]]])
ty = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[-1,-2,-3,-4,-5],[-6,-7,-8,-9,-10]]])

# Array Multiply.

def xmultiply(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        x[i] *= y[i]
    return x

# Matrix Multiply.

def mmultiply(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] *= y[i,j]
    return x

# Tensor Multiply.

def tmultiply(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for q in range(x.shape[2]):
                x[i,j,q] *= y[i,j,q]
    return x

def cvxcross(x,y):
    # X is Matrix.
    # Y is Vector.
    # Ndim Comprasion Always Have to be Like That : X > Y.
    # Vector values added seperately to each matrix columns.
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] *= y[j]
    return x

# RESULTS.

print(f"\n\nVX * VY\n{xmultiply(vx,vy)}\nNdim: {vx.ndim}")
print(f"\n\nMX * MY\n{mmultiply(mx,my)}\nNdim: {mx.ndim}")
print(f"\n\nTX * TY\n{tmultiply(tx,ty)}\nNdim: {tx.ndim}")
print(f"\n\nMX * VX\n{cvxcross(mx,vx)}")