# Python program to illustrate the concept
# of threading
# importing the threading module
# `import threading` is importing the threading module in Python, which provides a way to create and
# manage threads in a program.
# import threading
from threading import Lock, Thread
from assign_task import assign_mapping_by_row, assign_mapping_by_group
from utils import benchmark, init_table

import time
import random

mutex = Lock()






# arg: (thread_id, l)
# (i,j) j > i, i,j <= n-1








def run_seq(p: list, n: int):
    global m
    init_table(n)
    for L in range(1,n-1):
        for i in range(1,n-L):
            j = i + L
            for k in range(i, j):
                # print(i,j)
                m[i][j] = min(m[i][j],   m[i][k] + m[k + 1][j]
					+ p[i - 1] * p[k] * p[j])
    return m[1][n-1]

def run_parallel(p: list, n: int):
    global m
    init_table(n)
    for l in range(2,n+1): # now trigger thread
        for i in range(1,n):
            for j in range(1,n):
                if j-i+1 >= l and math.ceil((j-i+1)/2) + 1 <= l:
                    # First
                    m[i][j] = min(m[i][j], m[i][i+l-2] + m[i+l-1][j] + p[i-1]*p[i+l-2]*p[j])

                    # Second
                    m[i][j] = min(m[i][j], m[i][j-l+1] + m[j-l+2][j] + p[i-1]*p[j-l+1]*p[j])
    return m[1][n-1]




def task_parallel(thread_id: int, l: int):
    global mapping, m, p
    for (i,j) in mapping[thread_id]:
        if j-i+1 >= l and math.ceil((j-i+1)/2) + 1 <= l:
            # First
            m[i][j] = min(m[i][j], m[i][i+l-2] + m[i+l-1][j] + p[i-1]*p[i+l-2]*p[j])

            # Second
            m[i][j] = min(m[i][j], m[i][j-l+1] + m[j-l+2][j] + p[i-1]*p[j-l+1]*p[j])


def run_thread(p: list, n: int):
    global m, nums_thread
    init_table(n)
    assign_mapping(nums_thread, n)
    for l in range(2,n+1):
        list_thread = [Thread(target=task_parallel, args=(idx,l)) for idx in range(nums_thread)]

        for thread in list_thread:
            thread.start()
        
        for thread in list_thread:
            thread.join()
    return m[1][n-1]

# a = {(1,2), (2,3)}
# if (1,2) in a:
#     print("as")
import math
# mapping[0] = {(),()}
# print(list(range(1,1,-1)))

p = [100, 2, 30, 400, 50]
n = 5
nums_thread = 3

print(run_thread(p, n))



# >> Test mapping is true
# for i in mapping:
#     print(i)

# arr = [[0 for _ in range(n)] for _ in range(n)]
# for idx in range(len(mapping)):
#     for (i,j) in mapping[idx]:
#         arr[i][j] = idx + 1

# for i in range(1,n):
#     for j in range(1,n):
#         print(arr[i][j], end=' ')
#     print()