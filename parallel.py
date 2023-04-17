
from threading import Thread, Lock
from assign_task import assign_mapping_by_row, assign_mapping_by_group
from utils import init_table
import math

## >> Global configs for Parallel
# assign task for each thread. Each thread have id is the index of mapping
# the element is a set (hash table best for finded) of tuple (containes a couple (i,j))
mapping: list[set[tuple[int,int]]] 

# memory table for Dynamic programming approach
m: list[list] 

# list of dimensions
p: list[int]

def task_parallel(thread_id: int, l: int):
    global m # only m change
    for (i,j) in mapping[thread_id]:
        if j-i+1 >= l and math.ceil((j-i+1)/2) + 1 <= l:
            # First
            m[i][j] = min(m[i][j], m[i][i+l-2] + m[i+l-1][j] + p[i-1]*p[i+l-2]*p[j])

            # Second
            m[i][j] = min(m[i][j], m[i][j-l+1] + m[j-l+2][j] + p[i-1]*p[j-l+1]*p[j])


def run_parallel(_p: list, n: int, nums_thread: int, is_time: bool = False):
    global m, p, mapping
    m = init_table(n)
    p = _p
    mapping = assign_mapping_by_group(nums_thread, n) # Or assign_mapping_by_row

    import time
    interval = 0
    for l in range(2,n+1):
        start = time.time()
        list_thread = [Thread(target=task_parallel, args=(idx,l)) for idx in range(nums_thread)]

        # interval += time.time() - start1
        for thread in list_thread:
            thread.start()
        
        # start2 = time.time()
        for thread in list_thread:
            thread.join()
        interval += time.time() - start
    
    if is_time:
        return (m[1][n-1], interval/10)
    else:
        return m[1][n-1]