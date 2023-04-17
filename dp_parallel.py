import math
from utils import init_table

def run_dp_parallel(p: list, n: int):
    m = init_table(n)
    for l in range(2,n+1): # now trigger thread
        for i in range(1,n):
            for j in range(1,n):
                if j-i+1 >= l and math.ceil((j-i+1)/2) + 1 <= l:
                    # First
                    m[i][j] = min(m[i][j], m[i][i+l-2] + m[i+l-1][j] + p[i-1]*p[i+l-2]*p[j])

                    # Second
                    m[i][j] = min(m[i][j], m[i][j-l+1] + m[j-l+2][j] + p[i-1]*p[j-l+1]*p[j])
    return m[1][n-1]