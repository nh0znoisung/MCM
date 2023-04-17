# Matrix Chain Multiplication
Matrix Chain Multiplication (MCM) is the problem aimed to find the minimim scalar computation when multiple a chain of matrix. Denote that, if A\*B with A size d1\*d2 and B have size d2\*d3, so the computation scalar is d1\*d2\*d3. In general, we have chain M1\*M2\*...\*Mn which have the dimension of a sequence of matrices in an array arr[] length n+1, where the dimension of the i-th matrix is (arr[i-1] * arr[i]), the task is to find the most efficient way to multiply these matrices together such that the total number of element multiplications is minimum.

This is the Assignment of **Parallel Computing** class, so we try to solve the problem with simple approach (recursion), dynamic programming approach with Memoization and Parallel approach that can be split the task into many threads. In this problem, we design a algorithm that can use the number of thread that restrict from 1 to n*(n-1)/2 for fasten the computation. The idea is based on paper **An Efficient Parallel Dynamic Programming Algorithm** - *D.TANG and G.GUPTA* ([link](https://core.ac.uk/download/pdf/81964986.pdf))


## Authors 
**Quach Minh Tuan - Nguyen Hoai Thuong - Vo Anh Nguyen**

## Version
1.0.0

## Requirements
+ `Python` >= 3.10.9
+ `Pip` >= 23.0.1

## Installation
### Clone our source code
```sh
git clone https://github.com/nh0znoisung/MCM
cd MCM
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

Run program

```sh
python main.py < sample.txt
```

### Generate testcases
```sh
python3 gen_testcase.py --path './' --nt 10 --ne 10 --lb 1 --ub 10
```
+ `--path`: The target path of testcae folder containing the  testcase
+ `--nt`: The number of testcases we want to generate
+ `--ne`: The max number of elements in a testcase
+ `--lb`: The lowerbound of the dimension values in a testcase. Need to be an integer greater than 0
+ `--ub`: The upperbound of the dimension values in a testcase

**General format of a testcase**
```txt
n
a_1
a_2
a_3
...
a_n
```
+ `n`: The number of dimensions in this testcase
+ `a_i`: The values of **i-th** dimensions. Threfore, the matrix `M_i` have the shape (`a_i`, `a_(i+1)`)