from dp_parallel import run_dp_parallel
from recursion import run_recursion
from dp import run_dp
from parallel import run_parallel
from utils import benchmark
import time

# >> For input
n = int(input())
p = []
for i in range(n):
    ele = int(input())
    p.append(ele)

# # >> For manually
# p = [100, 2, 30, 400, 50]
# n = 5

(res, interval) = benchmark(run_recursion, p, n)
print(">> Run by recursion approach")
print("Result:", res)
print("Elapsed time:", interval)

(res, interval) = benchmark(run_dp, p, n)
print(">> Run by parallel approach")
print("Result:", res)
print("Elapsed time:", interval)

(res, interval) = benchmark(run_dp_parallel, p, n)
print(">> Run by parallel approach")
print("Result:", res)
print("Elapsed time:", interval)

# Run parallel approach
nums_thread = 7
(res, interval) = run_parallel(p, n, nums_thread, True)
print(">> Run by parallel approach")
print("Result:", res)
print("Elapsed time:", interval)
