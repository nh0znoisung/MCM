import matplotlib.pyplot as plt
import glob
from utils import read_testcase
from parallel import run_parallel




def get_result():
    dim_list = [] # x
    parallel_list = [ [] for _ in range(12) ] # list of list
    lst_file = glob.glob('testcases-parallel/*')
    lst_file.sort()


    for filename in lst_file:
        print("Start", filename)
        p, n = read_testcase(filename)
        dim_list.append(n)

        for nums_thread in range(1, 13):
            (_, parallel_elapse) = run_parallel(p, n, nums_thread, True)
            parallel_list[nums_thread-1].append(parallel_elapse)

        print("Done", filename)

    return dim_list, parallel_list

def get_result_1(thread: int = 12):
    dim_list = [i for i in range(1, thread + 1)] # x
    parallel_list = [] # list

    print("Start")
    p, n = read_testcase('sample.txt')


    for nums_thread in range(1, thread+1):
        (_, parallel_elapse) = run_parallel(p, n, nums_thread, True)
        parallel_list.append(parallel_elapse)

    print("Done")
    print(dim_list)
    print(parallel_list)

    return dim_list, parallel_list


# dim_list,parallel_list = get_result()


thread = 30
dim_list,parallel_list = get_result_1(thread)






# plotting the points 
# for i in range(thread):
plt.plot(dim_list, parallel_list)



# plt.legend()
  
# plt.ylabel('Elapsed time')
plt.xlabel('Number of threads')
plt.title('Compare time on 1 sample between number of threads')

plt.savefig('a.png')
# 
plt.show()

