import math
import random
# from configs import *


def assign_mapping_by_row(nums_thread, n):
    # global mapping
    mapping = [set() for _ in range(nums_thread)]
    for l in range(n-2,0,-1):
        t = n-1-l # nums of nodes
        m = t%nums_thread
        curr = 1
        for thread_id in range(m):
            for _ in range(math.ceil(t/nums_thread)):
                mapping[thread_id].add( (curr,curr+l) )
                curr += 1
        for thread_id in range(m,nums_thread):
            for _ in range(math.floor(t/nums_thread)):
                mapping[thread_id].add( (curr,curr+l) )
                curr += 1
    return mapping


def generate_mapping_list(n):
    return [(i,j) for i in range(1,n) for j in range(i+1,n)]

def assign_mapping_by_group(nums_thread, n):
    mapping_list = generate_mapping_list(n)
    random.shuffle(mapping_list)
    mapping = [set(mapping_list[i::nums_thread]) for i in range(nums_thread)]
    return mapping



# >> Test mapping is true
def test_mapping():
    n = 6
    k = 3
    mapping = assign_mapping_by_group(k,n)

    for i in mapping:
        print(i)

    arr = [[0 for _ in range(n)] for _ in range(n)]
    for idx in range(len(mapping)):
        for (i,j) in mapping[idx]:
            arr[i][j] = idx + 1

    for i in range(1,n):
        for j in range(1,n):
            print(arr[i][j], end=' ')
        print()