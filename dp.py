from utils import init_table

def run_dp(p: list, n: int):
    m = init_table(n)
    for L in range(1,n-1):
        for i in range(1,n-L):
            j = i + L
            for k in range(i, j):
                # print(i,j)
                m[i][j] = min(m[i][j],  m[i][k] + m[k + 1][j]
					+ p[i - 1] * p[k] * p[j])
    return m[1][n-1]
