 
# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n
def matrix_chain_order(p, i, j):
    if i == j:
        return 0
 
    _min = float('inf')
 
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k)
                 + matrix_chain_order(p, k + 1, j)
                 + p[i-1] * p[k] * p[j])
 
        if count < _min:
            _min = count
 
    return _min
 
def run_recursion(p, n):
    return matrix_chain_order(p, 1, n-1)




