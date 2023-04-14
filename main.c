#include <limits.h>
#include <stdio.h>

// Matrix A_i has dimension p[i-1] x p[i] for i = 1..n
// We vectorize this chain of matrix A_1, A_2,..., A_n-1 have chain of dimensions: p[0],p[1],..,p[n-1]

// We have the dynamic programming formula

// m[i][i] = 0 for i = 1...n-1
// m[i][j] = min(i <= k < j) {m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] } for i,j = 1...n-1 and j >= i

// We need to calculate m[1][n-1]

int mcm_dp(int p[], int n)
{ // Dynamic Programming Approach
    /* 
        >> p[i] : the array of vectorized matrix chain
        >> n : length of the array of p[]
    */

    /*
        Proposed method:
            Observation:  m[i][j] = min(i <= k < j) {m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] }
                -  m[i][j] have a restriction that j >= i
                -  m[i][j] we need to calculate have the substraction of j and i is j-i. This value we call as L = j-i. We can see that:                                    
                                                     0 <= L <= n-2
                - The elements of memorized matrix in sub-task of dp have index [(i,k) and (k+1,j)]
                Assume we fixed the value i and j. The collection of all substraction is U = [k-i,j-k-1] for k in i...j-1
                Denote that LL is max of this collection. 
                We have that                    
                                        LL = max ( max(k-i), max(j-k-1) ) for k in i...j-1 
                                    <=> LL = max (j-i-1, j-i-1) = j-i-1
                    => So, we can see that, the length of all sub-task have upperbound j-i-1, smaller than j-i which is the length of base task
                    => So we can calculate the base on the length of base task. For example, with base task with length L, we can calculate base on sub-task which length from 0 to L-1
                - With L is fixed, we have j = i + L and i,j in [1,n-1]. So i >= 1 and i+L <= n-1
                                                    -> 1 <= i <= n-L-1
            Pseduo Code:
                m[i][i] = 0 for i in 1...n-1

                for L in 0...n-2:
                    for i in 1...n-L-1:
                        j = i + L
                        m[i][j] = INF
                        for k in i...i+L-1:
                            m[i][j] = min (m[i][k] + m[k + 1][j]+ p[i - 1] * p[k] * p[j] , m[i][j]);
                
    */

    /*
        Parallel idea:
            (i,j) -> ((i,k), (k+1,j))
            If we have at least [L/2] length that we can start min for length L
    */

	int m[n][n]; // Matrix 2D with len n*n and 0-indexed for memorize the value


	// Initialize the cost is INT_MAX for memorized matrix
	for (int i = 1; i < n; i++)
		m[i][i] = 0;

	// L is chain length.
	for (int L = 1; L <= n-2; L++) {
		for (int i = 1; i < n - L + 1; i++){
			int j = i + L;
			m[i][j] = INT_MAX;
			for (int k = i; k <= j - 1; k++){
				int q = m[i][k] + m[k + 1][j]
					+ p[i - 1] * p[k] * p[j];
				if (q < m[i][j])
					m[i][j] = q;
			}
		}
	}

	return m[1][n - 1];
}

// Driver code
int main()
{
	int p[] = { 12,3,9,10 }; // Vectorize the chain of dimensions of matrix
	int size = sizeof(p) / sizeof(p[0]);

	printf("Minimum number of multiplications is %d ",
		mcm_dp(p, size));

	return 0;
}
