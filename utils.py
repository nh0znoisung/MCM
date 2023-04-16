import time

# For benchmarking - Compare the performance of some function
def benchmark(nums_thread):
    start = time.time()
    # run_thread(nums_thread)
    end = time.time()
    print(f"{nums_thread} threads in {end-start} s")


def init_table(n: int):
    global m
    m = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(1,n): #index from 1 to n-1
        m[i][i] = 0

def clear_table():
    global m
    m = []

def print_table(n):
    for i in range(1,n):
        for j in range(1,n):
            print(m[i][j], end=' ')
        print()