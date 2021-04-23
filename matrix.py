
def multiply_vec_by_scalar(vec, n):
    new_vec = [n*c for c in vec]
    return new_vec

def multiply_matrix_by_scalar(mat, n):
    new_mat = [multiply_vec_by_scalar(row,n) for row in mat]
    return new_mat 

def multiply_mat_by_mat(A,B):
    pass

def transpose(mat):
    pass

def print_matrix(A):
    for row in A:
        row_str = ''
        for a in row:
            row_str += str(a) + ' '
        print(row_str)
        
    

def add_mat(A,B):
    pass

# print(multiply_vec_by_scalar([1,1,1],3))

# A = [[1,1,1],[2,2,2],[3,3,3]]
# print(multiply_matrix_by_scalar(A,4))

A = [[1,2],[3,4]]
print_matrix(A)