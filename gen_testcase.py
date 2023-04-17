import os
import random
import math
import argparse

def get_dec(n: int) -> int:
    return math.floor(math.log10(n)) + 1

def gen_testcase(file_path: str, num_ele: int, lb: int, ub: int):
    # num_ele = random.randint(1, num_ele_range)
    with open(file_path, "w") as f:
        f.write(f'{num_ele}\n')
        for _ in range(num_ele):
            value = random.randint(lb, ub) # both include
            f.write(f'{value}\n')

def gen_testsuite(path: str = 'testcases', num_tests: int=10, lb: int = 1, ub: int = 30):
    if lb < 1:
        raise ValueError("Invalid lower bound")
    os.makedirs(path, exist_ok=True)
    dec = get_dec(num_tests)
    for i in range(2, num_tests+1):
        file_path = os.path.join(path, 'test-{:0{dec}}.txt'.format(i, dec=dec))
        gen_testcase(file_path, i, lb, ub)



parser = argparse.ArgumentParser(description='Generate testcase arguments')
parser.add_argument('--path', required=False, default='testcases', type=str, help="Enter the path of testcase folder containing the testcases")
parser.add_argument('--nt', required=False, default=10, type=int, help="Enter the number of testcases we want to generate")
# parser.add_argument('--ne', required=False, default=10, type=int, help="Enter the max number of elements in a testcase")

parser.add_argument('--lb', required=False, default=1, type=int, help="Enter the lowerbound of the dimension values in a testcase. Need to be an integer greater than 0")
parser.add_argument('--ub', required=False, default=30, type=int, help="Enter the upperbound of the dimension values in a testcase")

args = parser.parse_args()


gen_testsuite(args.path, args.nt, args.lb, args.ub)
