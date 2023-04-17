import time

# For benchmarking - Compare the performance of some function
def benchmark(func, p, n, **kwargs):
    start = time.time()
    res = func(p, n, **kwargs)
    end = time.time()
    return (res, end-start)


def read_testcase(filename: str = 'sample.txt'):
    with open(filename, 'r') as f:
        read = f.readlines()
        n = int(read[0])
        p = list(map(lambda x: int(x), read[1:]) ) 
        return p, n

def init_table(n: int):
    m = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(1,n): #index from 1 to n-1
        m[i][i] = 0
    return m


def print_table(m,n):
    """
    m: memorization table
    n: size of array
    """
    for i in range(1,n):
        for j in range(1,n):
            print(m[i][j], end=' ')
        print()