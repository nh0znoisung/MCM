import numpy as np
import matplotlib.pyplot as plt
import glob
from utils import read_testcase

from dp_parallel import run_dp_parallel
from recursion import run_recursion
from dp import run_dp
from parallel import run_parallel
from utils import benchmark

nums_thread = 4


def get_result():
    dim_list = [] # x
    rec_list = []
    dp_list = []
    dp_par_list = []
    parallel_list = []
    lst_file = glob.glob('testcases-approach/*')
    lst_file.sort()


    for filename in lst_file:
        print("Start", filename)
        p, n = read_testcase(filename)
        (_, rec_elapse) = benchmark(run_recursion, p, n)
        (_, dp_elapse) = benchmark(run_dp, p, n)
        (_, dp_par_elapse) = benchmark(run_dp_parallel, p, n)
        (_, parallel_elapse) = run_parallel(p, n, nums_thread, True)

        # Add to list
        dim_list.append(n)
        rec_list.append(rec_elapse)
        dp_list.append(dp_elapse)
        dp_par_list.append(dp_par_elapse)
        parallel_list.append(parallel_elapse)

        print("Done", filename)

    return dim_list, rec_list, dp_list, dp_par_list, parallel_list

# Compare time / #of ele in 4 approach, 5-thread

# print(get_result())

dim_list, rec_list, dp_list, dp_par_list, parallel_list = get_result()




# plotting the points 
# plt.plot(dim_list, rec_list, label='Recursion')
plt.plot(dim_list, dp_list, label='Dynamic Programming')
plt.plot(dim_list, dp_par_list, label='DP + Parallel')
plt.plot(dim_list, parallel_list, label='Parallel')



plt.legend()
  
# plt.ylabel('Elapsed time')
plt.xlabel('Number of dimensions')
plt.title('Compare time between three approachs')

plt.savefig('a.png')
# 
plt.show()

# Compare thread