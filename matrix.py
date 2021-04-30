
def multiply_vec_by_scalar(vec, n):
    """vec is 1D list, n - numeric"""
    new_vec = [n*c for c in vec]
    return new_vec

def multiply_matrix_by_scalar(mat, n):
    new_mat = [multiply_vec_by_scalar(row,n) for row in mat]
    return new_mat 

def mat_print(A):
    for row in A:
        row_str = ''
        for a in row:
            row_str += str(a) + ' '
        print(row_str)    

def mat_add(i, q):
    """ Subtract two square matrices with equal dims."""
    if len(i) != len(i[0]) or len(q) != len(q[0]):
        raise Exception("non-square matrices")

    if len(i) != len(q):
        raise Exception("Cannot subtract matrices of different sizes")

    s = []
    d = len(i) 
    for r in range(d):
        sRow = []
        for c in range(d):
            sRow.append(i[r][c] + q[r][c])
        s.append(sRow)
    return s

def mat_subtract(A,B):
    """Returns A-B"""
    minusB = multiply_matrix_by_scalar(B, -1)
    return mat_add(A,minusB)

def transposeMatrix(m):
    """ Transpose matrix """
    t = []
    for i in range(len(m)):
        tRow = []
        for j in range(len(m[0])):
            tRow.append(m[j][i])
        t.append(tRow)
    return t

def mat_multiply(a, b):
    """Return the product of 2 matrices of incompatible dims."""
    if a == [] or b == []:
        raise Exception("Cannot multiply empty matrices")

    if len(a[0]) != len(b):
        raise Exception("Cannot multiply matrices of incompatible sizes")

    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            dotProd = 0
            for i in range(iters):
                dotProd += a[r][i]*b[i][c]
            mRow.append(dotProd)
        m.append(mRow)
    return m
